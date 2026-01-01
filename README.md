# For Dummys (Fortis)
## A Super Simple Guide to Baldur's Gate 3 Modding

---

# What Even Is a Mod?

A mod is just a collection of text files that tell the game "hey, do this differently!"

Think of it like leaving sticky notes for the game. The game reads your notes and follows your instructions.

---

# The Folder Structure (Where Stuff Goes)

Your mod is just a bunch of folders inside folders. Here's what it looks like:

```
YourModName/
├── Mods/
│   └── YourModName/
│       └── meta.lsx          ← Your mod's ID card
│
└── Public/
    └── YourModName/
        ├── ClassDescriptions/    ← What your class IS
        ├── Progressions/         ← What you GET at each level
        ├── Lists/                ← Menus and choices
        ├── Stats/Generated/      ← Numbers and items
        └── Localization/         ← Text players see
```

**Think of it like a filing cabinet:**
- `Mods/` = The label on the outside of the cabinet
- `Public/` = All the actual papers inside

---

# What is a UUID? (The Scary Looking Code)

A UUID looks like this: `5e3f0164-0424-4e43-87a1-a0cc45ee4454`

**Don't panic!** It's just a unique ID number. Like a social security number, but for game stuff.

### Why do we need them?
The game has THOUSANDS of things - spells, items, classes. It needs a way to tell them apart. Names can repeat, but UUIDs never do.

### Where do I get one?
Just google "UUID generator" and click the first link. It makes them for free, OR you can use the BG3 Toolkit to generate one. 

### Golden Rule
**NEVER copy someone else's UUID.** Always make your own. If two things have the same UUID, the game gets confused and breaks.

---

# The Important Files Explained

## 1. meta.lsx - Your Mod's ID Card

This file tells the game "Hey, I exist! Here's who I am!"

```
What it contains:
- Your mod's name
- Your mod's UUID (its unique ID)
- What other mods it needs to work (dependencies)
- Who made it (you!)
```

**Real life example:** It's like the cover of a book - title, author, ISBN number.

---

## 2. ClassDescriptions.lsx - What Your Class IS

This file creates your class and says what it's all about.

```
What it contains:
- Class name (like "Flashblade" or "Necromancer")
- How much health you start with
- What stats you use (Strength? Dexterity?)
- What equipment you start with
```

**Real life example:** It's like a job description - "This job requires X skills, pays Y salary, starts on Z date."

---

## 3. Progressions.lsx - What You GET at Each Level

This file is a shopping list for each level. Level 1 you get this, Level 2 you get that.

```
What it contains:
- Level 1: Get these spells, these abilities
- Level 2: Get this new power
- Level 3: Pick a subclass
- Level 4: Get a feat
... and so on
```

**Real life example:** It's like a school curriculum - "Grade 1: Learn ABCs. Grade 2: Learn to read sentences."

---

## 4. Equipment.txt - Starting Gear

This file lists what items you start with when you pick this class.

```
What it contains:
- Weapons (sword, bow, staff)
- Armor (leather, robes)
- Potions
- Supplies
```

**Real life example:** It's like a packing list - "Bring: toothbrush, pajamas, snacks."

---

## 5. EquipmentLists.lsx - Choice Menus

Sometimes you want players to PICK their starting weapon. This file creates those dropdown menus.

```
What it contains:
- A UUID (so the game can find this menu)
- A list of items to choose from
```

**Real life example:** It's like a restaurant menu - "Pick one: Burger, Pizza, or Salad"

---

## 6. Localization Files (.xml) - The Words Players See

Everything has a code name internally (like `hFB_Class_DisplayName`). But players need to see real words like "Flashblade".

This file translates codes into real words.

```
Code: hFB_Class_DisplayName
Shows as: "Flashblade"

Code: hFB_Class_Description
Shows as: "A swift warrior who throws kunai and teleports."
```

**Real life example:** It's like a dictionary - "Bonjour means Hello"

---

# How Files Talk to Each Other

This is the MAGIC part. Files reference each other using UUIDs.

**Example Chain:**

1. **ClassDescriptions.lsx** says:
   - "My class uses equipment set called `EQP_CC_Flashblade`"

2. **Equipment.txt** has a section called:
   - `EQP_CC_Flashblade` with all the starting items listed

