# FLASHBLADE MOD - Development Workflow Guide

**Version:** 1.0  
**Generated:** January 1, 2026  
**Mod UUID:** `b7ba1c69-c6be-e9a9-619c-f0a2d0080587`

---

## TABLE OF CONTENTS

1. [Project Overview](#1-project-overview)
2. [File Location Map](#2-file-location-map)
3. [Development Workflow](#3-development-workflow)
4. [Current Issues & Fixes](#4-current-issues--fixes)
5. [Testing Checklist](#5-testing-checklist)
6. [Publishing Steps](#6-publishing-steps)
7. [Quick Reference](#7-quick-reference)

---

## 1. PROJECT OVERVIEW

### Mod Concept

A ninja-inspired class based on Minato from Naruto featuring kunai-throwing and teleportation mechanics.

### Key UUIDs

| Element                    | UUID                                   |
| -------------------------- | -------------------------------------- |
| **Mod**                    | `b7ba1c69-c6be-e9a9-619c-f0a2d0080587` |
| **Flashblade Class**       | `5e3f0164-0424-4e43-87a1-a0cc45ee4454` |
| **Flashblade Progression** | `ad1d81d7-be0b-4588-8e33-6eef835d8060` |
| **Way of the Ricochet**    | `d879c361-8e57-4a8f-a3b3-a365db1405fe` |

### Class Stats

- **Base HP:** 8
- **HP Per Level:** 5
- **Primary Ability:** Dexterity (2)
- **Spellcasting Ability:** Dexterity (2)
- **Starting Equipment:** `EQP_CC_Flashblade`

---

## 2. FILE LOCATION MAP

### Your Project Folder (SOURCE OF TRUTH)

```
C:\Users\calvi\Projects\BG3_Mods\Flashblade_b7ba1c69-c6be-e9a9-619c-f0a2d0080587\
```

### Project Structure

```
Flashblade_b7ba1c69-c6be-e9a9-619c-f0a2d0080587/
├── ActionResourceDefinitions/
│   └── ActionResourceDefinitions.lsx          # Custom resources (if any)
├── ClassDescriptions/
│   └── ClassDescriptions.lsx                  # Class & subclass definitions
├── Content/
│   └── [PAK]_Flashblade/                      # Packaged content
├── Lists/
│   ├── EquipmentLists.lsx                     # Equipment list references
│   ├── SkillLists.lsx                         # Skill list references
│   └── SpellLists.lsx                         # Spell list references
├── Localization/
│   └── English/
│       ├── Flashblade.loca                    # Compiled localization (BINARY)
│       └── Flashblade.loca.xml                # Source localization (EDITABLE)
├── Progressions/
│   ├── ProgressionDescriptions.lsx            # Progression UI text
│   └── Progressions.lsx                       # Level-up progression data
├── RootTemplates/                             # Item/character templates
├── Stats/
│   └── Generated/
│       ├── Equipment.txt                      # Starting equipment definition
│       └── Data/
│           ├── Passive.txt                    # Passive abilities
│           ├── Spell_Projectile.txt           # Kunai throw abilities
│           ├── Spell_Target.txt               # Teleport abilities
│           └── Status_BOOST.txt               # Status effects
└── README.md
```

### Steam Toolkit Folders (DEPLOYMENT TARGET)

```
C:\Program Files (x86)\Steam\steamapps\common\Baldurs Gate 3\Data\
├── Public\Flashblade_b7ba1c69-c6be-e9a9-619c-f0a2d0080587\
│   ├── ClassDescriptions\
│   ├── Lists\
│   ├── Progressions\
│   ├── RootTemplates\
│   └── Stats\Generated\Data\
├── Mods\Flashblade_b7ba1c69-c6be-e9a9-619c-f0a2d0080587\
│   ├── Localization\English\
│   └── meta.lsf
└── Editor\Mods\Flashblade_b7ba1c69-c6be-e9a9-619c-f0a2d0080587\
    └── (Editor-specific files)
```

### File Type → Destination Mapping

| File Type                                       | Project Location                | Steam Location                                     |
| ----------------------------------------------- | ------------------------------- | -------------------------------------------------- |
| `.lsx` (ClassDescriptions, Progressions, Lists) | `[folder]/[file].lsx`           | `Data\Public\Flashblade_...\[folder]\`             |
| `.txt` (Stats)                                  | `Stats\Generated\Data\*.txt`    | `Data\Public\Flashblade_...\Stats\Generated\Data\` |
| `Equipment.txt`                                 | `Stats\Generated\Equipment.txt` | `Data\Public\Flashblade_...\Stats\Generated\`      |
| `.loca` (Localization)                          | `Localization\English\`         | `Data\Mods\Flashblade_...\Localization\English\`   |
| `meta.lsf`                                      | (Toolkit generates)             | `Data\Mods\Flashblade_...\`                        |

---

## 3. DEVELOPMENT WORKFLOW

### Daily Workflow: Edit → Deploy → Test

#### STEP 1: Edit Files in Project Folder

```
📁 C:\Users\calvi\Projects\BG3_Mods\Flashblade_b7ba1c69-c6be-e9a9-619c-f0a2d0080587\
```

- Edit `.txt` files (spells, passives, statuses) with any text editor
- Edit `.lsx` files (class definitions, progressions) with any text editor
- Edit `.loca.xml` files for localization text

#### STEP 2: Convert Localization (If Changed)

```powershell
# Open LSLib Toolkit
# File → Open: Flashblade.loca.xml
# File → Save As: Flashblade.loca
# Save to: Localization\English\Flashblade.loca
```

#### STEP 3: Copy Files to Steam Folders

```powershell
# PowerShell script to deploy (run from project folder)
$project = "C:\Users\calvi\Projects\BG3_Mods\Flashblade_b7ba1c69-c6be-e9a9-619c-f0a2d0080587"
$steamPublic = "C:\Program Files (x86)\Steam\steamapps\common\Baldurs Gate 3\Data\Public\Flashblade_b7ba1c69-c6be-e9a9-619c-f0a2d0080587"
$steamMods = "C:\Program Files (x86)\Steam\steamapps\common\Baldurs Gate 3\Data\Mods\Flashblade_b7ba1c69-c6be-e9a9-619c-f0a2d0080587"

# Copy Stats
Copy-Item "$project\Stats\Generated\*" "$steamPublic\Stats\Generated\" -Recurse -Force

# Copy ClassDescriptions
Copy-Item "$project\ClassDescriptions\*" "$steamPublic\ClassDescriptions\" -Recurse -Force

# Copy Progressions
Copy-Item "$project\Progressions\*" "$steamPublic\Progressions\" -Recurse -Force

# Copy Lists
Copy-Item "$project\Lists\*" "$steamPublic\Lists\" -Recurse -Force

# Copy Localization
Copy-Item "$project\Localization\*" "$steamMods\Localization\" -Recurse -Force

Write-Host "Deployment complete!"
```

#### STEP 4: Test in Toolkit

1. Open **BG3 Toolkit**
2. Load your **Flashblade** project
3. Click **Project → Game Mode** (or press F5)
4. Create new character → Select Flashblade class
5. Test abilities in combat

#### STEP 5: Debug Issues

- Check **Message Log** in Toolkit for errors
- Use **Debug Console** (Ctrl+Shift+F11) to add spells:
  ```
  addDebugSpell Projectile_MarkedKunai
  ```

---

## 4. CURRENT ISSUES & FIXES

### Issue 1: Kunai Abilities "Pause Then Nothing"

**Status:** 🔴 BROKEN  
**Cause:** Missing `Trajectories` and `SpellAnimation` in Spell_Projectile.txt

**Fix:** Add to `Stats\Generated\Data\Spell_Projectile.txt`:

```
// Add these lines to Projectile_MarkedKunai entry:
data "Trajectories" "fbb99127-2487-4a4a-b33f-db7ce9a534b4"
data "SpellAnimation" "dd86aa43-8189-4d9f-9a5c-454b5fe4a197,,;,,;cb171bca-edc9-4ff6-8ad6-6c44c6bcf55b,,;827de88b-81d0-4dfb-bfcb-d747e65c7cc5,,;38f0c916-3daf-4fd2-9ad4-00467d848407,,;,,;3d7b3e44-cce9-4cdd-9f1b-7bb2f7928a71,,;,,;,,"
data "CastTextEvent" "Cast"
```

**Alternative Trajectories (for thrown dagger feel):**

- Straight throw: `fbb99127-2487-4a4a-b33f-db7ce9a534b4`
- Magic Missile (homing): `348013df-7958-4ca9-ac9f-80337e054bee,7bff57fa-fd21-4ab3-9384-83fb14237690`

---

### Issue 2: "Not Found" Text Everywhere

**Status:** 🟡 PARTIALLY FIXED  
**Cause:** Localization handles not matching or .loca file not loaded

**Your Localization Handles (must match in .loca.xml):**

```xml
<!-- Class -->
<content contentuid="hFB_Class_DisplayName">Flashblade</content>
<content contentuid="hFB_Class_Description">A swift warrior who marks enemies...</content>

<!-- Subclasses -->
<content contentuid="hFB_Ricochet_DisplayName">Way of the Ricochet</content>
<content contentuid="hFB_Ricochet_Description">Masters of bouncing kunai...</content>
<content contentuid="hFB_Ricochet_ShortName">Ricochet</content>

<!-- Statuses -->
<content contentuid="hFB_Advantage_DisplayName">Flash Strike</content>
<content contentuid="hFB_Advantage_Description">Advantage on next attack.</content>
<content contentuid="hFB_Slowed_DisplayName">Gravity Well</content>
<content contentuid="hFB_Slowed_Description">Movement speed reduced.</content>
```

**Fix Steps:**

1. Verify all handles in `.loca.xml` match handles in `.lsx` and `.txt` files
2. Convert `.loca.xml` to `.loca` using LSLib
3. Copy `.loca` to `Steam\Data\Mods\Flashblade_...\Localization\English\`

---

### Issue 3: No Armor Equipped at Start

**Status:** 🟢 LIKELY FIXED  
**Your Equipment.txt Location:** `Stats\Generated\Equipment.txt` ✓ CORRECT

**Verify Equipment.txt contains:**

```
new equipment "EQP_CC_Flashblade"
add initialweaponset "Melee"
add equipmentgroup
add equipment entry "ARM_Leather_Body"
add equipmentgroup
add equipment entry "ARM_Gloves_Leather_D"
add equipmentgroup
add equipment entry "ARM_Boots_Leather"
```

**Verify ClassDescriptions.lsx contains:**

```xml
<attribute id="ClassEquipment" type="FixedString" value="EQP_CC_Flashblade"/>
```

✓ Already present in your file!

---

### Issue 4: Missing Class Icon

**Status:** 🟢 FIXED  
**Your ClassDescriptions.lsx has:** `Icon="Rogue"` ✓

For custom icon later:

1. Create 300x300 .dds file named `Flashblade.dds`
2. Place in: `Data\Mods\Flashblade_...\GUI\Assets\ClassIcons\`

---

### Issue 5: Teleport Spell Syntax

**Status:** 🟡 NEEDS CHECK  
**File:** `Stats\Generated\Data\Spell_Target.txt`

**If using TeleportSource():**

```
// WRONG - for ground targeting
data "SpellSuccess" "GROUND:TeleportSource()"

// CORRECT - for teleporting to marked kunai
data "SpellSuccess" "TeleportSource()"
```

---

## 5. TESTING CHECKLIST

### Pre-Test Setup

- [ ] All files copied to Steam folders
- [ ] Toolkit restarted after file changes
- [ ] Game Mode launched fresh

### Character Creation Tests

- [ ] Flashblade class appears in class list
- [ ] Class name displays correctly (not "Not Found")
- [ ] Class description displays correctly
- [ ] Class icon shows (Rogue icon)
- [ ] Subclasses appear at level 3
- [ ] Subclass names/descriptions display correctly
- [ ] Starting equipment equipped (leather armor, gloves, boots)

### Ability Tests

| Ability        | Expected Behavior                 | Status |
| -------------- | --------------------------------- | ------ |
| Marked Kunai   | Throws projectile, marks enemy    | ⬜     |
| Flash Step     | Teleports to marked enemy         | ⬜     |
| Ricochet Throw | Kunai bounces to multiple targets | ⬜     |
| Explosive Tag  | AOE damage on marked kunai        | ⬜     |

### Combat Flow Test

1. [ ] Throw Marked Kunai at enemy → Projectile flies, enemy marked
2. [ ] Use Flash Step → Character teleports to enemy
3. [ ] Attack after teleport → Advantage applied
4. [ ] Status icons display correctly
5. [ ] Cooldowns function properly

---

## 6. PUBLISHING STEPS

### Option A: Toolkit Publish (Recommended)

1. Open BG3 Toolkit
2. Load Flashblade project
3. **Project → Publish Local**
4. Find `.pak` file in: `Data\Mods\Flashblade_...\`

### Option B: LSLib Package (Manual)

1. Open LSLib ConverterApp
2. **Create Package** tab
3. Set paths:
   - Source: Your project folder
   - Output: `Flashblade.pak`
4. Click **Create Package**

### Post-Publish Cleanup

Before testing `.pak`, delete loose files:

```powershell
# Remove "zombie" folders so game loads .pak instead
Remove-Item "C:\Program Files (x86)\Steam\steamapps\common\Baldurs Gate 3\Data\Public\Flashblade_b7ba1c69-c6be-e9a9-619c-f0a2d0080587" -Recurse -Force
Remove-Item "C:\Program Files (x86)\Steam\steamapps\common\Baldurs Gate 3\Data\Editor\Mods\Flashblade_b7ba1c69-c6be-e9a9-619c-f0a2d0080587" -Recurse -Force
```

### Distribution

1. Upload `.pak` to Nexus Mods or mod.io
2. Include:
   - Mod name: Flashblade
   - Version: X.X.X
   - Requirements: None (standalone class)

---

## 7. QUICK REFERENCE

### PowerShell Deploy Script (Save as `deploy.ps1`)

```powershell
# Run from project folder
$project = $PWD.Path
$uuid = "b7ba1c69-c6be-e9a9-619c-f0a2d0080587"
$steam = "C:\Program Files (x86)\Steam\steamapps\common\Baldurs Gate 3\Data"

# Deploy to Public
$items = @("Stats", "ClassDescriptions", "Progressions", "Lists", "ActionResourceDefinitions")
foreach ($item in $items) {
    if (Test-Path "$project\$item") {
        Copy-Item "$project\$item\*" "$steam\Public\Flashblade_$uuid\$item\" -Recurse -Force
        Write-Host "Copied $item"
    }
}

# Deploy to Mods
Copy-Item "$project\Localization\*" "$steam\Mods\Flashblade_$uuid\Localization\" -Recurse -Force
Write-Host "Copied Localization"

Write-Host "`nDeployment complete! Restart Toolkit to test."
```

### Common Debug Commands (In-Game Console)

```
addDebugSpell Projectile_MarkedKunai
addDebugSpell Target_FlashStep
SetLevel(_Player, 5)
```

### Localization Handle Format

```
hFB_[Element]_[Property]

Examples:
hFB_Class_DisplayName
hFB_MarkedKunai_Description
hFB_Ricochet_ShortName
```

### File Edit → Test Cycle

```
1. Edit file in Project folder
2. Run deploy.ps1
3. Restart Toolkit (if .lsx changed) OR reload stats (if .txt changed)
4. F5 → Game Mode
5. Test
6. Repeat
```

---

## NEXT OBJECTIVES

### Immediate (Fix Core Functionality)

1. [ ] Add Trajectories to Spell_Projectile.txt
2. [ ] Add SpellAnimation to Spell_Projectile.txt
3. [ ] Verify all localization handles match
4. [ ] Test kunai throw works

### Short-Term (Complete Basic Class)

5. [ ] Test teleport to marked kunai
6. [ ] Balance damage scaling
7. [ ] Add all subclass abilities
8. [ ] Create custom class icon

### Long-Term (Polish)

9. [ ] Custom kunai visual/model
10. [ ] Sound effects
11. [ ] VFX for teleportation
12. [ ] Playtesting and balance

---

_Last Updated: January 1, 2026_
