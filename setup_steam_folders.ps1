$project = "C:\Users\calvi\Projects\BG3_Mods\Flashblade_b7ba1c69-c6be-e9a9-619c-f0a2d0080587"
$steam = "C:\Program Files (x86)\Steam\steamapps\common\Baldurs Gate 3\Data"

# USE THE NEW UUID (the one with valid skeleton)
$uuid = "b7ba1c69-c6be-e9a9-619c-f0a2d0080587"

# Copy to Public folder
Copy-Item "$project\Stats" "$steam\Public\Flashblade_$uuid\" -Recurse -Force
Copy-Item "$project\ClassDescriptions" "$steam\Public\Flashblade_$uuid\" -Recurse -Force
Copy-Item "$project\Progressions" "$steam\Public\Flashblade_$uuid\" -Recurse -Force
Copy-Item "$project\Lists" "$steam\Public\Flashblade_$uuid\" -Recurse -Force
Copy-Item "$project\ActionResourceDefinitions" "$steam\Public\Flashblade_$uuid\" -Recurse -Force

# Copy to Mods folder
New-Item -ItemType Directory -Path "$steam\Mods\Flashblade_$uuid\Localization\English" -Force
Copy-Item "$project\Localization\English\Flashblade.loca" "$steam\Mods\Flashblade_$uuid\Localization\English\" -Force

Write-Host "Deployed to UUID: $uuid"
