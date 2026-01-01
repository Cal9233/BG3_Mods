# Flashblade Mod for Baldur's Gate 3

A custom class mod featuring swift kunai-throwing warriors who mark enemies and teleport between them.

## Localization Setup

The mod uses XML localization files that must be converted to binary `.loca` format for the game to read them.

### Source File
```
Flashblade_b7ba1c69-c6be-e9a9-619c-f0a2d0080587\Localization\English\Flashblade.loca.xml
```

### Output Destination
```
C:\Program Files (x86)\Steam\steamapps\common\Baldurs Gate 3\Data\Mods\Flashblade_b7ba1c69-c6be-e9a9-619c-f0a2d0080587\Localization\English\Flashblade.loca
```

### Conversion Tools

#### Option 1: LSLib (Recommended)
Download from: https://github.com/Norbyte/lslib

Using Divine CLI:
```
divine -g bg3 -a convert-loca -s Flashblade.loca.xml -d Flashblade.loca
```

#### Option 2: BG3 Modder's Multitool
An all-in-one modding tool with GUI localization conversion.

## Class Features

- **Kunai Points**: Action resource that replenishes on short rest
- **Marked Kunai**: Throw kunai to mark enemies for teleportation
- **Flash Step/Strike**: Teleport to marked targets
- **Two Subclasses**: Way of the Ricochet (bouncing kunai) and Way of the Explosive (detonating marks)
