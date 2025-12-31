from firecrawl import Firecrawl
import time

# --- CONFIGURATION ---
API_KEY = "fc-8a1cddf1f3c44526b357390714ae9f27"

# 1. PASTE YOUR URLS HERE
URLS = [
    "https://mod.io/g/baldursgate3/r/getting-started-creating-a-new-mod",
    "https://mod.io/g/baldursgate3/r/creation-guidelines-weapons",
    "https://mod.io/g/baldursgate3/r/adding-new-dice",
    "https://mod.io/g/baldursgate3/r/creation-guidelines-armor",
    "https://mod.io/g/baldursgate3/r/adding-new-classes",
    "https://mod.io/g/baldursgate3/r/editor-navigation",
    "https://mod.io/g/baldursgate3/r/ui-basic-setup",
    "https://mod.io/g/baldursgate3/r/ui-extending-the-ui",
    "https://mod.io/g/baldursgate3/r/adding-an-armor",
    "https://mod.io/g/baldursgate3/r/publishing-a-mod",
    "https://mod.io/g/baldursgate3/r/adding-a-new-spell-basic",
    "https://mod.io/g/baldursgate3/r/editor-shortcuts-and-tips",
    "https://mod.io/g/baldursgate3/r/editor-overriding-resources",
    "https://mod.io/g/baldursgate3/r/hair-and-beards-part-one",
    "https://mod.io/g/baldursgate3/r/hair-and-beards-part-2-character-creation",
    "https://mod.io/g/baldursgate3/r/hair-and-beards-part-3-helmet-hair",
    "https://mod.io/g/baldursgate3/r/vfx-part-1-making-the-effect",
    "https://mod.io/g/baldursgate3/r/vfx-part-2-creating-a-resource",
    "https://mod.io/g/baldursgate3/r/vfx-part-3-assigning-and-testing-the-effect",
    "https://mod.io/g/baldursgate3/r/getting-started",
    "https://mod.io/g/baldursgate3/r/adding-skill-and-item-icons",
    "https://mod.io/g/baldursgate3/r/generating-icons-for-character-creation",
    "https://mod.io/g/baldursgate3/r/adding-a-new-spell-projectile",
    "https://mod.io/g/baldursgate3/r/making-a-wall-spell",
    "https://mod.io/g/baldursgate3/r/how-to-extend-transmogrification-lite",
    "https://mod.io/g/baldursgate3/r/how-to-make-a-custom-class-for-bg3",
    "https://mod.io/g/baldursgate3/r/pommelstrikes-atlas-icons-photoshop-addon"
]

# 2. OUTPUT FILE NAME
OUTPUT_FILE = "Flash_Kunai_Mod_Guide.md"

# 3. CONTENT SELECTOR (The most important part!)
# Inspect the website. Find the HTML tag that holds the ACTUAL text.
# Common examples: 'article', 'div.main-content', 'div.post-body', 'div#content'
# If you leave this as None, it tries to grab the whole body (messy).
CONTENT_SELECTOR = 'article' 

# --- THE SCRIPT ---

def main():
    app = Firecrawl(api_key=API_KEY)

    # Create/Wipe the file clean
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(f"# MOD KNOWLEDGE BASE\nGenerated: {time.strftime('%Y-%m-%d')}\n\n")

    print(f"[*] Starting scrape of {len(URLS)} pages...")

    for url in URLS:
        print(f"Processing: {url}...")
        try:
            # The magic happens here: Scrape directly to Markdown
            scrape_result = app.scrape(url, formats=['markdown'])

            # v4 returns a Document object with attributes
            markdown_content = scrape_result.markdown if hasattr(scrape_result, 'markdown') else ''

            if markdown_content:
                with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
                    f.write(f"\n\n---\n# SOURCE: {url}\n---\n\n")
                    f.write(markdown_content)
                print(f"[OK] Saved.")
            else:
                print(f"[WARN] No content found for {url}")

        except Exception as e:
            print(f"[ERROR] Failed to scrape {url}: {e}")

        # Respect rate limits - free tier is 10 req/min
        time.sleep(7)

    print(f"\n[DONE] Your file '{OUTPUT_FILE}' is ready for Claude.")

if __name__ == "__main__":
    main()