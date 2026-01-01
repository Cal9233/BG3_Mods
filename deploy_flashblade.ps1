$project = "C:\Users\calvi\Projects\BG3_Mods\Flashblade_b7ba1c69-c6be-e9a9-619c-f0a2d0080587"
$steam = "C:\Program Files (x86)\Steam\steamapps\common\Baldurs Gate 3\Data"

# USE THE NEW UUID (the one with valid skeleton)
$uuid = "b7ba1c69-c6be-e9a9-619c-f0a2d0080587"

# Convert localization XML to LOCA binary
Write-Host "Converting localization..."
$divine = "C:\Users\calvi\Projects\BG3_Mods\lslib-1.20.3\divine.exe"
$locaSource = "$project\Localization\English\Flashblade.loca.xml"
$locaOutput = "$project\Localization\English\Flashblade.loca"
& $divine -g bg3 -a convert-loca -s $locaSource -d $locaOutput
Write-Host "Localization converted"

# Copy to Public folder
Copy-Item "$project\Stats" "$steam\Public\Flashblade_$uuid\" -Recurse -Force
Write-Host "Copied Stats"

Copy-Item "$project\ClassDescriptions" "$steam\Public\Flashblade_$uuid\" -Recurse -Force
Write-Host "Copied ClassDescriptions"

Copy-Item "$project\Progressions" "$steam\Public\Flashblade_$uuid\" -Recurse -Force
Write-Host "Copied Progressions"

Copy-Item "$project\Lists" "$steam\Public\Flashblade_$uuid\" -Recurse -Force
Write-Host "Copied Lists"

Copy-Item "$project\ActionResourceDefinitions" "$steam\Public\Flashblade_$uuid\" -Recurse -Force
Write-Host "Copied ActionResourceDefinitions"

# Copy to Mods folder
New-Item -ItemType Directory -Path "$steam\Mods\Flashblade_$uuid\Localization\English" -Force | Out-Null
Copy-Item "$project\Localization\English\Flashblade.loca" "$steam\Mods\Flashblade_$uuid\Localization\English\" -Force
Write-Host "Copied Localization"

Write-Host "`nDeployed to UUID: $uuid"