3. **Game reads both**, connects them, and gives your character the right stuff!

**Another Example:**

1. **Progressions.lsx** says:
   - "At level 1, let them pick from equipment list `99059633-1460-4246-817f-723046755106`"

2. **EquipmentLists.lsx** has that UUID and says:
   - "This list contains: Dagger, Shortsword, Shortbow"

3. **Game shows** a menu with those three weapon choices!

---

# The Building Blocks

## Handles (h-something)

When you see something like `hFB_Class_DisplayName`, that's a "handle."

Handles are like coat hooks. You hang a piece of text on them.
- The handle: `hFB_Class_DisplayName`
- What's hanging on it: "Flashblade"

## GUIDs (the long code with dashes)

Same as UUID. Just another name for it. You'll see both terms used.

## LSString vs FixedString

- **LSString** = A label that can change (like a name tag you write on)
- **FixedString** = A label that's set in stone (like an engraved nameplate)

For beginners: Don't worry about this. Just copy the format from existing files from the DreadOverlord Mod.

---

# Step-by-Step: How to Read a Mod

Let's say you open a mod and want to understand it:

### Step 1: Find meta.lsx
This tells you the mod's name and UUID. Write these down.

### Step 2: Find ClassDescriptions.lsx
This shows you what classes the mod adds. Look for:
- `Name` = The class name
- `ClassEquipment` = What equipment set they start with
- `ProgressionTableUUID` = The UUID that links to level-up stuff

### Step 3: Find Progressions.lsx
Search for the ProgressionTableUUID from step 2. This shows you:
- What you get at each level
- When you pick subclasses
- When you get feats

### Step 4: Find Equipment.txt
Search for the ClassEquipment name from step 2. This shows you:
- All the starting items

### Step 5: Find Localization files
These show you all the text players actually see.

---

# Step-by-Step: How to Make a Simple Change

**Example: Change starting weapon from Dagger to Sword**

1. Open `Equipment.txt`
2. Find your class's equipment section
3. Find the line that says `WPN_Dagger`
4. Change it to `WPN_Longsword`
5. Save the file
6. Repack the mod and test!

---

# Common Mistakes (And How to Avoid Them)

### Mistake 1: Copying UUIDs
**Problem:** You copied a UUID from another mod
**Fix:** Generate your own new UUID

### Mistake 2: Typos in references
**Problem:** ClassDescriptions says `EQP_CC_Flashblade` but Equipment.txt says `EQP_CC_FlashBlade` (capital B)
**Fix:** Spell things EXACTLY the same everywhere

### Mistake 3: Missing localization
**Problem:** Your class shows as `hMyClass_Name` instead of "My Cool Class"
**Fix:** Add the text to your localization .xml file

### Mistake 4: Wrong file location
**Problem:** You put Equipment.txt in the wrong folder
**Fix:** Follow the folder structure exactly. Equipment.txt goes in `Stats/Generated/`

---

# Helpful Tips

1. **Always backup before changing anything**

2. **Copy from working mods** - Find a mod that does something similar and use it as a template

3. **Change ONE thing at a time** - Then test. If it breaks, you know exactly what caused it.

4. **UUID Generator** - Bookmark this. You'll use it a lot.

5. **Case matters!** - `Flashblade` and `flashblade` are different to the game

6. **Spaces matter!** - Don't add random spaces in UUIDs or file names

---

# Glossary (Fancy Words Made Simple)

| Fancy Word | Simple Meaning |
|------------|----------------|
| UUID/GUID | A unique ID number (like a social security number) |
| Handle | A hook to hang text on |
| Localization | Translating codes into words players see |
| Progression | What you get when you level up |
| Selector | A menu that lets you pick something |
| Dependency | Another mod yours needs to work |
| LSX | A type of file the game uses (like .doc for Word) |
| Parse | When the game reads your file |
| Attribute | One piece of information (like "Name" or "Level") |
| Node | A container that holds attributes |

---

# You Got This!

Modding looks scary at first, but it's really just:
1. Text files
2. With unique IDs
3. That point to each other

Start small. Change one thing. Test it. Learn from it.

Every modder started exactly where you are now.

Good luck! 🎮

---