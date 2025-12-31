# MOD KNOWLEDGE BASE
Generated: 2025-12-31



---
# SOURCE: https://mod.io/g/baldursgate3/r/getting-started-creating-a-new-mod
---

[Browse games](https://mod.io/g)

Browse games

[My library](https://mod.io/library)

My library

[My content](https://mod.io/content)

My content

My account

mod.io

mod.io

[All games](https://mod.io/g) [Baldur's Gate 3](https://mod.io/g/baldursgate3) [Guides](https://mod.io/g/baldursgate3/r) [Editor](https://mod.io/g/baldursgate3/r?tags=Editor) Creating a New Mod

Creating a New Mod

Share

Report

Follow

This guide assumes that you have already installed the Baldur's Gate 3 game and Baldur's Gate 3 Toolkit following the instructions in **[Installing the Toolkit](https://mod.io/g/baldursgate3/r/installing-the-toolkit)**.

* * *

## Launching the Toolkit

The first time you launch the Toolkit, you will be asked to input the Data path. The default data folder depends on where your Baldur's Gate 3 game is installed.

On Steam, the default data path is: `C:\Program Files (x86)\Steam\steamapps\common\Baldurs Gate 3\Data`

On GOG, the default data path is: `C:\Program Files (x86)\GOG Galaxy\Games\Baldurs Gate 3\Data`

> `If at any point you’d like to clear the config completely:`
>
> 1. `Close the Editor`
>
> 2. `Open File Explorer`
>
> 3. `Paste the following in the address bar: C:\Users\%username%\AppData\Local\Larian Studios\Glasses`
>
> 4. `Delete Config.xml from that folder`
>
> 5. `Relaunch the Editor`

## Creating a New Mod

Once the Editor has launched, you’ll see the Browser window. In this window, select either “New Project” or the “Create +” button.

[![](https://image.modcdn.io/members/63c0/31088933/profilecreate/create_02.png)](https://image.modcdn.io/members/63c0/31088933/profilecreate/create_02.png)

You will be taken to the following view. Input your Project Name (mod name), and then select “Create”.

[![](https://image.modcdn.io/members/63c0/31088933/profilecreate/create_03.png)](https://image.modcdn.io/members/63c0/31088933/profilecreate/create_03.png)

At this point, you’ll need to wait for the Editor to load the basic mod setup. When done, you’ll see another Browser window that prompts you to “Select your level”.

Open the directory `Act_1A_WLD` and select the `WLD_Crashsite_D` level, which is the beginning of Act I, just after the nautiloid crashes on the beach.

> Some levels contain many smaller ones. For example, `WLD_Main_A` contains quite a bit of content, including the Crashsite, Emerald Grove, Goblin Camp, Underdark, and much more! Because it's so big, it also takes long time to load.
>
> To save on loading times, load smaller levels with the specific content you want, like `WLD_Crashsite_D`.

[![](https://image.modcdn.io/members/63c0/31088933/profilecreate/create_04.png)](https://image.modcdn.io/members/63c0/31088933/profilecreate/create_04.png)

Once the level loads, it should look like this:

[![](https://image.modcdn.io/members/63c0/31088933/profilecreate/create_05.png)](https://image.modcdn.io/members/63c0/31088933/profilecreate/create_05.png)

## Setting Up the Source Asset Data Path

If you plan to import assets as part of your mod (e.g. hairstyles, weapon models, textures), you will need to make sure you’ve defined a Source Asset Data Path.

In the Options menu, select “Preferences”, or simply press Ctrl+P.

[![](https://image.modcdn.io/members/63c0/31088933/profilecreate/sourcedata_01.png)](https://image.modcdn.io/members/63c0/31088933/profilecreate/sourcedata_01.png)

Navigate to Global Settings, and scroll down to the Source Asset Data Path field.

[![](https://image.modcdn.io/members/63c0/31088933/profile/sourcedata_02.png)](https://image.modcdn.io/members/63c0/31088933/profile/sourcedata_02.png)

Click on “…” to select your Source Asset Data Path.

**Your Source Asset Data Path must end in a \\Data\ folder.** It can live under a more complex hierarchy, or just inside your mod’s main folder (e.g. `...\steamapps\common\Baldurs Gate 3\Data\Mods\MyMod\Data`).

Because it’s specific to the mod you’re working on, you will need to update this data path every time you change which mod project you have loaded, so long as you want to import resources.

Once selected, click “Save & Close” in the Preferences window.

Some assets must be located inside the Source Asset Data Path in order to import correctly. If there are additional requirements, the relevant guides will let you know.

## Understanding the Mod Folders

Currently, files related to your mod project are stored in **four** different folders inside the Baldur's Gate 3 /Data/ folder, depending on what kind of file they are.

`Data/Projects/[YourMod]`

- Contains the data for the mod project to show up in the Toolkit.
- You can also add a PNG image into this folder (must be called `thumbnail.png`), and it will show up in the editor as the image for your project.

`Data/Editor/Mods/[YourMod]`

- Not packed.
- For editor files, like UUID or Stats files, that contain editor-specific data.

`Data/Mods/[YourMod]`

- Mod data that will be packed.
- Examples: UI assets, localisation, Osiris scripts, some level data, Thoth scripts

`Data/Public/[YourMod]`

- Mod data that will be packed.
- Examples: stats files, root templates, UUID tables, any created Resources (VisualResources, AnimationResource, etc) and their corresponding assets, texture atlases

`Data/Generated/Public/[YourMod]`

- Mod data that will be packed.
- Examples: Virtual Textures, `.dds` files for overwritten textures.

## Next Steps

Now that you’re created a new mod project, you’ll probably want to delve a little bit deeper into the editor interface. Check out the [**Editor: Navigation**](https://mod.io/g/baldursgate3/r/editor-navigation) guide for a quick introduction to some of the most commonly used panels and tools.

Alternatively, you can look through the list of available guides and follow a tutorial suited to the kind of mods you’d like to create: see the [**Getting Started**](https://mod.io/g/baldursgate3/r/getting-started) page.

[G\\
\\
GrumpyWashbear](https://mod.io/g/baldursgate3/u/grumpywashbear/r)

Follow GrumpyWashbear

Log in to join the discussion!

[E](https://mod.io/g/baldursgate3/u/eviluess)

[Eviluess](https://mod.io/g/baldursgate3/u/eviluess)• [81d ago](https://mod.io/g/baldursgate3/r/getting-started-creating-a-new-mod#1505261 "10/10/2025, 10:10 PM GMT-4")

Where should the anubis ann file put?
Hello, according to the guide:
Placing the Script into the Correct Directory
Move your Anubis script (Guard.ann) to the folder \\Stable\\LSProjects\\Apps\\\Data\\Mods\\\Scripts\\anubis\\node.
Is it correct? Say my mod and project named Test3, it will be:
Test3\\Stable\\LSProjects\\Apps\\Test3\\Data\\Mods\\Test3\\Scripts\\anubis\\node
I put the sample code and config files inside but just cannot be seen by the toolkit when I am assigning the config to a template.

[E](https://mod.io/g/baldursgate3/u/eviluess)

[Eviluess](https://mod.io/g/baldursgate3/u/eviluess)• [81d ago](https://mod.io/g/baldursgate3/r/getting-started-creating-a-new-mod#1505159 "10/10/2025, 07:50 PM GMT-4")

How to downlevel a player or the party progress level? Such as from level 5 to level 1
Hi,

I tried to set the player (or party progress) level to 1 by using SetLevel(\_player, 1) but failed.

However, if I repleace it to SetLevel(\_Player ,9) and the \_player's level is 1~8 it works.

So is there any way to downlevel a player or the party progress level?

Thanks in advance.

[G](https://mod.io/g/baldursgate3/u/grimmjowjgrjack)

[Grimmjowjgrjack](https://mod.io/g/baldursgate3/u/grimmjowjgrjack)• [143d ago](https://mod.io/g/baldursgate3/r/getting-started-creating-a-new-mod#1444970 "8/10/2025, 12:46 PM GMT-4")

Should probably add in big WARNING letters that character count matters in your UUID and stat tables. It seem like 4096 is the maximum. Any ideas how to fix this so the hours I put into make a mod doesn't go to waste? [@GrumpyWashbear](https://mod.io/u/GrumpyWashbear)? Can't load the project mod anymore.

[E](https://mod.io/g/baldursgate3/u/eviluess)

[Eviluess](https://mod.io/g/baldursgate3/u/eviluess)• [150d ago](https://mod.io/g/baldursgate3/r/getting-started-creating-a-new-mod#1436323 "8/3/2025, 03:36 AM GMT-4")

How to make my mod available in XBox, PS5 and macOS? I see only windows. Thanks.

[A](https://mod.io/g/baldursgate3/u/acererakinatophat)

[AcererakInATopHat](https://mod.io/g/baldursgate3/u/acererakinatophat)• [167d ago](https://mod.io/g/baldursgate3/r/getting-started-creating-a-new-mod#1416432 "7/17/2025, 03:40 AM GMT-4")

Howdy all. Just made a mod for a new subclass, but my subclass icons are not appearing in-game. When testing in the toolkit, they appear as expected. Anyone have an idea as to why this issue may be occurring? They are in the following folders with filename SubclassName.dds, where SubclassName is the name of the subclass in my class description :
\- MyMod/GUI/Assets/ClassIcons
\- MyMod/GUI/Assets/ClassIcons/hotbar
\- MyMod/GUI/AssetsLowRes/ClassIcons
\- MyMod/GUI/AssetsLowRes/ClassIcons/hotbar

No other mods are present and this mod was built without any dependencies.

[W](https://mod.io/g/baldursgate3/u/wyntervibez)

[wyntervibez](https://mod.io/g/baldursgate3/u/wyntervibez)• [277d ago](https://mod.io/g/baldursgate3/r/getting-started-creating-a-new-mod#1283297 "3/29/2025, 02:15 PM GMT-4")

btw there is typo in the start of the guide
on the steam the default path isnt
C:\\Program Files (x86)\\Steam\\steamapps\\common\\Baldur's Gate 3\\Data
its
C:\\Program Files (x86)\\Steam\\steamapps\\common\\Baldurs Gate 3\\Data

without the '

its not big problem but still, fix that for future readers

[M](https://mod.io/g/baldursgate3/u/modiouser4886264)

[ModioUser4886264](https://mod.io/g/baldursgate3/u/modiouser4886264)• [314d ago](https://mod.io/g/baldursgate3/r/getting-started-creating-a-new-mod#1227497 "2/19/2025, 04:30 PM GMT-5")

Hi, months ago in other PC i have to use Ring of no Justice mod for solving a bug, and now i want to resume my game but i can't load the save without this mod and it was removed from NexusMod, any solutions please?
I found the UUID by wayback machine, it is as follows:
<node id="ModuleShortDesc">
﻿<attribute id="Folder" value="RingOfNoJustice" type="LSString" />
<attribute id="MD5" value="" type="LSString" />
<attribute id="Name" value="RingOfNoJustice" type="LSString" />
<attribute id="UUID" value="6decdeb3-1fdb-4ab8-836d-e78ee2941599" type="FixedString" />
<attribute id="Version64" value="36028797018963968" type="int64" />
</node>
Thanks

[D](https://mod.io/g/baldursgate3/u/modiouser3176630)

[DragonSquirrel](https://mod.io/g/baldursgate3/u/modiouser3176630)• [1y ago](https://mod.io/g/baldursgate3/r/getting-started-creating-a-new-mod#1109354 "12/1/2024, 12:05 PM GMT-5")

Hi, I am having an issue getting beyond creating a new project. I name it, it starts loading BG3, and then it closes. No error is displaying or at least no error that I can see before it closes. I'm certain I've done something wrong, but I don't know what. Does anyone have any ideas?

[J](https://mod.io/g/baldursgate3/u/modiouser2120941)

[Jason-L](https://mod.io/g/baldursgate3/u/modiouser2120941)• [1y ago](https://mod.io/g/baldursgate3/r/getting-started-creating-a-new-mod#1005715 "9/25/2024, 08:29 PM GMT-4")

Hello, I have a question. I made a translation of a mod and I'd like to import this translation, but I have absolutely no idea how to do it, I don't have a “+ import” button like on your first picture. How do I do it?

[S](https://mod.io/g/baldursgate3/u/sanshelvetica)

[SansHelvetica](https://mod.io/g/baldursgate3/u/sanshelvetica)• [1y ago](https://mod.io/g/baldursgate3/r/getting-started-creating-a-new-mod#1101005 "11/25/2024, 02:54 PM GMT-5")

i was wondering the same thing

[A](https://mod.io/g/baldursgate3/u/azraeldrakephoenix)

[Azrael\_Drake\_Phoenix](https://mod.io/g/baldursgate3/u/azraeldrakephoenix)• [1y ago](https://mod.io/g/baldursgate3/r/getting-started-creating-a-new-mod#999778 "9/21/2024, 10:59 PM GMT-4")

I've been trying to follow the guides to create a new class and subclass, but when I attempt to publish, I can't open the Project Settings. Instead, I get an Unhandled Exception error saying "an item with the same key has already been added".

Does anyone know how to fix this?

[Z](https://mod.io/g/baldursgate3/u/modiouser2081481)

[ZCrover](https://mod.io/g/baldursgate3/u/modiouser2081481)• [1y ago](https://mod.io/g/baldursgate3/r/getting-started-creating-a-new-mod#985239 "9/13/2024, 01:20 PM GMT-4")

Is there any possibility to reset choose character level, or gear, or an entire level scene without quitting the toolkit and launching it again?

[G](https://mod.io/g/baldursgate3/u/gr8b8m8mods)

[GR8B8M8mods](https://mod.io/g/baldursgate3/u/gr8b8m8mods)• [1y ago](https://mod.io/g/baldursgate3/r/getting-started-creating-a-new-mod#1017674 "10/3/2024, 03:00 PM GMT-4")

God we need this so bad lol. Probably exist but cant find it.

[P](https://mod.io/g/baldursgate3/u/cytotoxictce11)

[PhalarAluve](https://mod.io/g/baldursgate3/u/cytotoxictce11)• [1y ago](https://mod.io/g/baldursgate3/r/getting-started-creating-a-new-mod#1038869 "10/14/2024, 08:43 PM GMT-4")

For the character level, you can at least open the console with F11 and then either do a ccStartNew to start a new character or ccStartRespec to start a respec for the one you already have!

1 reply

[W](https://mod.io/g/baldursgate3/u/modiouser2092714)

[Wolfheart846](https://mod.io/g/baldursgate3/u/modiouser2092714)• [1y ago](https://mod.io/g/baldursgate3/r/getting-started-creating-a-new-mod#985113 "9/13/2024, 11:44 AM GMT-4")

I can't get the path option to work for me at all. I customized the install location with GOG to C:\\BG3\\Baldurs Gate 3 because I have my nexus mods at C:\\BG3\\Nexus and I have the mod manger at C:\\BG3\\BGMM and now I've got the toolkit installed (from GOG) to C:\\BG3\\Toolkit but it doesn't matter if I type the folder address, use the file explorer, it always says it's not a valid path. I've uninstalled the game, all my mods, everything and started fresh and still this problem persists. any advice?

EDIT: The problem I found was that my BG3 data folder did NOT have an "Editor" folder inside it. Once I made a new folder and called it that the toolkit seemed to load just fine BUT my problem now is that all I get is crashdump files in the toolkit when I try to open it

Dumpfile contents

C:\\BG3\\Baldur's Gate 3 Toolkit\\EoCPlugin.dll \[version \]

An unhandled exception has occurred in the game, get a programmer!
Restart the editor to avoid data corruption!

Exception Type: EXCEPTION\_ACCESS\_VIOLATION
Additional Information: Attempted to read inaccessible data (Read access violation) at address 0x0

StackTrace:
\[Native\]
<unknown>
LSFrameworkPlugin!DomainBoundILStubClass.IL\_STUB\_ReversePInvoke(Int64)
DllCanUnloadNowInternal
UnhandledExceptionFilter
LdrResolveDelayLoadsFromDll
KiUserApcDispatcher
\_chkstk
RtlFindCharInUnicodeString
RtlRaiseException
RaiseException
DllCanUnloadNowInternal
DllCanUnloadNowInternal
DllCanUnloadNowInternal

\[Managed\]

AND ANOTHER ONE

C:\\BG3\\Baldur's Gate 3 Toolkit\\EoCPlugin.dll \[version \]

An unhandled exception has occurred in the game, get a programmer!
Restart the editor to avoid data corruption!

Exception Type: EXCEPTION\_ACCESS\_VIOLATION
Additional Information: Attempted to read inaccessible data (Read access violation) at address 0x0

StackTrace:
\[Native\]
<unknown>
LSFrameworkPlugin!DomainBoundILStubClass.IL\_STUB\_ReversePInvoke(Int64)
DllCanUnloadNowInternal
UnhandledExceptionFilter
memcpy
\_C\_specific\_handler
\_chkstk
RtlFindCharInUnicodeString
RtlRaiseException
RaiseException
GetMetaDataPublicInterfaceFromInternal
TranslateSecurityAttributes
WindowsBase!System.Windows.Threading.ExceptionWrapper.TryCatchWhen(System.Object, System.Delegate, System.Object, Int32, System.Delegate)
GetMetaDataPublicInterfaceFromInternal
GetMetaDataPublicInterfaceFromInternal
CoUninitializeEE
\_chkstk
RtlUnwindEx
LogHelp\_NoGuiOnAssert
CoUninitializeEE
\_chkstk
RtlFindCharInUnicodeString
RtlRaiseException
RaiseException
DllCanUnloadNowInternal
DllCanUnloadNowInternal
DllCanUnloadNowInternal

\[Managed\]

[S](https://mod.io/g/baldursgate3/u/sunbleached)

[Sunbleached](https://mod.io/g/baldursgate3/u/sunbleached)• [45d ago](https://mod.io/g/baldursgate3/r/getting-started-creating-a-new-mod#1534245 "11/15/2025, 09:41 PM GMT-5")

you have to go to BG3 steam store page, go to DLCs and download the Toolkit dlc AS WELL AS the separate Toolkit app

[E](https://mod.io/g/baldursgate3/u/modiouser21198091)

[EndofWinter](https://mod.io/g/baldursgate3/u/modiouser21198091)• [56d ago](https://mod.io/g/baldursgate3/r/getting-started-creating-a-new-mod#1526855 "11/4/2025, 06:24 PM GMT-5")

I'm extremely late to comment but did you have the additional dlc for base game downloaded? There should be two dlc's for baldur's gate 3, one of them is required to use with bg3 toolkit.

[S](https://mod.io/g/baldursgate3/u/saintabel)

[SaintAbel](https://mod.io/g/baldursgate3/u/saintabel)• [1y ago](https://mod.io/g/baldursgate3/r/getting-started-creating-a-new-mod#1092145 "11/18/2024, 05:06 PM GMT-5")

Did you manage to solve the problem?

[W](https://mod.io/g/baldursgate3/u/modiouser2092714)

[Wolfheart846](https://mod.io/g/baldursgate3/u/modiouser2092714)• [1y ago](https://mod.io/g/baldursgate3/r/getting-started-creating-a-new-mod#1092152 "11/18/2024, 05:09 PM GMT-5")

Nope, not at all. gave up on it and just kept playing and modding the old way

1 reply

[C](https://mod.io/g/baldursgate3/u/coloradohusky)

[Coloradohusky](https://mod.io/g/baldursgate3/u/coloradohusky)• [1y ago](https://mod.io/g/baldursgate3/r/getting-started-creating-a-new-mod#999515 "9/21/2024, 08:37 PM GMT-4")

That happens when your game is installed on a different drive, I think - for example, my Toolkit was on C: but my game was on D:, and I had the same error. Moving my game to C: fixed the issue

[S](https://mod.io/g/baldursgate3/u/saintabel)

[SaintAbel](https://mod.io/g/baldursgate3/u/saintabel)• [1y ago](https://mod.io/g/baldursgate3/r/getting-started-creating-a-new-mod#1092150 "11/18/2024, 05:08 PM GMT-5")

I have everything on the same disk, but the problem isn't resolved. Do you have any idea what else it might be?

[H](https://mod.io/g/baldursgate3/u/hitsuki-official)

[HitsukiOfficial](https://mod.io/g/baldursgate3/u/hitsuki-official)• [1y ago](https://mod.io/g/baldursgate3/r/getting-started-creating-a-new-mod#984661 "9/13/2024, 12:41 AM GMT-4")

!!!!!!!!!!!IF YOU'RE HAVING TROUBLE WITH THE FILE PATH!!!!!!!

This guide says Steam default path is "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Baldur's Gate 3" (with apostrophe in baldur's gate)
It should actually be "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Baldurs Gate 3" (withOUT apostrophe in baldurs gate)

[V](https://mod.io/g/baldursgate3/u/vahnsmash)

[VahnSmash](https://mod.io/g/baldursgate3/u/vahnsmash)• [1y ago](https://mod.io/g/baldursgate3/r/getting-started-creating-a-new-mod#983951 "9/12/2024, 04:29 PM GMT-4")

Please how do we rename Projects? I gave my first mod a working name not knowing the .pak file would have to be called that in perpetuity.

[M](https://mod.io/g/baldursgate3/u/modiouser20840171)

[ModioUser2084017](https://mod.io/g/baldursgate3/u/modiouser20840171)• [1y ago](https://mod.io/g/baldursgate3/r/getting-started-creating-a-new-mod#979394 "9/9/2024, 04:58 PM GMT-4")

Can you launch the toolkit on the steamdeck? I was able to install and map the folder, but it is unable to pass the loading screen.

[W](https://mod.io/g/baldursgate3/u/modiouser20841401)

[wandastan1999](https://mod.io/g/baldursgate3/u/modiouser20841401)• [1y ago](https://mod.io/g/baldursgate3/r/getting-started-creating-a-new-mod#976149 "9/7/2024, 09:23 PM GMT-4")

where do the .gr2 files go?

[P](https://mod.io/g/baldursgate3/u/modiouser2075693)

[pirate377](https://mod.io/g/baldursgate3/u/modiouser2075693)• [1y ago](https://mod.io/g/baldursgate3/r/getting-started-creating-a-new-mod#972329 "9/5/2024, 05:06 PM GMT-4")

Toolkit is not installed automatically, only files are downloaded, once you install the dlc. In order to launch toolkit, you need to access "Tools" section of your Steam library and then make sure that it shows all tools and not only the ones that are installed. From there you should be able to install the Baldur's Gate 3 Toolkit and then launch it.

[F](https://mod.io/g/baldursgate3/u/modiouser2075305)

[Falcain](https://mod.io/g/baldursgate3/u/modiouser2075305)• [1y ago](https://mod.io/g/baldursgate3/r/getting-started-creating-a-new-mod#972225 "9/5/2024, 04:02 PM GMT-4")

I've gotten it installed, Toolkit data and the Toolkit itself.
Attempted to launch the toolkit, set my data path(had to create 'Editor' file manually inside Data folder), after that it seems to be launching but it just closes itself after "adding plugins" step.
Is anyone else running into this or know what I'm doing wrong here?

[E](https://mod.io/g/baldursgate3/u/kvasir14)

[eKvasir](https://mod.io/g/baldursgate3/u/kvasir14)• [1y ago](https://mod.io/g/baldursgate3/r/getting-started-creating-a-new-mod#972774 "9/5/2024, 09:47 PM GMT-4")

look at this guide [@installing-the-toolkit](https://mod.io/g/baldursgate3/r/installing-the-toolkit)
specifically at 2) Enable the BG3 Toolkit Data DLC, in either the Steam or GOG section

There is data for the game that's separate from the toolkit that dosen't download automatically

[F](https://mod.io/g/baldursgate3/u/modiouser2075305)

[Falcain](https://mod.io/g/baldursgate3/u/modiouser2075305)• [1y ago](https://mod.io/g/baldursgate3/r/getting-started-creating-a-new-mod#972957 "9/6/2024, 12:22 AM GMT-4")

All of that was done and described in my previous post.
Issue was resolved anyways, thanks though!

[B](https://mod.io/g/baldursgate3/u/modiouser20761171)

[bzrker](https://mod.io/g/baldursgate3/u/modiouser20761171)• [1y ago](https://mod.io/g/baldursgate3/r/getting-started-creating-a-new-mod#972724 "9/5/2024, 09:04 PM GMT-4")

exact same problem here, can't dint anything about it.

update: simply verified my game files in steam and when that was done it worked

[S](https://mod.io/g/baldursgate3/u/shadowofradiance)

[shadowofradiance](https://mod.io/g/baldursgate3/u/shadowofradiance)• [1y ago](https://mod.io/g/baldursgate3/r/getting-started-creating-a-new-mod#972574 "9/5/2024, 07:18 PM GMT-4")

I am having this exact same problem, It is day one, I can wait a bit but I really want to make more mods and get them in the official channels for console players too.

[F](https://mod.io/g/baldursgate3/u/modiouser2075305)

[Falcain](https://mod.io/g/baldursgate3/u/modiouser2075305)• [1y ago](https://mod.io/g/baldursgate3/r/getting-started-creating-a-new-mod#972958 "9/6/2024, 12:23 AM GMT-4")

if the toolkit launcher hangs and closes at the "adding plugins" step, you likely have stray loose files from old mods like I did

[A](https://mod.io/g/baldursgate3/u/aromancer)

[Aromancer](https://mod.io/g/baldursgate3/u/aromancer)• [1y ago](https://mod.io/g/baldursgate3/r/getting-started-creating-a-new-mod#972128 "9/5/2024, 02:38 PM GMT-4")

I can't seem to find a link to launch the toolkit. When I try on the store page, it just loads up BG3. What am I doing wrong?

[M](https://mod.io/g/baldursgate3/u/st030)

[Majber](https://mod.io/g/baldursgate3/u/st030)• [1y ago](https://mod.io/g/baldursgate3/r/getting-started-creating-a-new-mod#972181 "9/5/2024, 03:30 PM GMT-4")

try resetting steam

[M](https://mod.io/g/baldursgate3/u/modiouser20749081)

[Mahdii-](https://mod.io/g/baldursgate3/u/modiouser20749081)• [1y ago](https://mod.io/g/baldursgate3/r/getting-started-creating-a-new-mod#972146 "9/5/2024, 02:54 PM GMT-4")

Check the filter in steam library and turn on "Tools"

[G](https://mod.io/g/baldursgate3/u/bobisbadat)

[GreatOldOneBob](https://mod.io/g/baldursgate3/u/bobisbadat)• [1y ago](https://mod.io/g/baldursgate3/r/getting-started-creating-a-new-mod#972193 "9/5/2024, 03:35 PM GMT-4")

Everyone keeps giving this advice but it's not showing up for me in tools at all. Shows as downloaded in the DLC section, but nowhere in my games does the toolkit launcher show up

[R](https://mod.io/g/baldursgate3/u/modiouser2075327)

[Rat\_Messiah](https://mod.io/g/baldursgate3/u/modiouser2075327)• [1y ago](https://mod.io/g/baldursgate3/r/getting-started-creating-a-new-mod#972182 "9/5/2024, 03:30 PM GMT-4")

yeah, still don't see anything? EDIT: Resetting Steam like the other guy said does it.

2 replies

Last updated

210d

Reading time

4 min read

Views

80,081

Comments

41

[G\\
\\
GrumpyWashbear](https://mod.io/g/baldursgate3/u/grumpywashbear/r)

Follow GrumpyWashbear

- [Guide](https://mod.io/g/baldursgate3/r/getting-started-creating-a-new-mod#guide)
- [Launching the Toolkit](https://mod.io/g/baldursgate3/r/getting-started-creating-a-new-mod#heading-1)
- [Creating a New Mod](https://mod.io/g/baldursgate3/r/getting-started-creating-a-new-mod#heading-2)
- [Setting Up the Source Asset Data Path](https://mod.io/g/baldursgate3/r/getting-started-creating-a-new-mod#heading-3)
- [Understanding the Mod Folders](https://mod.io/g/baldursgate3/r/getting-started-creating-a-new-mod#heading-4)
- [Next Steps](https://mod.io/g/baldursgate3/r/getting-started-creating-a-new-mod#heading-5)
- [Discussion](https://mod.io/g/baldursgate3/r/getting-started-creating-a-new-mod#discussion)

[Editor](https://mod.io/g/baldursgate3/r?tags=Editor) [English](https://mod.io/g/baldursgate3/r?tags=English) [Getting Started](https://mod.io/g/baldursgate3/r?tags=Getting+Started) [Official](https://mod.io/g/baldursgate3/r?tags=Official)

The first steps in mod creation - how to install the toolkit, create an empty mod, and assign the Source Asset Data Path.

Share

Report guide

---
# SOURCE: https://mod.io/g/baldursgate3/r/creation-guidelines-weapons
---

[Browse games](https://mod.io/g)

Browse games

[My library](https://mod.io/library)

My library

[My content](https://mod.io/content)

My content

My account

mod.io

mod.io

[All games](https://mod.io/g) [Baldur's Gate 3](https://mod.io/g/baldursgate3) [Guides](https://mod.io/g/baldursgate3/r) [Asset Creation](https://mod.io/g/baldursgate3/r?tags=Asset+Creation) Weapons - Creation Guidelines

Weapons - Creation Guidelines

Share

Report

Follow

This guide covers the most critical asset creation guidelines for new weapons, before you even import them into the Baldur’s Gate 3 Toolkit for use in your mod. While we won’t cover the specifics of 3D modelling or texturing, we’ll provide you with all the information to get your weapon assets set up with all of their necessary components.

## Model

If you want your weapon model to work with the existing in-game animations, make sure to follow these weapon creation guidelines.

For these guidelines, we’ve provided some reference files:

- [**WPN\_Weapon\_REFs.ma**](https://baldursgate3.game/mods/guides/WPN_Weapon_REFs.fbx)

- [**WPN\_Versatile\_Weapon\_REFs.ma**](https://baldursgate3.game/mods/guides/WPN_Versatile_Weapon_REFs.fbx)

- [**WPN\_Animated\_Weapons\_REF.ma**](https://baldursgate3.game/mods/guides/WPN_Animated_Weapons_REF.ma)


All weapon types have a reference mesh that indicates the **Grip** and the **No Funny Zone**.

The **Grip** is where the character will be holding the weapon. This needs to stay consistent with the reference in order to avoid the weapon clipping through or floating in the hands.

The **No Funny Zone** is the area that needs to stay clear of any artistic decoration or extra elements. This is an extension of the grip, in that the character might hold the weapon here during idle poses or might move their hands in this area.

[![](https://image.modcdn.io/members/63c0/31088933/profilecreate/createweap_01.png)](https://image.modcdn.io/members/63c0/31088933/profilecreate/createweap_01.png)

The setups we have in Maya are very specific, but necessary for the weapon models to work. The setup structures vary according to the weapon type.

### Setup: Non-Animated Weapons

These weapons do not have animated parts. They include weapons like spears, longswords, battleaxes, and daggers.

In the left column of the image below is the structure for versatile weapons. On the right is the structure for non-versatile weapons. If you’re not sure what kind of weapon yours is, it’s always safer to use the **versatile** structure.

[![](https://image.modcdn.io/members/63c0/31088933/profilecreate/createweap_02.png)](https://image.modcdn.io/members/63c0/31088933/profilecreate/createweap_02.png)

### Setup: Animated Weapons

These weapons have animated parts that you can either leave static or animate yourself. They include weapons like bows, flails, and whips.

If you decide to leave them static, follow the versatile weapon structure shown above for non-animated weapons. If you plan to animate the weapon, set it up as shown below.

[![](https://image.modcdn.io/members/63c0/31088933/profile/createweap_03.png)](https://image.modcdn.io/members/63c0/31088933/profile/createweap_03.png)

### Exporting a Model

Your models will need to be in a`.gr2`file format in order to use them in our engine.

## Textures

Depending on whether you make an entirely new weapon or adjust an existing one, you may have custom textures for it.

Textures should be exported as `.tga` files.

### Basic Textures

- **Base Map (BM or BMA):** This is your base colour. This should be mostly greyscale values if you want your weapon to be colour-customisable. If your weapon has opacity, that texture will be in the alpha channel of this map.

- **Normal Map (NM):** This contains the baked details from your highpoly sculpt.

- **Physical Map (PM):** This is a collection of different greyscale textures packed together.
  - Red Channel: Metalness map

  - Green Channel: Roughness map

  - Blue Channel: Ambient occlusion map

### Glow Map (Optional)

- **Glow Map (GM):** If your weapon needs to glow, you will need a glow map to indicate which regions should do so.


### Gradient Maps (Optional)

Gradient mapping takes the grey values on your texture and replaces them with colours of matching value.

[![](https://image.modcdn.io/members/63c0/31088933/profilecreate/createweap_04.png)](https://image.modcdn.io/members/63c0/31088933/profilecreate/createweap_04.png)

You can do this with the textures of a weapon to quickly make colour variations.

[![](https://image.modcdn.io/members/63c0/31088933/profile/createweap_05.png)](https://image.modcdn.io/members/63c0/31088933/profile/createweap_05.png)

Example colour variations for the glaive.

You’ll need two things for this:

- A gradient colour profile

- Gradient grayscale masks for the weapon


They go hand in hand!

### Gradient Colour Profile

Weapons use 2 gradients: a base gradient and an accent gradient. You can add up to 16 sets on a 256x256 texture.

You don’t need to follow the example below exactly. You just need to make sure the gray values on your weapon texture match your colors in the gradient.

[![](https://image.modcdn.io/members/63c0/31088933/profile/createweap_06.png)](https://image.modcdn.io/members/63c0/31088933/profile/createweap_06.png)

#### Gradient Grayscale Masks

Each weapon needs four grayscale masks. These will map the colours from the gradient colour profile. Build these up with your gradient in mind!

[![](https://image.modcdn.io/members/63c0/31088933/profile/createweap_07.png)](https://image.modcdn.io/members/63c0/31088933/profile/createweap_07.png)

**GMSK.r:** This map is a **BM mask**. Where the texture is black, you will see the gradient mapping. Where it’s white, you will see the BM colors.

**GMSK.g:** This map **assigns the base gradient** color to the weapon.

**GMSK.b:** This map **assigns the accent gradient** color to the weapon.

**GMSK.a:** This map masks base and accent gradient, where:

- black = base gradient,
- white = accent gradient.

## Next Steps

Now that you have your weapon asset ready, you can import it into the toolkit and set it up for use.

[G\\
\\
GrumpyWashbear](https://mod.io/g/baldursgate3/u/grumpywashbear/r)

Follow GrumpyWashbear

Log in to join the discussion!

[S](https://mod.io/g/baldursgate3/u/modiouser2079890)

[Substantial-tale](https://mod.io/g/baldursgate3/u/modiouser2079890)• [183d ago](https://mod.io/g/baldursgate3/r/creation-guidelines-weapons#1398270 "7/1/2025, 02:50 PM GMT-4")

Hello, I was just wondering if you go into more depth on how to change the color of a weapon. Like where is the menu to switch the colors and if the weapon does not already have the ability to change the color how do I go about creating a texture?

[C](https://mod.io/g/baldursgate3/u/seeker110)

[CybAnth](https://mod.io/g/baldursgate3/u/seeker110)• [1y ago](https://mod.io/g/baldursgate3/r/creation-guidelines-weapons#1121395 "12/11/2024, 04:07 PM GMT-5")

Perhaps this is the wrong place to ask this. But I keep searching around for the right place to ask it, and maybe I could be helped to find it.

I am not a modder. I can't even use the Toolkit - I'm on a Mac - doesn't work. But I've long been wondering about something.

Generically, how do modders take a Special Weapon Action from an existing weapon in the game, and add it to another weapon?
Like these:
[https://bg3.wiki/wiki/Weapon\_actions#Unique\_weapon\_actions](https://bg3.wiki/wiki/Weapon_actions#Unique_weapon_actions)

I know they CAN do it, I've seen it. For example:

Modders have taken Hellflame Cleave off the Hellfire Greataxe and put it on katanas and other weapons.
They've taken Zephyr Flash off Nyrulna and put in other weapons. In the case of Ki Duelist, they even made it a class ability.

Let's say I wanted to add one of these properties to a weapon. Like Profane Scourge, Shadowsoaked Blow, Colossal Onslaught, Grand Slam, etc., etc. Now I know it can be done through the Toolkit; obviously it has been.

I guess this is turning into a mod request, but I don't know where to ask people to do one (other than at Nexus, and it seems most of those requests are largely ignored.) Is there a way a modder could create a mod that would put this into the hands of PLAYERS?

Like - a sort of "weapons oils" mod but when they apply the oil to a weapon (vanilla or modded), it adds one of these unique weapon actions/properties to it?

Is this doable?
This is something I might even want to commission someone to do. I'm so interested in this possibility. If I COULD use the Toolkit, this would be one of the first things I'd explore doing.

[S](https://mod.io/g/baldursgate3/u/stuwil)

[StuWil](https://mod.io/g/baldursgate3/u/stuwil)• [347d ago](https://mod.io/g/baldursgate3/r/creation-guidelines-weapons#1174297 "1/18/2025, 07:53 AM GMT-5")

Message me on Nexus if you are still interested in this. My username is StuWil.

[M](https://mod.io/g/baldursgate3/u/moose261t)

[Moose261T](https://mod.io/g/baldursgate3/u/moose261t)• [239d ago](https://mod.io/g/baldursgate3/r/creation-guidelines-weapons#1335608 "5/6/2025, 07:08 AM GMT-4")

anything come from this?

[C](https://mod.io/g/baldursgate3/u/crosstour)

[Crosstour](https://mod.io/g/baldursgate3/u/crosstour)• [1y ago](https://mod.io/g/baldursgate3/r/creation-guidelines-weapons#1118420 "12/8/2024, 09:33 PM GMT-5")

Hello, I'm pretty new to modding and was wondering if you could give me some help. I was able to create a weapon (using Infernal rapier's looks) with my own unique weapon effects. All i really want to do is get rid of the red fiery glow from infernal rapier but have no idea how.

Thank you

[B](https://mod.io/g/baldursgate3/u/bek4096)

[Bek4096](https://mod.io/g/baldursgate3/u/bek4096)• [1y ago](https://mod.io/g/baldursgate3/r/creation-guidelines-weapons#1071709 "11/4/2024, 09:39 AM GMT-5")

Once again asking about .GR2 export.

How can this be done while preserving empties for VFX proxies and LODs? The Norbyte exporter for blender does not seem to allow the export of any mesh parented to an empty. This is a blocker for having working VFX on weapon models & LODs for performance.

edit: Okay, it seems you need to use the Armature setup.. but still haven't figured out exactly the right combination to properly align the weapon/FX proxies

[P](https://mod.io/g/baldursgate3/u/pointythegnome)

[PointyTheGnome](https://mod.io/g/baldursgate3/u/pointythegnome)• [1y ago](https://mod.io/g/baldursgate3/r/creation-guidelines-weapons#1054679 "10/24/2024, 07:43 AM GMT-4")

Thank you so much for making this guide and for providing the reference models, all the effort that's put into creating these resources is really much appreciated!

I am able to import my custom weapon model (.GR2 file) in the toolkit and set it up for use. The custom model is both visible in the examine window and when it is equipped on a character. But when I place the weapon on the ground the model becomes invisible.

The same thing happens when I try this with an unedited weapon model from the game. I'm wondering if something is wrong with with my export settings in Blender.

Does anyone know what could cause this problem?

[B](https://mod.io/g/baldursgate3/u/bek4096)

[Bek4096](https://mod.io/g/baldursgate3/u/bek4096)• [1y ago](https://mod.io/g/baldursgate3/r/creation-guidelines-weapons#1056860 "10/25/2024, 05:17 PM GMT-4")

Does it appear in the characters hands too, or only when stowed? I had an issue exporting from blender where, one model was working, then after I scaled it, would not render in the character hands during attack anims, but would when stowed (ie after idle, on characters back). I didn't try dropping it. If it's the same issue I just changed the scale and then it worked. I'm using FBX from blender.

I may have to try GR2 because I've got the current issue of LODs not importing, and probably the FX proxies are not properly importing (combustion oil for example FX is at wrong position). LODs I guess need the custom property in the gr2 data.

[P](https://mod.io/g/baldursgate3/u/pointythegnome)

[PointyTheGnome](https://mod.io/g/baldursgate3/u/pointythegnome)• [1y ago](https://mod.io/g/baldursgate3/r/creation-guidelines-weapons#1058486 "10/26/2024, 01:43 PM GMT-4")

For me the the item did show up in the characters hands, and in attack animations. Only when dropped on the ground they became invisible. The LODs do seem to work for me with the GR2 files.

My issue seems to be a problem with the BoundsMin and BoundsMax values in the item's .lsf file. (credit goes to the people in the Larian Discord who figured this out). These values are set to 0 in all my imported models. I'm not sure why this happens. Unfortunately I could't find a way to change this in the BG3 Toolkit.

In case anyone has a similar issue, here's how I fixed it manually:
\- Search for the item in the Toolkit's resource manager.
\- Find the item's .lsf file location below the Visual Resource, on the right hand side. You can find its file path under 'File Name'.
\- Convert the .lsf file to .lsx with Norbyte's LSlib Toolkit ConverterApp so you can edit it.
\- Inside the .lsx look for the BoundsMin and BoundsMax value, if they are set to 0 it looks like this:
attribute id="BoundsMin" type="fvec3" value="0 0 0"
attribute id="BoundsMax" type="fvec3" value="0 0 0"
\- I'm not sure what the correct values are here, but I replaced mine with the values that I found in an .lsf file of a simlar weapon type(in my case a javelin), and it seems to work for me. It looks like this:
attribute id="BoundsMin" type="fvec3" value="-0.10558531 -0.026308946 -1.1969713"
attribute id="BoundsMax" type="fvec3" value="0.090007596 0.040338572 0.56852365"
\- Save file and convert it back to an .lsf file with Norbyte's ConverterApp. Make sure you've replaced the old .lsf file with the new one in the item's file Path.
\- Now the item is hopefully visible again when dropped on the ground.

4 replies

[B](https://mod.io/g/baldursgate3/u/bek4096)

[Bek4096](https://mod.io/g/baldursgate3/u/bek4096)• [1y ago](https://mod.io/g/baldursgate3/r/creation-guidelines-weapons#1048076 "10/20/2024, 04:59 AM GMT-4")

the reference file WPN\_Weapon\_REFs.ma is actually an FBX for anyone wondering, it's just incorrectly labelled as a .ma file.

For blender 4.2.2 I deleted the empties which contained scale/rotation data, matched my model to the ref and exported as FBX. Works fine. However it might be better to use the same heirarchy/scale as the REFs, need to experiment more. (edit; FBX does not store FX proxies/LOD metadata afaik, so need to use .GR2, but blender .GR2 exporter refuses to export an empty than has children so... kinda stuck.

[C](https://mod.io/g/baldursgate3/u/commanderstrawberry)

[CommanderStrawberry](https://mod.io/g/baldursgate3/u/commanderstrawberry)• [1y ago](https://mod.io/g/baldursgate3/r/creation-guidelines-weapons#1032070 "10/11/2024, 11:24 AM GMT-4")

Would it be possible to please have a .fbx version of the 'animated weapons'? at present it downloads as a .ma, which is maya only.

Instrument guide meshes would be great too!

[S](https://mod.io/g/baldursgate3/u/sankojin1)

[Sankojin](https://mod.io/g/baldursgate3/u/sankojin1)• [1y ago](https://mod.io/g/baldursgate3/r/creation-guidelines-weapons#991842 "9/17/2024, 01:18 AM GMT-4")

Does anyone know if you need to do something special to add a custom weapon to a traders inventory? I made a custom weapon and when I add it to Arron's inventory it doesn't show up. I know I did it correctly because I can add items that are already in the game such as a longbow + 1 to his items for sale. Though if I make a new root template and change the name of it to make a whole new weapon it will not show up even if I use the games already existing assets.

[P](https://mod.io/g/baldursgate3/u/pommelstrike)

[pommelstrike](https://mod.io/g/baldursgate3/u/pommelstrike)• [1y ago](https://mod.io/g/baldursgate3/r/creation-guidelines-weapons#1077482 "11/8/2024, 02:41 PM GMT-5")

stats editors , treasure tables, look up ohfor loot on yt

[S](https://mod.io/g/baldursgate3/u/modiouser2092646)

[Standown](https://mod.io/g/baldursgate3/u/modiouser2092646)• [1y ago](https://mod.io/g/baldursgate3/r/creation-guidelines-weapons#981753 "9/11/2024, 06:25 AM GMT-4")

Is there a reliable way to import GR2 files (with all the dependencies) and compile them into the game again?
I have managed to export it to DAE which I can read with 3DS Max, but can this be changed into a GR2 game ready?

[S](https://mod.io/g/baldursgate3/u/sankojin1)

[Sankojin](https://mod.io/g/baldursgate3/u/sankojin1)• [1y ago](https://mod.io/g/baldursgate3/r/creation-guidelines-weapons#979035 "9/9/2024, 11:57 AM GMT-4")

I want to thank whomever is taking the time to make all these guides. I really appreciate them. Most other companies just release the tool kit with no tutorials at all. So the fact that you guys are doing this is awesome. Thank you again and really looking forward to the weapon guide that shows how to make a new weapon from a custom mesh. Though I do have it mostly figured out from the new armor mod guide.

[K](https://mod.io/g/baldursgate3/u/kalli22)

[Kallistrasza](https://mod.io/g/baldursgate3/u/kalli22)• [1y ago](https://mod.io/g/baldursgate3/r/creation-guidelines-weapons#976505 "9/8/2024, 01:08 AM GMT-4")

Feels like this guide started backwards. Why start the guide with the most complex actions such as custom models and textures? I was hoping for something starting with the basics like copy/pasting an asset, editing stats, recolouring, placement in the game world, and so on. I guess someone on youtube will beat you to it.

[R](https://mod.io/g/baldursgate3/u/raidey)

[Raidey](https://mod.io/g/baldursgate3/u/raidey)• [1y ago](https://mod.io/g/baldursgate3/r/creation-guidelines-weapons#975676 "9/7/2024, 04:45 PM GMT-4")

I was hoping for a guide on how to implement weapons in terms of stats, etc., or how to bring existing weapons and items into your mod

[T](https://mod.io/g/baldursgate3/u/modiouser2075245)

[TheRoaringForge](https://mod.io/g/baldursgate3/u/modiouser2075245)• [1y ago](https://mod.io/g/baldursgate3/r/creation-guidelines-weapons#972886 "9/5/2024, 11:08 PM GMT-4")

so how does one "Now that you have your weapon asset ready, you can import it into the toolkit and set it up for use." I guess the guide isn't complete yet?

[忘](https://mod.io/g/baldursgate3/u/526x2u8veu9xcbd1)

[忘川5](https://mod.io/g/baldursgate3/u/526x2u8veu9xcbd1)• [1y ago](https://mod.io/g/baldursgate3/r/creation-guidelines-weapons#973137 "9/6/2024, 04:31 AM GMT-4")

yeah i want to know how do i import gr2. and dds

[D](https://mod.io/g/baldursgate3/u/drakexop)

[Drakexop](https://mod.io/g/baldursgate3/u/drakexop)• [1y ago](https://mod.io/g/baldursgate3/r/creation-guidelines-weapons#982470 "9/11/2024, 05:56 PM GMT-4")

Try to follow the armour tutorial for that part, it worked for me. If you're using Blender you'll need the plugin that allows for GR2 exports.

[S](https://mod.io/g/baldursgate3/u/sainarkkranias)

[Sainark\_Kranias](https://mod.io/g/baldursgate3/u/sainarkkranias)• [1y ago](https://mod.io/g/baldursgate3/r/creation-guidelines-weapons#972758 "9/5/2024, 09:29 PM GMT-4")

Deeply disappointed that what I specifically wanted to do came with an incomplete guide. Should have first explained how to create a functional weapon and then how to give it a custom model.

[S](https://mod.io/g/baldursgate3/u/shadowofradiance)

[shadowofradiance](https://mod.io/g/baldursgate3/u/shadowofradiance)• [1y ago](https://mod.io/g/baldursgate3/r/creation-guidelines-weapons#973349 "9/6/2024, 10:05 AM GMT-4")

right? Honestly the mod tools are great for making and testing spells, doing some quest stuff, and class stuff, but weapons seem easier to hardcode functionality for from my experience with the tool so far. hopefully a guide comes out that changes that.

[O](https://mod.io/g/baldursgate3/u/oatatas)

[Oatatas](https://mod.io/g/baldursgate3/u/oatatas)• [1y ago](https://mod.io/g/baldursgate3/r/creation-guidelines-weapons#981624 "9/11/2024, 02:16 AM GMT-4")

I would have thought making a weapon would be one of the easiest things to do.

Last updated

1y

Reading time

5 min read

Views

11,683

Comments

27

[G\\
\\
GrumpyWashbear](https://mod.io/g/baldursgate3/u/grumpywashbear/r)

Follow GrumpyWashbear

- [Guide](https://mod.io/g/baldursgate3/r/creation-guidelines-weapons#guide)
- [Model](https://mod.io/g/baldursgate3/r/creation-guidelines-weapons#heading-1)
- [Setup: Non-Animated Weapons](https://mod.io/g/baldursgate3/r/creation-guidelines-weapons#heading-2)
- [Setup: Animated Weapons](https://mod.io/g/baldursgate3/r/creation-guidelines-weapons#heading-3)
- [Exporting a Model](https://mod.io/g/baldursgate3/r/creation-guidelines-weapons#heading-4)
- [Textures](https://mod.io/g/baldursgate3/r/creation-guidelines-weapons#heading-5)
- [Basic Textures](https://mod.io/g/baldursgate3/r/creation-guidelines-weapons#heading-6)
- [Glow Map (Optional)](https://mod.io/g/baldursgate3/r/creation-guidelines-weapons#heading-7)
- [Gradient Maps (Optional)](https://mod.io/g/baldursgate3/r/creation-guidelines-weapons#heading-8)
- [Gradient Colour Profile](https://mod.io/g/baldursgate3/r/creation-guidelines-weapons#heading-9)
- [Gradient Grayscale Masks](https://mod.io/g/baldursgate3/r/creation-guidelines-weapons#heading-10)
- [Next Steps](https://mod.io/g/baldursgate3/r/creation-guidelines-weapons#heading-11)
- [Discussion](https://mod.io/g/baldursgate3/r/creation-guidelines-weapons#discussion)

[Asset Creation](https://mod.io/g/baldursgate3/r?tags=Asset+Creation) [English](https://mod.io/g/baldursgate3/r?tags=English) [Official](https://mod.io/g/baldursgate3/r?tags=Official) [Weapons](https://mod.io/g/baldursgate3/r?tags=Weapons)

Guidelines on how to create new weapon assets so that they work easily inside the engine.

Share

Report guide

---
# SOURCE: https://mod.io/g/baldursgate3/r/adding-new-dice
---

[Browse games](https://mod.io/g)

Browse games

[My library](https://mod.io/library)

My library

[My content](https://mod.io/content)

My content

My account

mod.io

mod.io

[All games](https://mod.io/g) [Baldur's Gate 3](https://mod.io/g/baldursgate3) [Guides](https://mod.io/g/baldursgate3/r) [Dice](https://mod.io/g/baldursgate3/r?tags=Dice) Adding New Dice

Adding New Dice

Share

Report

Follow

In this guide, we will cover how to add new dice to your game. The guide assumes that you have already launched the BG3 Toolkit and created a mod. If you don't know how to do this yet, please refer to the [**Getting Started: Creating a New Mod**](https://mod.io/g/baldursgate3/r/getting-started-creating-a-new-mod) guide.

Our example mod in this guide is called “MyDice”.

## UUID Editor

When your project is first created, a window will prompt you to “Create” or “Open” a level. You can safely close this window.

Open the **UUID Object Editor** via a sheet icon located in the top right of the menu bar.

[![](https://image.modcdn.io/members/63c0/31088933/profile/dice_01.png)](https://image.modcdn.io/members/63c0/31088933/profile/dice_01.png)

In this editor, you will need to fill in the data for both the **CustomDice** and **DLC** sections.

## CustomDice

In the sidebar, expand the dropdown for your mod (in our case, “MyDice”) and navigate to the section called **CustomDice**. Create a new file by clicking on the “+” and selecting “CustomDice” in the resulting dropdown.

[![](https://image.modcdn.io/members/63c0/31088933/profile/dice_02.png)](https://image.modcdn.io/members/63c0/31088933/profile/dice_02.png)

Expand the contents to see your new file.

[![](https://image.modcdn.io/members/63c0/31088933/profile/dice_03.png)](https://image.modcdn.io/members/63c0/31088933/profile/dice_03.png)

Initially, all fields will be blank. Fill in the `Name` and `Display Name` fields and save the file. The UUID column should automatically populate itself when you complete the `Name`field. Even though the name used here is identical to the mod name, you can name it whatever you like, e.g. MyNewDice, AnnasCustomDice, etc.

[![](https://image.modcdn.io/members/63c0/31088933/profile/dice_04.png)](https://image.modcdn.io/members/63c0/31088933/profile/dice_04.png)

Save your changes by clicking on the Save icon on the CustomDice page.

[![](https://image.modcdn.io/members/63c0/31088933/profile/dice_05.png)](https://image.modcdn.io/members/63c0/31088933/profile/dice_05.png)

## DLC

Just as you navigated to the CustomDice section in the side bar, now navigate to **DLC**. Create a new DLC file, and fill in the `Name`, `CustomDice` and `UnlockType`. The `CustomDice` field should give you a drop down with your Dice present inside.

> The Name of the DLC can be whatever you wish - it's used only as an internal reference.

[![](https://image.modcdn.io/members/63c0/31088933/profile/dice_06.png)](https://image.modcdn.io/members/63c0/31088933/profile/dice_06.png)

Set the`UnlockType` field to `FreeDLC`.

Once you’ve filled in these three fields, save the file like you did for CustomDice.

## Dice Textures

Finally, copy the textures for your dice into the correct folder. To do this, open File Explorer and browse to `.../Data/Mods/YourModName/` and create the following folders: `GUI` → `Assets` → `DiceSets` → `DiceName`.

**Example:**

```swift
.../Data/Mods/MyMod_263daedd-4cab-46f9-9e56-b69a28d2ff40/GUI/Assets/DiceSets/MyFirstDice/
.../Data/Mods/MyMod_263daedd-4cab-46f9-9e56-b69a28d2ff40/GUI/Assets/DiceSets/MySecondDice/
```

**The name of each folder must be exactly same as was filled in the**`Name` **field in**`CustomDice` **.**

Now that you have the folders, you can copy over your images. A total of 25 images are needed for a die. Each of these must be correctly named and in `.dds` format.

> We've set up a file containing a reference of all the images required and what they should be named: **[example\_dice.zip](https://baldursgate3.game/mods/guides/example_dice.zip)**

## Done!

You can now try out your newly created dice set(s) in the game. For more information on how to publish your mod to the public, please refer to the [**Publishing a Mod Guide**](https://mod.io/g/baldursgate3/r/publishing-a-mod).

## Common Errors

**“Failed to create module with name ‘MyDice’!”**

This most likely means that there's already a mod present with that name OR that there’s a folder with the same name in `Data/Editor/Mods/`, `Data/Mods/`, or `Data/Public/`.

[G\\
\\
GrumpyWashbear](https://mod.io/g/baldursgate3/u/grumpywashbear/r)

Follow GrumpyWashbear

Log in to join the discussion!

[S](https://mod.io/g/baldursgate3/u/sephoraroth)

[sephoraroth](https://mod.io/g/baldursgate3/u/sephoraroth)• [1y ago](https://mod.io/g/baldursgate3/r/adding-new-dice#1036986 "10/13/2024, 08:27 PM GMT-4")

I'm having an issue with my dice textures not showing up. They show up perfectly if I publish the mod locally and put the pack into AppData\\Local\\Larian Studios\\Baldur's Gate 3\\Local Mods but it has been brought to my attention that after publishing it on mod.io, it does not display properly in game when downloaded through the in game mod manager. I can't figure out what the issue is, especially since it works when tested locally. Has anyone else experienced this? Is it maybe something to do with the source asset data path, or something else?

[S](https://mod.io/g/baldursgate3/u/sephoraroth)

[sephoraroth](https://mod.io/g/baldursgate3/u/sephoraroth)• [1y ago](https://mod.io/g/baldursgate3/r/adding-new-dice#1054012 "10/23/2024, 07:30 PM GMT-4")

Follow up to this. For anyone else having trouble, this is how I saved my .DDS files using paint.net.

DDS type is BC3 (Linear, DXT5)
To make sure Windows saves the file as .DDS uppercase and not .dds lowercase, put the filename in quotation marks when saving the new file. This only works when saving a new file and not when overwriting an existing file. Example: "d20.DDS" This will force Windows to save it with the uppercase letters. (I assume this trick can also work for Mac but I can't say for sure)

This seems to have fixed my issue and my dice skin appears to be working properly now when downloaded from the in game mod manager.

[X](https://mod.io/g/baldursgate3/u/xgodslayer)

[XandrGodslayer](https://mod.io/g/baldursgate3/u/xgodslayer)• [1y ago](https://mod.io/g/baldursgate3/r/adding-new-dice#1046651 "10/19/2024, 01:51 PM GMT-4")

Hello, have you found a solution yet? I'm having this issue myself, and I believe it may be that the textures are not being imported properly when publishing the mod, maybe not finding the correct asset folder

[S](https://mod.io/g/baldursgate3/u/sephoraroth)

[sephoraroth](https://mod.io/g/baldursgate3/u/sephoraroth)• [1y ago](https://mod.io/g/baldursgate3/r/adding-new-dice#1046948 "10/19/2024, 04:09 PM GMT-4")

Unfortunately I have not yet, but I also suspect it's something with trying to find the assets when being published for mod.io.

Someone suggested to me that, in my case, it could have something to do with the fact I installed BG3 and the toolkit onto an external hard drive rather than my main computer drive due to a space issue with my main drive. I've been meaning to see if there's anything within the toolkit that is maybe set to search for something within the main drive rather than the external, or try installing them on the main drive instead and seeing if that somehow fixes the issue. But since both programs are still installed to the same drive I'm not sure why this would cause a conflict, but really who knows lol.

When I get a chance to sit down and troubleshoot again I'll definitely update if I make any progress. It's just very odd that it works when locally tested but not publicly.

2 replies

[K](https://mod.io/g/baldursgate3/u/vaugnard)

[Kreiyu](https://mod.io/g/baldursgate3/u/vaugnard)• [1y ago](https://mod.io/g/baldursgate3/r/adding-new-dice#975632 "9/7/2024, 04:16 PM GMT-4")

the dice are invisible when i test it in game. i've checked multiple times, and my file paths for the project are correct. .dds files are where you tell me to put them. i'm just using the assets from a dice mod that i have on the nexus. the game has the dice in my dice list in game, but everything is invisible. is there a step you maybe forgot to mention?

[I](https://mod.io/g/baldursgate3/u/imscole)

[imScole](https://mod.io/g/baldursgate3/u/imscole)• [1y ago](https://mod.io/g/baldursgate3/r/adding-new-dice#976332 "9/7/2024, 11:10 PM GMT-4")

The name of each folder must be exactly the same as what was filled in the 'Name' field in CustomDice. For example, if the 'Name' field was filled with 'Water Dice', the folder should not be named 'WaterDice'; it should match exactly as 'Water Dice'.

I was experiencing the exact same issue as you, and it just started working for me now. It was because of that reason.

Last updated

1y

Reading time

3 min read

Views

5,148

Comments

8

[G\\
\\
GrumpyWashbear](https://mod.io/g/baldursgate3/u/grumpywashbear/r)

Follow GrumpyWashbear

- [Guide](https://mod.io/g/baldursgate3/r/adding-new-dice#guide)
- [UUID Editor](https://mod.io/g/baldursgate3/r/adding-new-dice#heading-1)
- [CustomDice](https://mod.io/g/baldursgate3/r/adding-new-dice#heading-2)
- [DLC](https://mod.io/g/baldursgate3/r/adding-new-dice#heading-3)
- [Dice Textures](https://mod.io/g/baldursgate3/r/adding-new-dice#heading-4)
- [Done!](https://mod.io/g/baldursgate3/r/adding-new-dice#heading-5)
- [Common Errors](https://mod.io/g/baldursgate3/r/adding-new-dice#heading-6)
- [Discussion](https://mod.io/g/baldursgate3/r/adding-new-dice#discussion)

[Dice](https://mod.io/g/baldursgate3/r?tags=Dice) [English](https://mod.io/g/baldursgate3/r?tags=English) [Official](https://mod.io/g/baldursgate3/r?tags=Official)

Quick guide on how to add new dice to the game.

Share

Report guide

---
# SOURCE: https://mod.io/g/baldursgate3/r/creation-guidelines-armor
---

[Browse games](https://mod.io/g)

Browse games

[My library](https://mod.io/library)

My library

[My content](https://mod.io/content)

My content

My account

mod.io

mod.io

[All games](https://mod.io/g) [Baldur's Gate 3](https://mod.io/g/baldursgate3) [Guides](https://mod.io/g/baldursgate3/r) [Armor](https://mod.io/g/baldursgate3/r?tags=Armor) Armor - Creation Guidelines

Armor - Creation Guidelines

Share

Report

Follow

In this guide, we will go over the steps required to prepare the model, materials, and textures for new armour to work correctly in your mod.

## Model

The first step is creating the asset you want. Below are example male and female human basemeshes, along with their limitation references:

[**HUM\_F\_NKD\_Mesh\_Limits.fbx**](https://baldursgate3.game/mods/guides/HUM_F_NKD_Mesh_Limits.fbx)

[**HUM\_M\_NKD\_Mesh\_Limits.fbx**](https://baldursgate3.game/mods/guides/HUM_M_NKD_Mesh_Limits.fbx)

If you want the armour to be available for other races, you’ll need to adjust it for each of those races individually. We have provided the basemeshes for other races in a package here:

[**BG3\_Armor\_Limit\_Guides.zip**](https://baldursgate3.game/mods/guides/BG3_Armor_Limit_Guides.zip)

### General Topology Rules

Try to create **as clean a topology as possible**. It will make skinning the asset easier later.

Make sure you can easily select different loops and elements in your mesh.

- Create clean loops and split off elements where needed.

- Minimise triangulated areas.

- Avoid spirals. (These greatly prolong the time it takes to skin a mesh.)


[![](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_02.png)](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_02.png)

- Make use of the centre line and symmetrise elements where possible.

[![](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_03.png)](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_03.png)

Check your mesh for common small issues like:

- Backfaces popping through the mesh

- Smoothing group mistakes, hard edges, or inverted normals

- Intersecting meshes not aligning nicely


[![](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_04.png)](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_04.png)

Check for common issues such as:

- N-gons, zero-length edges, or floating topology

- Unwelded vertices or vertices that got welded when they shouldn’t have

- Bad topology flow in the model


[![](https://image.modcdn.io/members/63c0/31088933/profilearmor/mor_05.png)](https://image.modcdn.io/members/63c0/31088933/profilearmor/mor_05.png)

Check the fit against the **actual body reference**.

[![](https://image.modcdn.io/members/63c0/31088933/profile/armor_06.png)](https://image.modcdn.io/members/63c0/31088933/profile/armor_06.png)

Try to avoid holes in your mesh. **Make an inside** and/or **cap your mesh** whenever possible.

[![](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_07.png)](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_07.png)

At this point, also check if any body parts would be hidden by the asset, and whether there are any gaps or clipping issues with other areas, especially when working with transparency.

[![](https://image.modcdn.io/members/63c0/31088933/profile/armor_08.png)](https://image.modcdn.io/members/63c0/31088933/profile/armor_08.png)

### Topology for Joints

To deform correctly, joints and corner points need specific topologies, as indicated in the image below.

[![](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_09.png)](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_09.png)

Deviating from these specific topologies can cause unnatural deformations. In those cases, increasing the topology will not make skinning easier, but potentially way worse.

In the following examples, you can see that this topology also carries over to the creature pipeline, and anything else that has these types of bending point.

[![](https://image.modcdn.io/members/63c0/31088933/profile/armor_13a.png)](https://image.modcdn.io/members/63c0/31088933/profile/armor_13a.png)

Red mesh doesn’t have joint topology.

[![](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_13b.png)](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_13b.png)

Red mesh doesn't have space to straighten the leg.

In short, all layers in this deformation area need the correct topology.

Even when hidden, this topology must be preserved. If you don’t, there is a chance it will pop out of the overlying model when animated, as shown in the next section.

### Topology for Movement

To support movement, make sure your armour has the **same topology as the naked body**, especially in regions that deform a lot and on skin-tight armours where you cannot hide the body mesh.

You have more leeway if parts of the body will be hidden, but even then, it is a good habit to get into to match the armour and body topologies as closely as you can.

[![](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_14a.png)](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_14a.png)

The shirt topology matches the body topology.

[![](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_14b.png)](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_14b.png)

The body loops match the shirt loops.

When there are different layers, apply this rule to **all the layers**.

[![](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_15.png)](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_15.png)

Every layer needs to have enough topology to support the deformation of the layer under it.

Further advice for modelling clothing:

- Make sure the upper body/skirt works with trousers.

- Avoid solid objects like clasps in low areas on skirts. These need openings to correctly simulate or stretch.

- Keep belts and ropes close to the body if they are not simulated. They will look odd otherwise.


[![](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_16.png)](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_16.png)

- Don’t put rigid objects on rotation points. They will heavily deform and look bugged.


[![](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_17.png)](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_17.png)

### Armor Across Races

Keep in mind that certain races (e.g. dragonborn and dwarves) have different proportions. While optimising is very important, don’t forget that meshes generally need to have **enough loops available** to support all of the race/gender variations, as you’ll want to keep the vertex order between versions identical.

The glove below looks a lot more low res on male dwarves (DWR\_M) because it’s heavily stretched.

[![](https://image.modcdn.io/members/63c0/31088933/profile/armor_18.png)](https://image.modcdn.io/members/63c0/31088933/profile/armor_18.png)

Certain races have shorter limbs and are more prone to clipping issues, so armours need to be scaled proportionally. Collars on dwarves, for example, need to be shorter than on humans to support their neck proportions.

[![](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_19.png)](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_19.png)

### Armor Limitations

Our equipment system allows you to equip many different items at once. Make sure to follow the same rules for all meshes so they can function in-game.

We have set up certain limitation meshes that, when followed, will ensure that everything easily clicks together. We have made these available for male and female humans. They can be found at the top of this guide.

#### Boots and Gloves

Width Limitation

Trouser and sleeve meshes need to **always be thinner** than the orange limit. They should **never stick out** at any location, unless it is with the green vertex colour and will be hidden.

[![](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_limit1.jpg)](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_limit1.jpg)

[![](https://image.modcdn.io/members/63c0/31088933/profile/armor_limit2.jpg)](https://image.modcdn.io/members/63c0/31088933/profile/armor_limit2.jpg)

Glove and boot meshes need to **always be bigger** than the orange limit. They need to fit snugly around it.

[![](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_limit3.jpg)](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_limit3.jpg)

[![](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_limit4.jpg)](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_limit4.jpg)

If you adhere to both these limitations, all trouser–boot and sleeve–glove combinations will work together and **not intersect**.

[![](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_limit5.jpg)](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_limit5.jpg)

[![](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_limit6.jpg)](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_limit6.jpg)

#### Length Limitation

Gloves need to reach the length disc (at minimum). Otherwise, there will be gaps.

[![](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_limit7.png)](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_limit7.png)

#### Necks and Collars

[![](https://image.modcdn.io/members/63c0/31088933/profilearmor/neck_1.png)](https://image.modcdn.io/members/63c0/31088933/profilearmor/neck_1.png)

[![](https://image.modcdn.io/members/63c0/31088933/profilearmor/neck_2.png)](https://image.modcdn.io/members/63c0/31088933/profilearmor/neck_2.png)

[![](https://image.modcdn.io/members/63c0/31088933/profilearmor/neck_3.jpg)](https://image.modcdn.io/members/63c0/31088933/profilearmor/neck_3.jpg)

[![](https://image.modcdn.io/members/63c0/31088933/profile/neck_4.jpg)](https://image.modcdn.io/members/63c0/31088933/profile/neck_4.jpg)

[![](https://image.modcdn.io/members/63c0/31088933/profilearmor/neck_5.jpg)](https://image.modcdn.io/members/63c0/31088933/profilearmor/neck_5.jpg)

#### Capes

[![](https://image.modcdn.io/members/63c0/31088933/profile/capes_1.jpg)](https://image.modcdn.io/members/63c0/31088933/profile/capes_1.jpg)

[![](https://image.modcdn.io/members/63c0/31088933/profile/capes_2.jpg)](https://image.modcdn.io/members/63c0/31088933/profile/capes_2.jpg)

### Export

Remember that after you finish creating your model, you will need to skin it.

To import your final mesh into the Baldur's Gate 3 toolkit, it needs to be in the `.gr2` file format. The final `.gr2` file can contain several meshes.

## Material

If your model consists of different meshes, you will need multiple materials for the outfit. If you are re-using existing pieces of armour, you can simply re-use those materials instead of creating copies.

## Textures

Depending on whether you make an entirely new armour or adjust an existing one, you may have custom textures for it.

Textures should be exported as `.tga` files.

### Basic Textures

In most cases, you'll have the following textures:

- **Base Map (BM or BMA):** This is your base colour. This should be mostly greyscale values if you want your outfit to be colour-customisable. If your outfit has opacity, that texture will be in the alpha channel of this map.

- **Normal Map (NM):** This contains the baked details from your highpoly sculpt.

- **Physical Map (PM):** This is a collection of different greyscale textures packed together.
  - Red Channel: Metalness map

  - Green Channel: Roughness map

  - Blue Channel: Ambient occlusion map
- **MSKcloth or MSK:** This is the ID mask that maps different areas of the outfit onto different colour options. This will enable colour customisation on the asset. MSKcloth is the more complex armour shader, whereas MSK is a simplified RGB mask with only 3 options (perfect for underwear meshes, for example!).


Your ID mask would look like this:

[![](https://image.modcdn.io/members/63c0/31088933/profilearmor/textures_01.png)](https://image.modcdn.io/members/63c0/31088933/profilearmor/textures_01.png)

These are the different values your mask should have:

[![](https://image.modcdn.io/members/63c0/31088933/profile/textures_02.png)](https://image.modcdn.io/members/63c0/31088933/profile/textures_02.png)

### Optional Textures

- **Glow Map (GM):** If your armour needs to glow (like the adamantine armour), you will need a glow map to indicate which regions should do so.

## What Next?

Once you're created your armor, you'll need to import it into the engine and set it up for use. Please move to the [**Adding New Armors**](https://mod.io/g/baldursgate3/r/adding-an-armor) guide for more details.

[G\\
\\
GrumpyWashbear](https://mod.io/g/baldursgate3/u/grumpywashbear/r)

Follow GrumpyWashbear

Log in to join the discussion!

Last updated

1y

Reading time

7 min read

Views

11,074

Comments

13

[G\\
\\
GrumpyWashbear](https://mod.io/g/baldursgate3/u/grumpywashbear/r)

Follow GrumpyWashbear

- [Guide](https://mod.io/g/baldursgate3/r/creation-guidelines-armor#guide)
- [Model](https://mod.io/g/baldursgate3/r/creation-guidelines-armor#heading-1)
- [General Topology Rules](https://mod.io/g/baldursgate3/r/creation-guidelines-armor#heading-2)
- [Topology for Joints](https://mod.io/g/baldursgate3/r/creation-guidelines-armor#heading-3)
- [Topology for Movement](https://mod.io/g/baldursgate3/r/creation-guidelines-armor#heading-4)
- [Armor Across Races](https://mod.io/g/baldursgate3/r/creation-guidelines-armor#heading-5)
- [Armor Limitations](https://mod.io/g/baldursgate3/r/creation-guidelines-armor#heading-6)
- [Boots and Gloves](https://mod.io/g/baldursgate3/r/creation-guidelines-armor#heading-7)
- [Length Limitation](https://mod.io/g/baldursgate3/r/creation-guidelines-armor#heading-8)
- [Necks and Collars](https://mod.io/g/baldursgate3/r/creation-guidelines-armor#heading-9)
- [Capes](https://mod.io/g/baldursgate3/r/creation-guidelines-armor#heading-10)
- [Export](https://mod.io/g/baldursgate3/r/creation-guidelines-armor#heading-11)
- [Material](https://mod.io/g/baldursgate3/r/creation-guidelines-armor#heading-12)
- [Textures](https://mod.io/g/baldursgate3/r/creation-guidelines-armor#heading-13)
- [Basic Textures](https://mod.io/g/baldursgate3/r/creation-guidelines-armor#heading-14)
- [Optional Textures](https://mod.io/g/baldursgate3/r/creation-guidelines-armor#heading-15)
- [What Next?](https://mod.io/g/baldursgate3/r/creation-guidelines-armor#heading-16)
- [Discussion](https://mod.io/g/baldursgate3/r/creation-guidelines-armor#discussion)

[Armor](https://mod.io/g/baldursgate3/r?tags=Armor) [Asset Creation](https://mod.io/g/baldursgate3/r?tags=Asset+Creation) [English](https://mod.io/g/baldursgate3/r?tags=English) [Official](https://mod.io/g/baldursgate3/r?tags=Official)

Guidelines on how to create new armor assets so that they work easily inside the engine.

Share

Report guide

---
# SOURCE: https://mod.io/g/baldursgate3/r/adding-new-classes
---

[Browse games](https://mod.io/g)

Browse games

[My library](https://mod.io/library)

My library

[My content](https://mod.io/content)

My content

My account

mod.io

mod.io

[All games](https://mod.io/g) [Baldur's Gate 3](https://mod.io/g/baldursgate3) [Guides](https://mod.io/g/baldursgate3/r) [English](https://mod.io/g/baldursgate3/r?tags=English) Adding New Classes or Subclasses

Adding New Classes or Subclasses

Share

Report

Follow

Let's build an imaginary class, Battlemage, that is proficient in heavy armour and many two-handed weapons. We’ll also give it access to a couple of spells.

Start by making a new mod for our class. In this guide, we’ll use `Battlemage` as the mod name.

## Defining Progressions

The first step is to define progression for our new class. This tells the game what the character receives with each level.

Open the Uuid Object Editor.

[![](https://image.modcdn.io/members/63c0/31088933/profileclasses/classes_01.png)](https://image.modcdn.io/members/63c0/31088933/profileclasses/classes_01.png)

We’ll add a Progressions table inside our mod.

[![](https://image.modcdn.io/members/63c0/31088933/profileclasses/classes_02.png)](https://image.modcdn.io/members/63c0/31088933/profileclasses/classes_02.png)

Start editing your newly-created Progressions table by double-clicking on it.

[![](https://image.modcdn.io/members/63c0/31088933/profileclasses/classes_03.png)](https://image.modcdn.io/members/63c0/31088933/profileclasses/classes_03.png)

Let’s start with the **Name** column. This is a technical name that will be used in data, so avoid using spaces. Once you’ve added a Name and pressed Enter, the UUID column should be automatically populated.

[![](https://image.modcdn.io/members/63c0/31088933/profileclasses/classes_04.png)](https://image.modcdn.io/members/63c0/31088933/profileclasses/classes_04.png)

Let’s set the **Level** to `1`, and **ProgressionType** to `0.` This tells the game that this is indeed a class progression.

[![](https://image.modcdn.io/members/63c0/31088933/profileclasses/classes_05.png)](https://image.modcdn.io/members/63c0/31088933/profileclasses/classes_05.png)

Next, we’ll need to fill in the **TableUUID**. This TableUUID is shared between all levels of a class. One quick trick here is to first copy and paste the value from the UUID column into the TableUUID…

[![](https://image.modcdn.io/members/63c0/31088933/profileclasses/classes_06.png)](https://image.modcdn.io/members/63c0/31088933/profileclasses/classes_06.png)

…and then right-click on the UUID cell, and select “Regenerate Value” from the dropdown.

[![](https://image.modcdn.io/members/63c0/31088933/profileclasses/classes_07.png)](https://image.modcdn.io/members/63c0/31088933/profileclasses/classes_07.png)

You should now have different values in the **UUID** and **TableUUID** columns.

[![](https://image.modcdn.io/members/63c0/31088933/profileclasses/classes_08.png)](https://image.modcdn.io/members/63c0/31088933/profileclasses/classes_08.png)

We want to make sure our Battlemage has a few specific traits:

- 2 spell slots

- Proficiency with all armors

- Proficiency with all weapons


We use the **Boosts** column to handle this. You can add various proficiencies and resources into Boosts, separating each one with `;`.

In this example, our final line will look like this:

`ActionResource(SpellSlot,2,1);Proficiency(LightArmor);Proficiency(MediumArmor);Proficiency(HeavyArmor);Proficiency(Shields);Proficiency(SimpleWeapons);Proficiency(MartialWeapons)`

[![](https://image.modcdn.io/members/63c0/31088933/profileclasses/classes_09.png)](https://image.modcdn.io/members/63c0/31088933/profileclasses/classes_09.png)

To make use of those spell slots, our Battlemage will need some spells, so we’ll need to build a list of spells they can have.

Let’s create a new **SpellLists** table in the Lists section of the left panel:

[![](https://image.modcdn.io/members/63c0/31088933/profileclasses/classes_10.png)](https://image.modcdn.io/members/63c0/31088933/profileclasses/classes_10.png)

We will create two lists in this table: one for cantrips, which will **all** be given to the character, and a second list for the level 1 spells the player will have to choose from.

> Spells in BG3 all have a prefix for their type. For example, Shocking Grasp is referenced as `Target_ShockingGrasp`. Any spell can be referenced by this structure:
>
> `Type_TechName`
>
> If you’ve made your own spells, perhaps following the **How to make a simple spell** \[\[TODO : Update link\]\] guide, you can use those spells here. The sample spell from that guide, **FireTouch**, would here have to be referenced as `Target_FireTouch`.

[![](https://image.modcdn.io/members/63c0/31088933/profileclasses/classes_11.png)](https://image.modcdn.io/members/63c0/31088933/profileclasses/classes_11.png)

In this example, we’ll give the player Shocking Grasp (`Target_ShockingGrasp`) and True Strike (`Target_TrueStrike`) cantrips, and let them select one spell from among Burning Hands (`Zone_BurningHands`), Jump (`Target_Jump`), and Longstrider (`Target_Longstrider`).

This means that our two lists in the SpellLists table will look like this:

[![](https://image.modcdn.io/members/63c0/31088933/profileclasses/classes_12.png)](https://image.modcdn.io/members/63c0/31088933/profileclasses/classes_12.png)

Your UUIDs will of course be different.

Now, we’ll take the UUIDs for each list and copy them back into our Progressions table, into the **Selectors** column.

Since we want to give the character all of the listed cantrips (no choice required), we’ll use `AddSpells()`. Add the UUID for the cantrip list in between the parentheses.

We want player to choose only one spell from the list, so here we’ll we use `SelectSpells()`. Add the UUID for the spell list in between the parentheses, followed by two more arguments:

`SelectSpells(<UUID>,1,0)`

- The `1` means the player will have to pick 1 spell

- The `0` means the player will be able to replace 0 of their previous spells


The final line in the Selectors cell should look similar to this (don't forget to change UUIDs for your own):

`AddSpells(714d1e3d-b436-4af7-9b40-107383e25a5d);SelectSpells(8fd1fe1e-ad9f-4d2c-a4c7-dcc687fc5ae6,1,0)`

[![](https://image.modcdn.io/members/63c0/31088933/profileclasses/classes_13.png)](https://image.modcdn.io/members/63c0/31088933/profileclasses/classes_13.png)

Let's add couple more levels to the Progression.

Selecting the whole row by clicking on the row number:

[![](https://image.modcdn.io/members/63c0/31088933/profileclasses/classes_14.png)](https://image.modcdn.io/members/63c0/31088933/profileclasses/classes_14.png)

Pressing Ctrl+C and Ctrl+V. The row should have been duplicated underneath, but with a new UUID.

[![](https://image.modcdn.io/members/63c0/31088933/profileclasses/classes_15.png)](https://image.modcdn.io/members/63c0/31088933/profileclasses/classes_15.png)

Change the Level in your new row to 2 (or higher). Repeat this a few more times, increasing the Level each time, until you have the first 5 levels.

[![](https://image.modcdn.io/members/63c0/31088933/profileclasses/classes_17.png)](https://image.modcdn.io/members/63c0/31088933/profileclasses/classes_17.png)

At this time, verify that the TableUUID is the same for all rows, and that each row has a unique UUID.

We can give the Battlemage a few extra cool features by defining more Boosts and Selectors for each additional level. We want to fill in the Progressions table as pictured below (note that your UUIDs will almost certainly be different from this image!):

[![](https://image.modcdn.io/members/63c0/31088933/profileclasses/classes_18.png)](https://image.modcdn.io/members/63c0/31088933/profileclasses/classes_18.png)

Let’s go through the additions and explain what’s going on.

- Level 2, **Selectors**: `SelectPassives(<UUID>,1,Battlestance)`
  - This allow the Battlemage their choice of Battlestance.

  - `<UUID>`: This is the UUID of the PassivesList the Battlemage is choosing from.
    - In this example, we’ll just reuse an existing list from the Shared>Lists>PassiveLists table:

    - [![](https://image.modcdn.io/members/63c0/31088933/profileclasses/classes_19.png)](https://image.modcdn.io/members/63c0/31088933/profileclasses/classes_19.png)
    - Find the Ranger fighting styles, and copy the UUID value. Paste this value into the <UUID> part of the Level 2 Selectors: `SelectPassives(a0bdb113-1cce-45ac-94fb-72d4c3f207e9,1,Battlestance)`
  - `1`: How many Passives the player can choose.

  - `Battlestance`: This is purely flavour text – sometimes you don’t want the passives to be presented as “Passives”. With this, the game will be asking the player to select a Battlestance, rather than a Passive. If we didn’t want this flavour text, we could simply write `SelectPassives(<UUID>,1)`.
- Level 2-5, **Boosts**: `ActionResource(SpellSlot,2,3)`
  - This gives the Battlemage extra ActionResources. The example here gives the Battlemage an additional two level 3 spell slots.
    - `SpellSlot`: The type of ActionResource given.

    - `2`: The number of SpellSlots given.

    - `3`: The level of SpellSlot given.
- Level 4, **AllowImprovement:**`Yes`
  - Marking AllowImprovement as Yes gives the Battlemage access to a Feat at this level, just like other classes.
- Levels 3-5, **Selectors**: `AddSpells(<UUID>)`
  - For these, we’re going to go back to our SpellLists table and add a few more rows, defining what Cantrips we’d like to give the Battlemage at levels 3, 4, and 5. Remember that these will _all_ be given. Here’s a basic example of what you could do:

  - [![](https://image.modcdn.io/members/63c0/31088933/profileclasses/classes_20.png)](https://image.modcdn.io/members/63c0/31088933/profileclasses/classes_20.png)
  - Once you’ve set up the new rows in SpellLists, copy the UUIDs for each list and paste them into the **Progressions** table, inside the `AddSpells()` for the relevant level’s **Selector** field. Using the above example, it’ll look like this:

  - [![](https://image.modcdn.io/members/63c0/31088933/profileclasses/classes_21.png)](https://image.modcdn.io/members/63c0/31088933/profileclasses/classes_21.png)

## Adding Subclasses

We’ll add three subclasses to our Battlemage class: Macemage, Staffmage, and Swordmage. Make three new rows in your Progressions table, and name them accordingly.

[![](https://image.modcdn.io/members/63c0/31088933/profileclasses/classes_22.png)](https://image.modcdn.io/members/63c0/31088933/profileclasses/classes_22.png)

Use the UUID → TableUUID copy trick to give each of these new subclasses an unique TableUUID, and regenerate their UUIDs. You should now have four different TableUUIDs in your Progressions table, like so:

[![](https://image.modcdn.io/members/63c0/31088933/profileclasses/classes_23.png)](https://image.modcdn.io/members/63c0/31088933/profileclasses/classes_23.png)

For each subclass, let’s set the Level to `3`. That’s the level at which the Battlemage will get access to them.

We’ll also set ProgressionType to `1`, which will define it as a subclass progression.

## Class Descriptions

Now that we have defined what our class does up to level 5, we have to add definitions for the class in order for it to show up in Character Creation. To do this, we add a ClassDescriptions table:

[![](https://image.modcdn.io/members/63c0/31088933/profileclasses/classes_24.png)](https://image.modcdn.io/members/63c0/31088933/profileclasses/classes_24.png)

As always, we start by filling up the **Name**. Use the same name that you used for the Progressions: `Battlemage`.

Into **ProgressionTableUUID** column, copy over the main class TableUUID from Progressions table (in the screenshot earlier, it would be the one in the green box).

[![](https://image.modcdn.io/members/63c0/31088933/profileclasses/classes_25.png)](https://image.modcdn.io/members/63c0/31088933/profileclasses/classes_25.png)

There are a few other fields we need to fill in here.

- **DisplayName:** This is what the player sees in-game.

- **Description:** This is the description of the class in the Character Creation.


[![](https://image.modcdn.io/members/63c0/31088933/profileclasses/classes_26.png)](https://image.modcdn.io/members/63c0/31088933/profileclasses/classes_26.png)

- **Primary Ability:** We’ll use `Strength`.

- **Spell Casting Ability:** We’ll use `Intelligence`.

- **Learning Strategy:** For classes, this should always be `AllChildren`.

- **Must Prepare Spells:** Does this class need to prepare spells like a Druid or Cleric? We’ll say `No`.

- **Can Learn Spells:** Can this class learn spells from scrolls like a Wizard? `No`.


[![](https://image.modcdn.io/members/63c0/31088933/profileclasses/classes_27.png)](https://image.modcdn.io/members/63c0/31088933/profileclasses/classes_27.png)

- **CharacterCreationPose:** We’ll use one that all classes use - `0f07ec6e-4ef0-434e-9a51-1353260ccff8`

- **BaseHp:** This is how much HP the class starts with. For the Battlemage, we’ll go with `12`.

- **HPPerLevel:** This is how much HP the class gains with each level. Let’s say `7`.

- **CommonHotbarColumns**, **ClassHotbarColumns**, and **ItemsHotbarColumns** describe the default hotbar separations. We will use the default values of `9`, `5` and `2` respectively.
  - The sum of these must always be 16.

[![](https://image.modcdn.io/members/63c0/31088933/profileclasses/classes_28.png)](https://image.modcdn.io/members/63c0/31088933/profileclasses/classes_28.png)

## Multiclassing

If you want your class to appear as an option for multiclassing, you'll need to add an extra row to the ClassDescriptions table.

Under the main Battlemage class, add a new row. This row will be a secondary level 1 that will act as multiclassing progression. Everything can be identical to the original Battlemage level 1 row, **except:**

- **UUID** must be different

- **IsMulticlass** should be Yes


It will look something like this:

[![](https://image.modcdn.io/members/63c0/31088933/profileclasses/multiclass01.png)](https://image.modcdn.io/members/63c0/31088933/profileclasses/multiclass01.png)

Now when you go to multiclass, your class will show up among the multiclassing options. The rest of the levels will come from the progressions you’ve already set up.

## Save Your Work

Before we continue, make sure to save **everything** you have done up until this part!

Did you do it?

When you’ve confident you’ve saved your work, close and restart the editor.

## Continuing with Class Descriptions

Reopen the ClassDescriptions table in the Uuid Object Editor.

We’ll need to add three new rows - these will be for our subclasses. Fill in the Name for each row with the same subclasses we started setting up earlier.

In the ParentUUIDs for these subclasses, select the class name from the dropdown - in our example, that’s `Battlemage`.

[![](https://image.modcdn.io/members/63c0/31088933/profileclasses/class_29.png)](https://image.modcdn.io/members/63c0/31088933/profileclasses/class_29.png)

Let’s first fill in the subclasses' **ProgressionTableUUID** s. The process is the same as for the class - open your Progressions table and find the **TableUUID** associated with each subclass. Copy and paste the **TableUUID** for each subclass from the Progressions table into that same subclass’s **ProgressionTableUUID** field in the ClassDescriptions table.

[![](https://image.modcdn.io/members/63c0/31088933/profileclasses/class_30.png)](https://image.modcdn.io/members/63c0/31088933/profileclasses/class_30.png)

Next, you’ll need to fill the **DisplayName**, **ShortName**, and **Description** for the class and subclasses. The ShortName is, as it sounds, a shorter way of referring to that subclass. This mostly appears on the in-game character sheet. If you don’t fill in a ShortName for the Battlemage subclasses, they’ll appear on the character sheet as:

- Macemage Battlemage

- Staffmage Battlemage

- Swordmage Battlemage


That’s a bit repetitive, so we’ll fill in the ShortNames as Mace, Staff, and Sword. This way, the character sheet will instead say:

- Mace Battlemage

- Staff Battlemage

- Sword Battlemage


[![](https://image.modcdn.io/members/63c0/31088933/profileclasses/class_31.png)](https://image.modcdn.io/members/63c0/31088933/profileclasses/class_31.png)

For the rest of the columns (L to O), copy the values from the class over to the subclasses.

[![](https://image.modcdn.io/members/63c0/31088933/profileclasses/update1.png)](https://image.modcdn.io/members/63c0/31088933/profileclasses/update1.png)

## Save Your Work Again

Once again, make sure you have saved all of your changes.

After saving, close the editor, then reopen it.

## Adding Subclass Selection to the Class

Let’s reopen the Progressions table in the Uuid Object Editor.

Go to the level 3 progression of our Battlemage. In the SubClasses column, we add all 3 new subclasses by double clicking on them in the dropdown. This allows player to choose which subclass they want to be when they reach level 3 of Battlemage.

[![](https://image.modcdn.io/members/63c0/31088933/profileclasses/class_33.png)](https://image.modcdn.io/members/63c0/31088933/profileclasses/class_33.png)

[![](https://image.modcdn.io/members/63c0/31088933/profileclasses/class_34.png)](https://image.modcdn.io/members/63c0/31088933/profileclasses/class_34.png)

With this, we’ve finished the main technical set up of our class and subclasses! Let’s save our work.

## Quick Testing

To test our creation thus far, let’s load into a level. For our purposes, Basic\_Level\_A is fine.

[![](https://image.modcdn.io/members/63c0/31088933/profileclasses/class_35.png)](https://image.modcdn.io/members/63c0/31088933/profileclasses/class_35.png)

Once the level has loaded, switch into Game Mode.

[![](https://image.modcdn.io/members/63c0/31088933/profileclasses/class_36.png)](https://image.modcdn.io/members/63c0/31088933/profileclasses/class_36.png)

Put your cursor over the character portrait, then press `Ctrl+Shift+L` to level up your character. In the game, open the Level Up screen, and click on the Add Class button.

[![](https://image.modcdn.io/members/63c0/31088933/profileclasses/class_37.png)](https://image.modcdn.io/members/63c0/31088933/profileclasses/class_37.png)

Select **Battlemage**.

[![](https://image.modcdn.io/members/63c0/31088933/profileclasses/class_38.png)](https://image.modcdn.io/members/63c0/31088933/profileclasses/class_38.png)

You can see the class description here, as well as the two cantrips we defined for the initial level.

Finish your level up into a Level 1 Battlemage, then level yourself up a few more times until you get to choose a subclass.

[![](https://image.modcdn.io/members/63c0/31088933/profileclasses/class_39.png)](https://image.modcdn.io/members/63c0/31088933/profileclasses/class_39.png)

You’ll also notice that our character is missing equipment, and that the Battlestance at level 2 is called Class Passives. Let's fix these issues now.

## Equipment

Equipment is defined in the Stats Editor. Just as we created other tables, let’s create a new Equipment table.

[![](https://image.modcdn.io/members/63c0/31088933/profileclasses/class_40.png)](https://image.modcdn.io/members/63c0/31088933/profileclasses/class_40.png)

Fill in the **Name** with something you can identify as the Battlemage’s starting equipment. Following our own internal guidelines, we’ll use `EQP_CC_Battlemage`, but you can do what you like provided that it doesn’t contain spaces.

We’ll put `Melee` as the **Initial Weapon Set,** since we want our Battlemage to show off their Greatsword. In the following columns (1, 2, 3, …), you can define additional items that the character will start with. Trying to fill those fields will open a massive dropdown with all possible items - you can search to narrow down the possibilities.

[![](https://image.modcdn.io/members/63c0/31088933/profileclasses/class_41.png)](https://image.modcdn.io/members/63c0/31088933/profileclasses/class_41.png)

Let’s use `WPN_Greatsword`, `ARM_ScaleMail_Body`, and `ARM_Boots_Leather`.

[![](https://image.modcdn.io/members/63c0/31088933/profileclasses/class_42.png)](https://image.modcdn.io/members/63c0/31088933/profileclasses/class_42.png)

Now, let’s open up the ClassDescriptions table. Use the Name you defined above (EQP\_CC\_Battlemage) and put it inside our the ClassEquipment field of the class. Do this for the class only, not the subclasses.

[![](https://image.modcdn.io/members/63c0/31088933/profileclasses/class_43.png)](https://image.modcdn.io/members/63c0/31088933/profileclasses/class_43.png)

## Progression Descriptions

Next we’ll fix the Class Passives name. For this we'll need to create a new ProgressionDescriptions table in the Progressions section:

[![](https://image.modcdn.io/members/63c0/31088933/profileclasses/class_44.png)](https://image.modcdn.io/members/63c0/31088933/profileclasses/class_44.png)

Let’s fill in the **DisplayName** and **Description** we want to show to players for our selection. In our case we want to call it Battle Stance. Remember that SelectPassives(<UUID>,1,Battlestance) we stuck into one of our Progressions earlier on?

This "Battlestance" is now important here. We put it into **SelectorId** column. Your row should look like this:

[![](https://image.modcdn.io/members/63c0/31088933/profileclasses/class_45.png)](https://image.modcdn.io/members/63c0/31088933/profileclasses/class_45.png)

Now, if you were test it in Game Mode again, you should see that the selection is properly named:

[![](https://image.modcdn.io/members/63c0/31088933/profileclasses/class_46.png)](https://image.modcdn.io/members/63c0/31088933/profileclasses/class_46.png)

> **TIP:** Having issues seeing this correctly named in game mode? Try closing and restarting the editor.

## Class Icon

We just need to change our class and subclass icons, both in Character Creation and on the hotbar.

### Preparing Assets

First, we need the images that we'll use for our class and subclass icons. These should be 300x300 pixel `.dds` files.

> **IMPORTANT:** These icons must be named identically to the class or subclass inside the ClassDescriptions UUID table.

You’ll need to place the images inside your mod folder like so:

`\Data\Mods\Battlemage\GUI\Assets\ClassIcons`

`\Data\Mods\Battlemage\GUI\AssetsLowRes\ClassIcons`

Hotbar icons go here:

`\Data\Mods\Battlemage\GUI\Assets\ClassIcons\hotbar`

`\Data\Mods\Battlemage\GUI\AssetsLowRes\ClassIcons\hotbar`

That’s all! Your icons should now show up correctly in-game.

#### DDS Conversion Settings

```bash
if image.mode == "RGBA":
		if sRGBBool:
			target_mode = "BC7_UNORM_SRGB"
		else:
			target_mode = "BC7_UNORM"
	if image.mode == "RGB":
		target_mode = "BC1_UNORM"
```

## Done!

Now you’ve made a very simple class with three subclasses.

[G\\
\\
GrumpyWashbear](https://mod.io/g/baldursgate3/u/grumpywashbear/r)

Follow GrumpyWashbear

Log in to join the discussion!

Last updated

1y

Reading time

14 min read

Views

39,952

Comments

219

[G\\
\\
GrumpyWashbear](https://mod.io/g/baldursgate3/u/grumpywashbear/r)

Follow GrumpyWashbear

- [Guide](https://mod.io/g/baldursgate3/r/adding-new-classes#guide)
- [Defining Progressions](https://mod.io/g/baldursgate3/r/adding-new-classes#heading-1)
- [Adding Subclasses](https://mod.io/g/baldursgate3/r/adding-new-classes#heading-2)
- [Class Descriptions](https://mod.io/g/baldursgate3/r/adding-new-classes#heading-3)
- [Multiclassing](https://mod.io/g/baldursgate3/r/adding-new-classes#heading-4)
- [Save Your Work](https://mod.io/g/baldursgate3/r/adding-new-classes#heading-5)
- [Continuing with Class Descriptions](https://mod.io/g/baldursgate3/r/adding-new-classes#heading-6)
- [Save Your Work Again](https://mod.io/g/baldursgate3/r/adding-new-classes#heading-7)
- [Adding Subclass Selection to the Class](https://mod.io/g/baldursgate3/r/adding-new-classes#heading-8)
- [Quick Testing](https://mod.io/g/baldursgate3/r/adding-new-classes#heading-9)
- [Equipment](https://mod.io/g/baldursgate3/r/adding-new-classes#heading-10)
- [Progression Descriptions](https://mod.io/g/baldursgate3/r/adding-new-classes#heading-11)
- [Class Icon](https://mod.io/g/baldursgate3/r/adding-new-classes#heading-12)
- [Preparing Assets](https://mod.io/g/baldursgate3/r/adding-new-classes#heading-13)
- [DDS Conversion Settings](https://mod.io/g/baldursgate3/r/adding-new-classes#heading-14)
- [Done!](https://mod.io/g/baldursgate3/r/adding-new-classes#heading-15)
- [Discussion](https://mod.io/g/baldursgate3/r/adding-new-classes#discussion)

[English](https://mod.io/g/baldursgate3/r?tags=English) [Official](https://mod.io/g/baldursgate3/r?tags=Official) [Stats](https://mod.io/g/baldursgate3/r?tags=Stats)

A tutorial on creating a new class with several subclasses, going through all of the main setups required.

Share

Report guide

---
# SOURCE: https://mod.io/g/baldursgate3/r/editor-navigation
---

[Browse games](https://mod.io/g)

Browse games

[My library](https://mod.io/library)

My library

[My content](https://mod.io/content)

My content

My account

mod.io

mod.io

[All games](https://mod.io/g) [Baldur's Gate 3](https://mod.io/g/baldursgate3) [Guides](https://mod.io/g/baldursgate3/r) [Editor](https://mod.io/g/baldursgate3/r?tags=Editor) Editor - Navigation

Editor - Navigation

Share

Report

Follow

If you haven’t yet installed the Baldur’s Gate 3 Toolkit, please see the [**Getting Started: Creating a Mod**](https://mod.io/g/baldursgate3/r/getting-started-creating-a-new-mod) guide.

## Opening or Creating a Project

When you open the editor, you are greeted with the Project Browser. Here you can open an existing project (mod), or create a new one. If you have existing projects, it will show them here. Just select the project you want to open, if it’s already existing.

[![](https://image.modcdn.io/members/63c0/31088933/profileeditor/nav_01.png)](https://image.modcdn.io/members/63c0/31088933/profileeditor/nav_01.png)

To create a new mod, select the New Project tab \[1\], then choose a Project Name for your mod \[2\] and click Create \[3\]. For this example I’ve named mine “LavaStatueMod“.

[![](https://image.modcdn.io/members/63c0/31088933/profileeditor/nav_02.png)](https://image.modcdn.io/members/63c0/31088933/profileeditor/nav_02.png)

## Loading a Level

After selecting a project and waiting for it to load, you’ll be presented with the choice of selecting a level. For many things, you don’t need to have a level actively open, so feel free to simply Cancel - but you’ll need to load one if you want to test your work.

Let’s search for a level called `WLD_Crashsite_D` in the search bar \[1\]. This level is the begining of ACT1, just after crashing the Nautiloid on the beach. Click on the thumbnail \[2\] and click Select \[3\] to load it.

[![](https://image.modcdn.io/members/63c0/31088933/profileeditor/nav_03.png)](https://image.modcdn.io/members/63c0/31088933/profileeditor/nav_03.png)

> **TIP:** Some levels contain other ones. For example `WLD_Main_A` contains quite a bit of content, including Crashsite, Druid Grove, Goblin Camp, Underdark and much more! Because it's so huge, it also takes a long time to load. Try to load smaller levels with specific content, like `WLD_Crashsite_D`.

Here is what the editor window looks like with a level loaded:

[![](https://image.modcdn.io/members/63c0/31088933/profileeditor/nav_04.png)](https://image.modcdn.io/members/63c0/31088933/profileeditor/nav_04.png)

## Exploring a Level

In our example, we see the vast blue skybox and no level to be found. That’s because our level is slightly offset from the world origin and we need to find it.

Hold the middle mouse button on the main viewport, and drag your mouse around to look around the level. Here are some other common controls you can use to navigate within the viewport when using the **editor camera**.

| **Action** | **Input** |
| --- | --- |
| **Forward** | W / Scroll forward |
| **Left** | A |
| **Backward** | S / Scroll backward |
| **Right** | D |
| **Up** | E |
| **Down** | Q |
| **Select object** | LMB click on an object |
| **Multi-select** | LMB click, hold and drag |

You can also double-click on one of the objects in the **World Outliner \[1\]**, like `BLD_HUM_Abbey_Arch_Pillar_B_006` \[2\] (the first one on the list). This will transport you to that object in the viewport.

[![](https://image.modcdn.io/members/63c0/31088933/profileeditor/nav_05.png)](https://image.modcdn.io/members/63c0/31088933/profileeditor/nav_05.png)

When selecting an object, we also see its properties in the **Sidebar**\[3\]. Though you can’t edit any of them directly, you _can_ edit the components they are built from, and the properties of their parent templates.

## Editing Templates

Let’s now edit the visuals of the statue in the middle of our scene.

Select the statue by locating it in the main viewport or in the World Outliner by looking for `DEC_GEN_Statue_Wizard_B_Broken_A_000` \[1\] \[2\].

Copy the `Root Template ID` by right clicking on the property Name in the left Sidebar \[3\] and selecting `Copy Value to Clipboard` \[4\]. In this case, the UUID is `6086ae20-f69b-4c39-b151-41c43d41ab6d`.

It’s usually better to find objects by UUID rather than by name, since many objects can share the same name but their UUIDs will always be different.

[![](https://image.modcdn.io/members/63c0/31088933/profileeditor/nav_06.png)](https://image.modcdn.io/members/63c0/31088933/profileeditor/nav_06.png)

**Root templates** are building blocks of our levels. When building a level, we place trees, rocks, items, chests and characters. Initially all of those are root templates, but once they are placed in the level they become **local templates**.

This means we can have a common root (ex. a Male Elf Guard), but many local override templates for Elf Guards with different faces, armor, equipment and other stats. Modifying the root will modify all instances of local templates that inherit from it.

[![](https://image.modcdn.io/members/63c0/31088933/profileeditor/nav_07.png)](https://image.modcdn.io/members/63c0/31088933/profileeditor/nav_07.png)

And modifying the root template is exactly what we’re going to do, so let’s find it! Open the **Root Template Manager** by clicking on the button in the toolbar \[1\], find the root template by pasting in the UUID we’ve just copied \[2\], select it \[3\], and copy another property, the **Visual Resource ID** \[4\], so we can modify its visual.

## Resources

To find the visual resource, we need to find it in **Resource Manager** which you can open with the highlighted button \[1\]. Search for the visual resource by pasting in the copied UUID into the Resource Manager’s **Filter** field \[2\]. Once the actual resource is shown, right click on it and select `Override in the Active Mod...` \[3\]. This makes this resource editable for you, and assigns it to your mod.

When asked "Do you want to keep the same package structure?", pick "Yes" . The resource is now editable!

We can edit it by double clicking on it \[4\], or opening the context menu (with RMB) and selecting `Open`.

[![](https://image.modcdn.io/members/63c0/31088933/profileeditor/nav_08.png)](https://image.modcdn.io/members/63c0/31088933/profileeditor/nav_08.png)

Properties of resources are not editable through the Sidebar, but through special Resource Editors.

Open the Visual Editor by double clicking on visual resource of our chosen statue in ResourceManager \[1\]. A new window will appear, where we can edit the properties of our visual \[2\].

[![](https://image.modcdn.io/members/63c0/31088933/profileeditor/nav_09.png)](https://image.modcdn.io/members/63c0/31088933/profileeditor/nav_09.png)

Search for an interesting Material Resource in the Resource Manager \[1\], like `NAT_Lava_Fall_A_Animated`(`4861504e-ccaf-d2a8-3bb8-13475136f133`). With the Material Resource selected \[2\], click on the arrows `(<-)` in the visual editor \[3\]\[4\] to assign that Material to our object for both LODs.

Click Apply \[5\].

[![](https://image.modcdn.io/members/63c0/31088933/profileeditor/nav_10.png)](https://image.modcdn.io/members/63c0/31088933/profileeditor/nav_10.png)

Congratulations! The statue in game, and everything else using the visual resource we’ve just modified, are now a little bit hotter 🔥 .

> **TIP:** Alternatively, we could create a new Visual Resource with new materials and assign it to the statue’s Root Template in the **Template Manager**, so only objects inheriting from that root template would get our changes.

## Testing while Playing in Editor

To see our changes in game, you can enter Game Mode. (To switch back to Editor Mode, click the same button again.)

[![](https://image.modcdn.io/members/63c0/31088933/profileeditor/nav_11.png)](https://image.modcdn.io/members/63c0/31088933/profileeditor/nav_11.png)

Whoops, where are we? Remember how the level was offset a bit from world origin? Well, now we’ve spawned in the middle of the void and cannot move. How unfortunate.

[![](https://image.modcdn.io/members/63c0/31088933/profileeditor/nav_12.png)](https://image.modcdn.io/members/63c0/31088933/profileeditor/nav_12.png)

One of the ways we can get out of this void is by switching to the **Editor Camera** while we’re in Game Mode – see the screenshot below. Try switching to Editor Camera and look around to find our level. Fly over to it using WASD controls. When you’ve found a bit of good walkable terrain, put your cursor over it, and press `Ctrl+T`. This will teleport your player character to where your cursor is.

[![](https://image.modcdn.io/members/63c0/31088933/profileeditor/nav_13.png)](https://image.modcdn.io/members/63c0/31088933/profileeditor/nav_13.png)

If you can’t find any terrain, you can also note the XYZ coordinates of a nearby object and try to fly to it. Both the camera coordinates (left) and selected object coorindates (right) can always be viewed on the bottom bar.

[![](https://image.modcdn.io/members/63c0/31088933/profileeditor/nav_14.png)](https://image.modcdn.io/members/63c0/31088933/profileeditor/nav_14.png)

Voila! After teleporting there, we can now walk around our statue in game and admire our work.

[G\\
\\
GrumpyWashbear](https://mod.io/g/baldursgate3/u/grumpywashbear/r)

Follow GrumpyWashbear

Log in to join the discussion!

[B](https://mod.io/g/baldursgate3/u/modiouser4110441)

[bentropy](https://mod.io/g/baldursgate3/u/modiouser4110441)• [1y ago](https://mod.io/g/baldursgate3/r/editor-navigation#1145794 "12/30/2024, 05:50 PM GMT-5")

Great tutorial! Thanks for the write up.

A few notes/questions...

1\. Scaling

The buttons of the Visual Editor window may overlap each other depending on the screen scale. Same for the toolbar buttons of the resource manager. This is not a comprehensive list of UI items which do not position/size themselves accordingly to the screen scale. There may need to be a global pass on that.

2\. Removing overrides

Is there a way to remove overrides? This question is also asked on the "Editor - Overriding Resources" guide \[1\]. Please consider linking guides together if someone wants to learn more on a specific topic.

\[1\] [@editor-overriding-resources](https://mod.io/g/baldursgate3/r/editor-overriding-resources)

3\. General layout

Please consider (1) increasing the size of the red call outs on the screenshots, and (2) putting the screen shots and the relevant instructions side-by-side; screenshots could be clickable and open a full screen modal to accommodate zooming.

[M](https://mod.io/g/baldursgate3/u/modiouser3731364)

[Mega4e1](https://mod.io/g/baldursgate3/u/modiouser3731364)• [1y ago](https://mod.io/g/baldursgate3/r/editor-navigation#1121048 "12/11/2024, 09:33 AM GMT-5")

Hi everyone!
how do I open published mods for editing? (.pak)

[W](https://mod.io/g/baldursgate3/u/w3dojo)

[w3dojo](https://mod.io/g/baldursgate3/u/w3dojo)• [1y ago](https://mod.io/g/baldursgate3/r/editor-navigation#1128564 "12/17/2024, 10:04 PM GMT-5")

The file extension \`.pak\` is used for game mods whose files have been bundled into a single directory (or folder if your picky about semantics) then compressed, much like zip files. In fact, pak files can sometimes use the same compression algorithm as a zip file, however, I don't think that's what is being used here. There is software that can be obtained for decompressing the pak files. Another option is to look for modules published with open source code. GitHub is the best place to look, and I can testify that there are many that exists on GH with the source code completely open to the public.

[M](https://mod.io/g/baldursgate3/u/morguerhea)

[MorgueRhea](https://mod.io/g/baldursgate3/u/morguerhea)• [1y ago](https://mod.io/g/baldursgate3/r/editor-navigation#1046408 "10/19/2024, 11:47 AM GMT-4")

Could you please make a guide on how to create passive toggles?

[S](https://mod.io/g/baldursgate3/u/lazyninja4)

[SleepyDrag0n](https://mod.io/g/baldursgate3/u/lazyninja4)• [1y ago](https://mod.io/g/baldursgate3/r/editor-navigation#1001573 "9/22/2024, 09:43 PM GMT-4")

I'm running into the same problem where the ok and apply buttons are grayed out. The only one that highlights is cancel. I set the source path, to ...\\Baldurs Gate 3\\Data\\MyMod\\Data. I'm thinking i'm missing something simple, but i'm not sure what.

[S](https://mod.io/g/baldursgate3/u/sunbleached)

[Sunbleached](https://mod.io/g/baldursgate3/u/sunbleached)• [45d ago](https://mod.io/g/baldursgate3/r/editor-navigation#1534609 "11/16/2025, 10:50 AM GMT-5")

do you actually have the Baldurs Gate 3\\Data\\MyMod\\Data folder on your computer? won't work without it

[A](https://mod.io/g/baldursgate3/u/astroleek)

[Astroleek](https://mod.io/g/baldursgate3/u/astroleek)• [1y ago](https://mod.io/g/baldursgate3/r/editor-navigation#995323 "9/19/2024, 11:20 AM GMT-4")

When I go into game mode, none of the game UI shows up. I can't open inventory or anything either. Does anyone know how to fix this?

[M](https://mod.io/g/baldursgate3/u/montra)

[Montra](https://mod.io/g/baldursgate3/u/montra)• [1y ago](https://mod.io/g/baldursgate3/r/editor-navigation#978499 "9/9/2024, 12:42 AM GMT-4")

Having issues applying the NAT\_Lava to the statue. The Apply and Ok buttons are simply greyed out. I went back to the other guides to double check I had set up the file path's correctly and all seem to be in order. I'm unsure on how to proceed from here.

[7](https://mod.io/g/baldursgate3/u/7darkscythe)

[7darkscythe](https://mod.io/g/baldursgate3/u/7darkscythe)• [1y ago](https://mod.io/g/baldursgate3/r/editor-navigation#979213 "9/9/2024, 02:51 PM GMT-4")

fixed it, after "When asked "Do you want to keep the same package structure?", pick "Yes" . The resource is now editable!" it will show you a new window import it and click on it

[D](https://mod.io/g/baldursgate3/u/danie1288)

[Danieamian](https://mod.io/g/baldursgate3/u/danie1288)• [1y ago](https://mod.io/g/baldursgate3/r/editor-navigation#980256 "9/10/2024, 07:33 AM GMT-4")

Could you clarify on what you mean? For me, after clicking "Override in this active mod" I get 4 dialogue boxes that appear, 3 of which don't seem to be in this guide.
\- Are you sure you want to override 1 resource?
\- Do you want to keep the same package structure?
\- Do you want to use: DEC\_GEN\_Statue\_Wizard\_B\_Broken\_A.GR2 as the source file?
\- Set the Source Asset Path in the Editor Configuration options. Cannot add new Visual Resource.

I have the same issue has the original post but it might be a different cause?

2 replies

[M](https://mod.io/g/baldursgate3/u/montra)

[Montra](https://mod.io/g/baldursgate3/u/montra)• [1y ago](https://mod.io/g/baldursgate3/r/editor-navigation#980005 "9/10/2024, 12:10 AM GMT-4")

This worked, thanks for the help!

[A](https://mod.io/g/baldursgate3/u/aquadire)

[Aquadire](https://mod.io/g/baldursgate3/u/aquadire)• [1y ago](https://mod.io/g/baldursgate3/r/editor-navigation#978687 "9/9/2024, 04:56 AM GMT-4")

Having the same issue

[M](https://mod.io/g/baldursgate3/u/modiouser2077089)

[ModioUser2077089](https://mod.io/g/baldursgate3/u/modiouser2077089)• [1y ago](https://mod.io/g/baldursgate3/r/editor-navigation#975931 "9/7/2024, 06:54 PM GMT-4")

When I selected the root template for the statue, I selected "No" initially. Now whenever I go to do the same step, it doesn't give me that dialogue box anymore to where I could say "yes", even if I make a new mod and go through the steps from scratch. Is there any way to get that dialogue box back?

[T](https://mod.io/g/baldursgate3/u/tdakh)

[Tdakh](https://mod.io/g/baldursgate3/u/tdakh)• [1y ago](https://mod.io/g/baldursgate3/r/editor-navigation#975430 "9/7/2024, 02:31 PM GMT-4")

Last bit mentions noting the camera or object coordinates and being able to fly to said coordinate directly, but doesn't mention how to actually do so. :(

[S](https://mod.io/g/baldursgate3/u/dragonfruit16)

[SlicedDF](https://mod.io/g/baldursgate3/u/dragonfruit16)• [1y ago](https://mod.io/g/baldursgate3/r/editor-navigation#978460 "9/9/2024, 12:05 AM GMT-4")

you fly using the editor camera (Ctrl+Shift+G) and teleport your character with Ctrl+T but I am not sure how to edit the position of an item manually.

[I](https://mod.io/g/baldursgate3/u/ivylust)

[IvyLust](https://mod.io/g/baldursgate3/u/ivylust)• [1y ago](https://mod.io/g/baldursgate3/r/editor-navigation#973518 "9/6/2024, 12:45 PM GMT-4")

i can't apply the NAT\_Lava\_Fall\_A\_Animated. It said im on "public" instance maybe i can't mod in this instance i don't know but i done step by step ur guide and nothing work :s

[S](https://mod.io/g/baldursgate3/u/sed35)

[Sedling](https://mod.io/g/baldursgate3/u/sed35)• [1y ago](https://mod.io/g/baldursgate3/r/editor-navigation#973837 "9/6/2024, 05:02 PM GMT-4")

You probably haven't set up the source asset data path. This page might help [https://mod.io/g/baldursgate3/r/getting-started-creating-a-new-mod.](https://mod.io/g/baldursgate3/r/getting-started-creating-a-new-mod.)

[S](https://mod.io/g/baldursgate3/u/dragonfruit16)

[SlicedDF](https://mod.io/g/baldursgate3/u/dragonfruit16)• [1y ago](https://mod.io/g/baldursgate3/r/editor-navigation#978427 "9/8/2024, 11:35 PM GMT-4")

Love u 4 this

[D](https://mod.io/g/baldursgate3/u/modiouser2076193)

[D3DBOY](https://mod.io/g/baldursgate3/u/modiouser2076193)• [1y ago](https://mod.io/g/baldursgate3/r/editor-navigation#972613 "9/5/2024, 07:56 PM GMT-4")

So can I not move objects around?

[T](https://mod.io/g/baldursgate3/u/thunder4884)

[Thunder4884](https://mod.io/g/baldursgate3/u/thunder4884)• [1y ago](https://mod.io/g/baldursgate3/r/editor-navigation#973323 "9/6/2024, 09:28 AM GMT-4")

This is just a conjecture but it seems like mod.io and Larian studios don't want to give users full reigns over level creation and home brew stories just yet. So, the public user mode doesn't provide access to asset transforms, object adding, and stuff like that.

Last updated

1y

Reading time

7 min read

Views

19,848

Comments

22

[G\\
\\
GrumpyWashbear](https://mod.io/g/baldursgate3/u/grumpywashbear/r)

Follow GrumpyWashbear

- [Guide](https://mod.io/g/baldursgate3/r/editor-navigation#guide)
- [Opening or Creating a Project](https://mod.io/g/baldursgate3/r/editor-navigation#heading-1)
- [Loading a Level](https://mod.io/g/baldursgate3/r/editor-navigation#heading-2)
- [Exploring a Level](https://mod.io/g/baldursgate3/r/editor-navigation#heading-3)
- [Editing Templates](https://mod.io/g/baldursgate3/r/editor-navigation#heading-4)
- [Resources](https://mod.io/g/baldursgate3/r/editor-navigation#heading-5)
- [Testing while Playing in Editor](https://mod.io/g/baldursgate3/r/editor-navigation#heading-6)
- [Discussion](https://mod.io/g/baldursgate3/r/editor-navigation#discussion)

[Editor](https://mod.io/g/baldursgate3/r?tags=Editor) [English](https://mod.io/g/baldursgate3/r?tags=English) [Official](https://mod.io/g/baldursgate3/r?tags=Official)

An overview of how to use the editor's basic functions.

Share

Report guide

---
# SOURCE: https://mod.io/g/baldursgate3/r/ui-basic-setup
---

[Browse games](https://mod.io/g)

Browse games

[My library](https://mod.io/library)

My library

[My content](https://mod.io/content)

My content

My account

mod.io

mod.io

[All games](https://mod.io/g) [Baldur's Gate 3](https://mod.io/g/baldursgate3) [Guides](https://mod.io/g/baldursgate3/r) [English](https://mod.io/g/baldursgate3/r?tags=English) UI Modding - General Setup

UI Modding - General Setup

Share

Report

Follow

UI modding is done through XAML editing. Mods have access to the same functionality and data as the existing BG3 UIs, so go wild!

## External Links

- For all possible info about XAML coding and the Microsoft WPF framework that our UI is based on:

[https://learn.microsoft.com/en-us/dotnet/desktop/wpf/getting-started/?view=netframeworkdesktop-4.8](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/getting-started/?view=netframeworkdesktop-4.8)

- For all the Noesis-specific info:

[https://www.noesisengine.com/docs/Gui.Core.Index.html](https://www.noesisengine.com/docs/Gui.Core.Index.html)
  - Noesis is the third party we use. It replicates the Microsoft WPF framework. We use version 3.1.6 of the Noesis framework.!

## Setup

You’ll first have to get your mod created, as explained in the Getting Started: Creating a New Mod guide.

Once that is done, we can start adding the UI-specific requirements to the mod.

### Setting Up the Folder Structure

Inside your mod project’s folder (`...\steamapps\common\Baldurs Gate 3\Data\[yourmodhere]\`), you’ll need to set up the file and folder structure according to the image below:

[![](https://image.modcdn.io/members/63c0/31088933/profile/ui_1.png)](https://image.modcdn.io/members/63c0/31088933/profile/ui_1.png)

As for what these folders and files specifically do...

| **Folder / File** | Notes |
| --- | --- |
| **Assets** | Folder to organize all your assets (images and the like). All assets should be in the `.dds` format, and ideally, defined inside your Resources. There's more detail on the DDS conversion settings later in this guide. |
| **Library** | You can have as many resource libraries (templates and styles that use your Resources data) in here as you like. <br>There are two required files. These two can contain templates and styles on their own, as well as a merged dictionary with all the dictionary .xamls inside this folder.<br>`Lib_Controller.xaml` \- This dictionary is loaded in controller mode.<br>`Lib_Keyboard.xaml` \- This dictionary is loaded in keyboard and mouse mode. |
| **Pages** | Folder to organize all your actual UIs. |
| **Resources** | Folder containing the required `Resources.xaml` as well as all your extra resource `.xaml`files, like registered images, brushes, fonts, colors, etc.<br>`Resources.xaml` \- Contains all the registered asset resources as well as single line resource declarations. |
| **StateMachines** | This folder should contain only the following two files. They are the link to our UI; this is where the UI flow is determined and where your pages are used.<br>`Controller.xaml` \- Your modified UIs for keyboard and mouse mode.<br>`Keyboard.xaml` \- Your modified UIs for controller mode. |
| `metadata.lsf` | This metadata file is required to be able to preload some file info from the `.DDS` assets inside the Assets folder. |

> **Note:** Resources are loaded before the libraries since their keys are used inside the libraries. All mod resources and libraries are loaded before the mod statemachines are applied.

### Assets

Although the used images inside your .xaml files have the `.png` extension, in the background that extension gets swapped for `.DDS`. The UI assets used need to be a specific `.DDS` format.

#### DDS Conversion Settings

```makefile
if image.mode == "RGBA":
if sRGBBool:
target_mode = "BC7_UNORM_SRGB"
else:
target_mode = "BC7_UNORM"
if image.mode == "RGB":
target_mode = "BC1_UNORM"
```

### Resources

Resources are a collection of [ResourceDictionaries](https://www.noesisengine.com/docs/Gui.Core._ResourceDictionary.html#noesis_doc_wrap) that can be merged into the **ResourceDictionaryContained** inside `Resources.xaml`. If you don't see the need to organize your resources in multiple files, all of them can be directly inside `Resources.xaml`.

Resources are all:

- [fonts](https://www.noesisengine.com/docs/Gui.Core._FontFamily.html)

- [colors](https://learn.microsoft.com/en-us/dotnet/api/system.windows.media.color?view=windowsdesktop-8.0)

- [brushes](https://www.noesisengine.com/docs/Gui.Core._Brush.html#noesis_doc_wrap)

- [imagesources](https://www.noesisengine.com/docs/Gui.Core._ImageSource.html#noesis_doc_wrap)

- predefined variable types


The following shows an example of a `Resources.xaml` file.

```xml
<ResourceDictionary xmlns="https://schemas.microsoft.com/winfx/2006/xaml/presentation"
                    xmlns:x="https://schemas.microsoft.com/winfx/2006/xaml"
                    xmlns:sys="clr-namespace:System;assembly=mscorlib">

    <ResourceDictionary.MergedDictionaries>
      <ResourceDictionary Source="/Core;component/Resources/OtherResourceFile.xaml" />
    </ResourceDictionary.MergedDictionaries>

    <BitmapImage x:Key="generalWarningIcon" UriSource="/ModBrowser;component/Assets/ico_warning_general.png"/>
    <BitmapImage x:Key="modioIcon" UriSource="/ModBrowser;component/Assets/ico_modio.png"/>
    <BitmapImage x:Key="splashScreenPanelDivider" UriSource="/ModBrowser;component/Assets/mods_introPane_panelDivider.png"/>
    <BitmapImage x:Key="splashScreenBg" UriSource="/ModBrowser;component/Assets/mods_introPane_panelBG.png"/>

    <FontFamily x:Key="DefaultFont" >pack://application:,,,/Core;component/Assets/Fonts/Alegreya/#Alegreya</FontFamily>
    <FontFamily x:Key="SpecialFont" >pack://application:,,,/Core;component/Assets/Fonts/AlegreyaSans/#Alegreya Sans</FontFamily>

    <Color x:Key="accent00Color">#584537</Color>
    <Color x:Key="accent25Color">#7d604a</Color>
    <Color x:Key="baseColor">#af8768</Color>
    <Color x:Key="accent75Color">#cbac95</Color>
    <Color x:Key="accent100Color">#E6DBC2</Color>
    <Color x:Key="disabledPadTxtColor">#7C6354</Color>

    <SolidColorBrush x:Key="LS_accent100TxtColor" Color="{StaticResource accent100Color}"/>
    <SolidColorBrush x:Key="LS_accent75TxtColor" Color="{StaticResource accent75Color}"/>
    <SolidColorBrush x:Key="LS_baseTxtColor" Color="{StaticResource baseColor}"/>
    <SolidColorBrush x:Key="LS_accent25TxtColor" Color="{StaticResource accent25Color}"/>

    <System:Double x:Key="InvSlotSize">116</System:Double>
    <System:Double x:Key="FilterSlotSize">84</System:Double>

    <Thickness x:Key="extraSectionPadding">0,0,0,0</Thickness>
    <Thickness x:Key="TextTopBottomMargin">0,12</Thickness>

</ResourceDictionary>
```

### Library

The Library contains a collection of [ResourceDictionaries](https://www.noesisengine.com/docs/Gui.Core._ResourceDictionary.html#noesis_doc_wrap) that can be merged into the `Lib_<>.xaml` file specific to your input method

- Keyboard and mouse mode will load`Lib_Keyboard.xaml`

- Controller mode will load `Lib_Controller.xaml`


You can organize your templates and styles directly inside these libraries, or you can decide to organise them in extra files and merge these inside the required keyboard and controller libraries.

Following is an example of `Lib_Keyboard.xaml`

```xml
<ResourceDictionary xmlns="https://schemas.microsoft.com/winfx/2006/xaml/presentation"
                    xmlns:x="https://schemas.microsoft.com/winfx/2006/xaml"
                    xmlns:sys="clr-namespace:System;assembly=mscorlib">

    <ResourceDictionary.MergedDictionaries>
      <ResourceDictionary Source="/MyMod;component/Library/Buttons.xaml" />
      <ResourceDictionary Source="/MyMod;component/Library/Panels.xaml" />
    </ResourceDictionary.MergedDictionaries>

    <Style x:Key="StyleA" TargetType="ContentControl">
      ...
    </Style>

    <ControlTemplate x:Key="ListItem" TargetType="ListBoxItem">
      <Grid x:Name="Root">
        ...
      <Grid>
      <ControlTemplate.Triggers>
        ...
      </ControlTemplate.Triggers>
    <ControlTemplate>

</ResourceDictionary>
```

### StateMachines

If your mod is only for keyboard and mouse **or** controller this folder will only contain one file. If the mod applies to both UI modes, it will contain two.

> **Note:** Without these files, the Pages you add inside your mod will not be accessible, because the framework will not recognise a change to the UI flow.

## Other Notes

When you want to mod the UI, whether it’s adding a panel, overriding a panel or overhauling the flow, your mod will link into the UI StateMachine. The StateMachine is the flow of the UI - it has UI states defined and linked to each other.

> **Note:** When loading mods the order matters. A mod can be added that defines new moddable root states for other mods to hook into. A mod can overhaul the entire UI, but you want one of those to be overridden by a next mod. While loading, the StateMachine is built mod per mod and the final result is the sum of all the mods in sequence.

## Guide Links

The different ways to mod the UI are:

- Overriding UI State

- [**Extending UI State**](https://mod.io/g/baldursgate3/r/ui-extending-the-ui) \- Guide available.

- Restyling UI Data


[G\\
\\
GrumpyWashbear](https://mod.io/g/baldursgate3/u/grumpywashbear/r)

Follow GrumpyWashbear

Log in to join the discussion!

[M](https://mod.io/g/baldursgate3/u/modiouser5985789)

[ModioUser5985789](https://mod.io/g/baldursgate3/u/modiouser5985789)• [80d ago](https://mod.io/g/baldursgate3/r/ui-basic-setup#1506646 "10/12/2025, 10:31 AM GMT-4")

Guide Links
The different ways to mod the UI are:

Overriding UI State

Extending UI State - Guide available.

Restyling UI Data

but only one guide

[S](https://mod.io/g/baldursgate3/u/splashofblue)

[SplashOfBlue](https://mod.io/g/baldursgate3/u/splashofblue)• [1y ago](https://mod.io/g/baldursgate3/r/ui-basic-setup#995799 "9/19/2024, 05:08 PM GMT-4")

when you mention this
"Inside your mod project’s folder (...\\steamapps\\common\\Baldurs Gate 3\\Data\\\[yourmodhere\]\\), you’ll need to set up the file and folder structure according to the image below:"
Under which folder after Data are we supposed to place the UI files, as when creating a new mod no \[modname\] folder is created directly under Data, but instead under \[Projects\] , \[Mods\], and \[Public\]

[D](https://mod.io/g/baldursgate3/u/dphkraken)

[DPhKraken](https://mod.io/g/baldursgate3/u/dphkraken)• [1y ago](https://mod.io/g/baldursgate3/r/ui-basic-setup#1037441 "10/14/2024, 01:52 AM GMT-4")

It's \[Mods\].
Historically it's been \[Public/Game\], but it changed with Patch 7.

Last updated

1y

Reading time

5 min read

Views

3,489

Comments

3

[G\\
\\
GrumpyWashbear](https://mod.io/g/baldursgate3/u/grumpywashbear/r)

Follow GrumpyWashbear

- [Guide](https://mod.io/g/baldursgate3/r/ui-basic-setup#guide)
- [External Links](https://mod.io/g/baldursgate3/r/ui-basic-setup#heading-1)
- [Setup](https://mod.io/g/baldursgate3/r/ui-basic-setup#heading-2)
- [Setting Up the Folder Structure](https://mod.io/g/baldursgate3/r/ui-basic-setup#heading-3)
- [Assets](https://mod.io/g/baldursgate3/r/ui-basic-setup#heading-4)
- [DDS Conversion Settings](https://mod.io/g/baldursgate3/r/ui-basic-setup#heading-5)
- [Resources](https://mod.io/g/baldursgate3/r/ui-basic-setup#heading-6)
- [Library](https://mod.io/g/baldursgate3/r/ui-basic-setup#heading-7)
- [StateMachines](https://mod.io/g/baldursgate3/r/ui-basic-setup#heading-8)
- [Other Notes](https://mod.io/g/baldursgate3/r/ui-basic-setup#heading-9)
- [Guide Links](https://mod.io/g/baldursgate3/r/ui-basic-setup#heading-10)
- [Discussion](https://mod.io/g/baldursgate3/r/ui-basic-setup#discussion)

[English](https://mod.io/g/baldursgate3/r?tags=English) [Official](https://mod.io/g/baldursgate3/r?tags=Official) [UI](https://mod.io/g/baldursgate3/r?tags=UI)

A summary of all the links and basic setup information needed to start creating UI mods.

Share

Report guide

---
# SOURCE: https://mod.io/g/baldursgate3/r/ui-extending-the-ui
---

[Browse games](https://mod.io/g)

Browse games

[My library](https://mod.io/library)

My library

[My content](https://mod.io/content)

My content

My account

mod.io

mod.io

[All games](https://mod.io/g) [Baldur's Gate 3](https://mod.io/g/baldursgate3) [Guides](https://mod.io/g/baldursgate3/r) [English](https://mod.io/g/baldursgate3/r?tags=English) UI Modding - Extending

UI Modding - Extending

Share

Report

Follow

When extending a state, you can:

- Add additional UI panels to existing states

- Add hooks to existing or new UI states.

- Adjust state properties


If you don’t want to adjust a state property or don’t want to add something to a specific section, it simply shouldn’t be added.

> **Warning:** Copying a state property into your extended state will make your version of the property the final version. If the original state needs a fix and changes this property, your mod will override it when it gets loaded on top, nullifying the fix on the original.

## Examples

### Adding Hooks

The following example adds hooks for UI states to the moddable GameRoot state.

The original:

```xml
<!-- Original -->
<ls:State Name = "GameRoot" Layout = "Common" Owner = "All" IsModdable="True">
    <ls:State.Events>
        <ls:StateEvent Name = "GE.OnStateLoadingStart">
            <ls:StateEvent.Actions>
                <ls:SetSubstate Name="Loading"/>
            </ls:StateEvent.Actions>
        </ls:StateEvent>
    </ls:State.Events>
</ls:State>
```

The modded:

```xml
<!-- Mod -->
<ls:State Name = "GameRoot" ModType="Extend">
    <ls:State.Events>
        <ls:StateEvent Name = "GE.OnStateMainMenu">
            <ls:StateEvent.Actions>
                <ls:SetSubstate Name="Eula"/>
            </ls:StateEvent.Actions>
        </ls:StateEvent>
        <ls:StateEvent Name = "GE.OnStateRunning">
            <ls:StateEvent.Actions>
                <ls:SetSubstate Name="Running"/>
            </ls:StateEvent.Actions>
        </ls:StateEvent>
        <ls:StateEvent Name = "GE.OnStateLobby">
            <ls:StateEvent.Actions>
                <ls:SetSubstate Name="Lobby"/>
            </ls:StateEvent.Actions>
        </ls:StateEvent>
        <ls:StateEvent Name = "GE.OnBusyShow">
            <ls:StateEvent.Actions>
                <ls:PushState Name="Busy"/>
            </ls:StateEvent.Actions>
        </ls:StateEvent>
        <ls:StateEvent Name = "GE.OnSaveShow">
            <ls:StateEvent.Actions>
                <ls:PushState Name="Saving"/>
            </ls:StateEvent.Actions>
        </ls:StateEvent>
        <ls:StateEvent Name = "GE.OnMovieShow">
            <ls:StateEvent.Actions>
                <ls:PushState Name="Movie"/>
            </ls:StateEvent.Actions>
        </ls:StateEvent>
        <ls:StateEvent Name = "GE.EditorMode">
            <ls:StateEvent.Actions>
                <ls:RemoveAllSubstates/>
            </ls:StateEvent.Actions>
        </ls:StateEvent>
    </ls:State.Events>
</ls:State>
```

### Adding a Panel

Original:

```xml
<!-- Original -->
<ls:State Name = "PlayerHUD" Layout = "Player" Owner = "Player" IsModdable=True>
    <ls:State.Widgets>
        <ls:StateWidget Filename="/MainUI;component/Pages/Overlay.xaml" Layer="Notifications"/>
        <ls:StateWidget Filename="/MainUI;component/Pages/HudIndicator.xaml" Layer="HUD" IgnoreHitTest="True"/>
        <ls:StateWidget Filename="/MainUI;component/Pages/OverheadInfo.xaml" Layer="HUD" IgnoreHitTest="True"/>
        <ls:StateWidget Filename="/MainUI;component/Pages/HotBar.xaml" Layer="HUDTop"/>
        <ls:StateWidget Filename="/MainUI;component/Pages/Minimap.xaml" Layer="HUD"/>
        <ls:StateWidget Filename="/MainUI;component/Pages/TargetInfo.xaml" Layer="HUD" IgnoreHitTest="True"/>
        <ls:StateWidget Filename="/MainUI;component/Pages/PlayerPortraits.xaml" Layer="PopupPanels"/>
        <ls:StateWidget Filename="/MainUI;component/Pages/TurnModeInfo.xaml" Layer="HUD"/>
        <ls:StateWidget Filename="/MainUI;component/Pages/CombatLog.xaml" Layer="HUD"/>
        <ls:StateWidget Filename="/MainUI;component/Pages/CombatantsOverlay.xaml" Layer="HUD"/>
        <ls:StateWidget Filename="/MainUI;component/Pages/CursorText.xaml" Layer="PopupPanels"/>
        <ls:StateWidget Filename="/MainUI;component/Pages/DragAndDropPreview.xaml" Layer="DragAndDrop" IgnoreHitTest="True"/>
        <ls:StateWidget Filename="/MainUI;component/Pages/PassiveRoll.xaml" Layer="PopupPanels"/>
        <ls:StateWidget Filename="/MainUI;component/Pages/AlwaysOnTopOverlay.xaml" Layer="PopupPanels"/>
    </ls:State.Widgets>
    <ls:State.InitialSubstates>
        <ls:InitialSubstate Name="PlayerPortraits" Metadata="InHUD"/>
    </ls:State.InitialSubstates>
    <ls:State.Events>
        <ls:StateEvent Name = "OpenSelectionFlyOut">
            <ls:StateEvent.Actions>
                <ls:AddSubstate Name="SelectionFlyOut"/>
            </ls:StateEvent.Actions>
        </ls:StateEvent>
    </ls:State.Events>
</ls:State>
```

Modded:

```xml
<!-- Mod -->
<ls:State Name = "PlayerHUD" ModType="Extend">
    <ls:State.Widgets>
        <ls:StateWidget Filename="TestModPanel.xaml" Layer="HUD"/>
    </ls:State.Widgets>
</ls:State>
```

## Tutorial

For a simple example, we’re going to add a UI to the MainMenu, in which we will add a button. This button will open a new panel. This panel on the MainMenu could then be used as a sort of hub to link your extension panels into.

For the initial mod setup, please follow the steps inside [**Getting Started: Creating a New Mod**](https://mod.io/g/baldursgate3/r/getting-started-creating-a-new-mod).

We've provided an [**empty UI mod pack**](https://baldursgate3.game/mods/guides/GUI.zip) for you to use in this tutorial.

Unzip it into the main folder of the mod you just created. The resulting structure should look something like this:

[![](https://image.modcdn.io/members/63c0/31088933/profile/ext_01.png)](https://image.modcdn.io/members/63c0/31088933/profile/ext_01.png)

For this example, we’ll just address the Keyboard version of the UI, so let's open the **Keyboard.xaml** inside `[yourmod]/GUI/StateMachines/Keyboard.xaml`.

Most of the UI states found inside our main UI are moddable, so we’ll include the MainMenu state in our Keyboard statemachine, inside the `ls:StateMachine.States` section.

We’ll also add the **Extend** Modtype to it to let the system know that we are going to extend it (by adding our own panel).

```xml
<ls:State Name = "MainMenu" ModType="Extend">

</ls:State>
```

Next, we’ll need to decide on a name for our new panel. Let’s go with `TestModHub`. Add it to the state widgets of the PlayerHUD state.

```xml
<ls:State Name = "MainMenu" ModType="Extend">
  <ls:State.Widgets>
    <ls:StateWidget Filename="TestModHub.xaml" Layer="HUD"/>
  </ls:State.Widgets>
</ls:State>
```

Our UI is visually organised in layers. Above, for our TestModHub panel, we select the **HUD** layer. This is our lowest visual layer. There is only one layer below it: the **Default** layer, which is set if you don’t select a layer.

Now, we can create a new `.xaml` file inside the **Pages** folder. The Pages in this folder are the actual UIs that will show up in-game. The package of files in this guide includes a `PageBlueprint.xaml` file that you can copy to use as the base for your new file.

`[yourmod]/GUI/Pages/TestModHub.xaml`

Open your newly created file.

1. Change the `x:Name` property to the UI name. In this case, `TestModPanel`.

2. Add the `<StackPanel>` section. For test purposes, we’ll go with this:


```xml
<StackPanel Orientation="Vertical" HorizontalAlignment="Right" VerticalAlignment="Top" Margin="0,50,50,0" Background="Magenta" MinWidth="100" MinHeight="100">

    </StackPanel>
```

Your full file should now look like this:

```xml
<ls:UIWidget x:Name="TestModPanel"
             xmlns="https://schemas.microsoft.com/winfx/2006/xaml/presentation"
             xmlns:x="https://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:mc="https://schemas.openxmlformats.org/markup-compatibility/2006"
             xmlns:ls="clr-namespace:ls;assembly=Code"
             xmlns:System="clr-namespace:System;assembly=mscorlib"
             xmlns:noesis="clr-namespace:NoesisGUIExtensions;assembly=Noesis.GUI.Extensions"
             xmlns:b="https://schemas.microsoft.com/xaml/behaviors"
             xmlns:d="https://schemas.microsoft.com/expression/blend/2008"
             mc:Ignorable="d"
             d:DataContext="{d:DesignInstance {x:Type ls:DCWidget}, IsDesignTimeCreatable=True}">

    <StackPanel Orientation="Vertical" HorizontalAlignment="Right" VerticalAlignment="Top" Margin="0,50,50,0" Background="Magenta" MinWidth="100" MinHeight="100">

    </StackPanel>

</ls:UIWidget>
```

Save your work, and let’s test it out. There is no way to load the Main Menu in editor, so you’ll have to test it locally in the actual game.

**Before**

[![](https://image.modcdn.io/members/63c0/31088933/profile/ext_02.png)](https://image.modcdn.io/members/63c0/31088933/profile/ext_02.png)

**After**

[![](https://image.modcdn.io/members/63c0/31088933/profile/ext_03.png)](https://image.modcdn.io/members/63c0/31088933/profile/ext_03.png)

Now, let’s add two buttons into the **StackPanel.** One will be a placebo button, just to show how using a stackpanel set up with Orientation=”Vertical” will arrange the buttons underneath each other, and to show that the Stackpanel scales to its content.

The other button will be functional. We’ll give it a **Command** and a **CommandParameter**.

For the **ModPanel** to perform an action, it needs a **Command**. We bind the **CustomEvent** command to it. This command is used to send events to our StateMachine. We add the name of the event into the **CommandParameter**.

```xml
<ls:LSButton x:Name="ModPanel" Style="{StaticResource BrownButtonStyle}" Content="Open Mod Panel" Command="{Binding CustomEvent}" CommandParameter="ToggleModPanel"/>
<ls:LSButton x:Name="Placebo" Style="{StaticResource BrownButtonStyle}" Content="Placebo"/>
```

[![](https://image.modcdn.io/members/63c0/31088933/profile/ext_04.png)](https://image.modcdn.io/members/63c0/31088933/profile/ext_04.png)

We’ll need to add our new custom event handling to the **StateMachine**, opening another UI panel.

For this, go back to the Keyboard.xaml StateMachine and add the **Events** section to our extended **State**. Inside this Events section, we will add our custom event handling. The Events section can contain multiple events.

```xml
<ls:State.Events>
    <ls:StateEvent Name = "ToggleModPanel">
        <ls:StateEvent.Actions>
            <ls:SetSubstate Name="ModPanelState"/>
        </ls:StateEvent.Actions>
    </ls:StateEvent>
</ls:State.Events>
```

Our event handling will have one action: setting the **SubState** of the MainMenu State. Uing the **SetSubState** action, a State can branch into several SubStates, or it can set a single SubState.

After adding the handling, we need to create the State that needs to be set as the SubState. We’ll add the **HideStatesBelow** property to this State to showcase that this property gives you the ability to hide all the previous states. The Widget that this State will open is the **TestModPanel.xaml**, which we will create in a following step.

```xml
<ls:State Name = "ModPanelState" HideStatesBelow = "True">
    <ls:State.Widgets>
        <ls:StateWidget Filename="TestModPanel.xaml" Layer="Panels"/>
    </ls:State.Widgets>
</ls:State>
```

Now we’ll create the Widget that is used in our newly added state.

This time we’ll create a **Grid** instead of a StackPanel. This is a different type of container to hold UIElements. Without these containers, the **UIWidget** itself can only hold one UIElement.

We’ll also add a CloseButton which we will position at the top right of the new UI panel, and we’ll add a **TextBlock** in the center of our Panel.

Make a new Page: `[yourmod]/GUI/Pages/TestModPanel.xaml`

```xml
<ls:UIWidget x:Name="TestModPanel"
             xmlns="https://schemas.microsoft.com/winfx/2006/xaml/presentation"
             xmlns:x="https://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:mc="https://schemas.openxmlformats.org/markup-compatibility/2006"
             xmlns:ls="clr-namespace:ls;assembly=Code"
             xmlns:System="clr-namespace:System;assembly=mscorlib"
             xmlns:noesis="clr-namespace:NoesisGUIExtensions;assembly=Noesis.GUI.Extensions"
             xmlns:b="https://schemas.microsoft.com/xaml/behaviors"
             xmlns:d="https://schemas.microsoft.com/expression/blend/2008"
             mc:Ignorable="d"
             d:DataContext="{d:DesignInstance {x:Type ls:DCWidget}, IsDesignTimeCreatable=True}">

    <Grid HorizontalAlignment="Center" VerticalAlignment="Center" Background="#55000000" MinWidth="500" MinHeight="500">

        <ls:LSButton x:Name="CloseButton" Style="{StaticResource CloseButton}" Margin="0,20,20,0" Command="{Binding CustomEvent}" CommandParameter="ClosePanel" HorizontalAlignment="Right" VerticalAlignment="Top" />
        <TextBlock HorizontalAlignment="Center" VerticalAlignment="Center" Text="Gather Your Party"/>

    </Grid>

</ls:UIWidget>
```

[![](https://image.modcdn.io/members/63c0/31088933/profile/ext_05.png)](https://image.modcdn.io/members/63c0/31088933/profile/ext_05.png)

If you test the changes thus far, you’ll notice that this pressing this CloseButton doesn’t close your UI panel. To get it working correctly, you’ll need to add the custom event handling to your **ModPanelState**, this time with the **RemoveState** action.

```xml
<ls:State.Events>
    <ls:StateEvent Name = "ClosePanel">
        <ls:StateEvent.Actions>
            <ls:RemoveState/>
        </ls:StateEvent.Actions>
    </ls:StateEvent>
</ls:State.Events>
```

With that, this very basic UI mod should be working.

[G\\
\\
GrumpyWashbear](https://mod.io/g/baldursgate3/u/grumpywashbear/r)

Follow GrumpyWashbear

Log in to join the discussion!

[R](https://mod.io/g/baldursgate3/u/rkirgizov)

[rkirgizov](https://mod.io/g/baldursgate3/u/rkirgizov)• [319d ago](https://mod.io/g/baldursgate3/r/ui-extending-the-ui#1217224 "2/14/2025, 07:54 PM GMT-5")

Hi!

Is it possible to find out the status of a player from the UI?
I tried different ways, but nothing works...
I didn't find anything like that in the code.

I need something like that.
Please help.

Condition Binding="{Binding CurrentPlayer.SelectedCharacter.StatusEffects.Status.IDString}" Value="SHIELD\_OF\_FAITH"

Condition Binding="{Binding CurrentPlayer.SelectedCharacter.HasStatus}" Value="SHIELD\_OF\_FAITH"

[P](https://mod.io/g/baldursgate3/u/modiouser3325978)

[Pixelaters](https://mod.io/g/baldursgate3/u/modiouser3325978)• [1y ago](https://mod.io/g/baldursgate3/r/ui-extending-the-ui#1072124 "11/4/2024, 04:01 PM GMT-5")

Got the magnetta block to eventually show, I had vortex as my mod manager so dragging it into vortex worked for me

[F](https://mod.io/g/baldursgate3/u/florodude)

[florodude](https://mod.io/g/baldursgate3/u/florodude)• [1y ago](https://mod.io/g/baldursgate3/r/ui-extending-the-ui#1013161 "9/30/2024, 03:49 PM GMT-4")

Has anybody gotten this to work recently?

[S](https://mod.io/g/baldursgate3/u/slafniy)

[slafniy](https://mod.io/g/baldursgate3/u/slafniy)• [1y ago](https://mod.io/g/baldursgate3/r/ui-extending-the-ui#1028738 "10/9/2024, 09:40 AM GMT-4")

Kinda. I'm trying to figure out how UI works, I'm using this as a reference. My issue was trying to Extend PlayerHUD name but is causes errors. I managed to extend PlayerUIs state like this (Keyboard.xaml states section):
(code was here but commet doesn't show it)
And then you can place anything you want into new widget. If I'm trying to Extend state containing widgets it does not work because I have to set all this widgets path anyway.

[S](https://mod.io/g/baldursgate3/u/slafniy)

[slafniy](https://mod.io/g/baldursgate3/u/slafniy)• [1y ago](https://mod.io/g/baldursgate3/r/ui-extending-the-ui#1011530 "9/29/2024, 02:42 PM GMT-4")

If you are trying to see magenta square but see nothing please note there are some errors in this guide:
1\. GUI related folders aren't in Data/YourModName/GUI, they should be placed into Data/Mods/YourModName/GUI
2\. If you get "UI state verification failed" in the game and "Default namespace not declared." in the Editor check TestModPanel.xaml namespaces, should be like this:
xmlns="https://schemas.microsoft.com/winfx/2006/xaml/presentation"
xmlns:x="https://schemas.microsoft.com/winfx/2006/xaml"
xmlns:mc="https://schemas.openxmlformats.org/markup-compatibility/2006"
xmlns:ls="clr-namespace:ls;assembly=Code"
xmlns:System="clr-namespace:System;assembly=mscorlib"
xmlns:noesis="clr-namespace:NoesisGUIExtensions;assembly=Noesis.GUI.Extensions"
xmlns:b="https://schemas.microsoft.com/xaml/behaviors"
xmlns:d="https://schemas.microsoft.com/expression/blend/2008"

[R](https://mod.io/g/baldursgate3/u/rowy-t)

[Rowy\_T](https://mod.io/g/baldursgate3/u/rowy-t)• [211d ago](https://mod.io/g/baldursgate3/r/ui-extending-the-ui#1367095 "6/2/2025, 07:35 PM GMT-4")

sorry to bother you, i literally copy and paste the tutorial code and tried yours too but the toolkit keeps showing the "UI state verification failed" in the game and "Default namespace not declared." in the Editor.
What am i doing wrong??
\[update\]
simply delete the "s" in the URLs, just write "http://(...)" in all namespaces

[F](https://mod.io/g/baldursgate3/u/florodude)

[florodude](https://mod.io/g/baldursgate3/u/florodude)• [1y ago](https://mod.io/g/baldursgate3/r/ui-extending-the-ui#1013162 "9/30/2024, 03:49 PM GMT-4")

Do we need to pak the file and put it in mods or something? I have tried this even with moving to Data/Mod/ModName/GUI and I still don't see a magenta square.

[S](https://mod.io/g/baldursgate3/u/slafniy)

[slafniy](https://mod.io/g/baldursgate3/u/slafniy)• [1y ago](https://mod.io/g/baldursgate3/r/ui-extending-the-ui#1013453 "9/30/2024, 06:58 PM GMT-4")

You need to go to Project settings -> Publish local and save .pak e.g. to Mods folder (in C:\\Users\\%user%\\AppData\\Local\\Larian Studios\\Baldur's Gate 3\\Mods)

[C](https://mod.io/g/baldursgate3/u/caa421)

[caa421](https://mod.io/g/baldursgate3/u/caa421)• [1y ago](https://mod.io/g/baldursgate3/r/ui-extending-the-ui#1004548 "9/24/2024, 11:30 PM GMT-4")

Is it currently possible to create a mod similar to, "Native Camera Tweaks" (https://www.nexusmods.com/baldursgate3/mods/945) using the native BG3 Toolkit? I hate the default, floaty , non-following camera and forced downward perspective. I've always wanted to play the game from a first-person perspective, with a 135 degree FoV, from the active actor's eye height and ability to look up and down. But I haven't the first clue where to begin to do this, or if it's even achievable with these tools since there are no examples on the camera topic. Any help or confirmation appreciated.

[P](https://mod.io/g/baldursgate3/u/plantigradewolf)

[PlantigradeWolf](https://mod.io/g/baldursgate3/u/plantigradewolf)• [1y ago](https://mod.io/g/baldursgate3/r/ui-extending-the-ui#998237 "9/21/2024, 06:21 AM GMT-4")

I would like to modify the 'Inventory and Equipment' panel UI to add some additional functionality. I have looked through the files, but I cannot seem to find any .xaml file pointing to the inventory and equipment panel. Is that panel something that can be modified using the BG3 Toolkit?

[S](https://mod.io/g/baldursgate3/u/splashofblue)

[SplashOfBlue](https://mod.io/g/baldursgate3/u/splashofblue)• [1y ago](https://mod.io/g/baldursgate3/r/ui-extending-the-ui#995800 "9/19/2024, 05:08 PM GMT-4")

I've tried to follow this tutorial and I can't get past the step of the very first purple box to show up. Only thing I can think that I'm doing wrong is where I am placing the UI folders at, I looked at the first UI guide as well and it isn't really clear to me under which folder these go as there is multiple \[mymod\] folders created in different spots but none created under \[Data\] as the first guide mentions

[L](https://mod.io/g/baldursgate3/u/yukishiku)

[LeonBlade](https://mod.io/g/baldursgate3/u/yukishiku)• [1y ago](https://mod.io/g/baldursgate3/r/ui-extending-the-ui#973846 "9/6/2024, 05:08 PM GMT-4")

How do I find a list of the UIs that I might want to extend from? Is there an easy way of discovering this?

[G](https://mod.io/g/baldursgate3/u/generalzero2)

[GeneralZeroZX](https://mod.io/g/baldursgate3/u/generalzero2)• [1y ago](https://mod.io/g/baldursgate3/r/ui-extending-the-ui#977171 "9/8/2024, 11:33 AM GMT-4")

I don't know if this helps, but I've been browsing the unpacked game files that the BG3 Modders Multitool provides. I can browse the "Game > Mods > MainUI > GUI > StateMachines > Keyboard.xaml" file. Under the second-level XML element (ls:StateMachine.States) I see a bunch of "ls:State" entries with names like:

\\* MainMenu
\\* PlayerHUD
\\* PartyPanel
\\* Trade
\\* GameOverMessageBox
\\* Book
\\* GameSettings

I am guessing that all of those are the various parts of the UI you can extend, but keep in mind that I have only listed a few. The XAML file is quite large. Again, you can find that file at the below path if you have already run the BG3 Modders Multitool application and used the "Utilities > Game File Operations > Unpack Game Files" feature.

C:\\<parent-folder>\\bg3-modders-multitool\\UnpackedData\\Game\\Mods\\MainUI\\GUI\\StateMachines

NOTE: You can also find individual panels under the "Game > Mods > MainUI > GUI > Pages" directory, but it seems that not every element of the UI is defined in its own, separate file. For example, "PlayerHUD".

Last updated

1y

Reading time

7 min read

Views

2,639

Comments

13

[G\\
\\
GrumpyWashbear](https://mod.io/g/baldursgate3/u/grumpywashbear/r)

Follow GrumpyWashbear

- [Guide](https://mod.io/g/baldursgate3/r/ui-extending-the-ui#guide)
- [Examples](https://mod.io/g/baldursgate3/r/ui-extending-the-ui#heading-1)
- [Adding Hooks](https://mod.io/g/baldursgate3/r/ui-extending-the-ui#heading-2)
- [Adding a Panel](https://mod.io/g/baldursgate3/r/ui-extending-the-ui#heading-3)
- [Tutorial](https://mod.io/g/baldursgate3/r/ui-extending-the-ui#heading-4)
- [Discussion](https://mod.io/g/baldursgate3/r/ui-extending-the-ui#discussion)

[English](https://mod.io/g/baldursgate3/r?tags=English) [Official](https://mod.io/g/baldursgate3/r?tags=Official) [UI](https://mod.io/g/baldursgate3/r?tags=UI)

Overview of how to extend the UI, and a short tutorial showing the basic steps.

Share

Report guide

---
# SOURCE: https://mod.io/g/baldursgate3/r/adding-an-armor
---

[Browse games](https://mod.io/g)

Browse games

[My library](https://mod.io/library)

My library

[My content](https://mod.io/content)

My content

My account

mod.io

mod.io

[All games](https://mod.io/g) [Baldur's Gate 3](https://mod.io/g/baldursgate3) [Guides](https://mod.io/g/baldursgate3/r) [Armor](https://mod.io/g/baldursgate3/r?tags=Armor) Adding New Armors

Adding New Armors

Share

Report

Follow

In this guide we will go over the process of importing a new armor and setting it up for in-game use. This requires you to already have the model, materials, and textures already created and in the correct formats for import. Please refer to the [Creation Guidelines: Armor](https://mod.io/g/baldursgate3/r/creation-guidelines-armor) page for details on how to prepare these.

## Importing the Assets

To import a model, it must be in the **.gr2** file format, and already be placed inside the [**Source Asset Data Path**](https://mod.io/g/baldursgate3/r/getting-started-creating-a-new-mod) of your mod.

The file can contain several meshes, and should already contain skinning.

In the editor, open your mod project, then open the **Resource Manager**.

[![](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_01.png)](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_01.png)

You will need locate the folder and package where you would like to add your armor. You can add the armor to any package in your mod - including the base package. If you’d like to add some structure and organization, however, you’re welcome to create folders and additional packages at this time.

[![](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_02.1.png)](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_02.1.png)

For the purposes of this guide, we’ll go with the following structure.

[![](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_03.1.png)](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_03.1.png)

### Model

With the NewArmors package selected, click on the `Add resource...` button.

[![](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_04.1.png)](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_04.1.png)

[![](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_05.png)](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_05.png)

In the **Add Resource Wizard** window, select **Model**. Navigate to where you exported your armor models – remember that these must be `.gr2` files, and located inside your mod's **Source Asset Data Path**. You can select multiple files here, and they will all import.

You will now get a pop up window where you can doublecheck which project each model is being imported into, the target package location, and name of the asset you are importing. You can change the name of the asset at this time if you’d like.

After confirming the information, click **Ok**.

[![](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_06.png)](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_06.png)

The model will now appear in your Resource Manager in the target package. When you click on it, you will see the mesh preview in the right-hand side panel, with many different settings underneath.

[![](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_07.1.png)](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_07.1.png)

For armors, you mainly need to look at these 4 settings:

[![](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_08.png)](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_08.png)

**Slot ID** determines which tab this mesh will be placed in inside the Character Editor and in the Equipment data editor.

| **Slot Name** | **Uses** |
| --- | --- |
| **Unassigned** | Default value - this should not actually be used. |
| **Test** | Test meshes. |
| **Head** | Head meshes. Not to be confused with items that are attached to heads! These are the heads themselves. |
| **Private Parts** | Genital meshes. |
| **ModestyLeaf** | The leaf mesh that covers the genital meshes when you have nudity turned off. |
| **Hair** | Default version of hairstyle meshes and their accessories. This is the version that gets snapped to most races. |
| **HelmetHair** | Hair meshes that are meant for the HelmetHair system - the hairstyles that you swap to with specific equipment, depending on your hair type and length. |
| **Hair DWR** | Hair meshes for non-default versions. You can read more about these in the Hair & Beards guide [here](https://larianstudios.atlassian.net/wiki/spaces/GUS/pages/3529244691/CC+Hair+and+Beards#%5BhardBreak%5DAdding-Hair-to-CC). |
| **Beard** | Beard meshes and their accessories. |
| **Body** | Any equipment on the main body (pants/shirts/belts/shoulderpads/scarves/…) |
| **Headwear** | Collars, circlets, hats, hoods, masks, etc. Items that you’d want to add in the “Headwear“ slot of your equipment in-game. |
| **Gloves** | Bracers, gloves, bracelets, rings - anything you want in the “Glove“ slot in your equipment. |
| **Cloak** | Capes, or potential back attachments you’d like to have instead of capes. |
| **Footwear** | Boots, shoes, foot jewelry. If you want Crusher’s toe ring as gear, for example, you’d put it here. |
| **Underwear** | Underwear meshes or anything that should go in that slot, like body jewelry. |
| **Piercing** | Piercing meshes. |
| **Horns** | Horns for Tieflings only. |
| **DragonbornTop** | Top attachments (horns) for Dragonborn heads. |
| **DragonbornJaw** | Jaw attachments for Dragonborn heads. |
| **DragonbornChin** | Chin attachments for Dragonborn heads. |

In this example we have two meshes - a top and pants. Both fall into the `Body` category, so that's what we'll put for the Slot ID on both.

**Supports Vertex Color** **Masking** is needed for the hiding system we use on equipment. Since we want the sleeves to be hidden when the player equips gloves on top of them, and to hide the pants when boots are equipped, we’ll need to enable the checkbox on both items.

Note that if this checkbox is enabled, you’ll need to make sure the shader you select later on supports this system. The shader will have VertCut in the name.

**Tags** are mainly used on hair and headwear meshes. For hair and helmet hair meshes, apply the `Hair` tag so that it shows correctly.

[![](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_09.1.png)](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_09.1.png)

On Headwear meshes you can add the other tags to specify whether the hair, ears, and/or horns should be hidden. Hair will automatically get hidden by items in the **Headwear** slot, so if you are adding a collar, mask, circlet or anything similar and don't want your character to rock the bald cut whenever its equipped, make sure to add the `Never Hide Hair` tag.

We do not need any tags for this example, as we’re not adding hair or headwear.

**Vertex Color Mask Slots** are another type of tags that we can add to meshes so the system understands what it needs to hide on other meshes. Tag the ones that should be **hidden** by your armor. In the example here, for the shirt we would check the following boxes:

- Shoulders

- Upperarm

- Torso

- Underwear\_bra

- Nipple covers


And check these boxes for the pants:

- Underwear\_bra

- Underwear\_panties

- Underwear\_panties\_tail

- Private parts

- Modesty leaf

- Thighs

- Knees

- Shins

- Pants


Below is an overview of the different vertex color slots and what they affect. These vary slightly between different genders and races so make sure to always double check in the editor.

[![](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_10.1.png)](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_10.1.png)

[![](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_11.1.png)](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_11.1.png)

[![](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_12.1.png)](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_12.1.png)

### Material

#### Reusing an Existing Material

We recommend reusing an existing material.

You can browse through the various existing materials inside the /All/ folder at the top of the Resource Manager’s sidebar.

[![](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_13.png)](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_13.png)

To view only the materials, **right-click** on the globe icon.

[![](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_14.png)](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_14.png)

You can right-click on it again to remove the filter and view all asset types.

Once you find a material that already has the shader you want, right-click on it, and select `Create New from Selected`.

Once you’ve found a Material to base yours on, right click on it in the Resource Manager and select “Create New from Selected“.

[![](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_15.1.png)](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_15.1.png)

For this example, we’ll go with `HUM_M_ARM_Astarion_Shirt` for the shirt, and `HUM_M_ARM_Astarion_Pants` for the pants.

Give it the same Resource Package as where you placed the mesh, and a name. If your model consists of different meshes, you will need multiple materials for this armor. If you are re-using existing pieces of armor, you can simply re-use those materials instead of creating copies.

[![](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_16.1.png)](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_16.1.png)

### Textures

Depending on if you’re making an entirely new armor or adjusting an existing one, you might have custom textures for it. These should be exported as `.dds` files, and need to be inside `/YourModName/Assets/Public/`. They can be further organized into subfolders, if you like.

We’ll use the **Add Resource Wizard** to import these too.

[![](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_17.1.png)](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_17.1.png)

#### BM, NM, and PM

The BM, NM, and PM should be imported as Virtual Textures. Select all three files at once.

If you’ve named your textures with \_BM, \_NM, and \_PM suffixes, these should already have sorted correctly, but you can still adjust the import path in the **Virtual Texture Importer** window.

You’re also welcome to adjust the Scale at this time, if necessary.

[![](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_18.png)](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_18.png)

When ready, press the **Import All** button at the top. The bottom bar of the Virtual Texture Importer will change to show that it’s converting.

Once the conversion is complete, you’ll see a single new VirtualTextureResource (containing all three maps) appear in your target package.

#### GM, MSK, or CLOTH

Any additional textures like GM, MSK or CLOTH can be imported as default textures. When importing these, you will be asked if they’re sRGB.

Once the textures are imported, we need to plug these into the material. Double click on a material in the Resource Manager to open it. You will see default colors that you can set. Scroll down in this view to see the texture settings.

In the Resource Manager, with this window still open, select the texture you want to assign, and in the material settings window, click on the arrow to assign the selected texture. Make sure the checkbox is checked. Do this for all textures in the material.

[![](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_19.1.png)](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_19.1.png)

Then, select your mesh (VisualResource), and double-click to open the Edit Visual window. Here, assign the the new material to the mesh using the same workflow as above.

[![](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_20.png)](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_20.png)

You should now have an implemented asset in the resource manager!

[![](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_21.png)](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_21.png)

## Equipment System

To actually use this as equipment, it needs to have a root template. A root template is a description of how an item looks in the world, what it says in the tooltip, how it looks when a character equips it, and so on.

The easiest option when creating a new root template is to inherit from an existing root template. This way, all of its parameters will be inherited, and you can just modify the visuals.

[![](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_22.png)](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_22.png)

Open the Root Template Manager via the icon on the top bar.

> **NOTE:** To use the Root Template Manager, you must have a level loaded.
>
> If the icon is greyed out, check to see if you already have the Root Template Manager open!

Switch to the Inheritance View (green outline in screenshot below) and navigate to

`item → [WIP] BASE_ARMOR → [WIP] BASE_ARMOR_Body`

[![](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_24.png)](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_24.png)

You can narrow it down further from here - for example, if you were making a robe, you might want to go to

`items -> [WIP] BASE_ARMOR -> [WIP] BASE_ARMOR_Body -> [WIP] ARM_Cloth -> [WIP] ARM_Robe`

In our case, we’ll select `[WIP] ARM_Civilian_Body` from under `[WIP] ARM_Cloth`.

Right-click on the desired root, and select “Create inherited from selected”.

The CreateObjectWizard will appear.

[![](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_25.png)](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_25.png)

First, fill in a new name for the root template (yellow outline on screenshot above) - we’ll go with `ARM_Leather_StylishPants`. You can already adjust some of the other settings now, but these will also be available after creation, so we’ll skip them for now.

Press the Create button.

After creation, your new root template will be visible in the hierarchy:

[![](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_26.png)](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_26.png)

A sidebar should also have opened, but if not, click on your new template to do so now. In this sidebar, fill in the Display Name.

[![](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_27.png)](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_27.png)

> **TIP:** You can search for a particular field by typing it into the search bar at the top:
>
> [![](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_28.png)](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_28.png)

Here, you can also adjust which model will be visible when you drop the item in the world. By default, a basic folded model should be filled in, but if you do decide to make a custom mesh for it, you can fill in the model and physics files here:

[![](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_29.png)](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_29.png)

The most important part visually is the Equipment Data. This is where you assign the actual visuals on the various races. Scroll down or filter on “Equipment Data“ and click on the “…” to open the Equipment Data Editor.

[![](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_30.png)](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_30.png)

In the Equipment Data Editor, the different races will still be wearing their assigned robes from the root template you copied. You can click on the different tabs to see:

[![](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_31.png)](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_31.png)

Here, you can assign the correct visual and color presets for all races. If you do not make your custom armor available for all of the races, you can still assign fallback armors from something existing - there is no hard requirement that the armors must visually match.

You can also use the “+” to add other race/gender combinations. For example, if you’d like female Drow to wear something else, select that from the dropdown.

> **NOTE:** If they don’t have their own outfits assigned here, elves, half-elves, and tieflings default to whatever is assigned to the humans.

[![](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_32.png)](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_32.png)

The yellow area of the editor shows what’s currently assigned. The red is a browser for all the available items. You can filter the items shown in this part by using the search bar (green in the screenshot above). Double-click on items to assign them, or to remove them from assignment.

Once you’re done assigned, go to `File > Save All`. Close the equipment editor.

## Assigning Stats

Now you have a new item that can be used as loot!

It still has same statistics as the root template you copied. If you want it to provide magic benefits or have custom gameplay effects, you’ll need to change the Stats parameter on the root to an existing magical item, or make a new one.

This is done with an Armor table in the Stats Editor. We’ll open the Stats Editor via the icon on the top bar, and look for our mod (in this case, `NewArmor`).

[![](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_33.png)](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_33.png)

[![](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_34.png)](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_34.png)

Click on the “+” by Stats, and select Armor from the dropdown. It’ll be created under Stats. Double-click on this new file to open it.

Fill in the **RootTemplate** field with the name of the root template you created. In this case, that’s `ARM_Leather_StylishPants`.

You’ll also need to give the Armor entry a **Name**\- using the same name as the root template is fine.

For **Parent**, you can fill in the name of an existing Armor, and your new armor will then use the same properties. To see stats for existing armors, along with their names, feel free to browse the GustavDev Armor table.

[![](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_35.1.png)](https://image.modcdn.io/members/63c0/31088933/profilearmor/armor_35.1.png)

Once you’ve filled in these three fields, make sure to save your work.

[G\\
\\
GrumpyWashbear](https://mod.io/g/baldursgate3/u/grumpywashbear/r)

Follow GrumpyWashbear

Log in to join the discussion!

[P](https://mod.io/g/baldursgate3/u/periodstain)

[periodstain](https://mod.io/g/baldursgate3/u/periodstain)• [81d ago](https://mod.io/g/baldursgate3/r/adding-an-armor#1505299 "10/10/2025, 11:28 PM GMT-4")

hmmm, how would I go about hiding helmet hair when using the headwear tag?

[E](https://mod.io/g/baldursgate3/u/ectoteeth)

[Ecto-Teeth](https://mod.io/g/baldursgate3/u/ectoteeth)• [1y ago](https://mod.io/g/baldursgate3/r/adding-an-armor#1111252 "12/2/2024, 10:05 PM GMT-5")

From a lot of trial and error I have figured out some things that have made everything work better for me and thought I'd share in case anyone is still here struggling with this guide like I was:

1\. If you can't find your imported visual resources in the Equipment Data editor, the parent you used in the stats table may not be the correct parent for the armor you're making. The name of the visual resource starting with Race\_Gender (ex. HUM\_M\_) also helps, but I'm not sure if its a hard requirement

2\. Save your Stats table, File>Save All, then CTRL+R to refresh the editor. Find your root template again, type "stats" into the search bar, and replace the vanilla table with the one you just made.

3\. Make your Stats table and add it to your root template BEFORE filling in the Equipment Data. I've had an easier time getting my imported visual resources to show up right away this way.

4\. If you want your armor to actually show up in the game, you will need a treasure table. Padme400 and OhforTheGamer both have extremely helpful guides on treasure tables and armor/item creation. In fact I recommend Ohfor's whole series of guides he has posted on here they are incredibly easy to follow and amazing for beginners!

[M](https://mod.io/g/baldursgate3/u/modiouserbrvf)

[ModioUserbrvf](https://mod.io/g/baldursgate3/u/modiouserbrvf)• [1y ago](https://mod.io/g/baldursgate3/r/adding-an-armor#1073205 "11/5/2024, 12:27 PM GMT-5")

Seems to be an issue importing virtual textures

Message: GrBuildLib.InvalidDllException: Couldn't load GrimWrapperCPP.dll, make sure Granite SDK is correctly installed, you have a valid license, and check the prerequisites in the documentation. ---> System.TypeInitializationException: The type initializer for 'Grim.GrimWrapperCPPPINVOKE' threw an exception. ---> System.TypeInitializationException: The type initializer for 'SWIGExceptionHelper' threw an exception. ---> System.DllNotFoundException: Unable to load DLL 'GrimWrapperCPP': The specified module could not be found. (Exception from HRESULT: 0x8007007E)
at Grim.GrimWrapperCPPPINVOKE.SWIGExceptionHelper.SWIGRegisterExceptionCallbacks\_GrimWrapperCPP(ExceptionDelegate applicationDelegate, ExceptionDelegate arithmeticDelegate, ExceptionDelegate divideByZeroDelegate, ExceptionDelegate indexOutOfRangeDelegate, ExceptionDelegate invalidCastDelegate, ExceptionDelegate invalidOperationDelegate, ExceptionDelegate ioDelegate, ExceptionDelegate nullReferenceDelegate, ExceptionDelegate outOfMemoryDelegate, ExceptionDelegate overflowDelegate, ExceptionDelegate systemExceptionDelegate)
at Grim.GrimWrapperCPPPINVOKE.SWIGExceptionHelper..cctor()
\-\-\- End of inner exception stack trace ---
at Grim.GrimWrapperCPPPINVOKE.SWIGExceptionHelper..ctor()
at Grim.GrimWrapperCPPPINVOKE..cctor()
\-\-\- End of inner exception stack trace ---
at Grim.GrimWrapperCPPPINVOKE.ImageFactory\_Create(IntPtr& jarg1)
at Grim.ImageFactory.Create(IImage& image)
at GrBuildLib.Tools.NixelTools.CheckDlls()
\-\-\- End of inner exception stack trace ---
at GrBuildLib.GrBuildLibInterface.InitializeGrBuild()
at GrBuildLib.ProjectBuilder.Initialize()
at LSVirtualTextureImport.Models.PlatformVirtualTextureSerializer.Save(IConvertedVirtualTexture data, Path path, String filename)
at LSImport.Base.PlatformFileUtility.Save\[T\](T processedData, IPlatformSerializer\`1 platformSerializer, IVersionControlWrapper versionControl, Path platformSpecificFilePath)
at LSFrameworkUI.Importer.VirtualTexture.VirtualTextureConverter.<>c\_\_DisplayClass29\_3.b\_\_11()
at System.Threading.Tasks.Task\`1.InnerInvoke()
at System.Threading.Tasks.Task.Execute()
\-\-\- End of stack trace from previous location where exception was thrown ---
at System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()
at LSFrameworkUI.Importer.VirtualTexture.VirtualTextureConverter.d\_\_29.MoveNext()

[E](https://mod.io/g/baldursgate3/u/jcobal)

[El0bal](https://mod.io/g/baldursgate3/u/jcobal)• [1y ago](https://mod.io/g/baldursgate3/r/adding-an-armor#1006006 "9/26/2024, 01:56 AM GMT-4")

I'm going crazy. Everything works fine, I close the toolkit, and when I open it again the root templates have empty or lost data, and trying to fill it back in assigns it to the wrong template, until they all get mixed up. What am I doing wrong?

[T](https://mod.io/g/baldursgate3/u/awakuzutakeo)

[Thesonofdisaster](https://mod.io/g/baldursgate3/u/awakuzutakeo)• [1y ago](https://mod.io/g/baldursgate3/r/adding-an-armor#1028423 "10/9/2024, 01:15 AM GMT-4")

Im having the same problem, except I dont even have to close the toolkit, just trying to save my root templates deletes all the data. The one exception is a magic handcrossbow I made. Im completely lost as to what is going wrong. Did you ever figure it out?

[O](https://mod.io/g/baldursgate3/u/overseer32)

[OverseerNZ](https://mod.io/g/baldursgate3/u/overseer32)• [1y ago](https://mod.io/g/baldursgate3/r/adding-an-armor#1072610 "11/4/2024, 10:08 PM GMT-5")

I found a fix! This was happening to me because I had published locally to test the mod out. You need to remove the .pak from your mods folder in appdata once you're finished testing, because the toolkit draws from the same resources the game does. Hope that helps!

[S](https://mod.io/g/baldursgate3/u/sa-foxhead)

[SA\_Foxhead](https://mod.io/g/baldursgate3/u/sa-foxhead)• [1y ago](https://mod.io/g/baldursgate3/r/adding-an-armor#1005658 "9/25/2024, 07:55 PM GMT-4")

So two things. Whenever I add my gr2 file into the resource manager, the whole program will more often than not just crash. When I manage to get back in and try again without a crash, my model shows up in the preview to import, but does not show up in the right hand preview after I import it. Not sure what I'm doing wrong here as I followed all the other steps. Any suggestions?

[E](https://mod.io/g/baldursgate3/u/jcobal)

[El0bal](https://mod.io/g/baldursgate3/u/jcobal)• [1y ago](https://mod.io/g/baldursgate3/r/adding-an-armor#1005941 "9/25/2024, 11:43 PM GMT-4")

the same happens to me, and then it messes my root templates, referencing the wrong resource or getting their data mixed up. I think the problem comes from some resources I stopped using. But I just cannot remove them from my mod's resource list; even deleting the files from the source folders doesn't stop them from appearing and (I suspect) causing errors.

[S](https://mod.io/g/baldursgate3/u/sankojin1)

[Sankojin](https://mod.io/g/baldursgate3/u/sankojin1)• [1y ago](https://mod.io/g/baldursgate3/r/adding-an-armor#996570 "9/20/2024, 03:47 AM GMT-4")

Does anyone know if there is something special that you have to do when you make a virtual texture in the toolkit? The materials that I make are not brightly lit like the game's base assets. It's like the default materials have a lighted material attached to them. When I make a new virtual texture and a new material it's not as brightly lit as the game's assets. The ball on the left is the game's asset and the ball on the right is mine. You can see the game's asset has a lot better lighting to it. [https://gyazo.com/aad533c18fb9d0971d61bb1de393f29a](https://gyazo.com/aad533c18fb9d0971d61bb1de393f29a)

[M](https://mod.io/g/baldursgate3/u/medusae)

[Medusae](https://mod.io/g/baldursgate3/u/medusae)• [1y ago](https://mod.io/g/baldursgate3/r/adding-an-armor#986484 "9/14/2024, 07:19 AM GMT-4")

For anyone not able to find their custom mesh / visual resource in the equipment data, your mesh needs to start with Race\_Gender for what it's set for (for example, a mesh for Human female would start with HUM\_F like vanilla items). It will show up then. I was also banging my head against the wall, hope this helps!

[M](https://mod.io/g/baldursgate3/u/modiousery09d)

[ModioUsery09d](https://mod.io/g/baldursgate3/u/modiousery09d)• [131d ago](https://mod.io/g/baldursgate3/r/adding-an-armor#1457148 "8/21/2025, 10:06 PM GMT-4")

GOD THANK YOU SO MUCH I WAS ABOUT TO TEAR MY HAIR OUT

[B](https://mod.io/g/baldursgate3/u/modiouser66026891)

[bubuesfurtocskehun](https://mod.io/g/baldursgate3/u/modiouser66026891)• [1y ago](https://mod.io/g/baldursgate3/r/adding-an-armor#976163 "9/7/2024, 09:31 PM GMT-4")

Did everything as in the tutorial, but I can not select my created visual resource in the equipment data. Is something missing in the tutorial?

[Q](https://mod.io/g/baldursgate3/u/quillspirit15971)

[QuillSpirit15971](https://mod.io/g/baldursgate3/u/quillspirit15971)• [1y ago](https://mod.io/g/baldursgate3/r/adding-an-armor#1017965 "10/3/2024, 06:32 PM GMT-4")

A month late, but make sure to double check that the correct SlotID was checked when importing the model used. I was having trouble finding specific armours in the equipment data, and that was what was missing when I went back to double check.

[B](https://mod.io/g/baldursgate3/u/modiouser66026891)

[bubuesfurtocskehun](https://mod.io/g/baldursgate3/u/modiouser66026891)• [1y ago](https://mod.io/g/baldursgate3/r/adding-an-armor#980456 "9/10/2024, 11:17 AM GMT-4")

A temporary solution to this problem (which worked for me) is to import your own visual resource, then use 'create new from selected' to copy an original resource. After that, manually set the source file of the copied resource to the .gr2 file you just created by importing your visual resource. Then your own resource still won't show up in the equipment data panel, but the one which you copied will appear with your own armor, visuals (and the new name you gave to the copy of the original resource).

Still a more detailed guide is needed (this one is missing key details). Hopefully someone will upload a video somewhere which covers this topic from start to finish, for example, it also shows the working custom armor (with correct animation) in the game at the end, since this one does not show the results of the steps, so we can not know if we correctly applied the steps.

[M](https://mod.io/g/baldursgate3/u/modiouser2074551)

[ModioUser2074551](https://mod.io/g/baldursgate3/u/modiouser2074551)• [1y ago](https://mod.io/g/baldursgate3/r/adding-an-armor#980530 "9/10/2024, 12:19 PM GMT-4")

I just found

BG3 Mod Toolkit Tutorial: Weapons and Armour - YouTube

[Photo image of Chemikal Ink](https://www.youtube.com/channel/UCxjMmn94wJHNWvaRHf0Gz2Q?embeds_referring_euri=https%3A%2F%2Fmod.io%2F)

Chemikal Ink

266 subscribers

[BG3 Mod Toolkit Tutorial: Weapons and Armour](https://www.youtube.com/watch?v=GUXBk-5Ro8k)

Chemikal Ink

Search

Watch later

Share

Copy link

Info

Shopping

Tap to unmute

If playback doesn't begin shortly, try restarting your device.

More videos

## More videos

You're signed out

Videos you watch may be added to the TV's watch history and influence TV recommendations. To avoid this, cancel and sign in to YouTube on your computer.

CancelConfirm

Share

Include playlist

An error occurred while retrieving sharing information. Please try again later.

[Watch on](https://www.youtube.com/watch?v=GUXBk-5Ro8k&embeds_referring_euri=https%3A%2F%2Fmod.io%2F)

0:00

0:00 / 28:33

•Live

•

which I think is the one (and only) video that has "more detailed" guide what someone has been able to discover. I myself got stuck on stats...

2 replies

[K](https://mod.io/g/baldursgate3/u/modiouser2075678)

[kotobelka4](https://mod.io/g/baldursgate3/u/modiouser2075678)• [1y ago](https://mod.io/g/baldursgate3/r/adding-an-armor#975144 "9/7/2024, 11:31 AM GMT-4")

where will the armor I made appear in the game? will it appear randomly in barrels or at merchants? can I specify its location myself?

[M](https://mod.io/g/baldursgate3/u/modiouser2074551)

[ModioUser2074551](https://mod.io/g/baldursgate3/u/modiouser2074551)• [1y ago](https://mod.io/g/baldursgate3/r/adding-an-armor#980535 "9/10/2024, 12:21 PM GMT-4")

I have not tested but in Stats Editor -> Gustav -> Treasure Tables you can find in "TUT" party how items are in tutorial chest. Which you can then reuse and put newly made items to tutorial chest. (Atleast thats what I've been able to think)

[C](https://mod.io/g/baldursgate3/u/cobaltcactus)

[CobaltCactus](https://mod.io/g/baldursgate3/u/cobaltcactus)• [1y ago](https://mod.io/g/baldursgate3/r/adding-an-armor#982691 "9/11/2024, 08:00 PM GMT-4")

Were you ever able to figure this out? Kept trying to add it to the TUT\_SHAR\_CHEST, no dice.

2 replies

[R](https://mod.io/g/baldursgate3/u/renardblagueur)

[RenardBlagueur](https://mod.io/g/baldursgate3/u/renardblagueur)• [1y ago](https://mod.io/g/baldursgate3/r/adding-an-armor#974709 "9/7/2024, 04:43 AM GMT-4")

Very good guide !
How do you make new items icon ? The guide is here : [@adding-skill-and-item-icons](https://mod.io/g/baldursgate3/r/adding-skill-and-item-icons)

[M](https://mod.io/g/baldursgate3/u/modiouser2074768)

[ModioUser2074768](https://mod.io/g/baldursgate3/u/modiouser2074768)• [1y ago](https://mod.io/g/baldursgate3/r/adding-an-armor#973019 "9/6/2024, 01:29 AM GMT-4")

So i've made my armor (I think). What now tho ? where do I find it ?

[S](https://mod.io/g/baldursgate3/u/soap163)

[Soapdish123](https://mod.io/g/baldursgate3/u/soap163)• [1y ago](https://mod.io/g/baldursgate3/r/adding-an-armor#973728 "9/6/2024, 03:35 PM GMT-4")

You can console command it in to see if its working - ctrl+shift+f11 then create and whatever name you called it.

[M](https://mod.io/g/baldursgate3/u/modiouser2074768)

[ModioUser2074768](https://mod.io/g/baldursgate3/u/modiouser2074768)• [1y ago](https://mod.io/g/baldursgate3/r/adding-an-armor#973986 "9/6/2024, 06:36 PM GMT-4")

crtl+shift+f11 doesn't seem to do anything, are you sure it's the right combination ?

1 reply

[H](https://mod.io/g/baldursgate3/u/handsomejack3)

[HandsomeJack3](https://mod.io/g/baldursgate3/u/handsomejack3)• [1y ago](https://mod.io/g/baldursgate3/r/adding-an-armor#972648 "9/5/2024, 08:21 PM GMT-4")

the new mesh doesn't appear when you try to assign it in the root template ??

[T](https://mod.io/g/baldursgate3/u/modiouser2082634)

[TheNeXXus3](https://mod.io/g/baldursgate3/u/modiouser2082634)• [1y ago](https://mod.io/g/baldursgate3/r/adding-an-armor#976191 "9/7/2024, 09:47 PM GMT-4")

Having the same issue, did you ever find a solution?

Last updated

1y

Reading time

14 min read

Views

17,106

Comments

29

[G\\
\\
GrumpyWashbear](https://mod.io/g/baldursgate3/u/grumpywashbear/r)

Follow GrumpyWashbear

- [Guide](https://mod.io/g/baldursgate3/r/adding-an-armor#guide)
- [Importing the Assets](https://mod.io/g/baldursgate3/r/adding-an-armor#heading-1)
- [Model](https://mod.io/g/baldursgate3/r/adding-an-armor#heading-2)
- [Material](https://mod.io/g/baldursgate3/r/adding-an-armor#heading-3)
- [Reusing an Existing Material](https://mod.io/g/baldursgate3/r/adding-an-armor#heading-4)
- [Textures](https://mod.io/g/baldursgate3/r/adding-an-armor#heading-5)
- [BM, NM, and PM](https://mod.io/g/baldursgate3/r/adding-an-armor#heading-6)
- [GM, MSK, or CLOTH](https://mod.io/g/baldursgate3/r/adding-an-armor#heading-7)
- [Equipment System](https://mod.io/g/baldursgate3/r/adding-an-armor#heading-8)
- [Assigning Stats](https://mod.io/g/baldursgate3/r/adding-an-armor#heading-9)
- [Discussion](https://mod.io/g/baldursgate3/r/adding-an-armor#discussion)

[Armor](https://mod.io/g/baldursgate3/r?tags=Armor) [English](https://mod.io/g/baldursgate3/r?tags=English) [Official](https://mod.io/g/baldursgate3/r?tags=Official) [Stats](https://mod.io/g/baldursgate3/r?tags=Stats)

What to do after you have your armors created: how to implement them in the engine and assign stats.

Share

Report guide

---
# SOURCE: https://mod.io/g/baldursgate3/r/publishing-a-mod
---

[Browse games](https://mod.io/g)

Browse games

[My library](https://mod.io/library)

My library

[My content](https://mod.io/content)

My content

My account

mod.io

mod.io

[All games](https://mod.io/g) [Baldur's Gate 3](https://mod.io/g/baldursgate3) [Guides](https://mod.io/g/baldursgate3/r) [Editor](https://mod.io/g/baldursgate3/r?tags=Editor) Publishing a Mod

Publishing a Mod

Share

Report

Follow

To publish your mod to mod.io, you will need a Larian account, a mod.io account, and to have connected the two of them. See the instructions in [**Getting Started: Creating a Mod.**](https://mod.io/g/baldursgate3/r/getting-started-creating-a-new-mod)

Before starting the publish process, you only need to load into your mod project; loading into a level is not necessary.

Open the Project menu and select “Project Settings”.

[![](https://image.modcdn.io/members/63c0/31088933/profilecreate/publish_01a.png)](https://image.modcdn.io/members/63c0/31088933/profilecreate/publish_01a.png)

This view allows you to modify your project’s properties, manage dependencies and conflicts, and publish your mod.

## Project Settings

The **Name, Description** and **Thumbnail** fields are mandatory. The Name has a limit of 50 characters - if you exceed this, your mod will not publish.

[![](https://image.modcdn.io/members/63c0/31088933/profilecreate/publish_02b.png)](https://image.modcdn.io/members/63c0/31088933/profilecreate/publish_02b.png)

All of these properties can be adjusted on mod.io after publishing.

### Dependencies

Dependencies allow you to tell the game which other mods are required for yours to function correctly.

This is very useful for the regular player, who might not know when or what other mods are required for your mod to function. When set up correctly, dependencies are automatically downloaded and enabled for players when they download a mod.

> Setting a dependency in the Toolkit is different to doing it on mod.io. You will need to do both to set your dependencies correctly. We’ll go over the mod.io side later in this guide.

On the **Dependencies** tab, you can see a list of all mods that you are working on, as well as all mods that you have downloaded.

If you don’t see your mod in the list, make sure it's downloaded and present your mod folder located in `%localappdata%\Larian Studios\Baldur's Gate 3\Mods\`.

[![](https://image.modcdn.io/members/63c0/31088933/profilecreate/dependencies01.png)](https://image.modcdn.io/members/63c0/31088933/profilecreate/dependencies01.png)

You can now start selecting which mods your mod is dependent on. By giving your mod a dependency, you are saying that your mod is dependent on _something_ from the other mod in order to function, and thus the other mod should be loaded **before** yours.

For example:

- The **MyClass** mod introduces a new class into the game: Artificer.

- The **MySubclass** mod introduces a new subclass for Artificer into the game: Alchemist.

- Because Alchemist is a subclass of Artificer, and the player can’t use Alchemist without first getting the Artificer class mod, we can say that **MySubclass** is dependent on **MyClass**.


Using the example above, let's set **MyClass** as a dependency of **MySubclass**.

With the **MySubclass** project loaded in the toolkit, we can open the **Dependencies** tab and select **MyClass** in the list on the left and then press the `>` button to move it over.

[![](https://image.modcdn.io/members/63c0/31088933/profilecreate/dependencies02.png)](https://image.modcdn.io/members/63c0/31088933/profilecreate/dependencies02.png)

**MySubclass** is now dependent on **MyClass.** The game will ensure that **MyClass** is loaded before **MySubclass** when players start a new game session with the **MySubclass** mod enabled.

### Conflicts

Defining conflicts for your mod allows the game to automatically disable your mod when one of the listed conflicts is detected. This can be used to protect your mod from being loaded in situations where you know it won’t function correctly.

This can save players some pain, as in most cases they won’t have the information to understand why a mod they are using isn’t working correctly.

In the **Conflicts** tab, you can see a list of all mods that you are working on, as well as all mods that you have downloaded.

If you don’t see you mod in the list, make sure it's downloaded and present your mod folder located in `%localappdata%\Larian Studios\Baldur's Gate 3\Mods\`.

[![](https://image.modcdn.io/members/63c0/31088933/profilecreate/conflicts01.png)](https://image.modcdn.io/members/63c0/31088933/profilecreate/conflicts01.png)

You can now start selecting the conflicting mods. By defining conflicting mods, you are saying that your mod won’t work correctly if the other mods are also active, and thus your mod should be disabled to prevent issues.

For example:

- The **MyConflictA** mod overrides the Firebolt spell with a new icon.

- The **MyConflictB** mod also overrides the Firebolt spell with extra damage.

- Because both mods override the same spell, only one of them will work.


Using the example above, let's set **MyConflictA** as a conflict for mod **MyConflictB**. To do that, select **MyConflictA** in the list on the left, then press the `>` button to move it over. It will now show in the right-hand side.

[![](https://image.modcdn.io/members/63c0/31088933/profilecreate/conflicts02.png)](https://image.modcdn.io/members/63c0/31088933/profilecreate/conflicts02.png)

**MyConflictB** now conflicts with **MyConflictA**, and the game will ensure that **MyConflictB** is disabled if a game is started with both **MyConflictA** and **MyConflictB** enabled.

> Not only will MyConflictB be disabled, but all of its dependencies will be disabled as well, **as long as other mods aren’t also dependent on them.**

Make sure to Save before closing the window.

## Publishing Locally

The **Publish Local** button will create a `.pak` file for you, without uploading it to mod.io. It requires no authentication.

After the packing process is complete, you will be asked where to save the `.pak` file.

## Publishing to Mod.io

### Authentication

To publish a mod to mod.io for public use, you must first authenticate with mod.io using the **Authenticate** button in the upper right corner of the Project Settings window.

The **Authentication wizard** will open. You must accept both the Larian and mod.io Terms and Conditions to continue.

Then, you will be presented with two authentication options: **Steam** or **Larian Account**.

[![](https://image.modcdn.io/members/63c0/31088933/profilecreate/auth01.png)](https://image.modcdn.io/members/63c0/31088933/profilecreate/auth01.png)

If you don’t already have a Larian account, you’ll need to create one [**here**](https://larian.com/account/create).

After logging in, the **Publish** button will be enabled, and you’ll be able to publish your mod to mod.io. After pressing the **Publish** button, you should see a progress bar at the top of the Project Settings window while the mod is packaged and uploaded.

[![](https://image.modcdn.io/members/63c0/31088933/profilecreate/upload01.png)](https://image.modcdn.io/members/63c0/31088933/profilecreate/upload01.png)

Once completed, a page will be automatically opened in your browser. You should see the File Manager page for your mod on mod.io.

[![](https://image.modcdn.io/members/63c0/31088933/profilecreate/web01.png)](https://image.modcdn.io/members/63c0/31088933/profilecreate/web01.png)

You can also verify that your mod was successfully published by checking the Message Log portion of the Editor window, where you should see the following line:

[![](https://image.modcdn.io/members/63c0/31088933/profilecreate/publish_04.png)](https://image.modcdn.io/members/63c0/31088933/profilecreate/publish_04.png)

### Editing Your Mod on Mod.io

Immediately after publishing, on theFile Managerpage of your mod on mod.io, you’ll likely see a little clock icon under “Scan”. This means that your mod is still waiting to go through the automation scanning. You cannot set your mod live until this scan is complete.

However, during this time, you can edit and set up other important fields of your mod.

#### General Settings > Mod Profile

If you’ve just published your mod, you’ll likely have a warning at the top of this page. In this case, we’re getting a “Needs File” warning because the mod file is still being scanned (as mentioned above).

[![](https://image.modcdn.io/members/63c0/31088933/profilecreate/web02.png)](https://image.modcdn.io/members/63c0/31088933/profilecreate/web02.png)

In the Basics section, you can fill in a variety of user-facing information, like the **Mod name**, **Summary**, a full **Description**, flag any mature content, and set the **Tags**.

#### General Settings > Media

In the Media section, you can upload additional screenshots that will be shown for your mod on the mod.io website, the baldursgate3.game website, and in the in-game Mod Manager. We recommend sticking to `.PNG` files for this.

You can also link to Youtube videos showing off your mod, but these will only be displayed on the web, not in-game.

[![](https://image.modcdn.io/members/63c0/31088933/profilecreate/web03.png)](https://image.modcdn.io/members/63c0/31088933/profilecreate/web03.png)

#### Dependencies

Dependencies on mod.io work slightly differently to the Toolkit, but with the same goal in mind. The main difference between the two is that while the Toolkit manages load order, mod.io uses the dependencies to allow the game to download the dependencies of a mod.

On the Dependencies tab of your mod’s page, you’ll be presented with the following view:

[![](https://image.modcdn.io/members/63c0/31088933/profilecreate/web04.png)](https://image.modcdn.io/members/63c0/31088933/profilecreate/web04.png)

In the **Search mods** field, you can browse all mods that have been uploaded to mod.io for Baldur's Gate 3, and select which ones are a dependency.

[![](https://image.modcdn.io/members/63c0/31088933/profilecreate/web05.png)](https://image.modcdn.io/members/63c0/31088933/profilecreate/web05.png)

### Setting the Mod Live

After verifying your mod details in the browser, you’ll need to click on the **Go live** button on mod.io to actually set it live.

[![](https://image.modcdn.io/members/63c0/31088933/profilecreate/publish_05.png)](https://image.modcdn.io/members/63c0/31088933/profilecreate/publish_05.png)

You don’t have to immediately set your mod live - you can take your time editing the information and set it live only after you’re ready. Just remember to press the **Save** button near the bottom of the page to save your changes before exiting.

[G\\
\\
GrumpyWashbear](https://mod.io/g/baldursgate3/u/grumpywashbear/r)

Follow GrumpyWashbear

Log in to join the discussion!

[R](https://mod.io/g/baldursgate3/u/modiouser2112914)

[RekhytFR](https://mod.io/g/baldursgate3/u/modiouser2112914)• [93d ago](https://mod.io/g/baldursgate3/r/publishing-a-mod#1494735 "9/29/2025, 09:52 AM GMT-4")

And when do mods go live for consoles/Mac?

[R](https://mod.io/g/baldursgate3/u/modiouser2090435)

[Raven405](https://mod.io/g/baldursgate3/u/modiouser2090435)• [175d ago](https://mod.io/g/baldursgate3/r/publishing-a-mod#1407035 "7/9/2025, 12:03 AM GMT-4")

When I try to upload , it looks like it cycles to the website then says "A task is canceled" in the editor. And nothing occurs. Please let me know.

[D](https://mod.io/g/baldursgate3/u/dazedmika)

[DazedMika](https://mod.io/g/baldursgate3/u/dazedmika)• [135d ago](https://mod.io/g/baldursgate3/r/publishing-a-mod#1453221 "8/17/2025, 07:45 PM GMT-4")

Having this same problem and I have no idea why.

[O](https://mod.io/g/baldursgate3/u/optio366)

[Optio366](https://mod.io/g/baldursgate3/u/optio366)• [219d ago](https://mod.io/g/baldursgate3/r/publishing-a-mod#1358320 "5/26/2025, 11:25 AM GMT-4")

I'm getting "Project properties validation failed" when trying to publish my mod. unclear what the issue is. My accounts are connected and am able to log in in project settings. Also, i notice "Mandatory Field" box in red that i haven't seen in other photos of the project settings screen. I have all the fields filled, so maybe that is the problem?

[S](https://mod.io/g/baldursgate3/u/silverstargg)

[SilverStarGG](https://mod.io/g/baldursgate3/u/silverstargg)• [131d ago](https://mod.io/g/baldursgate3/r/publishing-a-mod#1457454 "8/22/2025, 09:34 AM GMT-4")

Did you manage to solve this? It keeps happening to me too

[E](https://mod.io/g/baldursgate3/u/eviluessfansy)

[EviluessFansy](https://mod.io/g/baldursgate3/u/eviluessfansy)• [224d ago](https://mod.io/g/baldursgate3/r/publishing-a-mod#1352416 "5/21/2025, 11:58 AM GMT-4")

Hello,
I'm encountering an issue with republishing a mod.
Initially, I published my mod locally, and it worked fine in the game. However, if I save the game with this mod active, and then republish the mod (even with no changes made to the mod files themselves), attempting to load that save game will prompt a message stating the mod needs to be "downgraded."
I've confirmed that the toolkit has the "auto increase version" option checked.
If I stick to the version before this problematic republish (or simply don't republish it again), the saves load correctly, and the mod continues to work fine. The issue only appears after a republish action that increments the version, even without actual mod file changes.
Could there be a bug in the publishing process related to how save games track mod versions after a republish?
Thanks.

[T](https://mod.io/g/baldursgate3/u/turbohobo)

[TurboHobo](https://mod.io/g/baldursgate3/u/turbohobo)• [1y ago](https://mod.io/g/baldursgate3/r/publishing-a-mod#1116252 "12/7/2024, 11:46 AM GMT-5")

So I don't have an actual computer and have been working on a few mods using an Asus ROG Ally. I finally got the mods I was working on pretty much fully functional and ready to publish but the Project Settings window is literally too big and doesn't show me the bottom part that I need to save and publish. I can't scroll down and I can't seem to move the window up enough to let me click on those options. Any ideas?

[E](https://mod.io/g/baldursgate3/u/ed1241)

[EdHR](https://mod.io/g/baldursgate3/u/ed1241)• [333d ago](https://mod.io/g/baldursgate3/r/publishing-a-mod#1195742 "2/1/2025, 01:46 AM GMT-5")

Do you have the dock for the ROG Ally? you can connect an HDMI cable to a monitor or TV from the dock's HDMI port.

[R](https://mod.io/g/baldursgate3/u/reddrik)

[Reddrik](https://mod.io/g/baldursgate3/u/reddrik)• [1y ago](https://mod.io/g/baldursgate3/r/publishing-a-mod#1019356 "10/4/2024, 03:25 PM GMT-4")

When I try to publish my mod I only get the error message "An error occurred with this API request" with the info below: "An error occurred with this API request
Mod.io errorRef = 0"

I have connected with my Steam and Larian account and I've never posted a mod before. The only change the mod makes is a damage buff to a spell.

[R](https://mod.io/g/baldursgate3/u/reddrik)

[Reddrik](https://mod.io/g/baldursgate3/u/reddrik)• [1y ago](https://mod.io/g/baldursgate3/r/publishing-a-mod#1020773 "10/5/2024, 10:10 AM GMT-4")

I fixed the issue by changing the image I used for the mod. The one I used at first was broken since I converted from JPG to PNG in a way that didn't work that well.

[M](https://mod.io/g/baldursgate3/u/mrstigma)

[MrStigma](https://mod.io/g/baldursgate3/u/mrstigma)• [1y ago](https://mod.io/g/baldursgate3/r/publishing-a-mod#1006666 "9/26/2024, 03:26 PM GMT-4")

I'm having trouble packing my Class mod to publish on Vortex.
I've tried using the .pak file made by "Publish Local" but none of my class emblems show up.
So, I tried creating a folder for the mod with 3 folders inside "Localization" "Mods" & "Public" Localization and Public were copies of the Bg3/mods deployment folder
when I tried that the mod wouldn't show up at all.
when I test the mod threw the Toolkit it works, and all the class pictures show up.
All the DDS and PNG files are in the right folder, and I've already converted all UI assets.
Any help would be appreciated!

Edit: The mod contains a new class and 3 Subclasses if that makes a difference.

[J](https://mod.io/g/baldursgate3/u/modiouser2120941)

[Jason-L](https://mod.io/g/baldursgate3/u/modiouser2120941)• [1y ago](https://mod.io/g/baldursgate3/r/publishing-a-mod#1005744 "9/25/2024, 08:52 PM GMT-4")

Hello, I have a question. I've made a translation of a mod and I'd like to import this translation, but I have absolutely no idea how to do it. I'd like to know if it's possible to import a mod that I've translated, and if so, how?

[R](https://mod.io/g/baldursgate3/u/rahl81stefano)

[Rahl81](https://mod.io/g/baldursgate3/u/rahl81stefano)• [1y ago](https://mod.io/g/baldursgate3/r/publishing-a-mod#996414 "9/20/2024, 12:38 AM GMT-4")

Help
I can't start the tool...I have this error inside the folder::

C:\\Program Files (x86)\\Steam\\steamapps\\common\\Baldurs Gate 3 Toolkit\\EoCPlugin.dll \[version \]

An unhandled exception has occurred in the game, get a programmer!
Restart the editor to avoid data corruption!

Exception Type: EXCEPTION\_ACCESS\_VIOLATION
Additional Information: Attempted to read inaccessible data (Read access violation) at address 0x0

[O](https://mod.io/g/baldursgate3/u/orcsofthemintymounta)

[OrcsOfTheMintyMounta](https://mod.io/g/baldursgate3/u/orcsofthemintymounta)• [1y ago](https://mod.io/g/baldursgate3/r/publishing-a-mod#1015105 "10/1/2024, 09:14 PM GMT-4")

You can try uninstalling and reinstalling and that will probably fix it, or verify your files

[L](https://mod.io/g/baldursgate3/u/lokia2)

[Lokia2](https://mod.io/g/baldursgate3/u/lokia2)• [1y ago](https://mod.io/g/baldursgate3/r/publishing-a-mod#993646 "9/18/2024, 06:29 AM GMT-4")

what it is? and how to solve it?
Mod Status:
Not Accepted
This mod requires game moderator approval to be available to play.

[X](https://mod.io/g/baldursgate3/u/xichr15ix)

[Xichr15iX](https://mod.io/g/baldursgate3/u/xichr15ix)• [1y ago](https://mod.io/g/baldursgate3/r/publishing-a-mod#988017 "9/14/2024, 11:50 PM GMT-4")

I was trying to publish my mod but when I clicked publish it took me to Mod.io's site and said I didnt have access, Im fairly certain this was because I didnt have my Larian account linked. I have now linked my Larian account but now when I try to publish I get the following 2 error messages:

"The supplied access token has either been revoked, has expired or is malformed. Please generate a new one.
Mod.io errorRef = 11005"

"The mod ID you have included in your request could not be found.
Mod.io errorRef = 15024"

As stated in the first error, I am assuming I need to generate a new access token but how do I do that?
Any help would be greatly appreciated!

[S](https://mod.io/g/baldursgate3/u/ashleyskennedy)

[Selenazz](https://mod.io/g/baldursgate3/u/ashleyskennedy)• [1y ago](https://mod.io/g/baldursgate3/r/publishing-a-mod#1144881 "12/30/2024, 03:15 AM GMT-5")

trying to re-log into ur account in tooltik , i successfully resolve the same issue by this

[B](https://mod.io/g/baldursgate3/u/bonkers28)

[bonkurs](https://mod.io/g/baldursgate3/u/bonkers28)• [1y ago](https://mod.io/g/baldursgate3/r/publishing-a-mod#1005029 "9/25/2024, 12:26 PM GMT-4")

Same here. I managed to figure out this atrocious toolkit, but it still won...

[B](https://mod.io/g/baldursgate3/u/bellpaul)

[BellPaul](https://mod.io/g/baldursgate3/u/bellpaul)• [1y ago](https://mod.io/g/baldursgate3/r/publishing-a-mod#986568 "9/14/2024, 09:06 AM GMT-4")

Somehow my project is stuck at loading(buttom left corner one always stuck at around 70 to 80% after local publish and unable to public publish any more

I wonder why

[V](https://mod.io/g/baldursgate3/u/vahnsmash)

[VahnSmash](https://mod.io/g/baldursgate3/u/vahnsmash)• [1y ago](https://mod.io/g/baldursgate3/r/publishing-a-mod#986515 "9/14/2024, 07:56 AM GMT-4")

Okay so if I set a common library as a dependency in mod.io, anyone subscribed to my mod will auto-download the dependency? Because when I tested it myself the dependency didn't appear in my installed mods tab until I sought it out manually and subscribed, and I know the average user isn't going to do that.

[B](https://mod.io/g/baldursgate3/u/barazwolf)

[BarazWolf](https://mod.io/g/baldursgate3/u/barazwolf)• [1y ago](https://mod.io/g/baldursgate3/r/publishing-a-mod#982091 "9/11/2024, 01:33 PM GMT-4")

There is definately something confusing about how local projects are presented in BG3 :
\- my project mod is applied in practice when I load a save in BG3, yet \*not\* shown in the installed mods in BG3 ;
\- third-party BG3MM, on the other hand, clearly detects the project and shows it quite clearly.

To be clearer : I did not subscribe to the published version and the pak is also \*not\* placed in any of the Users..AppData... folders (so just saying here the pak is also not along the third-party mods, which is normal, and even the Local Mods folder is empty).

I am not 100% certain what happens if I subscribe to my own mod, but I think that works fine, but again that will certainly cause confusion between a new build of the project and the subscribed version. Some clarity will be needed.

SUGGESTION to Larian : show the active mod projects clearly in the BG3 internal mod manager, the same way BG3MM showcases them clearly. Also, a new build in the Toolkit and the subscribed version must be shown as two different mods.

[O](https://mod.io/g/baldursgate3/u/orioninvictus)

[OrionInvictus](https://mod.io/g/baldursgate3/u/orioninvictus)• [1y ago](https://mod.io/g/baldursgate3/r/publishing-a-mod#980274 "9/10/2024, 08:00 AM GMT-4")

For the life of me, I cannot publish locally. It just doesn't do anything. The log says it was successful, but there's no .pak file. I've asked on the Discord and a few other places for help, but nobody seems to know anything (or I'm just being ignored, but I doubt that's the case).

I've tried publishing on two different folders in two different drives multiple times. I've even tried running Steam with admin privileges, in case there was some weird thing about writing permissions. Nothing works.

EDIT: Turns out if you have non-English characters in your Windows user folder, the toolkit can't create the .pak. It's stupid that a quarter of the way into the 21st century we still have to deal with this, but alas.

The only fix I could find was to create a new Windows user whose name didn't contain non-English characters and do everything there instead.

[J](https://mod.io/g/baldursgate3/u/jbj3dart)

[JBJ\_3Dart](https://mod.io/g/baldursgate3/u/jbj3dart)• [1y ago](https://mod.io/g/baldursgate3/r/publishing-a-mod#995424 "9/19/2024, 12:51 PM GMT-4")

bg3 local mod publishing not working

I can confirm that this is the problem, it happened to me both in other programs and in the bg3 toolkit.

I couldn't find a solution, but one thing that is easy is that you can open the toolkit directly from the program files even if you are using another user (without foreign characters). Then just export it to the bg3 data folder and you will be able to access it in the original user

[S](https://mod.io/g/baldursgate3/u/sqelson1)

[Sqelson1](https://mod.io/g/baldursgate3/u/sqelson1)• [1y ago](https://mod.io/g/baldursgate3/r/publishing-a-mod#979762 "9/9/2024, 09:10 PM GMT-4")

trying to access Project Settings comes up with an error message of the following:

Unhandled exception has occured in a component in your application.
If you click Continue, the application will ignore the error and attempt to continue.

An item with the same key has already been added.

clicking continue doesn't seem to work or do anything, and the details don't make much sense to me either, but for context i am simply changing some item values (such as rarity, effects and damage) and have overridden GustavDev to do so (namely a couple of Weapons and a Passive in the Stats Browser)

EDIT: for those not in the discord, here is the solution copy-pasted (thank you chloé!):

I did, but I found the reason for my problem! (System.ArgumentException: An item with the same key has already been added.)

I'm gonna type it out here in case anyone else has it and is searching for it.
I looked through my message log and found error messages for 4 mods I had installed, with their UUIDs. (unvisual volo's eye, unvisual half illithid, blossom's presets, demon eyes). Coincidentally, whenever I tried to enable these mods in the ingame mod manager, the button simply didn't work. My current theory is that their UUIDs were simply invalid, and caused some kind of error in the game. I deleted those mods from my Mods folder (Local Appdata/larian/bg3/mods/)
And now I can open my Project Settings!

[B](https://mod.io/g/baldursgate3/u/bellpaul)

[BellPaul](https://mod.io/g/baldursgate3/u/bellpaul)• [1y ago](https://mod.io/g/baldursgate3/r/publishing-a-mod#1009989 "9/28/2024, 05:07 PM GMT-4")

Sorry but some how another way
Just move all mods from the Mod folder if your mod is not doing something big enough
But doing this will definitely clear out all your mods, so use this on your own risk and only put this as your last resort

[S](https://mod.io/g/baldursgate3/u/horro2)

[shimcot](https://mod.io/g/baldursgate3/u/horro2)• [1y ago](https://mod.io/g/baldursgate3/r/publishing-a-mod#979022 "9/9/2024, 11:47 AM GMT-4")

Why does my new class mod works in toolkit but not in game after publishing?

[K](https://mod.io/g/baldursgate3/u/vaugnard)

[Kreiyu](https://mod.io/g/baldursgate3/u/vaugnard)• [1y ago](https://mod.io/g/baldursgate3/r/publishing-a-mod#975657 "9/7/2024, 04:32 PM GMT-4")

tried installing after publishing locally, and the dice are invisible in game. they are listed in my dice menu, everything seems to have worked, but there are no visuals.

[F](https://mod.io/g/baldursgate3/u/frozenoj)

[FrozenOJ](https://mod.io/g/baldursgate3/u/frozenoj)• [1y ago](https://mod.io/g/baldursgate3/r/publishing-a-mod#979862 "9/9/2024, 10:15 PM GMT-4")

Did you figure it out? I just tried it with a set that I have published on Nexus and published locally I'm also getting invisible dice in game. ETA: Figured it out, I made a typo in the folder name lol

[I](https://mod.io/g/baldursgate3/u/inquisitormendoza)

[InquisitorMendoza](https://mod.io/g/baldursgate3/u/inquisitormendoza)• [1y ago](https://mod.io/g/baldursgate3/r/publishing-a-mod#975593 "9/7/2024, 03:52 PM GMT-4")

Is there a option to not Publish the mod but still use it yourself like there was in Divinity Original Sin 2 since I wanted to test the mod I made in the campaign so I could fine tune it better but I can't use it ingame.

[F](https://mod.io/g/baldursgate3/u/feartaylor)

[FearTaylor](https://mod.io/g/baldursgate3/u/feartaylor)• [1y ago](https://mod.io/g/baldursgate3/r/publishing-a-mod#979406 "9/9/2024, 05:09 PM GMT-4")

Yes, publish it locally directly into your mods folder

[K](https://mod.io/g/baldursgate3/u/kukoldun)

[Kukoldun](https://mod.io/g/baldursgate3/u/kukoldun)• [1y ago](https://mod.io/g/baldursgate3/r/publishing-a-mod#975551 "9/7/2024, 03:32 PM GMT-4")

I made my first mod and successfully uploaded it. Thank you very much!

[C](https://mod.io/g/baldursgate3/u/calamitysparks)

[CalamitySparks](https://mod.io/g/baldursgate3/u/calamitysparks)• [1y ago](https://mod.io/g/baldursgate3/r/publishing-a-mod#998432 "9/21/2024, 09:26 AM GMT-4")

I have the same issue. I created a rogue subclass with custome resource and some abilities - works fine in the toolkit but when I publish it, add it to the /users...../mods location and enable it in the game, it doesn't show the subclass when levelling up...

[M](https://mod.io/g/baldursgate3/u/modiouser5ett)

[ModioUser5ett](https://mod.io/g/baldursgate3/u/modiouser5ett)• [1y ago](https://mod.io/g/baldursgate3/r/publishing-a-mod#974712 "9/7/2024, 04:45 AM GMT-4")

Please provide instructions on how to install the .pak file after publishing locally

Edit: figured it out: put the .pak file in C:\\Users\\me\\AppData\\Local\\Larian Studios\\Baldur's Gate 3\\Mods

[I](https://mod.io/g/baldursgate3/u/ddezoete)

[iflod101](https://mod.io/g/baldursgate3/u/ddezoete)• [1y ago](https://mod.io/g/baldursgate3/r/publishing-a-mod#1005682 "9/25/2024, 08:07 PM GMT-4")

Expanding upon this solution.

I searched my PC and could not find the C:\\Users\\me\\AppData\\Local\\Larian Studios\\Baldur's Gate 3\\Mods folder.

I manually searched for 'larian' in my C drive and found the folder with the exact file path above. For some reason, on my PC, this is a ghost folder. It exists but isn't visible. I can access it by pasting the file path into my file browser. Very weird. I'm not super tech savy so I don't know what the issue is.

Just posting this in case anyone runs into the same issue. If you can't find the folder, search 'larian' in your C drive. When you find the folder in your search, make a shortcut so you don't need to search for it again.

[S](https://mod.io/g/baldursgate3/u/modiouser2074379)

[shinra528](https://mod.io/g/baldursgate3/u/modiouser2074379)• [1y ago](https://mod.io/g/baldursgate3/r/publishing-a-mod#1052613 "10/22/2024, 09:45 PM GMT-4")

The AppData folder is set to hidden by default. An easy way to get to it quickly is to type %localappdata% into the address bar of File Exporer.

[B](https://mod.io/g/baldursgate3/u/barazwolf)

[BarazWolf](https://mod.io/g/baldursgate3/u/barazwolf)• [1y ago](https://mod.io/g/baldursgate3/r/publishing-a-mod#982103 "9/11/2024, 01:40 PM GMT-4")

My experience, objectively, is that a locally published mod made in the Toolkit does \*not\* need a pak file anywhere under Users... AppData... It just works actually in game, BUT it is \*not\* shown in the BG3 internal mod manager, so it is quite confusing...

Yet the third-party BG3MM detects an active project perfectly and marks it clearly (still no pak needed).

Mind you, placing your mod as a pak under AppData... /Mods works also of course. I presume it overrides the project version, but that is totally unclear.

[R](https://mod.io/g/baldursgate3/u/realvondy)

[RealVondy](https://mod.io/g/baldursgate3/u/realvondy)• [1y ago](https://mod.io/g/baldursgate3/r/publishing-a-mod#988676 "9/15/2024, 11:40 AM GMT-4")

The fix he posted worked for me. If you start a fresh game with your mod in the projects folder it works, but because it's invisible, there is no way to enable it.

If you are testing a mod from a save file that WAS NOT started with the mod installed, you need to move the .pak file to where the top comment mentions, then check boxes in the in game manager to enable it.

[K](https://mod.io/g/baldursgate3/u/vaugnard)

[Kreiyu](https://mod.io/g/baldursgate3/u/vaugnard)• [1y ago](https://mod.io/g/baldursgate3/r/publishing-a-mod#975641 "9/7/2024, 04:21 PM GMT-4")

in the in game mod menu, go to the installed mods tab at the top. your mod should be listed, just check the box to enable it.

i'm having an issue though, where the dice are invisible in game. like it isn't packing the texture files or something. i installed the .pak file where i put all my previous mods, i can see it in the installed menu in the in game mod manager, but i'm not really sure if that is the right spot or not.

Last updated

302d

Reading time

8 min read

Views

8,196

Comments

38

[G\\
\\
GrumpyWashbear](https://mod.io/g/baldursgate3/u/grumpywashbear/r)

Follow GrumpyWashbear

- [Guide](https://mod.io/g/baldursgate3/r/publishing-a-mod#guide)
- [Project Settings](https://mod.io/g/baldursgate3/r/publishing-a-mod#heading-1)
- [Dependencies](https://mod.io/g/baldursgate3/r/publishing-a-mod#heading-2)
- [Conflicts](https://mod.io/g/baldursgate3/r/publishing-a-mod#heading-3)
- [Publishing Locally](https://mod.io/g/baldursgate3/r/publishing-a-mod#heading-4)
- [Publishing to Mod.io](https://mod.io/g/baldursgate3/r/publishing-a-mod#heading-5)
- [Authentication](https://mod.io/g/baldursgate3/r/publishing-a-mod#heading-6)
- [Editing Your Mod on Mod.io](https://mod.io/g/baldursgate3/r/publishing-a-mod#heading-7)
- [General Settings > Mod Profile](https://mod.io/g/baldursgate3/r/publishing-a-mod#heading-8)
- [General Settings > Media](https://mod.io/g/baldursgate3/r/publishing-a-mod#heading-9)
- [Dependencies](https://mod.io/g/baldursgate3/r/publishing-a-mod#heading-10)
- [Setting the Mod Live](https://mod.io/g/baldursgate3/r/publishing-a-mod#heading-11)
- [Discussion](https://mod.io/g/baldursgate3/r/publishing-a-mod#discussion)

[Editor](https://mod.io/g/baldursgate3/r?tags=Editor) [English](https://mod.io/g/baldursgate3/r?tags=English) [Getting Started](https://mod.io/g/baldursgate3/r?tags=Getting+Started) [Official](https://mod.io/g/baldursgate3/r?tags=Official)

Quick guide on how to publish your mod to mod.io, and other options available through that menu.

Share

Report guide

---
# SOURCE: https://mod.io/g/baldursgate3/r/adding-a-new-spell-basic
---

[Browse games](https://mod.io/g)

Browse games

[My library](https://mod.io/library)

My library

[My content](https://mod.io/content)

My content

My account

mod.io

mod.io

[All games](https://mod.io/g) [Baldur's Gate 3](https://mod.io/g/baldursgate3) [Guides](https://mod.io/g/baldursgate3/r) [English](https://mod.io/g/baldursgate3/r?tags=English) Adding a New Spell (Basic)

Adding a New Spell (Basic)

Share

Report

Follow

In this guide, we will cover how to make a simple target-based spell.

## Locating the Spell Data

Open the **Stats Editor** via the bar chart icon located in the top right of the menu bar.

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_01.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_01.png)

In the left column, there will be a list of Projects. Open the one that corresponds to your mod’s name – it should be the same as your project’s name. For the purposes of this guide, our mod is called **SimpleNewSpell**. Expand the project to see its subfolders.

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_02.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_02.png)

Here, you will see various sections you can open and modify. To create spells, go to SpellData and click the “+” symbol.

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_03.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_03.png)

This will open a dropdown of the various spell types that are available in the game.

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_04.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_04.png)

For the target spell we are making, you’ll need to add both `Target` and `Projectile` spell data. You might need to expand the SpellData folder to see your new additions.

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_05.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_05.png)

## Making a Target Spell

We will be making a Touch spell (a spell that requires the caster to touch the target) that explodes on a target. The explosion will deal Fire damage to everyone in the area and heal the caster.

Open your newly created Target spell data.

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_06.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_06.png)

For Target spells, there are a few **required** fields that must be filled in for the spell to execute correctly in the game. We will be going over those required fields, as well as some extras needed for the above example.

### Name (Technical Name)

You will need to fill in the **Name** field for the spell. This is the spell’s Technical Name, also rereferred to as its TechName. This is what the system uses to give a specific spell to the player.

This field:

- Does not accept spaces

- Accepts underscores `_` (often used in lieu of spaces)

- Accepts numbers and uppercase and lowercase letters


In our example, we will use the TechName `FireTouch`.

### Level and SpellSchool

If you want your spell to show up as part of a specific level (Cantrip, Level 1, etc.) or spell school (Evocation, Divination, Necromancy, etc.), fill out the **Level** and **SpellSchool** fields.

- The **Level** field accepts numbers.
  - 0 = Cantrip

  - 1 = Level 1 spell

  - 2 = Level 2 spell, etc.
- The **SpellSchool** field is a dropdown of spell schools.


We want to make our spell a Level 3 Evocation spell, similar to Fireball, so we’ll fill in 3 for the **Level**, and select `Evocation` from the **SpellSchool** dropdown.

This information will automatically appear in the in-game tooltip.

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_07.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_07.png)

### TargetRadius

The TargetRadius determines how close the caster has to be to the target in order to cast the spell.

We want to make our spell a Touch spell. This means that the player will need to be in melee range of their target in order to cast it in the first place.

- This field accepts numbers and decimals.

- The field’s value is in metres.


For our new spell `FireTouch`, we will fill in `1.5` for the **TargetRadius**. This is the value used for melee range in Baldur’s Gate 3.

### AreaRadius

The AreaRadius determines the area of effect of the spell.

We want our spell to affect those around us, so we will also need to fill in the **AreaRadius** field.

- This spot accepts numbers and will take decimals

- This value is in meters


For our new spell, we will fill in `3`. This means that the spell will effect everyone within 3 m of the target.

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_08.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_08.png)

### SpellRoll

All spells must have either **SpellRoll** or **SpellProperties** defined. In our case, we’ll use **SpellRoll**.

SpellRoll describes what type of spell it is. There are two common options used in BG3: `SavingThrow()` and `Attack()`.

For our example, we'll make a SavingThrow type spell, which is one that requires the target to make a Saving Throw. To do so, we’ll paste the following into the SpellRoll field:

`not SavingThrow(Ability.Dexterity, SourceSpellDC())`

You can change the `Ability.Dexterity` part to be any ability type in the game (e.g. `Ability.Charisma`, `Ability.Strength`).

Because we’re making a SavingThrow type of spell, we will need to fill in the **SpellSuccess** and **SpellFail** fields. We’ll go into how to fill in both of these in the next sections.

- **SpellSuccess** is for what happens **when the caster succeeds**, meaning the enemy has failed their Saving Throw.

- **SpellFail** is for what happens **when the caster fails**, meaning the enemy has passed their Saving Throw.
  - The **SpellFail** field is optional and can be left blank.

### SpellSuccess

Fill in the **SpellSuccess** field to define what happens when the caster succeeds. For our new spell, we want two things: we want to heal the caster, and we want to damage the target and any others in the area.

- Use `IF()` statements to define what happens to each character.

- To refer to the caster, use `Self()`.

- To refer to everyone except the caster, use `not Self()`.


To heal the caster, we will use `IF(Self()):RegainHitPoints(3d10)`

- `RegainHitPoints()` can take dice rolls (e.g. `3d10`) or specific numbers (e.g. `9`).


To damage the targets, since we want everyone else except for the caster to be damaged, we will use `IF(not Self()):DealDamage(3d10,Fire,Magical)`

- `DealDamage()` can take dice rolls or specific numbers.

- `Fire` indicates the damage type.

- `Magical` indicates that it deals magical damage, for the sake of resistance.
  - Because this is a spell, the damage is magical.

Separate each action with a `;`. Put together, it looks like this:

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_09.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_09.png)

### SpellFail

Fill in the **SpellFail** field to define what happens when the caster fails. We will do almost the same thing as we did for SpellSuccess, but for our new spell, we want to deal only half the healing and half the damage on fail. We can take what we wrote for SpellSuccess and modify it slightly by dividing the values by 2 using `/2`.

- For healing:`IF(Self()):RegainHitPoints(3d10/2)` or `IF(Self()):RegainHitPoints((3d10)/2)`

- For damage: `IF(not Self()):DealDamage(3d10/2,Fire,Magical)` or `IF(not Self()):DealDamage((3d10)/2,Fire,Magical)`


Again, separate each action with a `;`. Put together, it looks like this:

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_10.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_10.png)

### TargetConditions

**TargetConditions** filter out who the caster can cast the spell on. For example, if we input Self(), the player would would only be able to cast the spell on themselves.

Because we want the player to target any character that is alive, we will use: `Character() and not Dead()`

### AoEConditions

If we want the Area of Effect (AoE) of this spell to affect a specific type of character, we can define the conditions in the **AoEConditions** field. For example, if we only want the AoE explosion to affect the enemies of the caster, we can write `Enemy()` here. Another valid option in this field is `Ally()`.

In our new spell, `FireTouch`, we want _everyone_ to be damaged, so we’ll use the same as TargetConditions.

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_11.1.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_11.1.png)

## Player-facing Information

This next section of stats columns is all about filling the player-facing and tooltip information, so players can understand what the spell does.

### Icon

Here you can define an icon. For the purposes of this guide, let's reuse an existing spell icon from the Fireball spell: `Spell_Evocation_Fireball`.

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_14.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_14.png)

### DisplayName

This will be the spell name shown on the tooltip. Let’s call our new spell `Touch of Fire`.

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_15.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_15.png)

Below, you can see how this name would appear on the tooltip.

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_16.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_16.png)

### Description

This will be the information given to the player when they view the tooltip. This text should **only** include letters. Generally, you want to give players an idea of what the spell does.

For our spell we will write:

`Touch an enemy with the force of a fireball. Everyone in the area will take [1] and the caster will be [2].`

### DescriptionParams

As you may have noticed in the above description we used a `[1]` and `[2]`. These are filler spots for the description parameters - DescriptionParms.

In our spell’s tooltip description, we want to indicate that enemies take damage and the player is healed, so we will grab the same `DealDamage()` and`RegainHitPoints()` as we added to the `SpellSuccess`.

We will plug them into the DescriptionParms in same order we want the tooltip to display it.

- \[1\] should be DealDamage(3d10,Fire)

- \[2\] should be RegainHitPoints(3d10)


So into `DescriptionParms`, we’ll input `DealDamage(3d10,Fire);RegainHitPoints(3d10)`

Note that in this version of DealDamage() for the tooltip, the `Magical` is not used.

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_17.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_17.png)

If done correctly, your tooltip for the spell would now have text that indicates the damage and healing given by the spell:

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_18.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_18.png)

### TooltipDamageList and TooltipAttackSave

These are the last bits of the tooltip that we will be modifying for our spell. The **TooltipDamageList** gives the player a visually concise way to see the damage and healing effects of the spell. This will use the exact same functions as our DescriptionParms.

`DealDamage(3d10,Fire);RegainHitPoints(3d10)`

The **TooltipAttackSave** is used for Saving Throw spells to indicate what type of save it is. Our spell is a Dexterity based save so we will put Dexterity in this section.

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_19.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_19.png)

With those fields filled in, your spell’s tooltip would now show the dice visual, as well as the DEX Save at the bottom.

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_20.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_20.png)

### CastTextEvent

Spells all need their CastTextEvent filled out. This is related to the animation that the caster is using – animations look for this cast event to in order to execute parts of the spell.

For our spell we only want to execute one cast event, so we will just write `Cast` in this column.

If you forget to fill this out, your animation may have a delay instead of casting smoothly.

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_21.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_21.png)

### UseCost

This is used to determine what resource is needed to cast the spell. Right now, there is no use cost associated with our spell.

Let’s say that we want FireTouch to cost one Action Point and one Level 3 Spell Slot.

- ActionPoint:1
  - This means it will cost one Action Point.
- SpellSlotsGroup:1:1:3
  - This means it will take one level 3 spell slot to cast the spell.

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_22.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_22.png)

If you have done this correctly, your tooltip would now show the cost of the spell as below:

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_23.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_23.png)

### Spell Animation

All spells need a spell animation in order to be used. Without a spell animation, the spell cannot be cast.

Let’s grab an existing animation and use it. In the Stats Editor, unfold the Shared section on the left, then unfold the SpellData inside it.

Open the Target file inside that SpellData by double clicking on it.

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_24.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_24.png)

We are looking for a Touch animation spell, so we will `Ctrl+F` to open the search bar at the bottom and type in 'Touch'. Press Enter to search.

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_25.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_25.png)

You should see the area below the search bar update with the results, showing you all the spells in the Shared Target file that have the word Touch in their name.

Let’s use the Vampiric Touch animations.

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_26.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_26.png)

If you double click on Vampiric Touch (any of the VampiricTouch results will do) it will take you to that row in the Target file. It should be row 179.

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_27.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_27.png)

Scroll over until you find the SpellAnimation column (column BL).

Click on the cell containing VampiricTouch’s Spell Animation data, and `Ctrl+C` to copy all the spell animation information.

Return to your mod's Target file and `Ctrl+V` paste the copied spell animation into FireTouch’s Spell Animation column. Your Spell Animation column should now look like this.

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_28.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_28.png)

### PrepareEffect, CastEffect, HitEffect

These effects are how we apply visuals onto our spells. All of these columns are dropdowns that show all the existing effects available in game.

If you’d like to make your own effects, please refer to the VFX Guide **\[\[coming soon\]\]** \- but for now we’ll use some existing visuals.

`PrepareEffect` is the pre-casting of the spell. This is the period after you have chosen a spell, but you haven't yet selected the target. For `FireTouch` we want something fire-based, so let’s type ‘fire’ into the drop down to filter down the results.

The PrepareEffect requires an effect that has the `_PrepareEffect` suffix, so let’s use `Fireball_PrepareEffect`.

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_29.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_29.png)

`CastEffect` is the visual on the caster while the spell is being executed. You might have noticed earlier that Fireball also has a cast effect, so let’s use that one here. Like with PrepareEffect, the CastEffect should have the `_CastEffect` suffix.

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_30.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_30.png)

Finally, `HitEffect` is for the visual that plays on the target of the spell when it connects with them. Here too, the effect should end in `_HitEffect`, and once again we’ll reuse the one from Fireball: `Fireball_HitEffect`

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_31.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_31.png)

### PrepareSound, PrepareLoopSound, CastSound

These fields are how we apply sounds onto our spells. Creating new sounds is not supported at this time, and therefore the best method is to look for a similar spell and copy values from it to our spell, much like we did for the VFX. For our FireTouch spell, we’ll copy the Firebolt sounds from Shared → Projectile:

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_32.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_32.png)

Now our spell should have sound!

### SpellFlag

Spell flags are used to give additional information on how the spell is expected to behave. These can vary from case to case. The dropdown in this field allows multiple options to be selected.

For `FireTouch`, let’s select the following:

- HasVerbalComponent

- HasSomaticComponent

- IsMelee

- IsSpell

- IsHarmful


[![](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_33.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_33.png)

**HasVerbalComponent:** Spells with this flag will become unusable if the caster is Silenced.

**HasSomaticComponent:** Used for spells that require somatics in order to cast.

**IsMelee:** Used for attacks and/or spells that are within melee range.

**IsSpell:** Recommended for any spell that is meant to be considered a spell in DnD. Using this flag makes the spell work with other systems like silencing, counterspelling and armor proficiency requirements. Without this flag, your spell will show as a 'Class Action' on the tooltip if its spell level is 0.

**IsHarmful:** If enabled, this flag lets the AI know whether or not to bring NPCs into combat. If the spell does damage, this should naturally happen, but if there’s a chance that the target could save and negate the damage, we want this flag there as well.

A few other common flags that are not being used in this example, but might be interesting:

- **IsConcentration:** Used to make a spell into a concentration spell.

- **IsAttack:** Used for attacks that are not meant to be magical.

- **Temporary:** Used to open the temporary section of the hotbar for spells that the player only has for a short time.


## Testing Our Spell

Now, with all of these fields filled out, we can test the spell. To test the spell, we need to add it to one of the class spell lists so we can pick it during Character Creation or Level Up.

Open the UUID Editor and create a new SpellLists table in the Lists section:

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_34.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_34.png)

In the newly opened table, click on `+` to add a new entry. Fill in the Name column - this is just for developers/modders in case you want to add to your list later. In the `Spells` column, add the Tech Name of your new spell. In the case of multiple spells, separate them with a semicolon (`;`). Finally, in the `MergedInto` column, select the original list you want to add your new spell to. Since we made `FireTouch` a Level 3 spell, choose the `Cleric SLevel 3` list.

[![](https://image.modcdn.io/members/84a7/35494594/profile/image-2025-07-22t152356013.png)](https://image.modcdn.io/members/84a7/35494594/profile/image-2025-07-22t152356013.png)

> The “tech name” we refer to here is the `SpellType_SpellName`.
>
> In this case, the type is `Target`, and the spell name is `FireTouch`, so together it becomes `Target_FireTouch`.

We can leave Comment field empty. This field is not used by game in any way, and only serves as a note for developers.

Save all of your changes thus far.

To test, you’ll need to load a level, if you haven’t already. `Basic_Level_A` is perfectly sufficient. Once a level is loaded, enter Game Mode.

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_37.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_37.png)

With your cursor over the character portrait, press `Ctrl+Shift+L` to level them up. Click the Level Up button to enter the Level Up screen.

If your test character isn’t already a Cleric, add the Cleric class using the Multiclassing menu.

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_38.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_38.png)

You’ll need to level up a few more times, until you’re a level 5 Cleric, to get your level 3 spells list. Once there, go to the Spells tab - in the list of available spells, you should see the newly added spell: **Touch of Fire**. Once we pick it, we can use it in game and check that all parts work as intended.

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_41.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_41.png)

### TargetRadius and HitRadius

Use `Ctrl+Shift+3` to spawn in a wolf.

When casting the spell, there are two circles present on the ground. The smaller circle (highlighted green in screenshot below) is our TargetRadius of 1.5, and the larger circle (highlighted magenta) is our AreaRadius.

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_42.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_42.png)

### PrepareEffect, CastEffect, HitEffect, SpellAnimation

When going to cast our spell, we should be able to see that our character has a fire-based visual around her. This is the PrepareEffect along with the Spell Animation.

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_43.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_43.png)

When the charater goes to cast the spell, we can see them step forward with a glow on their hand. This is the CastEffect and Spell Animation.

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_44.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_44.png)

When the spell is used on the wolf, we can see it that it has a fire effect. This is the HitEffect.

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_45.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_45.png)

### Combat Log

In this example, Shadowheart was the caster of the spell against a wolf. In the combat log, you can double-check the values of the spell: our wolf enemy was dealt 7 fire damage (3d10/2) and Shadowheart was healed (3d10/2) because they both passed their saves.

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_46.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/basic_46.png)

[G\\
\\
GrumpyWashbear](https://mod.io/g/baldursgate3/u/grumpywashbear/r)

Follow GrumpyWashbear

Log in to join the discussion!

Last updated

162d

Reading time

17 min read

Views

28,462

Comments

98

[G\\
\\
GrumpyWashbear](https://mod.io/g/baldursgate3/u/grumpywashbear/r)

Follow GrumpyWashbear

- [Guide](https://mod.io/g/baldursgate3/r/adding-a-new-spell-basic#guide)
- [Locating the Spell Data](https://mod.io/g/baldursgate3/r/adding-a-new-spell-basic#heading-1)
- [Making a Target Spell](https://mod.io/g/baldursgate3/r/adding-a-new-spell-basic#heading-2)
- [Name (Technical Name)](https://mod.io/g/baldursgate3/r/adding-a-new-spell-basic#heading-3)
- [Level and SpellSchool](https://mod.io/g/baldursgate3/r/adding-a-new-spell-basic#heading-4)
- [TargetRadius](https://mod.io/g/baldursgate3/r/adding-a-new-spell-basic#heading-5)
- [AreaRadius](https://mod.io/g/baldursgate3/r/adding-a-new-spell-basic#heading-6)
- [SpellRoll](https://mod.io/g/baldursgate3/r/adding-a-new-spell-basic#heading-7)
- [SpellSuccess](https://mod.io/g/baldursgate3/r/adding-a-new-spell-basic#heading-8)
- [SpellFail](https://mod.io/g/baldursgate3/r/adding-a-new-spell-basic#heading-9)
- [TargetConditions](https://mod.io/g/baldursgate3/r/adding-a-new-spell-basic#heading-10)
- [AoEConditions](https://mod.io/g/baldursgate3/r/adding-a-new-spell-basic#heading-11)
- [Player-facing Information](https://mod.io/g/baldursgate3/r/adding-a-new-spell-basic#heading-12)
- [Icon](https://mod.io/g/baldursgate3/r/adding-a-new-spell-basic#heading-13)
- [DisplayName](https://mod.io/g/baldursgate3/r/adding-a-new-spell-basic#heading-14)
- [Description](https://mod.io/g/baldursgate3/r/adding-a-new-spell-basic#heading-15)
- [DescriptionParams](https://mod.io/g/baldursgate3/r/adding-a-new-spell-basic#heading-16)
- [TooltipDamageList and TooltipAttackSave](https://mod.io/g/baldursgate3/r/adding-a-new-spell-basic#heading-17)
- [CastTextEvent](https://mod.io/g/baldursgate3/r/adding-a-new-spell-basic#heading-18)
- [UseCost](https://mod.io/g/baldursgate3/r/adding-a-new-spell-basic#heading-19)
- [Spell Animation](https://mod.io/g/baldursgate3/r/adding-a-new-spell-basic#heading-20)
- [PrepareEffect, CastEffect, HitEffect](https://mod.io/g/baldursgate3/r/adding-a-new-spell-basic#heading-21)
- [PrepareSound, PrepareLoopSound, CastSound](https://mod.io/g/baldursgate3/r/adding-a-new-spell-basic#heading-22)
- [SpellFlag](https://mod.io/g/baldursgate3/r/adding-a-new-spell-basic#heading-23)
- [Testing Our Spell](https://mod.io/g/baldursgate3/r/adding-a-new-spell-basic#heading-24)
- [TargetRadius and HitRadius](https://mod.io/g/baldursgate3/r/adding-a-new-spell-basic#heading-25)
- [PrepareEffect, CastEffect, HitEffect, SpellAnimation](https://mod.io/g/baldursgate3/r/adding-a-new-spell-basic#heading-26)
- [Combat Log](https://mod.io/g/baldursgate3/r/adding-a-new-spell-basic#heading-27)
- [Discussion](https://mod.io/g/baldursgate3/r/adding-a-new-spell-basic#discussion)

[English](https://mod.io/g/baldursgate3/r?tags=English) [Official](https://mod.io/g/baldursgate3/r?tags=Official) [Spells](https://mod.io/g/baldursgate3/r?tags=Spells) [Stats](https://mod.io/g/baldursgate3/r?tags=Stats)

A step-by-step guide on creating a simple new spell - a Touch spell that explodes on a target, dealing Fire damage to everyone in the area, and healing the caster.

Share

Report guide

---
# SOURCE: https://mod.io/g/baldursgate3/r/editor-shortcuts-and-tips
---

[Browse games](https://mod.io/g)

Browse games

[My library](https://mod.io/library)

My library

[My content](https://mod.io/content)

My content

My account

mod.io

mod.io

[All games](https://mod.io/g) [Baldur's Gate 3](https://mod.io/g/baldursgate3) [Guides](https://mod.io/g/baldursgate3/r) [Editor](https://mod.io/g/baldursgate3/r?tags=Editor) Editor - Shortcuts and Tips

Editor - Shortcuts and Tips

Share

Report

Follow

## Did You Know?

- You can create shortcuts that will automatically load a certain mod or project, and immediately start loading a level, so that you don't waste time waiting for windows and clicking buttons:
  - The syntax is `Glasses.exe -project ProjectName -lvl LevelName`.

  - Example: `Glasses.exe -project GustavDev -lvl WLD_Plains_D`

  - You can create multiple copies of shortcuts on your desktop to quickly load certain levels you often need, and keep a shortcut without arguments so you can still load up the normal toolkit.
- **Filter on Type:** In the Root Templates window, **right-click** an icon to quickly deselect all other item types.
  - Example: Right-click on the item icon, and only items will be shown.

  - This also works in the Resource Manager.
- **Filter on Name**: Start typing in the filter box. Filter out results you don't want by adding a term with an exclamation mark. For instance, with` WLD_Main_A` loaded:
  - type **\_door\_** to show all door roots

  - type \_ **single\_ \_door\_** to show all single doors (the search is fairly intelligent and does not care about position)

  - type **single \_door\_ !temple** to show all single doors but exclude all roots that have “temple” in their names
- You can select **multiple roots** at the same time, and then change properties of roots **in bulk**. Example:
  - If all \_door\_ roots need a UseSound, filter roots (see above) and select all roots that you want (use shift and/or CTRL to multi select roots)

  - Click on the button "Load Multiselected Objects" in the properties window

  - Check out the selected roots (by either right click on the roots, or clicking the button on top of the properties window)

  - Change the property you want (OnUseSound)

  - Click Save

## Debug Console

Open the debug console with Ctrl+Shift+F11. The following commands are available:

- givetreasure

- create %item% %amount%

- addDebugSpell %name%

- addDebugSpellAsClass %spellname% %classname%

- levelup %amount%

- ccStartNew

- ccStartRespec

- killCombat

- peace

- god

- roll %value%

- reloadStats

- statusApply

- statusRemove

- applyPassive

- removePassive

- endTurnCombat

- Select

- SelectByUUID

- SelectPlayer


## Keyboard Shortcuts

### Debug

| **Shortcut** | **Action** |
| --- | --- |
| Ctrl+Shift+F7 | Graphics debug menu |
| Ctrl+Shift+F9 | Open gameplay debuggers |
| Ctrl+Shift+F10 | Opens a window with real-time renderstats |
| Ctrl+Shift+C | In the Main Menu, automatically connects your client to a host running on the same machine (direct connect must be enabled) |
| Ctrl+Shift+L | Levels up selected character (cursor must be over portrait) |
| Ctrl+Shift+1 | Recruit Shadowheart instantly |
| Ctrl+Shift+2 | Recruit Gale instantly |
| Ctrl+Shift+3 | Spawn an angry wolf in front of you (good for combat tests) |

### Editor Mode

| **Shortcut** | **Action** |
| --- | --- |
| Ctrl+Enter | Toggle Game Mode |
| Ctrl+Shift+F4 | Force close the editor |
| Ctrl+Shift+O | Open the project menu |
| Ctrl+O | Open level menu |
| Ctrl+R | Reload |
| Ctrl+B | Toggles visibility of the sidebar |
| Ctrl+G | Game mode camera |
| Ctrl+Shift+G | Editor mode camera |
| Ctrl+L | Hide/show all gizmos |
| Ctrl+T | Teleport active character to your cursor |
| Ctrl+Shift+T | Teleport whole party to your cursor |

### Game Mode

| **Shortcut** | **Action** |
| --- | --- |
| Ctrl+Shift+R | Resurrect party |
| Ctrl+Shift+S | Force-close interactive dialog (must hover mouse over the speaker) |
| Ctrl+Shift+P | Party editor |
| Ctrl+Shift+K | Kill unit (must hover over unit to kill, either model or portrait) |
| Ctrl+Shift+End | Skip a turn in combat |
| Ctrl+T | Teleport active character to your cursor |
| Ctrl+Shift+M | Unlock all waypoints |
| Shift+Q | Guaranteed success on all rolls |
| Shift+W | Guaranteed failure on all rolls |
| Shift+E | Disables both of the two guarantee dice roll modes |

[G\\
\\
GrumpyWashbear](https://mod.io/g/baldursgate3/u/grumpywashbear/r)

Follow GrumpyWashbear

Log in to join the discussion!

[S](https://mod.io/g/baldursgate3/u/skarsnik6)

[Skarsnik1931](https://mod.io/g/baldursgate3/u/skarsnik6)• [321d ago](https://mod.io/g/baldursgate3/r/editor-shortcuts-and-tips#1213940 "2/12/2025, 03:06 PM GMT-5")

Is there any way to use the debug console commands through scripting?

[O](https://mod.io/g/baldursgate3/u/outlawzgosu)

[outlawzgosu](https://mod.io/g/baldursgate3/u/outlawzgosu)• [1y ago](https://mod.io/g/baldursgate3/r/editor-shortcuts-and-tips#1028664 "10/9/2024, 08:10 AM GMT-4")

How do you get the camera gto go to tactical view in editor mode?

[I](https://mod.io/g/baldursgate3/u/imcioco2)

[imCioco](https://mod.io/g/baldursgate3/u/imcioco2)• [1y ago](https://mod.io/g/baldursgate3/r/editor-shortcuts-and-tips#998320 "9/21/2024, 08:12 AM GMT-4")

Can you simulate long resting while in the editor?
Edit: found it, you need to write the command "oe campon" in the debug console

[P](https://mod.io/g/baldursgate3/u/cytotoxictce11)

[PhalarAluve](https://mod.io/g/baldursgate3/u/cytotoxictce11)• [1y ago](https://mod.io/g/baldursgate3/r/editor-shortcuts-and-tips#1002685 "9/23/2024, 06:06 PM GMT-4")

It's wild that you managed to piece that together 😂 Does \`oe\` do anything else? I haven't seen examples before.

[N](https://mod.io/g/baldursgate3/u/nightingale75)

[Nightingale75](https://mod.io/g/baldursgate3/u/nightingale75)• [1y ago](https://mod.io/g/baldursgate3/r/editor-shortcuts-and-tips#985212 "9/13/2024, 12:52 PM GMT-4")

Is it possible to spawn a diferent enemy than a wolf? I'm trying to test damage against some resistances and the wolf has none

[X](https://mod.io/g/baldursgate3/u/xichr15ix)

[Xichr15iX](https://mod.io/g/baldursgate3/u/xichr15ix)• [1y ago](https://mod.io/g/baldursgate3/r/editor-shortcuts-and-tips#982810 "9/11/2024, 08:57 PM GMT-4")

Does anyone know how to change the character you spawn in as, for example if I spawn in as Gael but wanted to change to Karlach to test things specific to her character, is there a way to do this?

[L](https://mod.io/g/baldursgate3/u/modiouser2077428)

[Lily9824](https://mod.io/g/baldursgate3/u/modiouser2077428)• [1y ago](https://mod.io/g/baldursgate3/r/editor-shortcuts-and-tips#985819 "9/13/2024, 08:24 PM GMT-4")

ctrl + shift + F11 and then do ccStartNew

[R](https://mod.io/g/baldursgate3/u/modiouser2077729)

[RivtRevan](https://mod.io/g/baldursgate3/u/modiouser2077729)• [1y ago](https://mod.io/g/baldursgate3/r/editor-shortcuts-and-tips#973140 "9/6/2024, 04:35 AM GMT-4")

How to unlock the Assets to move and change them?

Last updated

1y

Reading time

5 min read

Views

15,941

Comments

8

[G\\
\\
GrumpyWashbear](https://mod.io/g/baldursgate3/u/grumpywashbear/r)

Follow GrumpyWashbear

- [Guide](https://mod.io/g/baldursgate3/r/editor-shortcuts-and-tips#guide)
- [Did You Know?](https://mod.io/g/baldursgate3/r/editor-shortcuts-and-tips#heading-1)
- [Debug Console](https://mod.io/g/baldursgate3/r/editor-shortcuts-and-tips#heading-2)
- [Keyboard Shortcuts](https://mod.io/g/baldursgate3/r/editor-shortcuts-and-tips#heading-3)
- [Debug](https://mod.io/g/baldursgate3/r/editor-shortcuts-and-tips#heading-4)
- [Editor Mode](https://mod.io/g/baldursgate3/r/editor-shortcuts-and-tips#heading-5)
- [Game Mode](https://mod.io/g/baldursgate3/r/editor-shortcuts-and-tips#heading-6)
- [Discussion](https://mod.io/g/baldursgate3/r/editor-shortcuts-and-tips#discussion)

[Editor](https://mod.io/g/baldursgate3/r?tags=Editor) [English](https://mod.io/g/baldursgate3/r?tags=English) [Official](https://mod.io/g/baldursgate3/r?tags=Official)

An overview of editor tips and shortcuts you can use.

Share

Report guide

---
# SOURCE: https://mod.io/g/baldursgate3/r/editor-overriding-resources
---

[Browse games](https://mod.io/g)

Browse games

[My library](https://mod.io/library)

My library

[My content](https://mod.io/content)

My content

My account

mod.io

mod.io

[All games](https://mod.io/g) [Baldur's Gate 3](https://mod.io/g/baldursgate3) [Guides](https://mod.io/g/baldursgate3/r) [Editor](https://mod.io/g/baldursgate3/r?tags=Editor) Editor - Overriding Resources

Editor - Overriding Resources

Share

Report

Follow

## **Resource Manager**

The Resource Manager is the view where you can see all the resources available in the game. Resources are things like textures, models, materials, etc. From the Resource Manager, resources can be searched, filtered, edited, created, overridden and deleted.

[![](https://image.modcdn.io/members/63c0/31088933/profileeditor/resource01.png)](https://image.modcdn.io/members/63c0/31088933/profileeditor/resource01.png)

After opening the Resource Manager via the button on the top bar, it’ll open below. Your view might initially show only a thin, tall bar, but you can adjust the size manually by dragging the borders.

[![](https://image.modcdn.io/members/63c0/31088933/profileeditor/resource02.png)](https://image.modcdn.io/members/63c0/31088933/profileeditor/resource02.png)

To get the view in the screenshot shown above, right click on the window title and select **Dock as Tabbed Document**.

[![](https://image.modcdn.io/members/63c0/31088933/profileeditor/resource03.png)](https://image.modcdn.io/members/63c0/31088933/profileeditor/resource03.png)

Now you will be able to see the entirety of the Resource Manager. It can be divided into five main sections:

- Filters

- Packages List

- Resources List

- Previewer

- Properties


[![](https://image.modcdn.io/members/63c0/31088933/profileeditor/resource04.png)](https://image.modcdn.io/members/63c0/31088933/profileeditor/resource04.png)

We’ll go through a few of these sections in more detail below.

### Packages List

The Packages List shows all of the packages in the game, along with the mod you currently have open.

[![](https://image.modcdn.io/members/63c0/31088933/profileeditor/resource05.png)](https://image.modcdn.io/members/63c0/31088933/profileeditor/resource05.png)

#### Package Filter

The first packages in the list, **All** and **Recents**, work as filters for the entire collection of packages.

- **All:** Shows or hidesresources from **all projects**.

- **Recents:** Shows or hides resources that were **opened/edited recently**.


#### Current Module Packages

This is the **loaded module**– the one you selected in the Project Browser Window.

You will be able to create new resources in this package, and edit them. It is shown with a blue title.

The Current Module Package folder contains all the resources that belong to the opened module. Inside the main folder, you will see at least one package (red outline below):

[![](https://image.modcdn.io/members/63c0/31088933/profileeditor/resource06.png)](https://image.modcdn.io/members/63c0/31088933/profileeditor/resource06.png)

Resources always belongs to a package. You can new resources to the package already created for your project, or create additional packages to hold them for better organization.

#### Other Loaded Modules

The loaded module might be dependent on other modules, like development modules that contain all the resources from the game.

Navigating through these modules' resources you will be able to find animations, items, equipment and a variety of other things used in Baldur’s Gate 3, which you can then override in your module, or use as a reference for your own mod.

### Filters

To filter by the file name, start typing in the filter box. Your results will depend on what folder or package you have selected.

For example, with the “All” folder selected, searching for druid returns a long list of different resource types that all contain “druid” in their name.

[![](https://image.modcdn.io/members/63c0/31088933/profileeditor/resource07.png)](https://image.modcdn.io/members/63c0/31088933/profileeditor/resource07.png)

To filter for only one type of resource, right click on its icon. For example, right clicking on the Effect button will show only EffectResources with `druid` in their name. (You can right-click on the same icon to remove the filter.)

[![](https://image.modcdn.io/members/63c0/31088933/profileeditor/resource08.png)](https://image.modcdn.io/members/63c0/31088933/profileeditor/resource08.png)

You can filter out results you don't want by adding a term with an exclamation mark. Adding `!script` and `!cinematic` to the search query will additionally filter out those two terms, for example.

[![](https://image.modcdn.io/members/63c0/31088933/profileeditor/resource09.png)](https://image.modcdn.io/members/63c0/31088933/profileeditor/resource09.png)

### Resources List, Previewer, and Properties

The **Resources List** shows the collection of resources in the selected package or folder based on what you have visible via filters. Clicking on an individual resource will show more information in the Properties and Previewer.

[![](https://image.modcdn.io/members/63c0/31088933/profileeditor/resource10.png)](https://image.modcdn.io/members/63c0/31088933/profileeditor/resource10.png)

The Properties view will show information about the selected resource. There are some fields that can be found in all resources:

[![](https://image.modcdn.io/members/63c0/31088933/profileeditor/resource11.png)](https://image.modcdn.io/members/63c0/31088933/profileeditor/resource11.png)

- **File Name**: Full path of the resource file.

- **GUID**: Identifier of the resource.

- **Name**: Resource’s name.

- **Package Name**: The package to which the resource belongs. It can be read as `{project}/../../../{package name}`


- **Source File**: Some resources have a file that contains more data. For example, a texture resource’s source file is the image file. Or in the current example of the armor, it is a .GR2 file.

## Overriding Resources

You modify existing resources by **overriding** them. Overriding resources is the process by which an exact copy of the resource you want to override is made, including the direct files necessary to have a standalone resource.

You can override a resource in two different ways:

1. Right click on the resource in the Resource Manager, and select **Override In the Active Mod**.

[![](https://image.modcdn.io/members/63c0/31088933/profileeditor/resource12b.png)](https://image.modcdn.io/members/63c0/31088933/profileeditor/resource12b.png)

2. Click on the resource to view its properties, then click on the **Override selected objects** button.

[![](https://image.modcdn.io/members/63c0/31088933/profileeditor/resource13.png)](https://image.modcdn.io/members/63c0/31088933/profileeditor/resource13.png)


On starting the override of a resource, you will be asked to confirm that you want to override the resource:

[![](https://image.modcdn.io/members/63c0/31088933/profileeditor/resource14.png)](https://image.modcdn.io/members/63c0/31088933/profileeditor/resource14.png)

On confirming the action, it will ask you if you want to maintain the same structure of filters and packages as the resource that is being overridden, or if you want to add it to a package of your choice.

[![](https://image.modcdn.io/members/63c0/31088933/profileeditor/resource15.png)](https://image.modcdn.io/members/63c0/31088933/profileeditor/resource15.png)

**Option 1: Keep package structure.**

All the structure of the original resource will be replicated in your module.

[![](https://image.modcdn.io/members/63c0/31088933/profileeditor/resource16.png)](https://image.modcdn.io/members/63c0/31088933/profileeditor/resource16.png)

**Option 2: Select a package of your choice.**

[![](https://image.modcdn.io/members/63c0/31088933/profileeditor/resource17.png)](https://image.modcdn.io/members/63c0/31088933/profileeditor/resource17.png)

If choosing this option, you will be asked to choose a target package to add the new resource, and a name for this resource.

Completing either of these two options results in a successful overridden resource.

[G\\
\\
GrumpyWashbear](https://mod.io/g/baldursgate3/u/grumpywashbear/r)

Follow GrumpyWashbear

Log in to join the discussion!

[S](https://mod.io/g/baldursgate3/u/siftherevenant)

[SifTheRevenant](https://mod.io/g/baldursgate3/u/siftherevenant)• [1y ago](https://mod.io/g/baldursgate3/r/editor-overriding-resources#1028155 "10/8/2024, 09:48 PM GMT-4")

when I selected "Override in the Active Mod" the texture disappeared from the armor piece, and I can't figure out how to fix it. Were there other files I was supposed to override with it?

[E](https://mod.io/g/baldursgate3/u/jcobal)

[El0bal](https://mod.io/g/baldursgate3/u/jcobal)• [1y ago](https://mod.io/g/baldursgate3/r/editor-overriding-resources#1005938 "9/25/2024, 11:36 PM GMT-4")

how do I delete overriden resources, or references to them, if I don't have a use for them any longer? I even tried deleting from my mod's source folder, and they keep appearing in the manager.

[M](https://mod.io/g/baldursgate3/u/modiouserc364)

[ModioUserc364](https://mod.io/g/baldursgate3/u/modiouserc364)• [55d ago](https://mod.io/g/baldursgate3/r/editor-overriding-resources#1527752 "11/6/2025, 06:05 AM GMT-5")

Hello, I'd like to ask if you have solved this problem now? thank you

[B](https://mod.io/g/baldursgate3/u/barazwolf)

[BarazWolf](https://mod.io/g/baldursgate3/u/barazwolf)• [1y ago](https://mod.io/g/baldursgate3/r/editor-overriding-resources#976215 "9/7/2024, 10:04 PM GMT-4")

Is there a way to slightly increase the font size. It is rather tiny on my screen (which is a common 1440p) and my Windows scale is not set to small.

Last updated

1y

Reading time

5 min read

Views

10,571

Comments

4

[G\\
\\
GrumpyWashbear](https://mod.io/g/baldursgate3/u/grumpywashbear/r)

Follow GrumpyWashbear

- [Guide](https://mod.io/g/baldursgate3/r/editor-overriding-resources#guide)
- [Resource Manager](https://mod.io/g/baldursgate3/r/editor-overriding-resources#heading-1)
- [Packages List](https://mod.io/g/baldursgate3/r/editor-overriding-resources#heading-2)
- [Package Filter](https://mod.io/g/baldursgate3/r/editor-overriding-resources#heading-3)
- [Current Module Packages](https://mod.io/g/baldursgate3/r/editor-overriding-resources#heading-4)
- [Other Loaded Modules](https://mod.io/g/baldursgate3/r/editor-overriding-resources#heading-5)
- [Filters](https://mod.io/g/baldursgate3/r/editor-overriding-resources#heading-6)
- [Resources List, Previewer, and Properties](https://mod.io/g/baldursgate3/r/editor-overriding-resources#heading-7)
- [Overriding Resources](https://mod.io/g/baldursgate3/r/editor-overriding-resources#heading-8)
- [Discussion](https://mod.io/g/baldursgate3/r/editor-overriding-resources#discussion)

[Editor](https://mod.io/g/baldursgate3/r?tags=Editor) [English](https://mod.io/g/baldursgate3/r?tags=English) [Official](https://mod.io/g/baldursgate3/r?tags=Official)

Quick overview of the Resource Manager and its panels, and how to change an existing resource by overriding it.

Share

Report guide

---
# SOURCE: https://mod.io/g/baldursgate3/r/hair-and-beards-part-one
---

[Browse games](https://mod.io/g)

Browse games

[My library](https://mod.io/library)

My library

[My content](https://mod.io/content)

My content

My account

mod.io

mod.io

[All games](https://mod.io/g) [Baldur's Gate 3](https://mod.io/g/baldursgate3) [Guides](https://mod.io/g/baldursgate3/r) [Asset Creation](https://mod.io/g/baldursgate3/r?tags=Asset+Creation) Hair and Beards - Part 1: Assets

Hair and Beards - Part 1: Assets

Share

Report

Follow

This is part one of a multipart guide about Hair and Beards. In this guide, we’ll cover the basics of what you need before you get started importing, how to import, and how to connect what you’ve imported in the Toolkit for further use.

## Requirements

To make a hair work in the engine, you need three things:

- A hair mesh (in `.FBX` or `.GR2` format)

- A hair texture (MSKA, in `.DDS` format, not sRGB)

- Optionally, a scalp texture (in `.DDS` format)


Using these, we will need to create:

- A hair preset

- A hair material

- If you have a scalp texture, a scalp material


## Tall and Small Race Versions

We generally have two different versions of hairstyles: one for tall races and one for small races.

The **tall race** version of the hairstyle gets assigned to:

- Humans

- Strong Female Humans/Elves/Half-Elves/Tieflings

- Elves

- Half-Elves

- Tieflings

- Drow

- Githyanki

- Female Half-Orcs


The **small race** version gets assigned to:

- Gnomes

- Dwarves

- Halflings


The small race version exists to make sure that the hair stays proportional to the overall size of the race and doesn’t get scaled down too much. Hair assets with the `HUM`or`GTY`tag are the **tall** **race** versions, whereas hair assets with the `DWR`tag are the **small race** versions.

> **You don’t necessarily need the small race version of the hairstyle.** If you make the tall race version automatically snap, it will snap all the same to every race. This just means that on small races, the hairstyle might look a bit disproportional.

### Exceptions: **Male Half-Orcs** and **Male Strong** Tall Races

There are two exceptions to the above: **Male Half-Orcs** and the **Male Strong body shape for tall races**. Even with automatic snapping, the heads of these body shapes often have clipping issues, requiring manual hairstyle adjustments.

Adding hair for these exceptions can get tedious, so it’s recommended to first set up the main “tall race” version and check it in-game. If there are visual problems, only then address them.

## Importing the Hair Mesh

Open the **Resource Manager** (the box of crayons icon) via the toolbar.

[![](https://image.modcdn.io/members/63c0/31088933/profilehair/hair01.png)](https://image.modcdn.io/members/63c0/31088933/profilehair/hair01.png)

Navigate to your mod in the left sidebar. If you like, you can create some subfolders here and a new package to better organise your assets. For the purposes of this guide, we’ll use the existing base package. With your package selected, click on the **Add Resource** button (the box of crayons with the `+` symbol).

[![](https://image.modcdn.io/members/63c0/31088933/profilehair/hair02.png)](https://image.modcdn.io/members/63c0/31088933/profilehair/hair02.png)

In the **Add Resource Wizard**, select **Model**. Your model should already be placed in your mod’s Source Asset Data Path, and in `.GR2`  or `.FBX` format. In the Rename/Move window, double-check that the asset is going into the right package. You can also change the name of the asset here, if you like.

[![](https://image.modcdn.io/members/63c0/31088933/profilehair/hair03.png)](https://image.modcdn.io/members/63c0/31088933/profilehair/hair03.png)

Click **OK**.

If you’re importing a `.FBX`, you’ll see the **Visual Importer** window. You don’t need to change any of the settings here. Just click on **Import** at the top of the window.

[![](https://image.modcdn.io/members/63c0/31088933/profilehair/importfbx.png)](https://image.modcdn.io/members/63c0/31088933/profilehair/importfbx.png)

Once the import process is done, the model should show up in the target package of the Resource Manager as a **VisualResource**. In this example, the new `HAIR_HUM_F_Test_A` asset has appeared:

[![](https://image.modcdn.io/members/63c0/31088933/profilehair/importfbx2.png)](https://image.modcdn.io/members/63c0/31088933/profilehair/importfbx2.png)

## Importing the Texture

As before, click on the Add Resource button, and this time select **Texture.** Your MSKA texture should already be in `.dds` format.

As with the model, double-check the target package and name, then click **OK** to import the asset. You will be asked if the texture is sRGB. MSKA textures should not be sRGB.

The imported texture should appear in the Resource Manager as a **TextureResource**.

If you have a scalp material, repeat the process above to import it.

## Creating a Hair Material

To use the texture(s) you imported, you’ll need to set up a material. The easiest way to do this is by using an existing MaterialResource as your base, and then adjusting it to fit your needs.

In the Resource Manager, click on the **All** folder in the sidebar, then type “hair” into the filter bar. Right-click on the **Material** icon (the blue globe) to show only MaterialResources.

[![](https://image.modcdn.io/members/63c0/31088933/profilehair/hair04.png)](https://image.modcdn.io/members/63c0/31088933/profilehair/hair04.png)

In the resulting list, you’ll want to find a hair material that uses the `CHAR_Hair.lsf` source file. You can change everything else – it’s this source file that you really need. We’ll use `HAIR_Straight_Long_A`.

[![](https://image.modcdn.io/members/63c0/31088933/profilehair/hair05.png)](https://image.modcdn.io/members/63c0/31088933/profilehair/hair05.png)

Right-click on the chosen MaterialResource file and select “Create New From Selected…”

[![](https://image.modcdn.io/members/63c0/31088933/profilehair/hair06.png)](https://image.modcdn.io/members/63c0/31088933/profilehair/hair06.png)

You’ll see a small Select Target Package dialogue window. Double-check the target resource package – it should be located in your mod – and give the material a new name. For this example, we’ll go with `HAIR_MyNewHair`.

[![](https://image.modcdn.io/members/63c0/31088933/profilehair/hair07.png)](https://image.modcdn.io/members/63c0/31088933/profilehair/hair07.png)

Press **OK**. Navigate to that target package, and you should see your new MaterialResource there. If you don’t, you’ll need to remove the filter - clear the text from the filter bar.

[![](https://image.modcdn.io/members/63c0/31088933/profilehair/hair08.png)](https://image.modcdn.io/members/63c0/31088933/profilehair/hair08.png)

Double-click on the MaterialResource to open the Material Editor.

[![](https://image.modcdn.io/members/63c0/31088933/profilehair/hair09.png)](https://image.modcdn.io/members/63c0/31088933/profilehair/hair09.png)

Scroll down until you find the section called 01Texture Maps. Look at the **IDDepth\_Root\_Alpha\_MSKA** parameter.

[![](https://image.modcdn.io/members/63c0/31088933/profilehair/hair10.png)](https://image.modcdn.io/members/63c0/31088933/profilehair/hair10.png)

With the Material Editor still open, go to the Resource Manager and look for the MSKA texture you imported earlier. It should be a TextureResource.

> **TIP:** If you still have only MaterialResources showing, right-click again on the Material icon to show all resource types again.

With the texture selected in the Resource Manager, click on the arrow pointing left (<=) in the Material Editor beside the **IDDepth\_Root\_Alpha\_MSKA** field. It should populate that field with your imported asset.

[![](https://image.modcdn.io/members/63c0/31088933/profilehair/hair11.png)](https://image.modcdn.io/members/63c0/31088933/profilehair/hair11.png)

In the Material Editor, click **OK**.

## Creating a Material Preset

While you can create a Material Preset from scratch, it can be time-consuming. It’s usually easier to take an existing Material Preset, make a copy, and modify it to suit your needs.

### Reusing Existing Material Presets

Navigate again to the **All** folder in the Resource Manager, and filter for Material Presets.

[![](https://image.modcdn.io/members/63c0/31088933/profilehair/hair12.png)](https://image.modcdn.io/members/63c0/31088933/profilehair/hair12.png)

Choose a `HAIR_` preset to copy. We’ll go with `HAIR_HUM_M_Wavy_Long_B`. Right-click on it and select “Create New From Selected”. In the following window, confirm the target resource package and give your new preset a name.

[![](https://image.modcdn.io/members/63c0/31088933/profilehair/hair13.png)](https://image.modcdn.io/members/63c0/31088933/profilehair/hair13.png)

After pressing **OK**, navigate to where the new preset was created and double-click on the file to open the Material Preset Editor.

[![](https://image.modcdn.io/members/63c0/31088933/profilehair/hair14.png)](https://image.modcdn.io/members/63c0/31088933/profilehair/hair14.png)

You can play around with these settings if you like – just make sure to click **Save** or **OK** so you don’t lose your work.

### Creating New Material Presets

If you’re determined to start from scratch, you’ll want to create a **Material Preset** via the **Add Resource Wizard**. It creates an empty preset. Give this preset a very similar (or identical) name to your hair mesh, to avoid confusion. Click **OK**.

Double-click on the preset to edit it.

[![](https://image.modcdn.io/members/63c0/31088933/profilehair/hair15.png)](https://image.modcdn.io/members/63c0/31088933/profilehair/hair15.png)

In the Material Preset window, click on the **Add Preset** (“\+ Preset”) button, and select **Scalar**.

[![](https://image.modcdn.io/members/63c0/31088933/profilehair/hair16.png)](https://image.modcdn.io/members/63c0/31088933/profilehair/hair16.png)

This creates a default **Scalar Parameter**. Double-click on the name to rename it to the correct parameter name. These include:

- Scatter

- ColorDepthContrast

- DepthColorExponent

- DepthColorIntensity

- HairBacklit

- IDContrast

- RootTransitionMidPoint

- RootTransitionSoftness

- Roughness

- RoughnessContrast

- PixelDepthOffset

- PixelDepthOffsetRoot

- DepthTransitionMidPoint

- DepthTransitionSoftness

- ScalpDarken

- ScalpDesaturation

- DreadNoiseBaseColor

- HairFrizz

- SharedNoiseTiling

- HairSoupleness

- MaxWindMovementAmount


[![](https://image.modcdn.io/members/63c0/31088933/profilehair/hair17.png)](https://image.modcdn.io/members/63c0/31088933/profilehair/hair17.png)

It’s up to you to play around with these settings as you like.

## Adding a Scalp Material

You’re not required to have a scalp material. If you don’t, go ahead and skip this section. If you do, you should already have imported it an the earlier section.

Now, let’s create the scalp material. Just you we did for the hair material, go to the **All** folder, filter out everything but the materials, and look for a “scalp” in the filter bar. Here, you’ll want to choose a material that uses the `CHAR_Scalp.lsf`shader.

[![](https://image.modcdn.io/members/63c0/31088933/profilehair/hair18.png)](https://image.modcdn.io/members/63c0/31088933/profilehair/hair18.png)

We’ll use `HUM_F_NKD_Hair_FemStraight_Short_A_Scalp`. Right-click on the file and select “Create New From Selected”. Give your scalp material a good name and press **OK**.

[![](https://image.modcdn.io/members/63c0/31088933/profilehair/hair19.png)](https://image.modcdn.io/members/63c0/31088933/profilehair/hair19.png)

Find your new scalp material inside your mod resource package, and double-click to open it. At the bottom of the settings, find **IDDepth\_Root\_Alpha\_MSKA** and, using the same method as before, set it to your imported scalp texture.

Now, you have everything you need to start setting up the mesh.

## Assigning Materials to the Mesh

Find your hair mesh file (VisualResource) and double-click it. An **Edit Visual** window will open.

[![](https://image.modcdn.io/members/63c0/31088933/profilehair/hair20.png)](https://image.modcdn.io/members/63c0/31088933/profilehair/hair20.png)

Using the left-facing arrow (<=) like before, assign your hair material to the material(s). There might be multiple, or just one. Click **OK**.

## Quick Check

With the materials assigned to your mesh, let’s take a moment to double-check how it’s looking in the preview window. Click on the VisualResource (the mesh) – you _should_ see a mesh with the texture correctly displayed. In the case of this example:

[![](https://image.modcdn.io/members/63c0/31088933/profilehair/check01.png)](https://image.modcdn.io/members/63c0/31088933/profilehair/check01.png)

### What if I don’t see anything in the preview?

If you see nothing in the preview window when the VisualResource is selected, try selecting one of the **MaterialResources.** If the preview also shows nothing for the MaterialResource, you’ll need to resave it. In the below screenshot, the material has this problem:

[![](https://image.modcdn.io/members/63c0/31088933/profilehair/check02.png)](https://image.modcdn.io/members/63c0/31088933/profilehair/check02.png)

To fix it, right-click on the MaterialResource in question, and select **Open in editor…**

[![](https://image.modcdn.io/members/63c0/31088933/profilehair/check03.png)](https://image.modcdn.io/members/63c0/31088933/profilehair/check03.png)

This will open the Material Editor. You don’t need to do anything here – just go to File > Save to save the material again.

[![](https://image.modcdn.io/members/63c0/31088933/profilehair/check04.png)](https://image.modcdn.io/members/63c0/31088933/profilehair/check04.png)

Your preview for the MaterialResource should now show correctly.

[![](https://image.modcdn.io/members/63c0/31088933/profilehair/check05.png)](https://image.modcdn.io/members/63c0/31088933/profilehair/check05.png)

Close the Material Editor.

> **Known Issue:** Opening the Material Editor will almost always cause errors to appear, despite having made no changes.

## Continuing the Mesh Setup

Make sure your mesh (VisualResource) is selected in the Resource Manager. In the right panel, find the **Hair Length**, **Hair Preset Resource ID**, **Scalp Material ID**, and **Slot ID** settings.

[![](https://image.modcdn.io/members/63c0/31088933/profilehair/hair21.png)](https://image.modcdn.io/members/63c0/31088933/profilehair/hair21.png)

- **Hair Length** is responsible for helmet hair (see the Helmet Hair section later in this guide). Pick the length according to the length of your new hairstyle.

- **Hair Preset Resource ID** is where you assign your Material Preset resource. Clicking on the arrow will reveal a dropdown menu where you can search for this preset. Select your preset and click on **Set**.

- **Scalp Material ID** is where you assign your scalp material, if you have chosen to use one.

- **Slot ID** determines which tab the mesh appears in when using the Character Editor. Hairstyles should always be **Hair**.


Once those fields are assigned, you’re ready for the next step.

[![](https://image.modcdn.io/members/63c0/31088933/profilehair/assigned.png)](https://image.modcdn.io/members/63c0/31088933/profilehair/assigned.png)

## What Next?

Now that you have the meshes, textures, and materials set up, you can proceed the second part of this guide, [**Hair and Beards - Part 2: Character Creation**](https://mod.io/g/baldursgate3/r/hair-and-beards-part-2-character-creation), in which we will add our new hairstyle to the Character Creation options.

[G\\
\\
GrumpyWashbear](https://mod.io/g/baldursgate3/u/grumpywashbear/r)

Follow GrumpyWashbear

Log in to join the discussion!

[G](https://mod.io/g/baldursgate3/u/grumpywumpy)

[GrumpyWumpy](https://mod.io/g/baldursgate3/u/grumpywumpy)• [1y ago](https://mod.io/g/baldursgate3/r/hair-and-beards-part-one#1006734 "9/26/2024, 04:19 PM GMT-4")

When I attempt to import an fbx file from Maya. I get an error: Sequence contains more than one element. is there something I need to set here? I have 1 mesh and 4 LOD objects plus the the bones.

[G](https://mod.io/g/baldursgate3/u/grumpywumpy)

[GrumpyWumpy](https://mod.io/g/baldursgate3/u/grumpywumpy)• [1y ago](https://mod.io/g/baldursgate3/r/hair-and-beards-part-one#1006779 "9/26/2024, 04:49 PM GMT-4")

Got it sorted, it seems that my rig weights got disconnected.

[T](https://mod.io/g/baldursgate3/u/turretproblems)

[Turretproblems](https://mod.io/g/baldursgate3/u/turretproblems)• [1y ago](https://mod.io/g/baldursgate3/r/hair-and-beards-part-one#988205 "9/15/2024, 02:39 AM GMT-4")

Does not cover vertex groups/weighting
my model appears at the floor and does not move. Clearly there is a step missing that is not listed, presumably vertex weights from the looks of the older modding tools, but as someone new to BG3 modding thats not very useful...
Looking for a solution.

[C](https://mod.io/g/baldursgate3/u/cobrachai)

[CobraChai](https://mod.io/g/baldursgate3/u/cobrachai)• [1y ago](https://mod.io/g/baldursgate3/r/hair-and-beards-part-one#991580 "9/16/2024, 09:48 PM GMT-4")

if your model is on the floor then there was an issue with your GR2 file itself. you need to make sure you have assigned your hair to an armature, and then make sure you hit Control A to apply ALL transforms before exporting. the toolkit doesnt cover how to MAKE a hair mod. i think it assumes you know how to, and its just about using the toolkit to upload the mesh you created.

[T](https://mod.io/g/baldursgate3/u/twinklewan)

[Twinklewan](https://mod.io/g/baldursgate3/u/twinklewan)• [1y ago](https://mod.io/g/baldursgate3/r/hair-and-beards-part-one#1023186 "10/6/2024, 11:43 AM GMT-4")

Hi, I'm new to modding and I kinda have the same issue but the hair is at the good place, like, over the head, but it is not attached to the head so when the character moves the hair doesn't. I can "fix" this problem by selecting "Needs skeleton remap" in the right panel below "Hair Preset Resource ID" but it create a new problem, it deforms the mesh in a weird way. It seems that in this tutorial it doesn't need to be selected so I don't think it is a good solution...

I've checked multiple time the Blender file, the mesh is attached to the original armature (I just made the hair length a bit longer, didn't touched anything else from the original mesh) and I did the Ctrl A thing you talked about just in case, but it didn't change anything :/
I use already existing materials so I don't think the problem comes from anything else than the mesh.

If anyone could help me I would really appreciate ;o; In the preview window of the resource manager everything works fine but when I test it it's just not attached to the character.

1 reply

[D](https://mod.io/g/baldursgate3/u/durghan)

[Durghan](https://mod.io/g/baldursgate3/u/durghan)• [1y ago](https://mod.io/g/baldursgate3/r/hair-and-beards-part-one#974453 "9/7/2024, 12:03 AM GMT-4")

What the heck is an MSKA texture and what is the .dds format? I don't see either of those available in my image editor (I use Affinity photo).

[C](https://mod.io/g/baldursgate3/u/cobrachai)

[CobraChai](https://mod.io/g/baldursgate3/u/cobrachai)• [1y ago](https://mod.io/g/baldursgate3/r/hair-and-beards-part-one#980870 "9/10/2024, 04:57 PM GMT-4")

MSKA is a mask texture file. Mask files are used in 3d modeling to control various visual properties. transparency, color variations, areas affected by shaders etc. these files can determine things like which parts of the hair are glossier, or have transparent edges. stuff like mska files are responsible for how like if you look at hair you can see thru some hair versus just cartoony 1 dimensional hair.

DDS format is a type of picture file you can save a pic in, JPG, TIFF. PNG etc. DDS is what BG3 uses. so all skin files are DDS, all icon pics etc. when exporting the hair texture file, it must be exported in DDS format. DDS stands for DirectDraw Surface. its developed for 3d applications like vidoe games. and it stores texture data. so if you like decomposed a DDS file it could like break down the pic into like 3 or 4 different layers that all look different. like for example, maybe the second layer is just the redness in a face, maybe the first later is the pores on the skin, maybe the third layer is yellowing in the skin or scars. but as one big DDS file all the parts would come together as one pic. it also stores diff versions of a texture at many resolutions, which helps with rendering. whether or not you are looking at a hair up close or from meters away.

DDS is useful because it supports compression of a file without having quality suffer.

photostop, or GIMP (Free) is usually recommended for editing DDS and MSKA files.

[D](https://mod.io/g/baldursgate3/u/durghan)

[Durghan](https://mod.io/g/baldursgate3/u/durghan)• [1y ago](https://mod.io/g/baldursgate3/r/hair-and-beards-part-one#981010 "9/10/2024, 06:36 PM GMT-4")

Yeah, I get all that, but how do you make them? What format is an MSKA texture file? Is that some sort of sRGB or CMYK formatting? Or is it not actually a format but just a term for that sort of image, kind of like how a normal map can just be a .png file? And I'm in Photoshop right now and it doesn't have an option to save a .dds file. Do I just rename a .jpg or .png file to .dds or what? I've worked in several 3D applications including Maya, Blender, Unity, and Unreal and none of them have ever referred to these formats that I've encountered. If they have they've used different terminology.

I did try to Google things but initial results just basically gave me the info you have which is not at all helpful in actually making these files. I feel this initial page should explain, or link to explanations, of what these files are and how to make them.

2 replies

Last updated

1y

Reading time

10 min read

Views

5,376

Comments

11

[G\\
\\
GrumpyWashbear](https://mod.io/g/baldursgate3/u/grumpywashbear/r)

Follow GrumpyWashbear

- [Guide](https://mod.io/g/baldursgate3/r/hair-and-beards-part-one#guide)
- [Requirements](https://mod.io/g/baldursgate3/r/hair-and-beards-part-one#heading-1)
- [Tall and Small Race Versions](https://mod.io/g/baldursgate3/r/hair-and-beards-part-one#heading-2)
- [Exceptions:](https://mod.io/g/baldursgate3/r/hair-and-beards-part-one#heading-3)
- [Importing the Hair Mesh](https://mod.io/g/baldursgate3/r/hair-and-beards-part-one#heading-4)
- [Importing the Texture](https://mod.io/g/baldursgate3/r/hair-and-beards-part-one#heading-5)
- [Creating a Hair Material](https://mod.io/g/baldursgate3/r/hair-and-beards-part-one#heading-6)
- [Creating a Material Preset](https://mod.io/g/baldursgate3/r/hair-and-beards-part-one#heading-7)
- [Reusing Existing Material Presets](https://mod.io/g/baldursgate3/r/hair-and-beards-part-one#heading-8)
- [Creating New Material Presets](https://mod.io/g/baldursgate3/r/hair-and-beards-part-one#heading-9)
- [Adding a Scalp Material](https://mod.io/g/baldursgate3/r/hair-and-beards-part-one#heading-10)
- [Assigning Materials to the Mesh](https://mod.io/g/baldursgate3/r/hair-and-beards-part-one#heading-11)
- [Quick Check](https://mod.io/g/baldursgate3/r/hair-and-beards-part-one#heading-12)
- [What if I don’t see anything in the preview?](https://mod.io/g/baldursgate3/r/hair-and-beards-part-one#heading-13)
- [Continuing the Mesh Setup](https://mod.io/g/baldursgate3/r/hair-and-beards-part-one#heading-14)
- [What Next?](https://mod.io/g/baldursgate3/r/hair-and-beards-part-one#heading-15)
- [Discussion](https://mod.io/g/baldursgate3/r/hair-and-beards-part-one#discussion)

[Asset Creation](https://mod.io/g/baldursgate3/r?tags=Asset+Creation) [Beards](https://mod.io/g/baldursgate3/r?tags=Beards) [Character Creation](https://mod.io/g/baldursgate3/r?tags=Character+Creation) [English](https://mod.io/g/baldursgate3/r?tags=English) [Hair](https://mod.io/g/baldursgate3/r?tags=Hair) [Official](https://mod.io/g/baldursgate3/r?tags=Official)

Part 1 of the Hair and Beards guide covers Meshes, Textures, and Materials: basics on requirements, how to import these assets into the editor, and set them up for basic use.

Share

Report guide

---
# SOURCE: https://mod.io/g/baldursgate3/r/hair-and-beards-part-2-character-creation
---

[Browse games](https://mod.io/g)

Browse games

[My library](https://mod.io/library)

My library

[My content](https://mod.io/content)

My content

My account

mod.io

mod.io

[All games](https://mod.io/g) [Baldur's Gate 3](https://mod.io/g/baldursgate3) [Guides](https://mod.io/g/baldursgate3/r) [Beards](https://mod.io/g/baldursgate3/r?tags=Beards) Hair and Beards - Part 2: Character Creation

Hair and Beards - Part 2: Character Creation

Share

Report

Follow

This guide assumes you have already imported all of the necessary resources following the [**Hair and Beards - Part 1: Assets**](https://mod.io/g/baldursgate3/r/hair-and-beards-part-one) guide.

## Hairstyle Versions

Hair in Baldur’s Gate 3 gets automatically snapped to _most_ races,with the exception of **Male Half-Orcs** and the **Male Strong** **body shape for tall races**.

> A guide to setting up hair for automatic snapping is in progress.

We generally have two different versions of hairstyles: one for tall races and one for small races.

The **tall race** version of the hairstyle gets assigned to:

- Humans

- Strong Female Humans/Elves/Half-Elves/Tieflings

- Elves

- Half-Elves

- Tieflings

- Drow

- Githyanki

- Female Half-Orcs


The **small race** version gets assigned to:

- Gnomes

- Dwarves

- Halflings


The small race version exists to make sure that the hair stays proportional to the overall size of the race and doesn’t get scaled down too much. Hair assets with the `HUM`or`GTY`tag are the **tall** **race** versions, whereas hair assets with the `DWR`tag are the **small race** versions.

> **You don’t necessarily need the small race version of the hairstyle.** If you make the tall race version automatically snap, it will snap all the same to every race. This just means that on small races, the hairstyle might look a bit disproportional.

## Exceptions: **Male Half-Orcs** and **Male Strong** Tall Races

As mentioned above, there are two exceptions: **Male Half-Orcs**, who only have one body shape, and the **Male Strong body shape for tall races**. Even with automatic snapping, the heads of these body shapes often have clipping issues, requiring manual hairstyle adjustments, and therefore manual addition into a separate table.

Adding hair for these exceptions can get tedious, so it’s recommended to first go the “Shared” route (see the CharacterCreationSharedVisuals section below). Then, load Character Creation and check your hairstyle on these body shapes. If there are visual problems, only then address them.

We’ll go into further detail about how to add these exceptions later in the guide.

## CharacterCreationSharedVisuals Table

To make sure your hairstyle shows up in Character Creation, you’ll need to create and populate a CharacterCreationSharedVisuals table.

Open the **UUID Object Editor** (the spreadsheet icon) via the toolbar.

[![](https://image.modcdn.io/members/63c0/31088933/profilehair/hair22.png)](https://image.modcdn.io/members/63c0/31088933/profilehair/hair22.png)

Create a new **CharacterCreationSharedVisuals** table in your mod, under **CharacterCreation**. Once made, double-click to open it.

[![](https://image.modcdn.io/members/63c0/31088933/profilehair/hair23.png)](https://image.modcdn.io/members/63c0/31088933/profilehair/hair23.png)

> **NOTE:** You can consult the existing tables in **Shared** if you’d like to see examples of how they’ve been done.

Start by filling in the **SlotName**. This describes the type of asset you’re adding and determines where in Character Creation it will be displayed. In our case, we’ll fill in `Hair`.

As soon as you’ve filled in a field on an empty row, a UUID will automatically be generated.

For the **VisualResource**, find the UUID of your asset in the Resource Manager. Right-click on your VisualResource, and select “Copy GUID to Clipboard”.

[![](https://image.modcdn.io/members/63c0/31088933/profilehair/hair24.png)](https://image.modcdn.io/members/63c0/31088933/profilehair/hair24.png)

Paste it into the **VisualResource** field in the UUID Object Editor.

**DisplayName** is what the hair will be called in Character Creation. Creatively, we’ll call ours `New Hairstyle`.

Fill in the **Name** field with the name of your VisualResource. In our example, that’s `HAIR_HUM_F_Test_A`. Just as for the UUID (GUID), you can copy this from the asset in the Resource Manager.

The **BoneName** and **Tags** fields have no relevance to hair, so leave them blank. Your filled-in table should look something like this:

[![](https://image.modcdn.io/members/63c0/31088933/profilehair/hair25.png)](https://image.modcdn.io/members/63c0/31088933/profilehair/hair25.png)

Don’t forget to **Save**.

## Races Table

Now, we’ll need to define which races can choose the new hairstyle we added in CharacterCreationSharedVisuals. This is done via a Races table.

Create a new **Races** table in your mod, again using the UUID Object Editor. Open the empty new table.

[![](https://image.modcdn.io/members/63c0/31088933/profilehair/hair26.png)](https://image.modcdn.io/members/63c0/31088933/profilehair/hair26.png)

To add a hairstyle to an existing race, you’ll need to override the race’s existing Races entry. To make this hairstyle available for humans, also open the existing Races table under **Shared**.

[![](https://image.modcdn.io/members/63c0/31088933/profilehair/hair27.png)](https://image.modcdn.io/members/63c0/31088933/profilehair/hair27.png)

Find the row for Human, and right-click on a cell in that row. Select **Override in** \> `[[yourmodname]]`. Our example mod is called `NewHair`, so we’ll override it there.

[![](https://image.modcdn.io/members/63c0/31088933/profilehair/hair28.png)](https://image.modcdn.io/members/63c0/31088933/profilehair/hair28.png)

Once you’ve done this, you should see the new row appear in your mod’s Races table:

[![](https://image.modcdn.io/members/63c0/31088933/profilehair/hair29.png)](https://image.modcdn.io/members/63c0/31088933/profilehair/hair29.png)

> **Note:**
>
> If you leave the cells, the subrace will inherit the visuals of their race parents.
>
> If you fill in the cells, the subraces will overwrite the visuals of their race parents.

Scroll over to the **Visuals** column.

[![](https://image.modcdn.io/members/63c0/31088933/profilehair/hair30.png)](https://image.modcdn.io/members/63c0/31088933/profilehair/hair30.png)

Clicking to edit this cell will open a drop-down menu that shows two lists. The top part (red) is a list of all hairstyles and beards already added to this race in Character Creation. The bottom part (green) is a list of hairstyles and beards not currently used by this race.

[![](https://image.modcdn.io/members/63c0/31088933/profilehair/hair31.png)](https://image.modcdn.io/members/63c0/31088933/profilehair/hair31.png)

In the search field at the top of this menu, type in your new hair’s `DisplayName`. In our case, our creatively named New Hairstyle will appear in the bottom list. **Double-click** on it to add it to the list.

[![](https://image.modcdn.io/members/63c0/31088933/profilehair/hair32.png)](https://image.modcdn.io/members/63c0/31088933/profilehair/hair32.png)

Repeat this process for every race that you want the hairstyle to be available for. When you’re done, make sure to save your work.

> **Note:** Only assets from the CharacterCreationSharedVisuals need to be added to the Races table as described here. Anything defined in CharacterCreationAppearanceVisuals (detailed below) will be automatically included in Character Creation for the specified race/body shape/body type.

## Adding Male Half-Orc and Male Strong Hairstyles to Character Creation

> Technically, as is the case with **small race** hairstyle versions, you can add just one hairstyle that will be shared among – and automatically snapped across – all the races with no exceptions. However, there is a _very high chance_ that for **Male Strong** body shapes and **Male Half-Orcs**,the hairstyle will have a lot of clipping issues.

In order to add **Male Strong** (Human, Githyanki, Tiefling, Elf, Half-Elf, Drow) and **Male Half-Orc** hairstyles, you need to follow a different route. Due to high clipping potential, they don’t rely on automatic snapping, and instead have their own manually snappedversions of a given hairstyle.

Because of this, these hairstyles need to be added in a different section of the UUID tables, and they need to be added for each race and body shape separately.

Openthe UUID Object Editorand create a **CharacterCreationAppearanceVisuals** table in your mod. Open it.

Here, the most relevant columns are…

| **Column Name** | **Note** |
| --- | --- |
| UUID | The table entry’s unique identifier |
| RaceUUID | The UUID of the race you’re assigning this hairstyle (or beard) to |
| BodyType | `Male` or `Female` |
| BodyShape | `Standard` or `Strong` |
| SlotName | The type of asset you’re adding: `Hair` or `Beard` |
| VisualResource | The UUID of the relevant VisualResource |
| DisplayName | The name of the asset that will appear in Character Creation |
| Name | The filename of your VisualResource |

Go to your newly created CharacterCreationAppearanceVisuals table. Let’s say that we noticed clipping on the Male Half-Orc, so we want to define an exception.

Since we’re adding hair in this case, set the **SlotName** fields to `Hair`.

For the **VisualResource** column, go to the Resource Manager and right-click on the hair’s VisualResource to “Copy GUID to Clipboard”.Paste the copied GUID into the **VisualResource** cells.

Give the hair a **DisplayName** in each row. This should ideally be the same name across all race, body shape, and body type combinations. We will again use `New Hairstyle`.

Fill in the **Name** column with the name of the VisualResource used (in our case, `HAIR_HUM_F_Test_A`).

Most importantly, you’ll need to fill in the **RaceUUID** with the UUID of the race, from the relevant Races table.

[![](https://image.modcdn.io/members/63c0/31088933/profilehair/hair33.png)](https://image.modcdn.io/members/63c0/31088933/profilehair/hair33.png)

> For quick reference, here are the RaceUUIDs for the exception races:
>
> - **Human:** 0eb594cb-8820-4be6-a58d-8be7a1a98fba
>
> - **Githyanki:** bdf9b779-002c-4077-b377-8ea7c1faa795
>
> - **Tiefling**: b6dccbed-30f3-424b-a181-c4540cf38197
>
> - **Elf:** 6c038dcb-7eb5-431d-84f8-cecfaf1c0c5a
>
> - **Half-Elf:** 45f4ac10-3c89-4fb2-b37d-f973bb9110c0
>
> - **Drow:** 4f5d1434-5175-4fa9-b7dc-ab24fba37929
>
> - **Half-Orc:** 5c39a726-71c8-4748-ba8d-f768b3c11a91
>
>
> You can always check for the UUIDs of existing races in the Races tables inside Shared or SharedDev.

Now we have one exception assigned.

However, if the same hairstyle is in CharacterCreationAppearanceVisuals and CharacterCreationSharedVisuals for a combination of body type, body shape, and race, it’ll appear twice in the Character Creation list. This means we need to remove this hairstyle from the Half-Orc data in our Races table.

That, in turn, means that the hair will no longer be available for other Half-Orc body type and shape combinations – namely, Female Half-Orcs.

To give the Female Half-Orc this hairstyle, we’ll need to also add it to CharacterCreationAppearanceVisuals for that combination, like so:

[![](https://image.modcdn.io/members/63c0/31088933/profilehair/hair34.png)](https://image.modcdn.io/members/63c0/31088933/profilehair/hair34.png)

In short, whenever you define an exception for a specific body type and body shape combination within a race, you need to remove that asset from the CharacterCreationSharedVisuals table, and instead define it individually for each body type and body shape combination in CharacterCreationAppearanceVisuals.

Once you’ve done this, **save** the sheet.

The hairstyle should now correctly appear in Character Creation. You can confirm this by loading the `SYS_CC_I` (Character Creation) level.

## **Adding Beards to Character Creation**

The process for beards is exactly the same as for hairstyles, except that there’s no need to worry about exceptions – **beards work for everyone in the same way**.

Add your beards to your CharacterCreationSharedVisuals table, but this time only select **Beard** for the SlotName.

You will also need to add those beards to the relevant races as you did with the hairstyles, also via the **Visuals** field.

## **Summary: Adding New Hair**

If you created a hairstyle and you want it to appear correctly for every single race and gender:

- You will need the following assets:
  - a shared “tall version”

  - (optional) a shared “small version” mesh

  - (optional) a version for each Male Strong tall race

  - (optional) a version for Male Half-Orc
- Import the assets, create the materials, and set up material presets.

- If there are no exceptions for the race:
  - Add the tall version and small version to a CharacterCreationSharedVisuals table.
- If there **are** exceptions:
  - Add every single body type and body shape combination for that race individually to the CharacterCreationAppearanceVisuals table.

  - The non-exception combinations can share the same VisualResource, while the exceptions (Male Strong, for example) will have their own VisualResource. For example:

    [![](https://image.modcdn.io/members/63c0/31088933/profilehair/hair35.png)](https://image.modcdn.io/members/63c0/31088933/profilehair/hair35.png)

  - The Male Strong version uses a custom VisualResource, while the others use the same general “tall version” of that hairstyle.

## **Adding Hair Colours to Character Creation**

Hair colours are created as **MaterialPresetResources**. To make our own, we’re going to start by copying an existing asset: find `HAIR_Color_Aqua_0` in the Resource Manager in the **All** folder by searching for it and filtering for Material Presets only.

Right-click on the asset and select “Create New From Selected”. Give your new Material Preset a name. We’ll go with `HAIR_Color_NewColor` for this example.

[![](https://image.modcdn.io/members/63c0/31088933/profilehair/hair36.png)](https://image.modcdn.io/members/63c0/31088933/profilehair/hair36.png)

Find your newly created Material Preset and double-click to open it. You’ll see a variety of values:

[![](https://image.modcdn.io/members/63c0/31088933/profilehair/hair37.png)](https://image.modcdn.io/members/63c0/31088933/profilehair/hair37.png)

For a single hair colour selected by the player, there are actually a number of different settings, so different “parts” of the hair can be adjusted independently to achieve a balanced result:

- Eyebrows

- Eyelashes

- Body Hair Colour

- Hair Colour

- Hair Scalp Colour


You’ll need to create a MaterialPresetResource for each new hair colour you want to add. Once you’re done fine-tuning the colours to your liking, make sure all of your work is saved.

Then, go to the UUID Object Editorand create a new **CharacterCreationHairColors** table. Open it.

> **Note:** You can consult the existing CharacterCreationHairColors table in Shared, if you like.

In your new table, first fill in the **Name** field with the name of the MaterialPresetResource from the Resource Manager. A UUID will be automatically generated afterwards.

[![](https://image.modcdn.io/members/63c0/31088933/profilehair/hair38.png)](https://image.modcdn.io/members/63c0/31088933/profilehair/hair38.png)

The **DisplayName** is the name the colour will have in Character Creation. For tutorial purposes, we’ll call this one `New Hair Color`.

For the **MaterialPresetUUID**, get the GUID of your MaterialPresetResource (right-click on it in the Resource Manager and select “Copy GUID”) and paste it into this field.

In the **UIColor** field, select a colour to represent this new hair colour in the coloured icon in Character Creation.

Your new row of stats in the table should look something like this:

[![](https://image.modcdn.io/members/63c0/31088933/profilehair/hair39.png)](https://image.modcdn.io/members/63c0/31088933/profilehair/hair39.png)

Repeat this process as many times as needed to add all the colour presets you’ve made.

Make sure to save your work afterwards!

[G\\
\\
GrumpyWashbear](https://mod.io/g/baldursgate3/u/grumpywashbear/r)

Follow GrumpyWashbear

Log in to join the discussion!

[B](https://mod.io/g/baldursgate3/u/modiouser6254986)

[badwitch\_69](https://mod.io/g/baldursgate3/u/modiouser6254986)• [1y ago](https://mod.io/g/baldursgate3/r/hair-and-beards-part-2-character-creation#993532 "9/18/2024, 03:12 AM GMT-4")

Overwriting causes races' names and descriptions to appear in English even in different localizations. How can I fix it?

[S](https://mod.io/g/baldursgate3/u/shaneh31)

[ShaneH147](https://mod.io/g/baldursgate3/u/shaneh31)• [1y ago](https://mod.io/g/baldursgate3/r/hair-and-beards-part-2-character-creation#1010757 "9/29/2024, 02:46 AM GMT-4")

Has anyone found a solution to this beside making a localization file for each language?

[M](https://mod.io/g/baldursgate3/u/modiouser2092976)

[ModioUser2092976](https://mod.io/g/baldursgate3/u/modiouser2092976)• [1y ago](https://mod.io/g/baldursgate3/r/hair-and-beards-part-2-character-creation#981970 "9/11/2024, 11:56 AM GMT-4")

Does this tutorial account for submeshes within the GR2 (mostly hair accessories)?

[C](https://mod.io/g/baldursgate3/u/coralinekoralina)

[CoralineKoralina](https://mod.io/g/baldursgate3/u/coralinekoralina)• [1y ago](https://mod.io/g/baldursgate3/r/hair-and-beards-part-2-character-creation#975393 "9/7/2024, 02:11 PM GMT-4")

What about physics? Will there be a tutorial for describing the bones in the physics file?

Last updated

1y

Reading time

12 min read

Views

3,675

Comments

4

[G\\
\\
GrumpyWashbear](https://mod.io/g/baldursgate3/u/grumpywashbear/r)

Follow GrumpyWashbear

- [Guide](https://mod.io/g/baldursgate3/r/hair-and-beards-part-2-character-creation#guide)
- [Hairstyle Versions](https://mod.io/g/baldursgate3/r/hair-and-beards-part-2-character-creation#heading-1)
- [Exceptions:](https://mod.io/g/baldursgate3/r/hair-and-beards-part-2-character-creation#heading-2)
- [CharacterCreationSharedVisuals Table](https://mod.io/g/baldursgate3/r/hair-and-beards-part-2-character-creation#heading-3)
- [Races Table](https://mod.io/g/baldursgate3/r/hair-and-beards-part-2-character-creation#heading-4)
- [Adding Male Half-Orc and Male Strong Hairstyles to Character Creation](https://mod.io/g/baldursgate3/r/hair-and-beards-part-2-character-creation#heading-5)
- [Adding Beards to Character Creation](https://mod.io/g/baldursgate3/r/hair-and-beards-part-2-character-creation#heading-6)
- [Summary: Adding New Hair](https://mod.io/g/baldursgate3/r/hair-and-beards-part-2-character-creation#heading-7)
- [Adding Hair Colours to Character Creation](https://mod.io/g/baldursgate3/r/hair-and-beards-part-2-character-creation#heading-8)
- [Discussion](https://mod.io/g/baldursgate3/r/hair-and-beards-part-2-character-creation#discussion)

[Beards](https://mod.io/g/baldursgate3/r?tags=Beards) [Character Creation](https://mod.io/g/baldursgate3/r?tags=Character+Creation) [English](https://mod.io/g/baldursgate3/r?tags=English) [Hair](https://mod.io/g/baldursgate3/r?tags=Hair) [Official](https://mod.io/g/baldursgate3/r?tags=Official)

Part 2 of the Hair and Beards guide covers how to set up Hair (and Beards) so they show up in Character Creation, how to set shared visual resources or exceptions, and how to add new hair colours.

Share

Report guide

---
# SOURCE: https://mod.io/g/baldursgate3/r/hair-and-beards-part-3-helmet-hair
---

[Browse games](https://mod.io/g)

Browse games

[My library](https://mod.io/library)

My library

[My content](https://mod.io/content)

My content

My account

mod.io

mod.io

[All games](https://mod.io/g) [Baldur's Gate 3](https://mod.io/g/baldursgate3) [Guides](https://mod.io/g/baldursgate3/r) [Asset Creation](https://mod.io/g/baldursgate3/r?tags=Asset+Creation) Hair and Beards - Part 3: Helmet Hair

Hair and Beards - Part 3: Helmet Hair

Share

Report

Follow

## Helmet Hair System

**Helmet hair** refers to a more optimised hairstyle made specifically to fit under various pieces of headwear to give the impression that the character has a natural hairstyle underneath. It is not meant to be used on its own.

[![](https://image.modcdn.io/members/63c0/31088933/profilehair/helmet01.png)](https://image.modcdn.io/members/63c0/31088933/profilehair/helmet01.png)

There are 2 headwear types where this system is used: Type A and Type C.

[![](https://image.modcdn.io/members/63c0/31088933/profilehair/helmet02.png)](https://image.modcdn.io/members/63c0/31088933/profilehair/helmet02.png)

## Hair

Helmet hairstyles do not follow the normal hair system where they can get shared between genders/races. This is because automatically snapped hair does not always fit correctly below a manually snapped helmet.

We therefore need to manually snap each helmet hairstyle to all available races, and make sure they work with the headwear limitations. We have provided helmet hair reference meshes for male and female humans here:

> **[REF\_Helmet\_Hair.fbx](https://baldursgate3.game/mods/REF_Helmet_Hair.fbx)**

[![](https://image.modcdn.io/members/63c0/31088933/profilehair/helmet03.png)](https://image.modcdn.io/members/63c0/31088933/profilehair/helmet03.png)

Importing helmet hair follows more or less the same steps at importing a regular hairstyle. You need to make sure that the helmet hair VisualResource has a **material**, **Hair Preset Resource ID**,and **Scalp Material ID** assigned. Also remember to add `Hair` to the **Tags**, and fill in the **Hair Length** that’s closest to your hairstyle.

Hair Length has long and short variations across 5 different styles:

- Afro

- Curly

- Dreadlocks

- Straight

- Wavy


[![](https://image.modcdn.io/members/63c0/31088933/profilehair/helmet04.png)](https://image.modcdn.io/members/63c0/31088933/profilehair/helmet04.png)

Finally, set the **Slot ID** to **HelmetHair**.

## Adding Headwear

During the modelling process for helmets, the helmet hair limits need to be kept in mind.

Helmets need to be larger than the reference volume, and have a similar shape to it. Below are some examples of the different helmet types.

> **Type A**
>
> [![](https://image.modcdn.io/members/63c0/31088933/profilehair/helmet05.png)](https://image.modcdn.io/members/63c0/31088933/profilehair/helmet05.png)

> **Type B**
>
> [![](https://image.modcdn.io/members/63c0/31088933/profilehair/helmet06.png)](https://image.modcdn.io/members/63c0/31088933/profilehair/helmet06.png)

When integrating headwear into the engine, the **Slot ID** should be `Headwear`. See the [**Adding New Armour**](https://mod.io/g/baldursgate3/r/adding-an-armor) guide (“Equipment System” section) for more details on setting up the root template for your new headwear.

When editing your root template’s Equipment Data, you'll need to fill in the different hair variations (in the green box below) with the helmet hair you want to use for it. If you have Type A headwear, you should use Type A helmet hair, and if you have Type C headwear, you should use Type C helmet hair. You will need to do this for every tab (Human Male, Human Female, etc.).

> **NOTE:** If you don’t fill these in, there will be no hair shown when the headwear is worn.

[![](https://image.modcdn.io/members/63c0/31088933/profilehair/helmet07.png)](https://image.modcdn.io/members/63c0/31088933/profilehair/helmet07.png)

## Tags

There are different tags you can add to a piece of headwear or hairstyle:

[![](https://image.modcdn.io/members/63c0/31088933/profilehair/helmet08.png)](https://image.modcdn.io/members/63c0/31088933/profilehair/helmet08.png)

- **Hair** should get assigned to actual hair meshes, not headwear!

- **Never Hide Hair** is used for circlets, crowns and masks, as well as anything else that should not automatically hide the hair or use helmet hair.

- **Hide Ears** makes the ear meshes (and any earrings) invisible when the headwear is equipped.

- **Hide Beard** hides the beard when the headwear is equipped. Use this when the chin or a large area of the chin gets covered by the headwear, as with the Grymskull Helm, for example. Don’t forget to add this tag to **female races** as well, since female characters can also have beards.


> [![](https://image.modcdn.io/members/63c0/31088933/profilehair/helmet09.png)](https://image.modcdn.io/members/63c0/31088933/profilehair/helmet09.png)
>
> The type of headwear that would call for the **Hide Beard** tag.

[G\\
\\
GrumpyWashbear](https://mod.io/g/baldursgate3/u/grumpywashbear/r)

Follow GrumpyWashbear

Log in to join the discussion!

[G](https://mod.io/g/baldursgate3/u/gysselyth)

[Gysselyth](https://mod.io/g/baldursgate3/u/gysselyth)• [340d ago](https://mod.io/g/baldursgate3/r/hair-and-beards-part-3-helmet-hair#1185947 "1/25/2025, 12:55 PM GMT-5")

Where do you actually go to add tags? Click Paths for these kinds of instructions would be very helpful.

Last updated

1y

Reading time

3 min read

Views

1,577

Comments

1

[G\\
\\
GrumpyWashbear](https://mod.io/g/baldursgate3/u/grumpywashbear/r)

Follow GrumpyWashbear

- [Guide](https://mod.io/g/baldursgate3/r/hair-and-beards-part-3-helmet-hair#guide)
- [Helmet Hair System](https://mod.io/g/baldursgate3/r/hair-and-beards-part-3-helmet-hair#heading-1)
- [Hair](https://mod.io/g/baldursgate3/r/hair-and-beards-part-3-helmet-hair#heading-2)
- [Adding Headwear](https://mod.io/g/baldursgate3/r/hair-and-beards-part-3-helmet-hair#heading-3)
- [Tags](https://mod.io/g/baldursgate3/r/hair-and-beards-part-3-helmet-hair#heading-4)
- [Discussion](https://mod.io/g/baldursgate3/r/hair-and-beards-part-3-helmet-hair#discussion)

[Asset Creation](https://mod.io/g/baldursgate3/r?tags=Asset+Creation) [Character Creation](https://mod.io/g/baldursgate3/r?tags=Character+Creation) [English](https://mod.io/g/baldursgate3/r?tags=English) [Hair](https://mod.io/g/baldursgate3/r?tags=Hair) [Headwear](https://mod.io/g/baldursgate3/r?tags=Headwear) [Official](https://mod.io/g/baldursgate3/r?tags=Official)

Part 3 of the Hair and Beards guide cover helmet hair: how to create it, where it's used, and how to set it up for new hairstyles you may have added in previous parts. It also covers some basics on asset creation for Headwear.

Share

Report guide

---
# SOURCE: https://mod.io/g/baldursgate3/r/vfx-part-1-making-the-effect
---

[Browse games](https://mod.io/g)

Browse games

[My library](https://mod.io/library)

My library

[My content](https://mod.io/content)

My content

My account

mod.io

mod.io

[All games](https://mod.io/g) [Baldur's Gate 3](https://mod.io/g/baldursgate3) [Guides](https://mod.io/g/baldursgate3/r) [English](https://mod.io/g/baldursgate3/r?tags=English) VFX - Part 1: Making the Effect

VFX - Part 1: Making the Effect

Share

Report

Follow

The Baldur's Gate 3 Toolkit contains the effect tools. Simply launch the Toolkit, load your mod project or create a new one, and wait for it to load.

> For more information on how to create and set up a project, please refer to [https://mod.io/g/baldursgate3/r/getting-started-creating-a-new-mod](https://larianstudios.atlassian.net/wiki/spaces/GUS/pages/3552575615).

For this tutorial, we will use an existing level named WLD\_Campfire\_E. You can find it in the Act\_1A\_WLD folder.

[![](https://image.modcdn.io/members/63c0/31088933/profilevfx/1_01.png)](https://image.modcdn.io/members/63c0/31088933/profilevfx/1_01.png)

From there, you will have the full editor open and will be able to follow this tutorial nicely.

## Effect Editor

Launch the Effect Editor (also called AllSpark) from the toolbar.

[![](https://image.modcdn.io/members/63c0/31088933/profilevfx/1_02.png)](https://image.modcdn.io/members/63c0/31088933/profilevfx/1_02.png)

### Interface

The default UI layout of the Effect Editor is outdated. The **Modules** and **Components** panels are no longer necessary, so you can close them.

You're free to customise and then save the layout to your liking using the **Save Layout** button via the main Editor’s **Options** menu.

When ready, press the **File** menu button in the Effect Editor and select **New**. A new window should open with your Untitled Effect. You should have something that looks like the image below. Let's use it for a quick tour.

[![](https://image.modcdn.io/members/63c0/31088933/profilevfx/1_03.png)](https://image.modcdn.io/members/63c0/31088933/profilevfx/1_03.png)

### Effect Preview Panel

On the top-left is the **Effect Preview Panel**. You will notice it has a few buttons on top for playback and visualisation. Most of them are labelled with mouse-over tooltips.

You can navigate in the preview with:

- Left mouse button to rotate around the centre of the panel

- Right mouse button to zoom

- Middle mouse button to pan


### Effects Panel

On the bottom-left, just under the **Effect Preview Panel**, is a file browser panel called **Effects**. You can quickly and easily open any effect file that you have on your disk from here. You can also easily copy its name with a right-click, which will be useful at a later stage.

> Only the Effects folders within the project are visible here. Their extension (`.lsefx` \- Larian Studios Editor FX) indicates that they are the "Editor" files, meaning they're uncompiled source files only used by the Editor. You can think of them as what Photoshop files would be for a texture.

### Work Panel

On the right part of the screen, where your new Untitled Effect has appeared in a tab, is the **Work Panel** with the currently open effects.

At the top is the timeline, where phases are defined and effect components are placed on tracks. Effect components are the building blocks of the effect (particle systems, models, forces, etc.).

At the bottom is the module stack for the selected component. Modules are the editable properties of a component.

## Setting Up the Effect

We're not going to delve into all the details of making an effect, just the first steps to get you set up and ready to go.

> TIP: Everything that you make (phases, component, group track, tracks, etc) can be deleted simply by **selecting it** and pressing the **Delete button of your keyboard**.

### Bounding Sphere or Box

Before doing anything else, let's add a **Bounding Sphere**.

To do so, right-click on the first empty track (beneath “Phases”) and select the **BoundingSphere** component.

[![](https://image.modcdn.io/members/63c0/31088933/profilevfx/1_04.png)](https://image.modcdn.io/members/63c0/31088933/profilevfx/1_04.png)

(All components are accessible via this right-click menu, which is why the Components window, which we closed earlier, is deprecated.)

> WARNING: All effects need a **Bounding Sphere or Box** that lasts as long as the effect. An effect without a **Bounding Sphere or Box** will trigger an error.

When an effect is outside the camera frustum, it is culled. Without a bounding sphere, it would disappear as soon as its centre is off-camera. The **Radius** of your **Bounding Sphere** or the **Size** of your **Bounding Box** can be adjusted to control the culling.

[![](https://image.modcdn.io/members/63c0/31088933/profilevfx/1_05.png)](https://image.modcdn.io/members/63c0/31088933/profilevfx/1_05.png)

### Adding Reference Models

Next, let’s add a character as a reference and a floor for better readability.

Create two **Model** components and drop them on each of the next two tracks.

Assign a model by selecting the Model component and clicking the arrow in the **Mesh GUID** field.

Characters are made of multiple separate parts that wouldn’t work in the Effect Editor, so instead we use "proxy models", which are collapsed, untextured versions of any race/gender for preview purposes. Since we want it to be a character, type "proxy" in the search filter.

Select the first Model track and assign the mesh `Proxy_HUM_M_Fullbody`. Select the second Model track to assign the `VFX_Static_Reference_20x20_Floor_01_Sand_01`mesh for the floor _._

[![](https://image.modcdn.io/members/63c0/31088933/profilevfx/1_06.png)](https://image.modcdn.io/members/63c0/31088933/profilevfx/1_06.png)

> Models and particles will only appear when the effect is running – it’s considered running when you press the **Play** button or have it paused.

Set their visibility like the picture below by clicking the little icons on the right of the track names. The first icon will "mute" the tracks, meaning they will not be exported when the effect is compiled. The second icon will force them to be visible in the preview when clicked twice.

[![](https://image.modcdn.io/members/63c0/31088933/profilevfx/1_07.png)](https://image.modcdn.io/members/63c0/31088933/profilevfx/1_07.png)

For this example, we will name the component with the character mesh `Character` by selecting it and typing it in the **Name** fieldin the Required module. We will do the same for the floor and name it `Floor`.

You can adjust the **Start/End Time** by typing it manually into the field or by dragging the module or its edges on the track.

You might want to have a preview of the character’s animation while working on your effect. There are two ways to play an animation of the model:

1. Load an animation resource directly in the Animation Resource field. The below screenshot shows where to assign an animation resource to the model.



[![](https://image.modcdn.io/members/63c0/31088933/profilevfx/1_08.png)](https://image.modcdn.io/members/63c0/31088933/profilevfx/1_08.png)
2. Load the animation by selecting an animation short name via the **Animation** field. This has the advantage of not relying on the character model’s race and gender as much, but it is more difficult to debug if the animation doesn’t play. The Animation subset is used when a singular animation short name uses different animations depending on weapons or classes.



The screenshot below shows where to assign an animation short name to the model.



[![](https://image.modcdn.io/members/63c0/31088933/profilevfx/1_09.png)](https://image.modcdn.io/members/63c0/31088933/profilevfx/1_09.png)


### Adding Phases

For this example, we’re making a Prepare effect, which is a looping effect. We therefore need phases.

Right-click in the Phases bar above the track list and add all three of these phases sequentially: **Lead In**, **Loop**, **Lead Out**. The end time of each phase can be adjusted in the boxes seen in the image below.

[![](https://image.modcdn.io/members/63c0/31088933/profilevfx/1_10.png)](https://image.modcdn.io/members/63c0/31088933/profilevfx/1_10.png)

> Effects that don’t loop (e.g. cast, impact) don’t require phases.
>
> In general, prepare, projectile, (some) beams and looping status effects are the ones that require all these phases.

Double-clicking on the time bar above the Phases will automatically adjust it to the duration of the components or phases contained in the effect, scrolling the mouse wheel up and down will zoom in and out of the timeline, and holding the middle mouse button and moving left and right will allow you to shift the timeline left and right.

The **Lead-In Phase** is the build-up phase where the elements are starting to appear. Its duration depends on what you’re trying to achieve, but we generally keep it quite short and punchy – no longer than the animation, in any case. Let’s set it to `0.50` seconds by filling this into the box, as shown previously.

The **Loop Phase** is usually kept very short so it can be interrupted at any point. Let’s type `0.60` in the box so that the duration of the loop becomes 0.10.

The **Lead-Out Phase** is the end of the effect. It should allow enough time for all the active particles to die and the other components, such as models or billboards, to disappear elegantly. It is also very important when a sound is used in an effect not to abruptly cut it short. It’s good practice to make the lead-out a few seconds long to let the particles end their life before the end of the phase. Let’s set it to `2` so that it's 1.90 seconds long.

After setting the phases, it should look something like this:

[![](https://image.modcdn.io/members/63c0/31088933/profilevfx/1-11.png)](https://image.modcdn.io/members/63c0/31088933/profilevfx/1-11.png)

You will see that your tracks are now shorter than your phase. Adjust their length by changing each one’s Start/End Time to `0` and `2`, respectively. Your effect should now be set to start and look as follows when you press **Play**:

[![](https://image.modcdn.io/members/63c0/31088933/profilevfx/1_12.png)](https://image.modcdn.io/members/63c0/31088933/profilevfx/1_12.png)

> There is currently no limitation to the number of Lead Ins, Loops, or Lead Outs you can add, but you don’t need more than one of each.

### Creating a Particule System

For the purposes of this tutorial, since we want to see the effect visually in the next steps, we will create a simple basic effect.

As a first step, we will create a new track group. Press the **Create new track group** button under the **Stop** button. It should create a new track group.

[![](https://image.modcdn.io/members/63c0/31088933/profilevfx/1_13.png)](https://image.modcdn.io/members/63c0/31088933/profilevfx/1_13.png)

From this new track group, right-click the first track and select **ParticleSystem**.

[![](https://image.modcdn.io/members/63c0/31088933/profilevfx/1_14.png)](https://image.modcdn.io/members/63c0/31088933/profilevfx/1_14.png)

Move your new Particle System to the left so that the system appears from the beginning of the **Lead-In Phase**.

We will leave all of the behaviour of this Particle System set to default, but we will assign a material to the particles – so that they aren’t just squares with a default texture – and scale them. To do so, click on the small arrow in the **Material GUID** parameter, find the material with the name `VFX_ParticleSystem_AlphaBlend_Unlit_Emissive_TwoSided_Glow_Circle_01`, and double-click on the file.

[![](https://image.modcdn.io/members/63c0/31088933/profilevfx/1_15.png)](https://image.modcdn.io/members/63c0/31088933/profilevfx/1_15.png)

We will scale the particles down a bit so that they aren’t too big. Select your Particle System, and under **Required**, right-click in the window and select the **Scale** → **Scale** module. This will add parameters to scale your particles.

[![](https://image.modcdn.io/members/63c0/31088933/profilevfx/1_16.png)](https://image.modcdn.io/members/63c0/31088933/profilevfx/1_16.png)

In the **Scale** module, locate the **Uniform Scale** parameter and select the **Min Scale**. Change the value from `1` to `0.5` for both the first and second point on the curve.

[![](https://image.modcdn.io/members/63c0/31088933/profilevfx/1_17.png)](https://image.modcdn.io/members/63c0/31088933/profilevfx/1_17.png)

Finally, now that we see that our **Bounding Sphere** is too small, we will adjust it to fit the effect correctly. Repeat the step for the **Bounding Sphere** from earlier and set the radius to 3 so that all the particles die inside the **Bounding Sphere**.

If you followed all of the above steps correctly, your effect should look like this:

[![](https://image.modcdn.io/members/63c0/31088933/profilevfx/1_18.png)](https://image.modcdn.io/members/63c0/31088933/profilevfx/1_18.png)

### Experimenting

That’s pretty much it for the initial setup! From there on, you’re ready to make the effect per se.

Add tracks and track groups, experiment with components and modules, and see the result in the preview window by clicking on the big **Play** button (or the small one in the **Effect Preview Panel** – they do the same thing).

Some quick tips:

- Don’t forget bounding spheres – every effect needs one.

- Force affects all the emitters in the same track group.

- The minimum duration for any phase or component is 0.10 seconds.


## Creating the Files

### Saving and Naming the Effect

Click **File > Save as…** or press **Ctrl+Shift+S** to save the effect.

[![](https://image.modcdn.io/members/63c0/31088933/profilevfx/1_19.png)](https://image.modcdn.io/members/63c0/31088933/profilevfx/1_19.png)

The root folder where the effect should be saved is: `\Data\Editor\Mods\[YourMod]\Assets\Effects\`

However, it is advised to create clearly named subfolders to keep your work organised. For this tutorial, we would create the following folder structure: `\Data\Editor\Mods\[YourMod]\Assets\Effects\Spells\Prepare\Paladin`

Name your effect `VFX_Prepare_Paladin_Test_01` and click the **Save** button.

[![](https://image.modcdn.io/members/63c0/31088933/profilevfx/1_20.png)](https://image.modcdn.io/members/63c0/31088933/profilevfx/1_20.png)

> For Baldur’s Gate 3, we typically included information about how the effect is intended to be used in the name where possible, to make it easier to manage during implementation (bone name and textkey). For more examples of naming conventions, simply look in the **Shared** folder.

### Compiling the Effect

As mentioned before, `.lsefx` files are just Editor files; they are not used by the game/engine. For them to be usable by the game, they must be compiled to `.lsfx` files.

To do so, click **Build > Compile Effect** from the menu bar in the Effect Editor while you have your effect open and selected.

[![](https://image.modcdn.io/members/63c0/31088933/profilevfx/1_21.png)](https://image.modcdn.io/members/63c0/31088933/profilevfx/1_21.png)

This will create a compiled version of the effect in a location outside of the Editor folders. It will follow a folder structure similar to the one used for the Editor files. A message will appear in the **Message Log** panel to let you know that the action was successful.

[![](https://image.modcdn.io/members/63c0/31088933/profilevfx/1_22.png)](https://image.modcdn.io/members/63c0/31088933/profilevfx/1_22.png)

This means that the subfolders you might have previously created will also be created there under the **Effects\_Banks** root folder:

`\Data\Public\[YourMod]\Assets\Effects\Effects_Banks\`

> This behaviour is hardcoded and cannot be changed.
>
> If you haven’t saved your effect before attempting to compile, you will get an error in the Message Log (outside AllSpark, in the main Editor window) and nothing else will happen.

## Conclusion of Part 1

You have created your very first effect! The process will be very similar for all of your effects.

You are now ready to move on to [Part 2](https://mod.io/g/baldursgate3/r/vfx-part-2-creating-a-resource) of this tutorial, where will explore the creation of resources so you can link the newly made effect.

[G\\
\\
GrumpyWashbear](https://mod.io/g/baldursgate3/u/grumpywashbear/r)

Follow GrumpyWashbear

Log in to join the discussion!

[E](https://mod.io/g/baldursgate3/u/ed1241)

[EdHR](https://mod.io/g/baldursgate3/u/ed1241)• [362d ago](https://mod.io/g/baldursgate3/r/vfx-part-1-making-the-effect#1151003 "1/3/2025, 02:48 AM GMT-5")

Nice guide, I was messing around with the toolkit and wanted to make a rotating effect around the character's feet, kind of like the Fireshield status effect but instead with a spiky rotating effect, i was trying to do it with a single scaled particle and a cone emitter but didn't find the settings to fix the particle to a single spot and couldn't make it to rotate. Any ideas on how to accomplish that would be appreciated.

[T](https://mod.io/g/baldursgate3/u/lightkeeper3)

[TheLightKeeper](https://mod.io/g/baldursgate3/u/lightkeeper3)• [1y ago](https://mod.io/g/baldursgate3/r/vfx-part-1-making-the-effect#1125003 "12/14/2024, 06:51 PM GMT-5")

Thanks for the guide! How do we add keyframes to a track? I'm trying to make an effect that grows when applied, then shrinks and disappears on ending, and my uniform scale track only has two keyframes (start and end)

[E](https://mod.io/g/baldursgate3/u/ed1241)

[EdHR](https://mod.io/g/baldursgate3/u/ed1241)• [356d ago](https://mod.io/g/baldursgate3/r/vfx-part-1-making-the-effect#1160063 "1/8/2025, 09:16 PM GMT-5")

Double-click (left-click) the uniform scale graph and it will place a new node, you can do that several times. There's also a few buttons in the top part of the same graph to change the curve type.

Last updated

1y

Reading time

12 min read

Views

6,131

Comments

3

[G\\
\\
GrumpyWashbear](https://mod.io/g/baldursgate3/u/grumpywashbear/r)

Follow GrumpyWashbear

- [Guide](https://mod.io/g/baldursgate3/r/vfx-part-1-making-the-effect#guide)
- [Effect Editor](https://mod.io/g/baldursgate3/r/vfx-part-1-making-the-effect#heading-1)
- [Interface](https://mod.io/g/baldursgate3/r/vfx-part-1-making-the-effect#heading-2)
- [Effect Preview Panel](https://mod.io/g/baldursgate3/r/vfx-part-1-making-the-effect#heading-3)
- [Effects Panel](https://mod.io/g/baldursgate3/r/vfx-part-1-making-the-effect#heading-4)
- [Work Panel](https://mod.io/g/baldursgate3/r/vfx-part-1-making-the-effect#heading-5)
- [Setting Up the Effect](https://mod.io/g/baldursgate3/r/vfx-part-1-making-the-effect#heading-6)
- [Bounding Sphere or Box](https://mod.io/g/baldursgate3/r/vfx-part-1-making-the-effect#heading-7)
- [Adding Reference Models](https://mod.io/g/baldursgate3/r/vfx-part-1-making-the-effect#heading-8)
- [Adding Phases](https://mod.io/g/baldursgate3/r/vfx-part-1-making-the-effect#heading-9)
- [Creating a Particule System](https://mod.io/g/baldursgate3/r/vfx-part-1-making-the-effect#heading-10)
- [Experimenting](https://mod.io/g/baldursgate3/r/vfx-part-1-making-the-effect#heading-11)
- [Creating the Files](https://mod.io/g/baldursgate3/r/vfx-part-1-making-the-effect#heading-12)
- [Saving and Naming the Effect](https://mod.io/g/baldursgate3/r/vfx-part-1-making-the-effect#heading-13)
- [Compiling the Effect](https://mod.io/g/baldursgate3/r/vfx-part-1-making-the-effect#heading-14)
- [Conclusion of Part 1](https://mod.io/g/baldursgate3/r/vfx-part-1-making-the-effect#heading-15)
- [Discussion](https://mod.io/g/baldursgate3/r/vfx-part-1-making-the-effect#discussion)

[English](https://mod.io/g/baldursgate3/r?tags=English) [Official](https://mod.io/g/baldursgate3/r?tags=Official) [VFX](https://mod.io/g/baldursgate3/r?tags=VFX)

Part 1 of the VFX editor (AllSpark) tutorial. In this part, we'll make a very basic effect, save it, and compile it for use in the engine.

Share

Report guide

---
# SOURCE: https://mod.io/g/baldursgate3/r/vfx-part-2-creating-a-resource
---

[Browse games](https://mod.io/g)

Browse games

[My library](https://mod.io/library)

My library

[My content](https://mod.io/content)

My content

My account

mod.io

mod.io

[All games](https://mod.io/g) [Baldur's Gate 3](https://mod.io/g/baldursgate3) [Guides](https://mod.io/g/baldursgate3/r) [English](https://mod.io/g/baldursgate3/r?tags=English) VFX - Part 2: Creating a Resource

VFX - Part 2: Creating a Resource

Share

Report

Follow

In most cases, for an effect to be usable in the game, you need to create a resource pointing to the compiled file of your effect. This part of the tutorial will explain how to do so using the effect created in [Part 1](https://mod.io/g/baldursgate3/r/vfx-part-1-making-the-effect) of this guide.

## Resource Manager

In the main Editor, locate and/or open the **Resource Manager** by clicking the crayon box icon in the toolbar.

[![](https://image.modcdn.io/members/63c0/31088933/profilevfx/2_01.png)](https://image.modcdn.io/members/63c0/31088933/profilevfx/2_01.png)

> Your **Resource Manager** and your **local folder** aren’t related. You could be in the Editor making a different structure to what you are doing in your local folder.

### Creating a Structure

Navigate to the folder of your mod where you want your resource to reside. You will find your own mod at the bottom of the list of folders in the **Resource Manager**. In this tutorial, our mod is called `Test_Documentation`, so the folder that was created by default has the same name and is where our files will be placed.

You might want to create new folders and packages following the desired structure in your own mod. For this, select the main folder of your mod and press the **Create a folder** button (the folder icon with a `+`) on the top-left of the folders panel. You can give it the name you desire, but for the purpose of this tutorial, we will follow the same structure as the main project – the one in the Shared folder – and call this new folder `Assets`.

[![](https://image.modcdn.io/members/63c0/31088933/profilevfx/2_02.png)](https://image.modcdn.io/members/63c0/31088933/profilevfx/2_02.png)

From there, we will create a folder called `Effects` inside the Assets folder. This will be the main VFX-related folder for the effects, the material resource, and more. Continue to add folder pathing as follows: Assets > Effects > Effects > Spells > Prepare > Arcane.

[![](https://image.modcdn.io/members/63c0/31088933/profilevfx/2_03.png)](https://image.modcdn.io/members/63c0/31088933/profilevfx/2_03.png)

Folders can’t contain directly resources. For this, we need to create **Packages**. Select the Arcane folder, create a new package with the 3rd button from the top-left, and name it `Paladin`.

[![](https://image.modcdn.io/members/63c0/31088933/profilevfx/2_04.png)](https://image.modcdn.io/members/63c0/31088933/profilevfx/2_04.png)

Your structure should now look like this:

[![](https://image.modcdn.io/members/63c0/31088933/profilevfx/2_05.png)](https://image.modcdn.io/members/63c0/31088933/profilevfx/2_05.png)

We can now move on to creating the resource.

> Packages that stay empty will disappear the next time you boot the Editor.
>
> Folder and package names aren’t limited to being used only once. You could have multiple Paladin packages, for example.

### Creating Resources

Select the new **Paladin** package created using the steps above and press the **Add Resource** button. A new window will open. There, select the resource type **Effect**.

[![](https://image.modcdn.io/members/63c0/31088933/profilevfx/2_06.png)](https://image.modcdn.io/members/63c0/31088933/profilevfx/2_06.png)

Effect resources are made from a compiled version of the effects. By default, the Editor will open right before the **Effects\_Banks** folder where you will find the effects you compiled.

> The path of your compiled effect should look something like: `\Data\Public\[YourMod]\Assets\Effects\Effects_Banks\`

Navigate through the folder and locate the effect VFX\_Prepare\_Paladin\_Test\_01 created in [Part 1](https://mod.io/g/baldursgate3/r/vfx-part-1-making-the-effect). Select it and press **Open**.

[![](https://image.modcdn.io/members/63c0/31088933/profilevfx/2_07.png)](https://image.modcdn.io/members/63c0/31088933/profilevfx/2_07.png)

A new window named **Rename/Move** will then open. Since we selected the package **Paladin** before clicking on the **Add Resource** button, the **Project**(which means your mod) and **Package** should be correspond correctly. If they do not, manually select them. The name of the resource will be, by default, the same as the name of your effect. The name of your resource should always correspond to the name of your effect file. It is better not to change it.

[![](https://image.modcdn.io/members/63c0/31088933/profilevfx/2_08.png)](https://image.modcdn.io/members/63c0/31088933/profilevfx/2_08.png)

> Unlike other types of assets, you can’t have two or more VFX resources pointing at the same source file. This will trigger an error. If you desire the same effect two times, it is better to create a new effect and save it under another name.
>
> The name of your resource should always correspond to the name of your effect file. The former is dependent on the latter. If it is changed and used, you might see an error saying that it can’t find the effect.

If you followed all of the above steps, you should have a new Effect Resource in the Paladin package of your `VFX_Prepare_Paladin_Test_01` effect. It should look like this:

[![](https://image.modcdn.io/members/63c0/31088933/profilevfx/2_09.png)](https://image.modcdn.io/members/63c0/31088933/profilevfx/2_09.png)

## Conclusion of Part 2

The resource has now been created, and the effect is ready for use. In Part 3 of this tutorial, we will see how to assign an effect to a new spell.

[G\\
\\
GrumpyWashbear](https://mod.io/g/baldursgate3/u/grumpywashbear/r)

Follow GrumpyWashbear

Log in to join the discussion!

[R](https://mod.io/g/baldursgate3/u/rswllthtndswll)

[rswllthtndswll](https://mod.io/g/baldursgate3/u/rswllthtndswll)• [1y ago](https://mod.io/g/baldursgate3/r/vfx-part-2-creating-a-resource#977777 "9/8/2024, 05:03 PM GMT-4")

What kind of audio file do I need my custom media to be in to use with bg3? I'm looking at sound effects inside the toolkit but the media player just wont trigger the audio in editor mode. What about for adding custom character voices?

[W](https://mod.io/g/baldursgate3/u/worldwalker42)

[WorldWalker42](https://mod.io/g/baldursgate3/u/worldwalker42)• [1y ago](https://mod.io/g/baldursgate3/r/vfx-part-2-creating-a-resource#979034 "9/9/2024, 11:57 AM GMT-4")

I found the sound effects in the Resource Manager and all of them are listed as .bnk files. It looks like this is an archive format (like ZIP) called Wwise soundbanks. Each soundbank has the potential to contain (or just reference?) a lot of audio files, and it might also store other kinds of information about them (for example, the toolkit threw an error that the .txt description file was missing when I tried to import a single file).

There might be some tools to make this easier, but for right now the only option I see to create soundbanks is the official Audiokinetic Wwise software. It has a free trial and you can get a free license for non-commercial / indie projects, but you do have to sign up for it and it's a pretty complicated program. If I can make it work, I'll try to write up the steps.

[R](https://mod.io/g/baldursgate3/u/rswllthtndswll)

[rswllthtndswll](https://mod.io/g/baldursgate3/u/rswllthtndswll)• [1y ago](https://mod.io/g/baldursgate3/r/vfx-part-2-creating-a-resource#982187 "9/11/2024, 02:56 PM GMT-4")

Thank you so much for replying! This is my first bg3 mod (and first 3d game lol) and I want to rerecord a side character's lines to dip my toes in before trying to make a completely new interactable npc. I'm having a great time learning here but are there any other resources you can think of that can help me move forward on this project?

3 replies

Last updated

1y

Reading time

4 min read

Views

4,975

Comments

6

[G\\
\\
GrumpyWashbear](https://mod.io/g/baldursgate3/u/grumpywashbear/r)

Follow GrumpyWashbear

- [Guide](https://mod.io/g/baldursgate3/r/vfx-part-2-creating-a-resource#guide)
- [Resource Manager](https://mod.io/g/baldursgate3/r/vfx-part-2-creating-a-resource#heading-1)
- [Creating a Structure](https://mod.io/g/baldursgate3/r/vfx-part-2-creating-a-resource#heading-2)
- [Creating Resources](https://mod.io/g/baldursgate3/r/vfx-part-2-creating-a-resource#heading-3)
- [Conclusion of Part 2](https://mod.io/g/baldursgate3/r/vfx-part-2-creating-a-resource#heading-4)
- [Discussion](https://mod.io/g/baldursgate3/r/vfx-part-2-creating-a-resource#discussion)

[English](https://mod.io/g/baldursgate3/r?tags=English) [Official](https://mod.io/g/baldursgate3/r?tags=Official) [VFX](https://mod.io/g/baldursgate3/r?tags=VFX)

Part 2 of the VFX tutorial. In this part, we'll create a folder structure, and import the effect we created in part 1.

Share

Report guide

---
# SOURCE: https://mod.io/g/baldursgate3/r/vfx-part-3-assigning-and-testing-the-effect
---

[Browse games](https://mod.io/g)

Browse games

[My library](https://mod.io/library)

My library

[My content](https://mod.io/content)

My content

My account

mod.io

mod.io

[All games](https://mod.io/g) [Baldur's Gate 3](https://mod.io/g/baldursgate3) [Guides](https://mod.io/g/baldursgate3/r) [English](https://mod.io/g/baldursgate3/r?tags=English) VFX - Part 3: Assigning and Testing the Effect

VFX - Part 3: Assigning and Testing the Effect

Share

Report

Follow

There are multiple ways to assign an effect, depending on the desired results. Following [Part 2](https://mod.io/g/baldursgate3/r/vfx-part-2-creating-a-resource) of this tutorial, we will assign our newly made effect to a new Target spell to demonstrate the process.

## Creating a New Target Spell

Assigning an effect to a spell is done in two steps:

1. Creating a **MultiEffectInfo** **(MEI)** file, which is essentially a collection of effects to be used in a specific phase of said spell or status, containing information about the bones they’re attached to, the textkey events that trigger them, and the conditions they need to satisfy to be displayed (tags).

2. Assigning the **MEI** to the spell in the **Stats Editor**.


### Creating a MultiEffectInfo

To open the **MEI Editor**, click on the button in the toolbar of the main Editor.

[![](https://image.modcdn.io/members/63c0/31088933/profilevfx/3_01.png)](https://image.modcdn.io/members/63c0/31088933/profilevfx/3_01.png)

> The **MEI Editor** can be very slow. When you select an effect in the central panel, make sure that the panel has had time to update to your choice before editing it, otherwise you might cause unwanted changes on your previous selection. The update can take upwards of 10 seconds.

Before you create new MEIs, you might want to create your own file structure in your mod. First, you will need to select your mod folder. By default, it should already be created and visible when you open the **MEI Editor**. In our case, our mod/project is called Test\_Documentation.

[![](https://image.modcdn.io/members/63c0/31088933/profilevfx/3_02.png)](https://image.modcdn.io/members/63c0/31088933/profilevfx/3_02.png)

When it has been selected, press the **Create New Group** icon (the folder with a `+` symbol on it) and name it `Spelldata_Target`.

[![](https://image.modcdn.io/members/63c0/31088933/profilevfx/3_03.png)](https://image.modcdn.io/members/63c0/31088933/profilevfx/3_03.png)

You will then be able to create a new MEI by clicking the **Create New File** icon (the big + symbol) and name it `Test_Paladin`.

[![](https://image.modcdn.io/members/63c0/31088933/profilevfx/3_04.png)](https://image.modcdn.io/members/63c0/31088933/profilevfx/3_04.png)

Here is an overview of the **MEI Editor** window:

- The left panel is the list of MEIs.

- The central panel is the list of effect resources used in the selected MEI.

- The rightmost panel contains the properties or conditions attached to the selected effect. Each of them should have a description in a tooltip when you hover over them.


You can now assign your effect to the new MEI. To do so, select the MEI **Test\_Paladin**. In the central panel, press the **Add New Item** (the `+` symbol) button to add a new **Empty** item. Select this new item and, in the **Visual** section that will appear in the far right panel, look for the **Resource ID** parameter and press the little down arrow to search for `VFX_Prepare_Paladin_Test_01`. Select the effect resource name and set it.

[![](https://image.modcdn.io/members/63c0/31088933/profilevfx/3_05.png)](https://image.modcdn.io/members/63c0/31088933/profilevfx/3_05.png)

We want the effect to play at the Root of the character. To do this, we need to fill in the **TargetBones** parameter in the **Transform** section with the name of the bone we want the effect to play on. Press the ellipsis button on the right of the TargetBones parameter. It will open a window. From the dropdown list, select the **Dummy\_Root** bone and press **Add**. It will add it to the list of bones that the effect will attach to. (It can be multiple bones.) When it’s done, press the **OK** button and it will update the **TargetBones** parameter.

> **TIP:** You can also type the bone if the one you need doesn’t appear in the dropdown list.

[![](https://image.modcdn.io/members/63c0/31088933/profilevfx/3_06.png)](https://image.modcdn.io/members/63c0/31088933/profilevfx/3_06.png)

> **NOTE:** The **TargetBones** parameter is used in most cases. Prepare, Cast and Status effects all predominantly use the TargetBones parameter. In some cases, like for a beam effect done via the MEI Editor, you might want to specify both the **SourceBones** and the **TargetBones** parameters.

Don’t forget to save your MEI when you’re done with it (top left buttons).

[![](https://image.modcdn.io/members/63c0/31088933/profilevfx/3_07.png)](https://image.modcdn.io/members/63c0/31088933/profilevfx/3_07.png)

Your MEI should now be ready to assign to the stats of a spell.

### Assign the MultiEffectInfo to a Spell in the Stats Editor

To demonstrate how to do this, we will create a new spell that will be really basic and parented to another existing spell from the main game.

> For a more complete guide on how to make a spell in the Stats Editor, please refer to the [Adding a New Spell (Basic)](https://mod.io/g/baldursgate3/r/adding-a-new-spell-basic) guide.

Open the **Stats Editor**.

[![](https://image.modcdn.io/members/63c0/31088933/profilevfx/3_08.png)](https://image.modcdn.io/members/63c0/31088933/profilevfx/3_08.png)

Locate the folder of your project/mod and press the small + button next to the **SpellData** folder. Select the **Target** type. It will create a **Target** spell, to which we will add a new spell entry.

[![](https://image.modcdn.io/members/63c0/31088933/profilevfx/3_09.png)](https://image.modcdn.io/members/63c0/31088933/profilevfx/3_09.png)

> In the screenshot above, the Target type was already created, so it is greyed out in the context menu, but available under the SpellData folder.

By default, one stat entry row will be created. Simply fill in `PaladinTestSpell` as the **Name** of the new spell and press enter to accept it.

[![](https://image.modcdn.io/members/63c0/31088933/profilevfx/3_10.png)](https://image.modcdn.io/members/63c0/31088933/profilevfx/3_10.png)

To assign basic behaviour to the spell we just created, we will give it a **Parent** spell. We will be using the **True Strike** spell as the parent. Click on the **Parent** cell and search for the **TrueStrike** spell name. You can type `TrueStrike` and you should be able to find it quickly.

[![](https://image.modcdn.io/members/63c0/31088933/profilevfx/3_11.png)](https://image.modcdn.io/members/63c0/31088933/profilevfx/3_11.png)

We can now move on to the **PrepareEffect** column on the right and, just like we did for the Parent, click in the cell to open the dropdown and type the name of your MEI, in our case `Test_Paladin`, to link it to the Prepare phase of the spell.

[![](https://image.modcdn.io/members/63c0/31088933/profilevfx/3_12.png)](https://image.modcdn.io/members/63c0/31088933/profilevfx/3_12.png)

With the **PrepareEffect** now set, we can test out the spell and see if our effect is working. Simply save the stats by clicking on the **Save and Export** button in the top left of the Target file.

[![](https://image.modcdn.io/members/63c0/31088933/profilevfx/3_13.png)](https://image.modcdn.io/members/63c0/31088933/profilevfx/3_13.png)

To apply a **CastEffect**, **TargetEffect**, and more, follow the above steps again. You simply need to make an MEI, set up the parameters in it, and add the MEI to the corresponding column in the stats file.

## Testing the New Spell

In this section, we will look at how to test the newly made spell to see if our PrepareEffect is properly showing. For this tutorial, we have been using the level called **WLD\_Campfire\_E**, which can be found in the **Act\_1A\_WLD** level folder.

With the level **WLD\_Campfire\_E** open, launch Game Mode via the **Switch Game/Editor** button.

[![](https://image.modcdn.io/members/63c0/31088933/profilevfx/3_14.png)](https://image.modcdn.io/members/63c0/31088933/profilevfx/3_14.png)

When you launch the game this way, you will already have one of the Origin characters assigned to you to move and play around with.

Press **F11** to open the **Console Window**.

[![](https://image.modcdn.io/members/63c0/31088933/profilevfx/3_15.png)](https://image.modcdn.io/members/63c0/31088933/profilevfx/3_15.png)

Using this window, you will be able to give your character the spell you just created. Simply type `addDebugSpell Target_PaladinTestSpell` in the bottom part of the console and press Enter on your keyboard. You should now see the spell in your hotbar. It should be named **True Strike** and have the same icon and description as the original spell, since we haven’t changed these elements.

[![](https://image.modcdn.io/members/63c0/31088933/profilevfx/3_16.png)](https://image.modcdn.io/members/63c0/31088933/profilevfx/3_16.png)

Select it – your newly made effect should play during the Prepare phase of the spell. If it does, it means that you have successfully assigned your first effect!

[![](https://image.modcdn.io/members/63c0/31088933/profilevfx/3_17.png)](https://image.modcdn.io/members/63c0/31088933/profilevfx/3_17.png)

## Conclusion of Part 3

After following this tutorial, you should now be able to play around with the Effect Editor and assign the effects to spells.

In Part 4, we will talk a bit more generally about different ways to connect effects to different tools and systems.

[G\\
\\
GrumpyWashbear](https://mod.io/g/baldursgate3/u/grumpywashbear/r)

Follow GrumpyWashbear

Log in to join the discussion!

[L](https://mod.io/g/baldursgate3/u/ikarus37)

[lkarus](https://mod.io/g/baldursgate3/u/ikarus37)• [1y ago](https://mod.io/g/baldursgate3/r/vfx-part-3-assigning-and-testing-the-effect#1042447 "10/17/2024, 05:30 AM GMT-4")

Hello, I am trying to make an effect that its target is either Dummy\_L\_HandFx or Dummy\_R\_HandFx, depending on if the character is dualwielding or not. How can I check that condition? I tried using the MainHand or Offhand conditions in the MultiEffectInfo editor, but the effect does not appear when I use them. How can I use those flags or how can I achieve this?

Last updated

1y

Reading time

7 min read

Views

3,363

Comments

1

[G\\
\\
GrumpyWashbear](https://mod.io/g/baldursgate3/u/grumpywashbear/r)

Follow GrumpyWashbear

- [Guide](https://mod.io/g/baldursgate3/r/vfx-part-3-assigning-and-testing-the-effect#guide)
- [Creating a New Target Spell](https://mod.io/g/baldursgate3/r/vfx-part-3-assigning-and-testing-the-effect#heading-1)
- [Creating a MultiEffectInfo](https://mod.io/g/baldursgate3/r/vfx-part-3-assigning-and-testing-the-effect#heading-2)
- [Assign the MultiEffectInfo to a Spell in the Stats Editor](https://mod.io/g/baldursgate3/r/vfx-part-3-assigning-and-testing-the-effect#heading-3)
- [Testing the New Spell](https://mod.io/g/baldursgate3/r/vfx-part-3-assigning-and-testing-the-effect#heading-4)
- [Conclusion of Part 3](https://mod.io/g/baldursgate3/r/vfx-part-3-assigning-and-testing-the-effect#heading-5)
- [Discussion](https://mod.io/g/baldursgate3/r/vfx-part-3-assigning-and-testing-the-effect#discussion)

[English](https://mod.io/g/baldursgate3/r?tags=English) [Official](https://mod.io/g/baldursgate3/r?tags=Official) [VFX](https://mod.io/g/baldursgate3/r?tags=VFX)

Part 3 of the VFX tutorial. In this part, we'll learn how to create a MultiEffectInfo (MEI) file, assign it to a spell using the Stats Editor, and check our effect in-game.

Share

Report guide

---
# SOURCE: https://mod.io/g/baldursgate3/r/getting-started
---

[Browse games](https://mod.io/g)

Browse games

[My library](https://mod.io/library)

My library

[My content](https://mod.io/content)

My content

My account

mod.io

mod.io

[All games](https://mod.io/g) [Baldur's Gate 3](https://mod.io/g/baldursgate3) [Guides](https://mod.io/g/baldursgate3/r) [English](https://mod.io/g/baldursgate3/r?tags=English) Getting Started

Getting Started

Share

Report

Follow

Welcome to the Baldur's Gate 3 Toolkit guides!

If this is your first time using the Toolkit, we suggest starting from these guides:

1. **[Installing the Toolkit](https://mod.io/g/baldursgate3/r/installing-the-toolkit):** How to install the toolkit and make sure it's set up correctly.
2. **[Creating a New Mod](https://mod.io/g/baldursgate3/r/getting-started-creating-a-new-mod):** Creating your first mod project, and some basic set up steps in the Toolkit itself.
3. **[Editor Navigation](https://mod.io/g/baldursgate3/r/editor-navigation):** A short tutorial walking you through the absolute basics of the editor and some of the main windows.
4. [**Editor Tips & Tricks**](https://mod.io/g/baldursgate3/r/editor-shortcuts-and-tips): Some extra functions and tips to make your time using the editor a bit smoother, including in-game debug functionality.

* * *

Once you've become a little more comfortable using the editor, we have some tutorials that take you step-by-step through the basics of creating certain kinds of mods.

- **[Adding a New Spell (Basic)](https://mod.io/g/baldursgate3/r/adding-a-new-spell-basic):**
- **[Adding New Dice](https://mod.io/g/baldursgate3/r/adding-new-dice):**
- **[Adding New Classes or Subclasses](https://mod.io/g/baldursgate3/r/adding-new-classes):**
- Adding New VFX
  - [**Part 1: Making the Effect**](https://mod.io/g/baldursgate3/r/vfx-part-1-making-the-effect)
  - [**Part 2: Creating a Resource**](https://mod.io/g/baldursgate3/r/vfx-part-2-creating-a-resource)
  - [**Part 3: Assigning and Testing the Effect**](https://mod.io/g/baldursgate3/r/vfx-part-3-assigning-and-testing-the-effect)

**Find more guides and tips for modding on the [Baldur's Gate 3 Modding Documentation Website](https://docs.baldursgate3.game/index.php?title=Main_Page)**

* * *

Looking for something more specific? We have a couple of guides about more granular topics.

### **General Editor Functionality**

- **[Editor - Overriding Resources](https://mod.io/g/baldursgate3/r/editor-overriding-resources):** A guide on the basics of the Resource Manager, its panels, and how to change an existing resource by overriding it.
- **[Documentation - Projectiles](https://mod.io/g/baldursgate3/r/documentation-projectiles):** Basic breakdown of projectiles - trajectory type, rotation mode, velocity mode, and spell data.

### **Character Customisation**

#### Asset Creation Guides

Aimed at those creat _i_ ng 3D assets and textures for use in the game. These guides describes some best practices for those assets, and which assets are needed.

- **[Armor Creation Guidelines](https://mod.io/g/baldursgate3/r/creation-guidelines-armor)**
- **[Weapons Creation Guidelines](https://mod.io/g/baldursgate3/r/creation-guidelines-weapons)**

#### Adding New Equipment

Once you have assets ready to be imported, how to actually import those assets into the editor, and set up the stats.

- **[Adding New Armors](https://mod.io/g/baldursgate3/r/adding-an-armor)**
- **Adding New Weapons**\[coming soon\]

### **Hair and Beards**

- **[Part 1: Assets](https://mod.io/g/baldursgate3/r/hair-and-beards-part-one)**\- This is an Asset Creation Guide that describes specifications for meshes, textures, and materials, and how to import them into the editor for further use.
- [**Part 2: Character Creation**](https://mod.io/g/baldursgate3/r/hair-and-beards-part-2-character-creation) \- This guide assumes you have already imported the necessary assets from Part 1, and describes how to set up hairstyles and beards to work across the various races.
- [**Part 3: Helmet Hair**](https://mod.io/g/baldursgate3/r/hair-and-beards-part-3-helmet-hair)\- This guide covers the Helmet Hair system. It describes how to create helmet hair, where it's used, and how to set it up for hairstyles you may have added in Part 2.

  - This guide also includes some basic info on how to create Headwear assets.
- **Part 4: Snapping** \[coming soon\]

### Scripting

- [**Introduction to Osiris**](https://mod.io/g/baldursgate3/r/introduction-to-osiris) \- What is the Osiris scripting language? This guide breaks down the main concepts and how to structure your scripts.
- [**Using the Story Editor**](https://mod.io/g/baldursgate3/r/scripting-using-the-story-editor) \- Understanding the Story Editor and goal hierarchy, how to build and reload scripts, how to fix common build errors, and basic debugging using logs.
- Scripting Your First Situation \[coming soon\]

[G\\
\\
GrumpyWashbear](https://mod.io/g/baldursgate3/u/grumpywashbear/r)

Follow GrumpyWashbear

Log in to join the discussion!

[M](https://mod.io/g/baldursgate3/u/modiouserekds)

[ModioUserekds](https://mod.io/g/baldursgate3/u/modiouserekds)• [1y ago](https://mod.io/g/baldursgate3/r/getting-started#1074631 "11/6/2024, 02:23 PM GMT-5")

Hi I have a dumb question but do I need to have the game in order to be able to mod it. I own the game on playstation but would like to make mods. Thank you

[S](https://mod.io/g/baldursgate3/u/siggbert)

[Siggbert](https://mod.io/g/baldursgate3/u/siggbert)• [1y ago](https://mod.io/g/baldursgate3/r/getting-started#1068680 "11/2/2024, 09:50 AM GMT-4")

Can you please make a guide for modifying existing weapons/armor?

I'm trying to add radiant damage to the Blood of Lathander but i can't get it to work ingame.

I'm overrideing the root template but i don't know how to make ongoing playthroughs use the modded template.

[S](https://mod.io/g/baldursgate3/u/syruscoleuk)

[SyrusCole](https://mod.io/g/baldursgate3/u/syruscoleuk)• [1y ago](https://mod.io/g/baldursgate3/r/getting-started#1063532 "10/29/2024, 03:38 PM GMT-4")

How do you get your mod into the full game once you've finished building it?

[W](https://mod.io/g/baldursgate3/u/39771)

[wrath01](https://mod.io/g/baldursgate3/u/39771)• [1y ago](https://mod.io/g/baldursgate3/r/getting-started#1041173 "10/16/2024, 10:23 AM GMT-4")

how to change the language of the program ?

[P](https://mod.io/g/baldursgate3/u/na238630)

[PhosphorusC](https://mod.io/g/baldursgate3/u/na238630)• [1y ago](https://mod.io/g/baldursgate3/r/getting-started#1035787 "10/13/2024, 05:29 AM GMT-4")

Waiting for a guide about how to add new faces : (

[M](https://mod.io/g/baldursgate3/u/modiouserjcsn)

[ModioUserjcsn](https://mod.io/g/baldursgate3/u/modiouserjcsn)• [1y ago](https://mod.io/g/baldursgate3/r/getting-started#990978 "9/16/2024, 04:22 PM GMT-4")

How do we add mods people have created? I downloaded/subscribed to them in the mod manager in game and nothing happened.

[H](https://mod.io/g/baldursgate3/u/meatball59)

[hanneroni](https://mod.io/g/baldursgate3/u/meatball59)• [1y ago](https://mod.io/g/baldursgate3/r/getting-started#1041258 "10/16/2024, 11:32 AM GMT-4")

Are the boxes checked when you look at your subscribed items tab? I think the first time you download stuff they aren't checked

[M](https://mod.io/g/baldursgate3/u/mitsudesu)

[mitsudesu](https://mod.io/g/baldursgate3/u/mitsudesu)• [1y ago](https://mod.io/g/baldursgate3/r/getting-started#1037819 "10/14/2024, 08:57 AM GMT-4")

i wonder that too can anybody help

[T](https://mod.io/g/baldursgate3/u/thekingkevin)

[TheKingKevin](https://mod.io/g/baldursgate3/u/thekingkevin)• [1y ago](https://mod.io/g/baldursgate3/r/getting-started#989724 "9/15/2024, 07:47 PM GMT-4")

Wow this is a ton. I just want to make a simple feat and am a bit overwhelmed

[M](https://mod.io/g/baldursgate3/u/modiouserduwd)

[ModioUserduwd](https://mod.io/g/baldursgate3/u/modiouserduwd)• [1y ago](https://mod.io/g/baldursgate3/r/getting-started#985220 "9/13/2024, 01:01 PM GMT-4")

A lookup for all available functions (functors?), with their respective inputs described, would be much appreciated for creating custom items.
I badly want to try to create a cursed weapon that always attacks recklessly, but if your attack misses it keeps using your available actions/bonus actions, until it either hits, or you run out of actions. But I can't seem to find any way to achieve this.

[C](https://mod.io/g/baldursgate3/u/cr1ogen)

[Cr1ogen](https://mod.io/g/baldursgate3/u/cr1ogen)• [1y ago](https://mod.io/g/baldursgate3/r/getting-started#981137 "9/10/2024, 08:09 PM GMT-4")

Does anyone know if there is a possibility of being able to make a mod to be able to choose whether your character can choose between left and right handed?

[K](https://mod.io/g/baldursgate3/u/kazemir14)

[Kazemir14](https://mod.io/g/baldursgate3/u/kazemir14)• [1y ago](https://mod.io/g/baldursgate3/r/getting-started#980978 "9/10/2024, 06:16 PM GMT-4")

Anybody knows how to install the mod that you create?

[I](https://mod.io/g/baldursgate3/u/modiouser20745172)

[Irbisthor](https://mod.io/g/baldursgate3/u/modiouser20745172)• [1y ago](https://mod.io/g/baldursgate3/r/getting-started#997471 "9/20/2024, 06:49 PM GMT-4")

If you don't want to watch whole video, just go to 27:47

Build your own equipment mod for Baldur's Gate 3 - Modding with Ohfor Ep. 1 - YouTube

[Photo image of Ohfor Fuksake](https://www.youtube.com/channel/UC9SUmecuI2ts22V4OmG694A?embeds_referring_euri=https%3A%2F%2Fmod.io%2F)

Ohfor Fuksake

888 subscribers

[Build your own equipment mod for Baldur's Gate 3 - Modding with Ohfor Ep. 1](https://www.youtube.com/watch?v=80OPtDCNkqU)

Ohfor Fuksake

Search

Watch later

Share

Copy link

Info

Shopping

Tap to unmute

If playback doesn't begin shortly, try restarting your device.

You're signed out

Videos you watch may be added to the TV's watch history and influence TV recommendations. To avoid this, cancel and sign in to YouTube on your computer.

CancelConfirm

More videos

## More videos

Share

Include playlist

An error occurred while retrieving sharing information. Please try again later.

[Why am I seeing this?](https://support.google.com/youtube/answer/9004474?hl=en)

[Watch on](https://www.youtube.com/watch?v=80OPtDCNkqU&embeds_referring_euri=https%3A%2F%2Fmod.io%2F)

0:00

0:00 / 32:11

•Live

•

[J](https://mod.io/g/baldursgate3/u/captainplank)

[jeffchou](https://mod.io/g/baldursgate3/u/captainplank)• [1y ago](https://mod.io/g/baldursgate3/r/getting-started#980322 "9/10/2024, 09:16 AM GMT-4")

coming soon????????please quickly~~~~~~~~~~

[7](https://mod.io/g/baldursgate3/u/7neon7)

[7NeoN7](https://mod.io/g/baldursgate3/u/7neon7)• [1y ago](https://mod.io/g/baldursgate3/r/getting-started#975584 "9/7/2024, 03:48 PM GMT-4")

hi just a question, is there any syntax for all the scripting ? if so can somebody send me a link ? thx

[T](https://mod.io/g/baldursgate3/u/taiscerayne2426)

[TaisceRayne](https://mod.io/g/baldursgate3/u/taiscerayne2426)• [1y ago](https://mod.io/g/baldursgate3/r/getting-started#974046 "9/6/2024, 07:13 PM GMT-4")

Is there any support for voice modding yet? Just basic pitch-shifting and the like? I was hoping this modding system would make it easier to locate the Point-and-Click lines

[M](https://mod.io/g/baldursgate3/u/modiouser20756622)

[ModioUser2075662](https://mod.io/g/baldursgate3/u/modiouser20756622)• [1y ago](https://mod.io/g/baldursgate3/r/getting-started#973750 "9/6/2024, 03:55 PM GMT-4")

Would love some documentation on available variables for spells and such. I'm having trouble accessing the character's maximum and current health for a spell because none of the variable names I've tried map to those values (also, I can't find any other spells that access those variables) and there's no autocomplete for variables in the toolkit.

[V](https://mod.io/g/baldursgate3/u/viile)

[viile](https://mod.io/g/baldursgate3/u/viile)• [1y ago](https://mod.io/g/baldursgate3/r/getting-started#972666 "9/5/2024, 08:32 PM GMT-4")

How to edit existing spells? Or how to add racial traits to other races, like dragonborn tails or tiefling horns?

[T](https://mod.io/g/baldursgate3/u/terkkaritero)

[TerkkariTero](https://mod.io/g/baldursgate3/u/terkkaritero)• [1y ago](https://mod.io/g/baldursgate3/r/getting-started#973264 "9/6/2024, 08:31 AM GMT-4")

I'm also wondering how to edit existing things. I tried to edit GustavDev directly but it says that I need to make an "add-on" and import GustavDev into there. How do you do this?

[F](https://mod.io/g/baldursgate3/u/finalshieldnobi)

[FinalShieldnobi](https://mod.io/g/baldursgate3/u/finalshieldnobi)• [1y ago](https://mod.io/g/baldursgate3/r/getting-started#972746 "9/5/2024, 09:19 PM GMT-4")

I second this. I've always wanted to learn how to edit existing things, like making Greatclubs deal 1d10, increasing the damage dealt by Phantasmal Force, or making Trickery Domain Cleric's Invoke Duplicity a Bonus Action.

[K](https://mod.io/g/baldursgate3/u/somegodguy)

[keys34](https://mod.io/g/baldursgate3/u/somegodguy)• [1y ago](https://mod.io/g/baldursgate3/r/getting-started#972744 "9/5/2024, 09:17 PM GMT-4")

that would most likely be similar to the creating hair and beard section for the tool kit [@hair-and-beards-part-one](https://mod.io/g/baldursgate3/r/hair-and-beards-part-one) there is also a tutorial showing how to create custom faces with the mod toolkit on YouTube right now

Creating a Head Mod using the BG3 Modders Toolkit - YouTube

[Photo image of UndefinedScribble](https://www.youtube.com/channel/UCz0Unn1lMsUx0ibfaqaoU0w?embeds_referring_euri=https%3A%2F%2Fmod.io%2F)

UndefinedScribble

390 subscribers

[Creating a Head Mod using the BG3 Modders Toolkit](https://www.youtube.com/watch?v=40GnRNjWXng)

UndefinedScribble

Search

Watch later

Share

Copy link

Info

Shopping

Tap to unmute

If playback doesn't begin shortly, try restarting your device.

More videos

## More videos

You're signed out

Videos you watch may be added to the TV's watch history and influence TV recommendations. To avoid this, cancel and sign in to YouTube on your computer.

CancelConfirm

Share

Include playlist

An error occurred while retrieving sharing information. Please try again later.

[Watch on](https://www.youtube.com/watch?v=40GnRNjWXng&embeds_referring_euri=https%3A%2F%2Fmod.io%2F)

0:00

0:00 / 20:01

•Live

•

[V](https://mod.io/g/baldursgate3/u/viile)

[viile](https://mod.io/g/baldursgate3/u/viile)• [1y ago](https://mod.io/g/baldursgate3/r/getting-started#972753 "9/5/2024, 09:24 PM GMT-4")

youre completely right, i ended up finding that video and using references. i copied the uuid of the horns into my mod and replaced the race uuid. only problem is that id have to edit something to get the gith male head to not have floating horns

Last updated

49d

Reading time

3 min read

Views

103,197

Comments

22

[G\\
\\
GrumpyWashbear](https://mod.io/g/baldursgate3/u/grumpywashbear/r)

Follow GrumpyWashbear

- [Guide](https://mod.io/g/baldursgate3/r/getting-started#guide)
- [General Editor Functionality](https://mod.io/g/baldursgate3/r/getting-started#heading-1)
- [Character Customisation](https://mod.io/g/baldursgate3/r/getting-started#heading-2)
- [Asset Creation Guides](https://mod.io/g/baldursgate3/r/getting-started#heading-3)
- [Adding New Equipment](https://mod.io/g/baldursgate3/r/getting-started#heading-4)
- [Hair and Beards](https://mod.io/g/baldursgate3/r/getting-started#heading-5)
- [Scripting](https://mod.io/g/baldursgate3/r/getting-started#heading-6)
- [Discussion](https://mod.io/g/baldursgate3/r/getting-started#discussion)

[English](https://mod.io/g/baldursgate3/r?tags=English) [Getting Started](https://mod.io/g/baldursgate3/r?tags=Getting+Started) [Official](https://mod.io/g/baldursgate3/r?tags=Official)

Start here! A brief overview of the guides available, and where you should start if you're feeling lost.

Share

Report guide

---
# SOURCE: https://mod.io/g/baldursgate3/r/adding-skill-and-item-icons
---

[Browse games](https://mod.io/g)

Browse games

[My library](https://mod.io/library)

My library

[My content](https://mod.io/content)

My content

My account

mod.io

mod.io

[All games](https://mod.io/g) [Baldur's Gate 3](https://mod.io/g/baldursgate3) [Guides](https://mod.io/g/baldursgate3/r) [English](https://mod.io/g/baldursgate3/r?tags=English) Adding Skill and Item Icons

Adding Skill and Item Icons

Share

Report

Follow

This guide describes how to create a new texture atlas, and add new icons for skills and/or items.

## Making a New Atlas

In the Editor, open the Texture Atlas Editor from the main toolbar.

[![](https://image.modcdn.io/members/63c0/31088933/profileicons/skill_01.png)](https://image.modcdn.io/members/63c0/31088933/profileicons/skill_01.png)

To create a new atlas in the Texture Atlas Editor, either click on the paper icon or go to `File > New`.

[![](https://image.modcdn.io/members/63c0/31088933/profileicons/skill_02.png)](https://image.modcdn.io/members/63c0/31088933/profileicons/skill_02.png)

This will open the **Create new texture atlas** dialogue box.

- **File path to .lsx:** There is no reason to change the actual path, but you can click on the “…” button beside the field to rename the new atlas to something more informative than `newAtlas.lsx`.

- **File path to .dds:** This is the .dds file that will contain the grid with the icon images. Again, no need to change the path, only the filename.

- **Icon size:** Keep to 64x64.

- **Texture size:** This is the total size of the texture atlas image. The sizes can only be powers of 2, from 32x32 to 4096x4096. We recommend sticking to 512x512 or 1024x1024.
  - 512x512: a grid of 8x8 spaces to house 64 icons (of 64x64)

  - 1024x1024: a grid of 16x16 spaces to house 256 icons (of 64x64)
- **Square icons:** Keep this enabled. All of our skill and item icons are 64x64 squares.

- **Custom:** This option lets you create texture atlases that are not square. We do not recommend this; please keep it disabled.

- **Package:** This is your mod package.


[![](https://image.modcdn.io/members/63c0/31088933/profileicons/skill_03.png)](https://image.modcdn.io/members/63c0/31088933/profileicons/skill_03.png)

Click Save.

Your new atlas should automatically open in the Texture Atlas Editor. You can confirm this by resizing the window to view the full filepath in the title:

[![](https://image.modcdn.io/members/63c0/31088933/profileicons/skill_04.png)](https://image.modcdn.io/members/63c0/31088933/profileicons/skill_04.png)

## Adding New Skill or Item Icons

The process is almost identical for adding both skill and item icons. You will need three versions of each icon:

| **Size** | **Details** |
| --- | --- |
| 64x64 PNG | Used on the hotbar. |
| 144x144 PNG | Should have a transparent background.<br>Used in the ControllerUI menu. |
| 380x380 PNG | Should have a transparent background and a fade effect.<br>Used in tooltips. |

We recommend organising the above assets under `/Data/Public/[modname]/GUI/` in the folder structure pictured below, but it’s not a requirement.

[![](https://image.modcdn.io/members/63c0/31088933/profileicons/skill_05.png)](https://image.modcdn.io/members/63c0/31088933/profileicons/skill_05.png)

### Adding the 64x64 Icon

In the Editor, open the Texture Atlas Editor from the main toolbar.

[![](https://image.modcdn.io/members/63c0/31088933/profileicons/skill_01.png)](https://image.modcdn.io/members/63c0/31088933/profileicons/skill_01.png)

Open an atlas (or create a new one following the steps above). We will use `newAtlas.lsx`, created in the section above.

To add a new icon, click on the Add Entries button.

[![](https://image.modcdn.io/members/63c0/31088933/profileicons/skills_06.png)](https://image.modcdn.io/members/63c0/31088933/profileicons/skills_06.png)

It will open a dialogue box that defaults to the `/GUI/` folder inside your `/Data/Public/[modname]/` path. Select your desired 64x64 PNG file, and press Open.

> If your icon is not added, and you have a message along the lines of `The icon ID "[icon name]" already exists in the atlas "[filepath]`" in the Message Log of the Editor, it means that your icon PNG’s filename is identical to an existing one. You’ll need to rename your icons to something that doesn’t already exist in the game.

If all’s gone well, you should see your icon appear in the atlas!

[![](https://image.modcdn.io/members/63c0/31088933/profileicons/skills_07.png)](https://image.modcdn.io/members/63c0/31088933/profileicons/skills_07.png)

Make sure to Save. This will update the following files:

- `/Data/Public/[modname]/Assets/Textures/Icons/[youratlasname].dds`

- `/Data/Public/[modname]/GUI/[youratlasname].lsx`


### Adding the 144x144 ControllerUI Icon

In the Editor, go to **Project > Convert UI Assets…**

[![](https://image.modcdn.io/members/63c0/31088933/profileicons/skills_08.png)](https://image.modcdn.io/members/63c0/31088933/profileicons/skills_08.png)

This will open the UI Assets Converter.

[![](https://image.modcdn.io/members/63c0/31088933/profileicons/skills_09.png)](https://image.modcdn.io/members/63c0/31088933/profileicons/skills_09.png)

Click on the **Add files…** button to open a system dialogue. Select the 144x144 PNG file(s) you organised earlier.

Verify that the **Selected mod** is correctly set to your currently open mod project.

Fill in the **Output subfolder** according to whether you’re adding a skill or an item icon.

| **Icon Type** | **Output Subfolder** |
| --- | --- |
| Skills | ControllerUIIcons/skills\_png |
| Items | ControllerUIIcons/items\_png |

Then, click on either of the twin input bars below ( **Output assets folder** or **Output lowres assets**) to make both bars automatically update to the correct filepath. You can scroll to the end of the filepath to verify that they’ve updated correctly.

[![](https://image.modcdn.io/members/63c0/31088933/profileicons/skills_10.png)](https://image.modcdn.io/members/63c0/31088933/profileicons/skills_10.png)

Click OK and wait for the conversion to complete. You should see a success message in the Message Log that looks something like ‘Converted 1 files, failed 0 in 0m00s’.

[![](https://image.modcdn.io/members/63c0/31088933/profileicons/skills_11.png)](https://image.modcdn.io/members/63c0/31088933/profileicons/skills_11.png)

For skills, the generated 144x144 DDS files are automatically placed into these folders:

- `/Data/Mods/[modname]/GUI/Assets/ControllerUIIcons/skills_png/`

- `/Data/Mods/[modname]/GUI/AssetsLowRes/ControllerUIIcons/skills_png/`


For items, the generated 144x144 DDS files are automatically placed into these folders:

- `/Data/Mods/[modname]/GUI/Assets/ControllerUIIcons/items_png/`

- `/Data/Mods/[modname]/GUI/AssetsLowRes/ControllerUIIcons/items_png/`


### Adding the 380x380 Tooltip Icon

Once again, open the UI Asset Converter. This time, select the 380x380 PNG file(s).

Fill in the **Output subfolder** according to whether you’re adding a skill or an item icon.

| **Icon Type** | **Output Subfolder** |
| --- | --- |
| Skills | Tooltips/Icons |
| Items | Tooltips/ItemIcons |

After filling it in, click on either of the twin input bars below ( **Output assets folder** or **Output lowres folder**) to make both bars automatically update to the correct filepath.

[![](https://image.modcdn.io/members/63c0/31088933/profileicons/skills_12.png)](https://image.modcdn.io/members/63c0/31088933/profileicons/skills_12.png)

Click OK.

For skills, the generated DDS files are automatically placed into these folders:

- `/Data/Mods/[modname]/GUI/Assets/Tooltips/Icons/`

- `/Data/Mods/[modname]/GUI/AssetsLowRes/Tooltips/Icons/`


For items, the generated DDS files are automatically placed into these folders:

- `/Data/Mods/[modname]/GUI/Assets/Tooltips/ItemIcons/`

- `/Data/Mods/[modname]/GUI/AssetsLowRes/Tooltips/ItemIcons/`


## Hooking Up the Icons

Your icons are now in atlases and in the correct folders. Now, in order for them to actually appear in-game, you’ll need to make sure your skill or item is correctly referencing those icons.

### Skills

For skills (or 'spells'), icons need to be defined via the Stats Editor. For example, if you followed the **[Adding a New Spell (Simple)](https://mod.io/g/baldursgate3/r/adding-a-new-spell-basic)** guide, you’d define the icon for the spell in the Target file. The icon name referenced below is identical to the icon’s filename, and also what you would see if you opened the atlas.

[![](https://image.modcdn.io/members/63c0/31088933/profileicons/skills_13.png)](https://image.modcdn.io/members/63c0/31088933/profileicons/skills_13.png)

[![](https://image.modcdn.io/members/63c0/31088933/profileicons/skills_14.png)](https://image.modcdn.io/members/63c0/31088933/profileicons/skills_14.png)

#### Testing in the Game

To quickly test how the icons look on your spell, load into `Basic_Level_A`. Once the level is loaded, enter Game Mode, then use `Ctrl+Shift+F11` to open the console window.

Use the `addDebugSpell %name%` command to add the spell to the player character. For example, for the FireTouch spell above, we would type `addDebugSpell Target_FireTouch.`

[![](https://image.modcdn.io/members/63c0/31088933/profileicons/skills_15.png)](https://image.modcdn.io/members/63c0/31088933/profileicons/skills_15.png)

Press Enter, and the spell will appear on the hotbar.

[![](https://image.modcdn.io/members/63c0/31088933/profileicons/skills_16.png)](https://image.modcdn.io/members/63c0/31088933/profileicons/skills_16.png)

### Items

Item icons are instead set on the root template of the item, in the **Item > Icon** property field of the Root Templates Manager.

[![](https://image.modcdn.io/members/63c0/31088933/profileicons/skills_17.png)](https://image.modcdn.io/members/63c0/31088933/profileicons/skills_17.png)

## Troubleshooting

### Icons aren't showing up when testing

If everything appears to have imported correctly when following the above steps, but the icons don’t appear when testing in-game, make sure you have all of your work saved and **restart the Editor**. This usually fixes the issue.

[G\\
\\
GrumpyWashbear](https://mod.io/g/baldursgate3/u/grumpywashbear/r)

Follow GrumpyWashbear

Log in to join the discussion!

[R](https://mod.io/g/baldursgate3/u/modiouser2112914)

[RekhytFR](https://mod.io/g/baldursgate3/u/modiouser2112914)• [23d ago](https://mod.io/g/baldursgate3/r/adding-skill-and-item-icons#1551469 "12/7/2025, 06:42 PM GMT-5")

When creating the Atlas, the "mod package" selector is empty and I can't select anything. I obviously have my mod that I've been working on for months loaded and restarted this fxcking mod editor several times.
I so hate this editor that makes mod editing so goddamn complicated. Had no issue making custom icons before, no crashes and lousy software eating 13 gb of RAM...

[A](https://mod.io/g/baldursgate3/u/ace150k)

[Ace150k](https://mod.io/g/baldursgate3/u/ace150k)• [31d ago](https://mod.io/g/baldursgate3/r/adding-skill-and-item-icons#1545826 "11/30/2025, 10:45 AM GMT-5")

Does this also apply to Class icons?

[D](https://mod.io/g/baldursgate3/u/dufulicious)

[DufuLicious](https://mod.io/g/baldursgate3/u/dufulicious)• [258d ago](https://mod.io/g/baldursgate3/r/adding-skill-and-item-icons#1308814 "4/17/2025, 12:01 AM GMT-4")

Whenever I use the converter to convert my icons, it turns them super dark. Is there a fix for that?

[K](https://mod.io/g/baldursgate3/u/kingraithwall)

[KingRaithwall](https://mod.io/g/baldursgate3/u/kingraithwall)• [178d ago](https://mod.io/g/baldursgate3/r/adding-skill-and-item-icons#1403804 "7/6/2025, 05:57 AM GMT-4")

Did you ever find a good fix for this? I'm also running into this issue now.

[F](https://mod.io/g/baldursgate3/u/flyfundev)

[FlyFunDev](https://mod.io/g/baldursgate3/u/flyfundev)• [238d ago](https://mod.io/g/baldursgate3/r/adding-skill-and-item-icons#1336413 "5/6/2025, 09:53 PM GMT-4")

I had the same issue. I don't remember exactly what I did to fix it, but I think it involved opening the file in an image viewer and resaving it. I think the issue was with the compression or the format or something?

[S](https://mod.io/g/baldursgate3/u/sorencdn)

[SorenCDN](https://mod.io/g/baldursgate3/u/sorencdn)• [1y ago](https://mod.io/g/baldursgate3/r/adding-skill-and-item-icons#1103052 "11/27/2024, 04:23 AM GMT-5")

I've restarted my toolkit quite a few times and my tooltip image won't function. The hotbar icon functions just fine, but the tooltip won't show and I get the error message "Couldn't find the file Assets/Tooltips/Icons/QuenIcon.png" every file I used in this process; the 64px, 144px, and 380px all used the same name "QuenIcon.png" pls assist ;-;

[S](https://mod.io/g/baldursgate3/u/sankojin1)

[Sankojin](https://mod.io/g/baldursgate3/u/sankojin1)• [254d ago](https://mod.io/g/baldursgate3/r/adding-skill-and-item-icons#1314315 "4/20/2025, 06:45 PM GMT-4")

You have to make sure all your icons for the same item have the same name. Such as longsword\_icon is the same for the 64, 144, and 380. If you have them with different names, such as longsword\_icon\_64, longsword\_icon\_144, the game will think they are different.

[S](https://mod.io/g/baldursgate3/u/slafniy)

[slafniy](https://mod.io/g/baldursgate3/u/slafniy)• [1y ago](https://mod.io/g/baldursgate3/r/adding-skill-and-item-icons#1016365 "10/2/2024, 06:17 PM GMT-4")

Trying to create new atlas (default parameters), getting this:
Failed to retrieve package ''!
Any ideas? :)

Upd. "Package" field seems empty by some reason
Upd2. You should create a package in Resources first

[S](https://mod.io/g/baldursgate3/u/siftherevenant)

[SifTheRevenant](https://mod.io/g/baldursgate3/u/siftherevenant)• [1y ago](https://mod.io/g/baldursgate3/r/adding-skill-and-item-icons#1027473 "10/8/2024, 03:29 PM GMT-4")

How do I create a package in Resources? I haven't seen anything about that in any guide.

[S](https://mod.io/g/baldursgate3/u/slafniy)

[slafniy](https://mod.io/g/baldursgate3/u/slafniy)• [1y ago](https://mod.io/g/baldursgate3/r/adding-skill-and-item-icons#1031709 "10/11/2024, 04:05 AM GMT-4")

Open Resources tab and look into top left corner of it (above of the packages tree). There are smaaaaaal icons without any tooltips, one of them creates new package :)

[L](https://mod.io/g/baldursgate3/u/1486009769)

[Linco1nwlc](https://mod.io/g/baldursgate3/u/1486009769)• [1y ago](https://mod.io/g/baldursgate3/r/adding-skill-and-item-icons#993058 "9/17/2024, 07:51 PM GMT-4")

Does anyonne know how to add a new icon for a new Action Resource? I added a new Action Resource, but i cant select a icon for it.

[F](https://mod.io/g/baldursgate3/u/firblo)

[firblo](https://mod.io/g/baldursgate3/u/firblo)• [1y ago](https://mod.io/g/baldursgate3/r/adding-skill-and-item-icons#997286 "9/20/2024, 04:33 PM GMT-4")

This worked perfectly for me: [@implementing-custom-action-resources-with-impui](https://mod.io/g/baldursgate3/r/implementing-custom-action-resources-with-impui)

[X](https://mod.io/g/baldursgate3/u/modiouser3617319)

[xStiven](https://mod.io/g/baldursgate3/u/modiouser3617319)• [1y ago](https://mod.io/g/baldursgate3/r/adding-skill-and-item-icons#1104929 "11/28/2024, 04:29 PM GMT-5")

You need to install additional mod ;/

[D](https://mod.io/g/baldursgate3/u/modiouser20822781)

[dreunik](https://mod.io/g/baldursgate3/u/modiouser20822781)• [1y ago](https://mod.io/g/baldursgate3/r/adding-skill-and-item-icons#981795 "9/11/2024, 07:21 AM GMT-4")

Hi, I'm having an error message when creating the texture atlas: "Unable to load DLL FreeImage". I've downloaded the DLL and placed it in the Window System folders (both 32 and 64 bits, just in case) and I'm still getting the error message. Does anyone had have a similar issue? Or any suggestion on where to put the DLL file?

Edit: I checked again, and realized that I already had the FreeImage.dll and FreeImageNET.dll files in the ToolKit Path. So, it's not something about the placement of the file.

[T](https://mod.io/g/baldursgate3/u/terpee93)

[terpee93](https://mod.io/g/baldursgate3/u/terpee93)• [1y ago](https://mod.io/g/baldursgate3/r/adding-skill-and-item-icons#1051857 "10/22/2024, 01:33 PM GMT-4")

Same here. I see the files \`FreeImage.dll\` and \`FreeImageNET.dll\` in \\Steam\\steamapps\\common\\Baldurs Gate 3 Toolkit\\. Do they belong somewhere else?

[F](https://mod.io/g/baldursgate3/u/till49)

[Faveyl](https://mod.io/g/baldursgate3/u/till49)• [1y ago](https://mod.io/g/baldursgate3/r/adding-skill-and-item-icons#1096954 "11/22/2024, 04:00 PM GMT-5")

This download fixed it for me: [https://www.microsoft.com/en-us/download/details.aspx?id=40784](https://www.microsoft.com/en-us/download/details.aspx?id=40784)

[F](https://mod.io/g/baldursgate3/u/flameancer)

[Flameancer](https://mod.io/g/baldursgate3/u/flameancer)• [1y ago](https://mod.io/g/baldursgate3/r/adding-skill-and-item-icons#978628 "9/9/2024, 02:45 AM GMT-4")

Wait, some slight confusion. Can you import just the 144x144 icon and have it convert to the 64x64 size for the hotbar? Will it automatically can the regular spell background or do I have to make a 64x64 icon that contains that background by default? If so is there a way to export the background?

[O](https://mod.io/g/baldursgate3/u/overseer32)

[OverseerNZ](https://mod.io/g/baldursgate3/u/overseer32)• [1y ago](https://mod.io/g/baldursgate3/r/adding-skill-and-item-icons#1047419 "10/19/2024, 08:05 PM GMT-4")

Second this, can't find the icon backgrounds online anywhere!

[O](https://mod.io/g/baldursgate3/u/overseer32)

[OverseerNZ](https://mod.io/g/baldursgate3/u/overseer32)• [1y ago](https://mod.io/g/baldursgate3/r/adding-skill-and-item-icons#1047422 "10/19/2024, 08:09 PM GMT-4")

[https://www.nexusmods.com/baldursgate3/mods/3125](https://www.nexusmods.com/baldursgate3/mods/3125)
Found! The brown and blue backgrounds are in here

1 reply

[R](https://mod.io/g/baldursgate3/u/renardblagueur)

[RenardBlagueur](https://mod.io/g/baldursgate3/u/renardblagueur)• [1y ago](https://mod.io/g/baldursgate3/r/adding-skill-and-item-icons#974788 "9/7/2024, 06:25 AM GMT-4")

There are some missings infos in this guide, for items, I could generate the 64x64 Icons (this works in the inventory), and the other ControllerUI and Tooltip Icon as DDS files with the toolkit (this does not seem to work in the tooltip view).
But in game the editor keeps asking for png files instead of dds :
"Image not found 'Assets/Tooltips/ItemIcons/KBGL\_Jesters\_Chain\_280.png'"

EDIT :
As said by LeoleR below : you must ensure that your icon images (64px, 144px, 380px) have the same names when you follow the guide, and after generating dds, restart editor
It worked for me that way :)

[P](https://mod.io/g/baldursgate3/u/pommelstrike)

[pommelstrike](https://mod.io/g/baldursgate3/u/pommelstrike)• [1y ago](https://mod.io/g/baldursgate3/r/adding-skill-and-item-icons#988186 "9/15/2024, 02:23 AM GMT-4")

🤣🤣🤣🤣yes thank you for assuring comment. yea its heavly implied that filename structure has to be very consistent ithoughout this toolkit but man the amount of tension these guides put one in, i would of been nice for them to at least show a screenshot of the same file names.

[C](https://mod.io/g/baldursgate3/u/chizfreak)

[ChizFreak](https://mod.io/g/baldursgate3/u/chizfreak)• [1y ago](https://mod.io/g/baldursgate3/r/adding-skill-and-item-icons#981601 "9/11/2024, 01:42 AM GMT-4")

Thank you for this comment, this fixed my missing icons.

[L](https://mod.io/g/baldursgate3/u/leoler)

[LeoleR](https://mod.io/g/baldursgate3/u/leoler)• [1y ago](https://mod.io/g/baldursgate3/r/adding-skill-and-item-icons#973900 "9/6/2024, 05:33 PM GMT-4")

In my experience, I wasn't able to link my spell to the tooltip icon until I renamed them all the same, and the 64x64 was .DDS at the time of import, not PNG.

Last updated

1y

Reading time

7 min read

Views

11,411

Comments

24

[G\\
\\
GrumpyWashbear](https://mod.io/g/baldursgate3/u/grumpywashbear/r)

Follow GrumpyWashbear

- [Guide](https://mod.io/g/baldursgate3/r/adding-skill-and-item-icons#guide)
- [Making a New Atlas](https://mod.io/g/baldursgate3/r/adding-skill-and-item-icons#heading-1)
- [Adding New Skill or Item Icons](https://mod.io/g/baldursgate3/r/adding-skill-and-item-icons#heading-2)
- [Adding the 64x64 Icon](https://mod.io/g/baldursgate3/r/adding-skill-and-item-icons#heading-3)
- [Adding the 144x144 ControllerUI Icon](https://mod.io/g/baldursgate3/r/adding-skill-and-item-icons#heading-4)
- [Adding the 380x380 Tooltip Icon](https://mod.io/g/baldursgate3/r/adding-skill-and-item-icons#heading-5)
- [Hooking Up the Icons](https://mod.io/g/baldursgate3/r/adding-skill-and-item-icons#heading-6)
- [Skills](https://mod.io/g/baldursgate3/r/adding-skill-and-item-icons#heading-7)
- [Testing in the Game](https://mod.io/g/baldursgate3/r/adding-skill-and-item-icons#heading-8)
- [Items](https://mod.io/g/baldursgate3/r/adding-skill-and-item-icons#heading-9)
- [Troubleshooting](https://mod.io/g/baldursgate3/r/adding-skill-and-item-icons#heading-10)
- [Icons aren't showing up when testing](https://mod.io/g/baldursgate3/r/adding-skill-and-item-icons#heading-11)
- [Discussion](https://mod.io/g/baldursgate3/r/adding-skill-and-item-icons#discussion)

[English](https://mod.io/g/baldursgate3/r?tags=English) [Icons](https://mod.io/g/baldursgate3/r?tags=Icons) [Official](https://mod.io/g/baldursgate3/r?tags=Official)

Overview on the assets required, how to create a new atlas, and how to add the necessary icons.

Share

Report guide

---
# SOURCE: https://mod.io/g/baldursgate3/r/generating-icons-for-character-creation
---

[Browse games](https://mod.io/g)

Browse games

[My library](https://mod.io/library)

My library

[My content](https://mod.io/content)

My content

My account

mod.io

mod.io

[All games](https://mod.io/g) [Baldur's Gate 3](https://mod.io/g/baldursgate3) [Guides](https://mod.io/g/baldursgate3/r) [Beards](https://mod.io/g/baldursgate3/r?tags=Beards) Generating Icons for Character Creation

Generating Icons for Character Creation

Share

Report

Follow

> This guide assumes a working knowledge of the Baldur’s Gate 3 Toolkit and the tools contained within. If you’re completely new to modding for Baldur’s Gate 3, we suggest starting with some of the basics outlined in the [**Getting Started**](https://mod.io/g/baldursgate3/r/getting-started) guide.

This guide aims to explain how Character Creation (CC) icons are generated. These icons provide previews of the appearance choices made available during CC.

We generate icons for:

- Heads

- Hair

- Beards

- Makeup

- Tattoos

- Scars

- Draconic scales

- Horns

- Tails


[![](https://image.modcdn.io/members/63c0/31088933/profilecreate/ex_head.png)](https://image.modcdn.io/members/63c0/31088933/profilecreate/ex_head.png)

CC icons are generated using mannequins in a booth. A mannequin is a 3D model used specifically for rendering these CC icons, and the booth serves as a virtual photo booth. The mannequins are set up in both **Shared** and **SharedDev** in the  `SYS_IconGeneration_A` level, and are driven by the **UUID Object Editor**.

## General Booth Setup

The booth setup consists of 4 elements and is the same for all icons:

- A spawn trigger

- A camera trigger

- A background

- Lights


The characters use a custom pose for the purposes of creating the icon: `CC_HairStyle_Icon_Still_01`.

[![](https://image.modcdn.io/members/63c0/31088933/profilehair/cc_01.png)](https://image.modcdn.io/members/63c0/31088933/profilehair/cc_01.png)

## Setting Up Heads, Hair, Beards, and Tails

For heads, hair, beards, and tails on **existing races**, you only need run a new CC icon render. If you’re not interested in the backend details, skip ahead to the **Rendering Icons** section towards the end of this guide.

> This section assumes that you have already set up your new assets. For a step-by-step walkthrough of how to import and set up new hair or beards, please see [**Hair and Beards - Part 1: Assets**](https://mod.io/g/baldursgate3/r/hair-and-beards-part-one).

The spawn and camera triggers in the **SYS\_IconGeneration\_A** level are all linked to a mannequin.

### Understanding the Triggers

The triggers use these naming conventions:

- Spawn trigger: **GeneratePortraitTrigger** \+ **\_%SlotName%**
  - **GeneratePortraitTrigger**: This is what is set up in the mannequin's template (see below).

  - **\_%SlotName%**: e.g. `_Head`, `_Beard`

  - Examples:
    - `Icon_CC_HalfElves_Female_Head`

    - `Icon_CC_Dragonborn_Male_Grey_DragonbornTop`
- Camera trigger: **Camera\_ + GetGeneratePortraitTrigger** \+ **\_%SlotName%**
  - **GeneratePortraitTrigger**: This is what is set up in the mannequin's template (see below).

  - **\_%SlotName%**: e.g. `_Head`, `_Beard`

  - Examples:
    - `Camera_Icon_CC_HalfElves_Female_Head`

    - `Camera_Icon_CC_Dragonborn_Male_Grey_DragonbornTop`

The **GeneratePortraitTrigger** can be found in the Sidebar of the mannequin’s root template in the Root Templates Manager (“Portrait Generation Trigger”).

[![](https://image.modcdn.io/members/63c0/31088933/profilecreate/cc_02.png)](https://image.modcdn.io/members/63c0/31088933/profilecreate/cc_02.png)

### Template Setup

To set up which mannequin template or body to render the visuals with, in the UUID Object Editor, navigate to **Shared** \> **Character Creation** \> **CharacterCreationIconSettings**.

[![](https://image.modcdn.io/members/63c0/31088933/profilecreate/cc_03.png)](https://image.modcdn.io/members/63c0/31088933/profilecreate/cc_03.png)

Here, paste the mannequin's UUID into the **RootTemplate** column. In **SlotNames**, select which slots the template should render with. The **Comment** column is used to distinguish records.

## Setting Up Tattoos, Makeup, Draconic Scales, and Scars

These icons have a different setup. Tattoos can be on either side of the face, so we need multiple cameras.

In these cases, we need to specify which mannequin to use, and also which camera. The triggers and camera are linked to the combination of the two.

[![](https://image.modcdn.io/members/63c0/31088933/profilecreate/cc_04.png)](https://image.modcdn.io/members/63c0/31088933/profilecreate/cc_04.png)

### Understanding the Trigger Setup

The triggers to render icons use these naming conventions:

- Spawn trigger: **GeneratePortraitTrigger** \+ **\_%MaterialType%**
  - **GeneratePortraitTrigger:** This is what is set up in mannequin's template (see below).

  - **\_%MaterialType%**: The MaterialType for existing assets can be found under Shared > Character Creation > CharacterCreationAppearanceMaterials in Column D, e.g. `_Tattoo`, `_Makeup`

  - Example:
    - `Icon_CC_Human_Male_Grey_Tattoo`
- Camera trigger: **%MaleCameraName% + \_+ GetGeneratePortraitTrigger** \+ **\_%MaterialType%**
  - **%MaleCameraName%:** The MaleCameraName and FemaleCameraName for existing assets can be found under Shared > Character Creation > CharacterCreationAppearanceMaterials in Columns H and J.

  - **GeneratePortraitTrigger:** This is what is set up in mannequin's template (see below).

  - **\_%MaterialType%**: The MaterialType for existing assets can be found under Shared > Character Creation > CharacterCreationAppearanceMaterials in Column D, e.g. `_Tattoo`, `_Makeup`

  - Example:
    - `Camera_01_Icon_CC_Human_Male_Grey_Tattoo`

The **GeneratePortraitTrigger** can be found in the Sidebar of the mannequin’s root template in the Root Templates Manager (“Portrait Generation Trigger”).

[![](https://image.modcdn.io/members/63c0/31088933/profilecreate/cc_05.png)](https://image.modcdn.io/members/63c0/31088933/profilecreate/cc_05.png)

### Template Setup

For these icons, we need to specify which mannequin needs to be used, as well as which camera. Both of these are defined in the **CharacterCreationAppearanceMaterials** table in the UUID Object Editor.

You can find this file for existing assets in Shared > Character Creation > CharacterCreationAppearanceMaterials.

[![](https://image.modcdn.io/members/63c0/31088933/profilecreate/cc_06.png)](https://image.modcdn.io/members/63c0/31088933/profilecreate/cc_06.png)

Under the **MaleRootTemplate** and **FemaleRootTemplate** columns, fill in the mannequin roots for the male and female mannequins. Under **MaleCameraName** and **FemaleCameraName**,specify which camera to use.

### Dragonborn Makeup

Dragonborn and non-dragonborn makeup uses the same entries in the UUID Object Editor. However, for dragonborn characters, you will need to fill in the **DragonbornMaleRootTemplate** and **DragonbornFemaleRootTemplate** fields in the **CharacterCreationAppearanceMaterials** table with their two respective mannequin root template UUIDs.

[![](https://image.modcdn.io/members/63c0/31088933/profilecreate/cc_07.png)](https://image.modcdn.io/members/63c0/31088933/profilecreate/cc_07.png)

Because we’re not specifying a new camera for Dragonborn makeup in the UUID Object Editor above, the naming convention for the relevant camera in the icon generation level is a little different.

The camera has `DGB_` in front of it. The spawn trigger remains the same.

- Example camera trigger: `DGB_Camera_01_Icon_CC_Dragonborn_Female_Grey_Makeup`

- Example spawn trigger: `Icon_CC_Dragonborn_Female_Grey_Makeup`


[![](https://image.modcdn.io/members/63c0/31088933/profilecreate/cc_08a.png)](https://image.modcdn.io/members/63c0/31088933/profilecreate/cc_08a.png)

[![](https://image.modcdn.io/members/63c0/31088933/profilecreate/cc_08b.png)](https://image.modcdn.io/members/63c0/31088933/profilecreate/cc_08b.png)

## Setting Up Dragonborn Attachments

The dragonborn attachments, e.g. their special chins and crests, are unique for each head. This makes it impossible to render all of them on the same mannequin, as some of them will clip with the head.

### Template Setup

The root templates for existing assets can be found in the **CharacterCreationIconSettings** file in the UUID Object Editor under Shared > Character Creation > CharacterCreationIconSettings.

**RootTemplate**, in column C, specifies the root template of the mannequin that should be used.

**HeadAppearanceUUID**, in column F, specifies the UUID of the head VisualResource used by the root template.

[![](https://image.modcdn.io/members/63c0/31088933/profilecreate/cc_09.png)](https://image.modcdn.io/members/63c0/31088933/profilecreate/cc_09.png)

Let’s take Row 31 of CharacterCreationIconSettings pictured above as an example.

The root template for this entry is `0da40707-4d75-4408-b185-e38f9e5830f0`. Using the Root Templates Manager panel, let’s search for that UUID.

[![](https://image.modcdn.io/members/63c0/31088933/profilecreate/cc_10.png)](https://image.modcdn.io/members/63c0/31088933/profilecreate/cc_10.png)

It returns `Dragonborn_Male_Mannequin_Head_D`. Right-click on that root template and select **Create new from selected**. You can delete this root template later; it is just so that you can view the character visuals. In this case, the new copy is named `TEMP_Dragonborn_Male_Mannequin_Head_D`.

[![](https://image.modcdn.io/members/63c0/31088933/profilecreate/cc_11.png)](https://image.modcdn.io/members/63c0/31088933/profilecreate/cc_11.png)

Click on the copy of the root template to view it in the Sidebar, then click on the “…” button by the Character Visual Resource parameter to open the **Character Editor**.

[![](https://image.modcdn.io/members/63c0/31088933/profilecreate/cc_12.png)](https://image.modcdn.io/members/63c0/31088933/profilecreate/cc_12.png)

The Character Editor looks like this:

[![](https://image.modcdn.io/members/63c0/31088933/profilecreate/cc_13.png)](https://image.modcdn.io/members/63c0/31088933/profilecreate/cc_13.png)

In the left panel, click the **Head** tab to see which head asset is being used.

[![](https://image.modcdn.io/members/63c0/31088933/profilecreate/cc_14.png)](https://image.modcdn.io/members/63c0/31088933/profilecreate/cc_14.png)

We can now see that `DGB_M_NKD_Head_D_Mannequin` is being used. We’ll want to find that head’s UUID - not the mannequin version, but the “real” version. We’ll therefore use the `DGB_M_NKD_Head_D` portion to search.

Click back to the main editor view and go to the Resource Manager. Select the “All” folder. Into the filter bar, paste the` _Mannequin`-less name: `DGB_M_NKD_Head_D`. Filter out everything but VisualResources.

[![](https://image.modcdn.io/members/63c0/31088933/profilecreate/cc_15.png)](https://image.modcdn.io/members/63c0/31088933/profilecreate/cc_15.png)

In the resulting list, find the VisualResource whose name matches. Right click on this VisualResource, and select **Copy GUID to Clipboard**. In this case, that’s `d454e061-e6ac-1d87-98da-f8da7c8a252d`.

[![](https://image.modcdn.io/members/63c0/31088933/profilecreate/cc_16.png)](https://image.modcdn.io/members/63c0/31088933/profilecreate/cc_16.png)

**Why do we need this original VisualResource’s GUID?** This is the resource that’s used to set up the link between the Dragonborn head and the Dragonborn attachments in the UUID Object Editor.

Let’s go back to the UUID Object Editor and open an existing **CharacterCreationAppearanceVisuals** table, from SharedDev >Character Creation > CharacterCreationAppearanceVisuals.

Using `Ctrl+F` to open the local search in the UUID Object Editor, paste the GUID value from earlier, and press Enter to search. It should return a single result, found in row 1 of the table.

[![](https://image.modcdn.io/members/63c0/31088933/profilecreate/cc_17.png)](https://image.modcdn.io/members/63c0/31088933/profilecreate/cc_17.png)

Now, let’s note the UUID from column A of that row: `7c538187-8c7f-4557-b850-e41a870c394b`

Go back to the **CharacterCreationIconSettings** file in Shared, and back to row 31, where we started this investigation. We can see that the UUID matches the contents of row 31’s column F.

[![](https://image.modcdn.io/members/63c0/31088933/profilecreate/cc_18.png)](https://image.modcdn.io/members/63c0/31088933/profilecreate/cc_18.png)

#### “No Attachment” Icon

The “no attachment” icon needs to be set up individually for each head, and needs an entry in the **TextureEntryPart** column of **CharacterCreationAppearanceVisuals**. This is used to tell them apart in code. Otherwise, all 4 entries will have the same name and thus only have 1 icon for the “no attachment” option across all heads.

[![](https://image.modcdn.io/members/63c0/31088933/profilecreate/cc_19.png)](https://image.modcdn.io/members/63c0/31088933/profilecreate/cc_19.png)

[![](https://image.modcdn.io/members/63c0/31088933/profilecreate/cc_20.png)](https://image.modcdn.io/members/63c0/31088933/profilecreate/cc_20.png)

The above examples are from SharedDev > Character Creation > CharacterCreationAppearanceVisuals.

## How Does All This Work Together?

We cycle through the mannequins (templates) in these tables and through the appearance visuals defined in **CharacterCreationSharedVisuals** and **CharacterCreationAppearanceVisuals**.

For each appearance, we check if its slot should be rendered with a template. If an appearance’s body type and race corresponds to a template’s body type and race, it will be rendered. Otherwise, it will be skipped.

## Rendering Icons

For new assets on existing races, you only need to make sure that the **CharacterCreationAppearanceVisuals** are correctly defined. This is covered for Hair and Beards in the relevant guide: [**Hair and Beards - Part 2: Character Creation**](https://larianstudios.atlassian.net/wiki/spaces/GUS/pages/3737780225).

> **WARNING:** Generating CC icons will regenerate _all_ CC icons, and therefore take quite some time.

In the main editor, go to Project > Render CC Icons.

[![](https://image.modcdn.io/members/63c0/31088933/profilecreate/cc_21.png)](https://image.modcdn.io/members/63c0/31088933/profilecreate/cc_21.png)

If you have not already loaded the correct level, `SYS_IconGeneration_A`, you will be asked if you want to load the booth level. Say “Yes”.

[![](https://image.modcdn.io/members/63c0/31088933/profilecreate/cc_22.png)](https://image.modcdn.io/members/63c0/31088933/profilecreate/cc_22.png)

Once the generation process starts, you will see a progress bar in the lower right corner of the game window.

[![](https://image.modcdn.io/members/63c0/31088933/profilecreate/cc_23.png)](https://image.modcdn.io/members/63c0/31088933/profilecreate/cc_23.png)

Wait patiently until the generation completes. Once done, the progress bar will disappear.

## Troubleshooting

### After generating CC icons, all of them turned invisible

A fix for this is in progress. In the meantime, if you encounter this, you can revert by deleting a couple files from inside your /Data/Public/\[yourmodname\]/ folder:

- Folder: `/Content/[PAK]_Generated_...`
- .dds File: `/Assets/Textures/Icons/Generated_..._CCIcons.dds`
- .lsx File: `/CharacterCreation/Generated_CCIcons.lsx`

[G\\
\\
GrumpyWashbear](https://mod.io/g/baldursgate3/u/grumpywashbear/r)

Follow GrumpyWashbear

Log in to join the discussion!

[T](https://mod.io/g/baldursgate3/u/kuranosh)

[Tabble\_Dabble](https://mod.io/g/baldursgate3/u/kuranosh)• [257d ago](https://mod.io/g/baldursgate3/r/generating-icons-for-character-creation#1309666 "4/17/2025, 05:07 PM GMT-4")

This video is very helpful if like me you don't do as well learning textually.

Generating Character Creation Icons with the Toolkit - BG3 Toolkit - YouTube

[Photo image of Padme4000](https://www.youtube.com/channel/UC9f4ab5N5qVijYA8G96CXRg?embeds_referring_euri=https%3A%2F%2Fmod.io%2F)

Padme4000

2.27K subscribers

[Generating Character Creation Icons with the Toolkit - BG3 Toolkit](https://www.youtube.com/watch?v=52a9OJ2N66I)

Padme4000

Search

Watch later

Share

Copy link

Info

Shopping

Tap to unmute

If playback doesn't begin shortly, try restarting your device.

More videos

## More videos

You're signed out

Videos you watch may be added to the TV's watch history and influence TV recommendations. To avoid this, cancel and sign in to YouTube on your computer.

CancelConfirm

Share

Include playlist

An error occurred while retrieving sharing information. Please try again later.

[Watch on](https://www.youtube.com/watch?v=52a9OJ2N66I&embeds_referring_euri=https%3A%2F%2Fmod.io%2F)

0:00

0:00 / 9:56

•Live

•

Last updated

1y

Reading time

9 min read

Views

4,311

Comments

1

[G\\
\\
GrumpyWashbear](https://mod.io/g/baldursgate3/u/grumpywashbear/r)

Follow GrumpyWashbear

- [Guide](https://mod.io/g/baldursgate3/r/generating-icons-for-character-creation#guide)
- [General Booth Setup](https://mod.io/g/baldursgate3/r/generating-icons-for-character-creation#heading-1)
- [Setting Up Heads, Hair, Beards, and Tails](https://mod.io/g/baldursgate3/r/generating-icons-for-character-creation#heading-2)
- [Understanding the Triggers](https://mod.io/g/baldursgate3/r/generating-icons-for-character-creation#heading-3)
- [Template Setup](https://mod.io/g/baldursgate3/r/generating-icons-for-character-creation#heading-4)
- [Setting Up Tattoos, Makeup, Draconic Scales, and Scars](https://mod.io/g/baldursgate3/r/generating-icons-for-character-creation#heading-5)
- [Understanding the Trigger Setup](https://mod.io/g/baldursgate3/r/generating-icons-for-character-creation#heading-6)
- [Template Setup](https://mod.io/g/baldursgate3/r/generating-icons-for-character-creation#heading-7)
- [Dragonborn Makeup](https://mod.io/g/baldursgate3/r/generating-icons-for-character-creation#heading-8)
- [Setting Up Dragonborn Attachments](https://mod.io/g/baldursgate3/r/generating-icons-for-character-creation#heading-9)
- [Template Setup](https://mod.io/g/baldursgate3/r/generating-icons-for-character-creation#heading-10)
- [“No Attachment” Icon](https://mod.io/g/baldursgate3/r/generating-icons-for-character-creation#heading-11)
- [How Does All This Work Together?](https://mod.io/g/baldursgate3/r/generating-icons-for-character-creation#heading-12)
- [Rendering Icons](https://mod.io/g/baldursgate3/r/generating-icons-for-character-creation#heading-13)
- [Troubleshooting](https://mod.io/g/baldursgate3/r/generating-icons-for-character-creation#heading-14)
- [After generating CC icons, all of them turned invisible](https://mod.io/g/baldursgate3/r/generating-icons-for-character-creation#heading-15)
- [Discussion](https://mod.io/g/baldursgate3/r/generating-icons-for-character-creation#discussion)

[Beards](https://mod.io/g/baldursgate3/r?tags=Beards) [Character Creation](https://mod.io/g/baldursgate3/r?tags=Character+Creation) [Editor](https://mod.io/g/baldursgate3/r?tags=Editor) [English](https://mod.io/g/baldursgate3/r?tags=English) [Hair](https://mod.io/g/baldursgate3/r?tags=Hair) [Official](https://mod.io/g/baldursgate3/r?tags=Official)

A general explanation of how the Character Creation (CC) icons are generated, and how the booth level for them is set up.

Share

Report guide

---
# SOURCE: https://mod.io/g/baldursgate3/r/adding-a-new-spell-projectile
---

[Browse games](https://mod.io/g)

Browse games

[My library](https://mod.io/library)

My library

[My content](https://mod.io/content)

My content

My account

mod.io

mod.io

[All games](https://mod.io/g) [Baldur's Gate 3](https://mod.io/g/baldursgate3) [Guides](https://mod.io/g/baldursgate3/r) [English](https://mod.io/g/baldursgate3/r?tags=English) Adding a New Spell (Projectile)

Adding a New Spell (Projectile)

Share

Report

Follow

This guide assumes that you have basic familiarity with creating a spell using the Stats and UUID Editors. If not, please first consult the [**Adding a New Spell (Simple)**](https://mod.io/g/baldursgate3/r/adding-a-new-spell-basic) guide.

## Making a Projectile Spell

By the end of this tutorial, we will have made a projectile spell that navigates around objects, like Magic Missile, and creates a tressym summon at the target location.

First, open the Stats Editor and create a new Projectile file under SpellData in your mod. In this tutorial, our mod is called `NewProjectileSpell`.

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/adv01.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/adv01.png)

Let’s open that new Projectile file and start filling in data for our new spell.

> You can hide columns in the Stats Editor by right-clicking on the column names and selecting “Hide\\Show columns”. In the sub-menu, you can deselect columns you don’t want to see.
>
> [![](https://image.modcdn.io/members/63c0/31088933/profilespells/adv02.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/adv02.png)
>
> You can re-enable the visibility of these columns via the same menu, or enable all columns at once by selecting “Show all columns”.
>
> In the screenshots shown in this guide, some columns have been hidden to make it easier to see the relevant cells.

### Name

The Name you set here will become part of the TechName of the spell.

This field:

- Does not accept spaces

- Accepts underscores `_` (often used in lieu of spaces)

- Accepts numbers and uppercase and lowercase letters


For the spell in this tutorial, we’ll use the TechName `MagicMissile_Tressym`.

> It’s important to note that the Name you see here is **not how the spell is referenced elsewhere!**
>
> We almost always use the TechName to refer to a spell. The TechName is simply `<type>_<name>`, where `<type>` is the table that the spell comes from (e.g. `Projectile`, `Target`), and `<name>` is what appears in the Name column in the SpellData (e.g. `MagicMissile_Tressym`).
>
> So, for this example, the TechName we would use elsewhere in the Toolkit to refer to this spell would be `Projectile_MagicMissile_Tressym`.

### Level and SpellSchool

If you want your spell to show up as part of a specific level (Cantrip, Level 1, etc.) or spell school (Evocation, Divination, Necromancy, etc.), fill out the **Level** and **SpellSchool** fields. Technically, these are not required, and mostly affect the information displayed in the tooltip.

#### Effect on Tooltips

For example, this is the default Fire Bolt tooltip:

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/adv03.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/adv03.png)

But this is how that same spell looks if the **Level** and **SpellSchool** fields are left blank:

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/adv04.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/adv04.png)

Note that above, it still says “Cantrips”. This is because the **SpellFlags** field still has “IsSpell” checked. If you check “IsSpell” but don’t define a **Level**, the spell will default to “Cantrips” in the tooltip.

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/adv05.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/adv05.png)

However, if “IsSpell” is unchecked, the tooltip will no longer show “Cantrips”.

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/adv06.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/adv06.png)

If both **Level** and **SpellSchool** are left blank, and "IsSpell" isn't checked in **SpellFlags**, your spell will be called a “Class Action”.

#### Level

The **Level** field accepts numbers.

- 0 = Cantrip

- 1 = Level 1 spell

- 2 = Level 2 spell, etc.


We’ll set our new Projectile spell’s **Level** to `0`, making it a Cantrip.

#### SpellSchool

The **SpellSchool** field is a dropdown of the existing spell schools in the game.

We’ll use `Conjuration` for our new spell.

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/adv07.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/adv07.png)

### SpellProperties

For this new spell, we want the tressym to always be summoned at the target location. This means we don't want to use **SpellRoll**, **SpellSuccess** or **SpellFail**, as those have a chance of failure.

Instead, we’ll use the **SpellProperties** field, which will execute each time the spell is cast.

Let’s use the `Summon()` functor. The Summon() functor has a few parameters to fill in.

`Summon(<template uuid>, <lifetime>, <spell override for ai>, <extendConcentration>, <stack id>, <status to be applied once it spawns>)`

> Technically, the Summon() functor has even more parameters -- we're just not using them for this example! Only **<template uuid>** is absolutely required, but at minimum you should also include **<lifetime>**. Without **<lifetime>**, your creature will only be summoned for 1 turn in Forced Turn-Based Mode (FTB), and auto-killed outside of FTB.
>
> The full list of parameters for Summon() is:
>
> `Summon(<template uuid>, <lifetime>, <spell override for ai>, <extendConcentration>, <stack id>, <status to be applied once it spawns>, <status2>, <status3>, <status4>, <lateJoinPenalty>, <UseCasterPassives>)`

Let’s have a look at these parameters and how to fill them in correctly.

#### Summon: <template uuid>

> To be able to see the Root Templates list, we must have a level loaded in the Editor. The easiest way to do this is to go to `File -> Load Level...` and select `Basic_Level_A.`

First, we’ll need to put in the GUID of the creature we’re summoning – in this case, a tressym. Go to the Root Templates panel on the main screen of the Editor.

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/adv08.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/adv08.png)

We can use the search bar to find the tressym’s root template.

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/adv09.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/adv09.png)

In the filtered list, click on **\[WIP\] Cat\_Tressym**. You should see the model appear in the Preview box on the right.

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/adv10.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/adv10.png)

Right-click on **\[WIP\] Cat\_Tressym**, and select “Copy GUID to clipboard”.

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/adv11.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/adv11.png)

Paste the resulting GUID into the Summon() functor, inside the **SpellProperties** field, like so: `Summon(04975002-a4ac-4eac-beae-7b44c939c354)`. You now have the template UUID filled in.

#### Summon: <lifetime>

This parameter determines the lifetime of the summon. It takes whole numbers, which indicate how many rounds it will be active for.

- `3` will make the summon last for 3 rounds.

- `-1` will make the summon last until a Long Rest.


For our example, we’ll use `-1`. Add that to the Summon() functor.

Our Summon() functor should now look like this: `Summon(04975002-a4ac-4eac-beae-7b44c939c354,-1)`.

#### Summon: <spell override for ai>

This is usually not used for player spells – it’s purely for the AI when doing spell calculations. We’ll leave this blank by just adding a comma, like so: `Summon(04975002-a4ac-4eac-beae-7b44c939c354,-1,)`.

> If you were to use the above Summon() in its current state, you would have to remove the last `,`. We’re adding the `,` now because we will be filling in more parameters after it.

#### Summon: <extendConcentration>

Extended concentration is rarely used in Baldur’s Gate 3. If a player is already concentrating on a summon, and they cast the same concentration spell, using this parameter will extend the length of the concentration.

Like with <spell override for ai>, we’ll leave this blank, but we need to make sure to add `,` after the previous parameter, like so: `Summon(04975002-a4ac-4eac-beae-7b44c939c354,-1,,)`.

#### Summon: <stack id>

The Stack ID is used to keep track of the summon active on a player. This is what prevents a player from having multiple Find Familiars active at once.

If something with the same Stack ID is cast by the player, it will remove the original in favour of the new cast.

The Stack ID can be any string you choose, so long as the Stack IDs used by different spells are unique. In our example, we will use `Tressym` as the Stack ID. Put the Stack ID inside quotes (`''`) when adding it to the functor, like so: `Summon(04975002-a4ac-4eac-beae-7b44c939c354,-1,,,'Tressym')`.

#### Summon: <status to be applied once it spawns>

If you want a creature to have a specific status active on them when summoned, you can add it here. These statuses are **permanent** and will last for the summon’s entire lifetime.

You can choose any Status\_BOOST to use here; existing Statuses can be found in **Shared > StatusData**, but of course you are welcome to make your own.

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/adv12.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/adv12.png)

To serve as an example, let’s give our summoned tressym the Bless status. Open **Shared > StatusData > Status\_BOOST** and search for “BLESS”. In the matching row, confirm the Name in column A - this is what we’ll use in the Summon() functor.

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/adv14.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/adv14.png)

Our full Summon() functor should now look like this: `Summon(04975002-a4ac-4eac-beae-7b44c939c354,-1,,,'Tressym',BLESS)`.

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/adv13.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/adv13.png)

#### Adjusting the Summon() Functor

If you were to try out the Summon() functor as written so far, you would find that the spell won’t work as expected because it will look for a target to affect, but it won’t consider the ground a valid target.

Because the intent of this spell is to spawn the tressym on the ground, we need the ground to be a valid target for the Summon. We can fix this by adding `GROUND:` in front of the whole Summon() functor: `GROUND:Summon(04975002-a4ac-4eac-beae-7b44c939c354,-1,,,'Tressym',BLESS)`.

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/adv15.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/adv15.png)

> `GROUND:` is added to functors when the player is expected to target the ground to make something happen. Without this, the player can click on the ground to cast the spell, but nothing will happen.

### TargetConditions

The **TargetConditions** field determines who or what the caster can cast the spell on. For example, if we type `Self()`, the player would need to select themselves to cast the spell.

Because we want the tressym to be summoned on the ground at the specific location the player chooses, we will need to use `CanStand()`. Unlike `GROUND:`, this checks that the character (in this case, the tressym) has enough space on the ground to be created there.

This will again require the tressym GUID that you copied for the Summon() earlier: `04975002-a4ac-4eac-beae-7b44c939c354`.

Unlike Summon(), CanStand() requires quotes (`''`) around the GUID, like so: `CanStand('04975002-a4ac-4eac-beae-7b44c939c354')`.

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/adv16.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/adv16.png)

### Trajectories

Trajectories determine the spell’s pathfinding and apply the spell’s visuals. You can make your own trajectory in the Root Templates Manager by creating a Projectile. You can find more [**documentation about Projectiles here**](https://larianstudios.atlassian.net/wiki/spaces/GUS/pages/3820421121).

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/adv17.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/adv17.png)

For this tutorial, we’ll stick to using an existing trajectory. Projectile spells are the only ones that use trajectories, so let’s open the existing Projectile file in **Shared** to find one we can use.

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/adv18.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/adv18.png)

Find **MagicMissile** on row 70.

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/adv19.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/adv19.png)

Scroll sideways to the **Trajectories** column (AB), and copy the contents of the cell:

`348013df-7958-4ca9-ac9f-80337e054bee,7bff57fa-fd21-4ab3-9384-83fb14237690`

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/adv20.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/adv20.png)

Paste that value into the **Trajectories** field of our new `MagicMissile_Tressym` spell.

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/adv21.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/adv21.png)

### Icon, DisplayName, Description

These columns are used to fill in the tooltip for the spell so the player understands what the spell does.

#### Icon

The icon is what will show up on the hotbar and in other UI elements. You can learn how to add new icons for spells by following the guide [**here**](https://mod.io/g/baldursgate3/r/adding-skill-and-item-icons), but for the purposes of this tutorial, we’ll use an existing icon.

Open the Texture Atlas Editor from the Editor’s main toolbar.

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/adv22.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/adv22.png)

The Texture Atlas Editor might open fairly small at first – feel free to resize it.

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/adv23.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/adv23.png)

Click on the **Open** icon on the Texture Atlas Editor’s toolbar, or go to `File > Open`. Navigate to `...\Data\Public\Shared\GUI\`. You should see some `.lsx` files here. These are the existing icon texture atlases. Select `Icons_Skills.lsx` and open it in read-only mode.

The Texture Atlas Editor should now show a multitude of icons on the right, and a list of corresponding **TechNames** on the left.

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/adv24.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/adv24.png)

Since we are looking for something tressym-like, let’s use the bottom search bar to filter our results. Type `Cat` into the search bar.

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/adv25.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/adv25.png)

This will filter for icons that have “Cat” in their TechName.

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/adv26.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/adv26.png)

If you click on one of the names, for example `Skill_Druid_Wildshape_Cat`, you will see the matching icon on the right gain a red overlay. You may need to resize the Texture Atlas Editor window to see the icon.

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/adv27.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/adv27.png)

Let’s use the `Skill_Druid_WildShape_Cat` icon. Right-click on the name of the icon in the list and select “Copy name to clipboard”.

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/adv28.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/adv28.png)

Return to the Stats Editor, and in the **Icon** column for your spell, paste the TechName you just copied.

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/adv29.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/adv29.png)

#### Display Name, Description

These fields are for the name and description that appear in the in-game tooltip. For this example, we’ll use the following text:

- **DisplayName**: `The Magnificent Meowser`

- **Description**: `Conjure forth a tressym.`


Because our spell is mostly just summoning a tressym, we don't need to fill out the other description or tooltip fields, like **ExtraDescription** or **TooltipDamageList**.

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/adv30.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/adv30.png)

When using Summon(), a status will be added automatically to the tooltip to indicate that a creature is part of the spell.

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/adv31.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/adv31.png)

### CastTextEvent

We only want to execute one cast event, so we will just write Cast in the **CastTextEvent** column.

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/adv32.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/adv32.png)

> Multiple Cast events are mostly used for Multiattack spells - if you were to use these, you’d want to fill out AlternativeCastTextEvents with the additional casts, `Cast2;Cast3;Cast4`, as seen below. Please note that even with multiple Casts, there is no “Cast1” - `Cast` is already treated like Cast1.
>
> [![](https://image.modcdn.io/members/63c0/31088933/profilespells/adv33.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/adv33.png)

### UseCosts

Because our spell is a Conjuration cantrip, we won't need to add a spell slot cost to this spell. Instead, we will use `ActionPoint:1`. This means using our spell will cost an Action Point.

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/adv34.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/adv34.png)

### Spell Animation

For **Spell Animation**, we will once again borrow an existing set. Since we already borrowed the Magic Missile trajectory, let’s also use Magic Missile’s Spell Animation.

Open the **Projectile** file in Shared again, and find Magic Missile’s Spell Animation (column BL). Copy and paste the contents of the cell into our new spell’s.

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/adv35.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/adv35.png)

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/adv36.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/adv36.png)

### SpellFlags

Here, we’ll select a few flags to make sure our spell behaves as intended.

- `HasVerbalComponent`: Spells with this flag will become unusable if the caster is Silenced.

- `HasSomaticComponent`: Spells with this flag require somatics to be cast.

- `IsSpell`: This tells the engine that our skill is a spell. If this is unchecked, it will instead be treated as a Class Action.

- `HasHighGroundRangeExtension`: See below.

- `RangeIgnoreVerticalThreshold`: See below.


`HasHighGroundRangeExtension`and `RangeIgnoreVerticalThreshold` are a little more complex.

These are used with spells meant to be cast from higher elevation/ground, especially with projectiles that have a direct path to the enemy. These flags help adjust the spell range to match what would happen if the player had cast on a flat surface to an enemy in front of them.

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/adv37.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/adv37.png)

### PrepareEffect, CastEffect

These fields tell the engine which VFX to play for the Prepare and Cast portions of the spell.

For more information on spell effects, please refer to the [**Adding a New Spell (Basic)**](https://mod.io/g/baldursgate3/r/adding-a-new-spell-basic) guide, or, if you’re interested in making your own effects, check out the [**VFX guides**](https://mod.io/g/baldursgate3/r/vfx-part-1-making-the-effect). For this example, we’ll grab an existing effect from, you guessed it, Magic Missile.

Magic Missile only has a **PrepareEffect** and **CastEffect**, so we’ll plug those same effects into our own spell, into the `PrepareEffect` and `CastEffect` columns.

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/adv38.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/adv38.png)

### PrepareSound, PrepareLoopSound, CastSound, VocalComponentSound

These fields are how we apply sound effects to our spells. They are optional, but your spell will be silent without them.

Creating new sounds is not supported in the Toolkit, so we recommend looking for a similar spell and copying its values to your new spell. In this example, we will once again copy from Magic Missile:

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/adv39.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/adv39.png)

## Testing Our Spell

Make sure to save your changes!

With all these fields populated, we have enough to test our spell in-game. Make sure you’ve saved all your changes, and close the Stats Editor. In the main Editor, make sure you have `Basic_Level_A` loaded, then enter Game Mode.

In-game, open the debug Console Window with `Ctrl+Shift+F11`. To prevent accidentally triggering the other hotkeys, make sure to click into the text field of the Console Window to focus there.

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/adv40.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/adv40.png)

In this input field, type `addDebugSpell` and press space. You will see a list on the right of all the possible spell options. You can use the bottom right corner of the Console Window to expand the whole window, and the line separating the left and right to adjust the right panel’s width.

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/adv41.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/adv41.png)

Remember how, earlier in this guide, we talked about the **TechName** of the spell? Even though our spell’s name is `MagicMissile_Tressym`, that’s not how it’s referenced inside the engine. Because the spell is a Projectile-type spell and originates from that table, its Tech Name is actually `Projectile_MagicMissile_Tressym`. That’s the name we’ll want to type into this console.

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/adv42.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/adv42.png)

You can also type enough of the name to narrow down the results in the right-hand panel, and just click on the name there instead.

Press **Enter** to run the command, and close the Console Window.

The spell should have been added to the character’s hotbar.

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/adv43.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/adv43.png)

> If the spell doesn’t get added to the character’s hotbar, the first method of troubleshooting is always to save your work, and then close and reopen the Editor. If the spell is still not getting added after reopening and repeating the above testing steps, then it’s probably an issue with the spell data itself.

If you’ve followed the steps above, you should see everything correctly displayed on the tooltip. Now, let’s dive a bit deeper into how we verify the core functionality.

### Trajectory

For this screenshot below, we’ve loaded into Act 1's Blighted Village. As you can see, when casting the spell, the path is able to bend around the furniture and the walls instead of running straight into the wall. This is due to the **Trajectory** we used.

You can learn more about Trajectories in the [**official documentation**](https://mod.io/g/baldursgate3/r/documentation-projectiles).

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/adv44.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/adv44.png)

### Spell Animation, PrepareEffect, CastEffect

The **Prepare** state is when the player has selected a spell, but not yet selected a target. Below, we can see that Gale has an animation, as well as a **PrepareEffect**.

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/adv45.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/adv45.png)

### Summon()

When the spell is cast, we should see a tressym appear. The tressym's portrait is also attached to Gale’s portrait on the party tracker. This is correct behaviour for a summon.

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/adv46.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/adv46.png)

### StackID

When we cast the spell a second time, we can see the original tressym being removed, and a new one being added beside Gale’s portrait. This is correct behaviour based on how we’ve set the StackID.

[![](https://image.modcdn.io/members/63c0/31088933/profilespells/adv47.png)](https://image.modcdn.io/members/63c0/31088933/profilespells/adv47.png)

## What Next?

Congratulations on making a new projectile spell! Once you’ve got spell creation down, you can learn how to add spells to new or existing classes using the [**Adding New Classes or Subclasses**](https://mod.io/g/baldursgate3/r/adding-new-classes) guide.

[G\\
\\
GrumpyWashbear](https://mod.io/g/baldursgate3/u/grumpywashbear/r)

Follow GrumpyWashbear

Log in to join the discussion!

[D](https://mod.io/g/baldursgate3/u/andrewmoto)

[DistantEarth](https://mod.io/g/baldursgate3/u/andrewmoto)• [243d ago](https://mod.io/g/baldursgate3/r/adding-a-new-spell-projectile#1329967 "5/1/2025, 03:39 PM GMT-4")

I created projectile and zone cantrips and have tried changing the spell animations to 4 elements monk spell animations, but the result always ends up in the character standing still. For example, one of my spells uses the witch bolt animation. Is it possible to assign any monk animations to this?

[K](https://mod.io/g/baldursgate3/u/kingraithwall)

[KingRaithwall](https://mod.io/g/baldursgate3/u/kingraithwall)• [195d ago](https://mod.io/g/baldursgate3/r/adding-a-new-spell-projectile#1383772 "6/19/2025, 04:28 AM GMT-4")

I've had that same issue. The monk skill animations never work unless on a monk, which is weird.

[V](https://mod.io/g/baldursgate3/u/modiouser55970541)

[ViniMoraes](https://mod.io/g/baldursgate3/u/modiouser55970541)• [252d ago](https://mod.io/g/baldursgate3/r/adding-a-new-spell-projectile#1318653 "4/23/2025, 01:24 PM GMT-4")

Anyone knows how to add the character ability modifier to the duration of the summon? I've tried a couple of times, but I can't seem to get it done.

[A](https://mod.io/g/baldursgate3/u/atlas264)

[Atlas-](https://mod.io/g/baldursgate3/u/atlas264)• [333d ago](https://mod.io/g/baldursgate3/r/adding-a-new-spell-projectile#1194732 "1/31/2025, 02:42 PM GMT-5")

how did you get the spell to path around objects?
I've tried everything I can think of in the spell editor and it is always a straight line

[G](https://mod.io/g/baldursgate3/u/grimmjowjgrjack)

[Grimmjowjgrjack](https://mod.io/g/baldursgate3/u/grimmjowjgrjack)• [1y ago](https://mod.io/g/baldursgate3/r/adding-a-new-spell-projectile#1130839 "12/19/2024, 07:57 PM GMT-5")

Don't know who needs to know this but this but I figured out how you can do the additional dmg with level mapping.

Create row of level mapping for your normal dmg rolls 1d8 (i.e. lvl 1 - 1d8, lvl 2 - 1d8, lvl 3 - 2d8, etc)
Create another row of level mapping for you additional damage you want to add on (i.e. +2, +4, +6, etc) but you don't have to do the plus symbol just number.

In your SpellSuccess and TooltipDamageList it will look like this.
SpellSuccess: DealDamage(LevelMapValue(CBCantrip)+LevelMapValue(CBBase),Necrotic,Magical) or DealDamage(LevelMapValue(1stRowName)+LevelMapValue(2ndRowName),Necrotic,Magical)

TooltipDamageList: DealDamage(LevelMapValue(CBCantrip)+LevelMapValue(CBBase),Necrotic) or DealDamage(LevelMapValue(1stRowName)+LevelMapValue(2ndRowName),Necrotic)

Now you'll have a spell that scales with level and will display correct tool tip and do correct dmg rolls in example above: lvl 1 - 1d8+2, lvl 2 - 1d8+4, lvl 3 - 2d8+6

[S](https://mod.io/g/baldursgate3/u/stuwil)

[StuWil](https://mod.io/g/baldursgate3/u/stuwil)• [1y ago](https://mod.io/g/baldursgate3/r/adding-a-new-spell-projectile#1128916 "12/18/2024, 08:27 AM GMT-5")

Hi there, any chance you know where it is in the game files that relates spells' vocal components to the spells themselves? I do not mean the VocalComponentSound in the stats for a spell, as many spells do not use that. I know that changing the level and type of damage dealt of a spell will affect the vocal audio, but why and where does this take place in the files?

[G](https://mod.io/g/baldursgate3/u/grimmjowjgrjack)

[Grimmjowjgrjack](https://mod.io/g/baldursgate3/u/grimmjowjgrjack)• [1y ago](https://mod.io/g/baldursgate3/r/adding-a-new-spell-projectile#1124816 "12/14/2024, 04:28 PM GMT-5")

I'm trying to build a cantrip that scales in level. I saw it's tied to LevelMapValue. I can get it to scale in damage when using normal 1d8, 2d8, etc. but if I do 1d8+2 so the base damage is higher it no longer accepts the value. My only thought of a work around is to add and remove spells upon level up (if I knew the command for remove spell). Any pointer to get the +2 base damage to take or how to remove a spell i.e. AddSpells() but reverse option.

[W](https://mod.io/g/baldursgate3/u/waterwitch83)

[WaterWitch83](https://mod.io/g/baldursgate3/u/waterwitch83)• [1y ago](https://mod.io/g/baldursgate3/r/adding-a-new-spell-projectile#1114746 "12/5/2024, 11:33 PM GMT-5")

I'm using the cleric spell "Knowledge of the ages" as a guide for a new spell, but if I use the requirements logic for that spell then it lets me cast any of the spells even if I have proficiency in a specific skill. It of course does nothing except use up the spell. If I use the logic below then it doesn't let me cast any of the variant spells. Any ideas what I can do differently?

1\. Requirements used that doesn't allow any variant to be casted:
\\* not HasProficiencyBonus('Athletics',context.Source)
2\. Requirements used in knowledge of the ages (allows me to cast regardless of having proficiency or not):
\\* not HasProficiencyBonus(context.CheckedAbility,context.CheckedSkill,context.Source)

[W](https://mod.io/g/baldursgate3/u/waterwitch83)

[WaterWitch83](https://mod.io/g/baldursgate3/u/waterwitch83)• [1y ago](https://mod.io/g/baldursgate3/r/adding-a-new-spell-projectile#1115735 "12/6/2024, 11:40 PM GMT-5")

Got it working. Join the Larian Studios Discord channel! That's where I got my answer at least. :)

[W](https://mod.io/g/baldursgate3/u/waterwitch83)

[WaterWitch83](https://mod.io/g/baldursgate3/u/waterwitch83)• [1y ago](https://mod.io/g/baldursgate3/r/adding-a-new-spell-projectile#1094129 "11/20/2024, 07:23 AM GMT-5")

Is there a way to link spells so one triggers its effects separately from a second spell effect? I know there's the ApplyStatus route, but I'm not sure that would really apply in this situation but maybe I'm wrong. I'm trying to combine cleave with something like cone of cold. But I don't want to apply weapon damage to targets outside of melee weapon range nor do I want to limit the targets outside of melee weapon reach to just 3 targets.

[W](https://mod.io/g/baldursgate3/u/waterwitch83)

[WaterWitch83](https://mod.io/g/baldursgate3/u/waterwitch83)• [1y ago](https://mod.io/g/baldursgate3/r/adding-a-new-spell-projectile#1086503 "11/14/2024, 07:11 PM GMT-5")

So I'm playing around in the passives table and stumble across a ScaleMultiplier option under Boosts. It takes in a parameter, but I'm not finding anything that uses it. Anyone have any idea how to use it and what it's used for? I have an idea what it's used for, but would like to be certain.

[K](https://mod.io/g/baldursgate3/u/kingraithwall)

[KingRaithwall](https://mod.io/g/baldursgate3/u/kingraithwall)• [1y ago](https://mod.io/g/baldursgate3/r/adding-a-new-spell-projectile#1074940 "11/6/2024, 06:35 PM GMT-5")

I got to say. Your guides are all top tiers! I find myself reading your guides the most and they help me do what I want 100% of time. Thank you for taking the time to do all your guides. they helped so much.

[W](https://mod.io/g/baldursgate3/u/waterwitch83)

[WaterWitch83](https://mod.io/g/baldursgate3/u/waterwitch83)• [1y ago](https://mod.io/g/baldursgate3/r/adding-a-new-spell-projectile#1086509 "11/14/2024, 07:13 PM GMT-5")

Agreed! I came out here just the other day wondering what exactly GROUND was used for. I see it all the time in other spells. Yup, there it is! Right here in this guide. :D

[G](https://mod.io/g/baldursgate3/u/gawesome)

[Gawesome](https://mod.io/g/baldursgate3/u/gawesome)• [1y ago](https://mod.io/g/baldursgate3/r/adding-a-new-spell-projectile#1074760 "11/6/2024, 04:26 PM GMT-5")

I'm trying to port over a ton of spell data I already created pre-toolkit. The big issue I'm running into is that some things, like "PrepareEffect", won't take in GUIDs of existing effects, like this one: 60ec0a2d-1b72-4fb2-9eaf-571638aca25d.

Because it is a dropdown with descriptive names, I have no idea how to find the effect that matches the GUID. Does anyone know of an efficient way to solve this problem?

[G](https://mod.io/g/baldursgate3/u/gawesome)

[Gawesome](https://mod.io/g/baldursgate3/u/gawesome)• [1y ago](https://mod.io/g/baldursgate3/r/adding-a-new-spell-projectile#1074753 "11/6/2024, 04:24 PM GMT-5")

I can't seem to access the Confluence link you posted above about projectiles. After signing into confluence with my email, it said that I don't have access:

[https://larianstudios.atlassian.net/wiki/spaces/GUS/pages/3820421121](https://larianstudios.atlassian.net/wiki/spaces/GUS/pages/3820421121)

[M](https://mod.io/g/baldursgate3/u/modiouser3853684)

[megapatato](https://mod.io/g/baldursgate3/u/modiouser3853684)• [1y ago](https://mod.io/g/baldursgate3/r/adding-a-new-spell-projectile#1129632 "12/18/2024, 06:24 PM GMT-5")

Same, the Confluence thing seems to require membership in the Larian Studios organization.

[B](https://mod.io/g/baldursgate3/u/betatester)

[BetaTester](https://mod.io/g/baldursgate3/u/betatester)• [1y ago](https://mod.io/g/baldursgate3/r/adding-a-new-spell-projectile#1063355 "10/29/2024, 12:36 PM GMT-4")

Can you make a guide about adding abilities to the summons? I'm trying to make a summoners class thats based on Lo po Bia Traumerei? And thanks for the guide

[L](https://mod.io/g/baldursgate3/u/ladyfiur)

[LadyFiur](https://mod.io/g/baldursgate3/u/ladyfiur)• [1y ago](https://mod.io/g/baldursgate3/r/adding-a-new-spell-projectile#1046584 "10/19/2024, 01:16 PM GMT-4")

is there some documentation about the parameters for commands like ApplyStatus, RemoveStatus, SelectSpells, Summon, etc.?
I can find the usage in the editor, but would like to see the available parameters for each command.

[L](https://mod.io/g/baldursgate3/u/ladyfiur)

[LadyFiur](https://mod.io/g/baldursgate3/u/ladyfiur)• [1y ago](https://mod.io/g/baldursgate3/r/adding-a-new-spell-projectile#1051820 "10/22/2024, 12:57 PM GMT-4")

found it:
[https://github.com/Norbyte/lslib/blob/master/LSLibDefinitions.xml](https://github.com/Norbyte/lslib/blob/master/LSLibDefinitions.xml)

[T](https://mod.io/g/baldursgate3/u/tarrinofazinor)

[TarrinOfAzinor](https://mod.io/g/baldursgate3/u/tarrinofazinor)• [1y ago](https://mod.io/g/baldursgate3/r/adding-a-new-spell-projectile#1040616 "10/15/2024, 10:14 PM GMT-4")

I'm following the guide and attempting to open the suggested icon file in the texture atlas editor (path ending with ...\\Data\\Public\\Shared\\GUI\\) but I'm getting an error in the message log saying that it can't open the file 'Reason File belongs to a developer project.' Any ideas on how to work around this?

[L](https://mod.io/g/baldursgate3/u/ladyfiur)

[LadyFiur](https://mod.io/g/baldursgate3/u/ladyfiur)• [1y ago](https://mod.io/g/baldursgate3/r/adding-a-new-spell-projectile#1046863 "10/19/2024, 03:36 PM GMT-4")

I have this message as well, but I get new windows with a warning 'This atlas can only open in read only mode, would you like to open this in read only? By conforming it, I can see the icons.

[W](https://mod.io/g/baldursgate3/u/waterwitch83)

[WaterWitch83](https://mod.io/g/baldursgate3/u/waterwitch83)• [1y ago](https://mod.io/g/baldursgate3/r/adding-a-new-spell-projectile#1033127 "10/11/2024, 09:52 PM GMT-4")

Thank you so much! Any chance there will be a tutorial on spell containers? I've been struggling with this for a few days now. Even using other container spells (IE: Target\_ElementalWeapon) as examples isn't working. I get the concept and how it should work. But I'm missing something that I need to get it to work.

[L](https://mod.io/g/baldursgate3/u/ladyfiur)

[LadyFiur](https://mod.io/g/baldursgate3/u/ladyfiur)• [1y ago](https://mod.io/g/baldursgate3/r/adding-a-new-spell-projectile#1046999 "10/19/2024, 04:31 PM GMT-4")

I got it to work. The important part is the container needs the SpellFlag "IsLinkedSpellContainer" and the SpellContainerID and ContainerSpells need the right syntax TYPE\_NAME eg.

BookOfSpells
\- SpellContainerID = empty
\- ContainerSpells = Projectile\_Fireball;Projectile\_IceLance (these are just examples, not actual spells ingame ;-))

Fireball
\- ContainerSpellID = Projectile\_BookOfSpells
\- ContainerSpells = empty

IceLance
\- ContainerSpellID = Projectile\_BookOfSpells
\- ContainerSpells = empty

[S](https://mod.io/g/baldursgate3/u/modiouser2278986)

[santiagooo](https://mod.io/g/baldursgate3/u/modiouser2278986)• [1y ago](https://mod.io/g/baldursgate3/r/adding-a-new-spell-projectile#1020535 "10/5/2024, 05:25 AM GMT-4")

thanks for guide!

[E](https://mod.io/g/baldursgate3/u/explicitpeach)

[ExplicitPeach](https://mod.io/g/baldursgate3/u/explicitpeach)• [1y ago](https://mod.io/g/baldursgate3/r/adding-a-new-spell-projectile#1020207 "10/4/2024, 11:05 PM GMT-4")

Can't seem to figure out how to make a spell be able to critical hit

[M](https://mod.io/g/baldursgate3/u/modiouser2121849)

[ModioUser2121849](https://mod.io/g/baldursgate3/u/modiouser2121849)• [1y ago](https://mod.io/g/baldursgate3/r/adding-a-new-spell-projectile#1018601 "10/4/2024, 03:14 AM GMT-4")

Hi! Can you guys help me with a spell called Mind Steal that is used by the Gith Inquisitor. I have tried hard but just couldn't figure out how to create that spell for a character to fully use it as the spell tooltip suggests.

[M](https://mod.io/g/baldursgate3/u/modiouser6582792)

[Mannie25691989](https://mod.io/g/baldursgate3/u/modiouser6582792)• [1y ago](https://mod.io/g/baldursgate3/r/adding-a-new-spell-projectile#1010657 "9/29/2024, 12:55 AM GMT-4")

If we make a summon based off an existing one, how would we add a custom spell list to it, or to this one? passives? for example, i want to add rage to this summon, and a charge attack, or a custom attack?

[L](https://mod.io/g/baldursgate3/u/ladyfiur)

[LadyFiur](https://mod.io/g/baldursgate3/u/ladyfiur)• [1y ago](https://mod.io/g/baldursgate3/r/adding-a-new-spell-projectile#1046890 "10/19/2024, 03:43 PM GMT-4")

Status effects can be used with the summon statement.

Summon(template uuid, lifetime, spell override for ai, extendConcentration, stack id, status to be applied once it spawns, status2, status3, status4,l ateJoinPenalty, UseCasterPassives)

eg. Summon(UUID, -1,,,MyUniqueSummon,RAGE)

for the spell list you can add those in the root template under Character > SpellSet or Character > Spells (is a list).
For passives you can set up a character entry, and add the new added entry under Character > Stats in the root template (might need an editor restart, I needed one so that the new entry is added to the list)

[T](https://mod.io/g/baldursgate3/u/turbohobo)

[TurboHobo](https://mod.io/g/baldursgate3/u/turbohobo)• [1y ago](https://mod.io/g/baldursgate3/r/adding-a-new-spell-projectile#1110858 "12/2/2024, 03:53 PM GMT-5")

After making a custom character to use as a summon, they stopped following the character that summon them and wouldn't move unless I manually moved them. Any chance someone would know why that is cause I can't seem to find anything obvious that would change that?

Last updated

1y

Reading time

17 min read

Views

6,176

Comments

29

[G\\
\\
GrumpyWashbear](https://mod.io/g/baldursgate3/u/grumpywashbear/r)

Follow GrumpyWashbear

- [Guide](https://mod.io/g/baldursgate3/r/adding-a-new-spell-projectile#guide)
- [Making a Projectile Spell](https://mod.io/g/baldursgate3/r/adding-a-new-spell-projectile#heading-1)
- [Name](https://mod.io/g/baldursgate3/r/adding-a-new-spell-projectile#heading-2)
- [Level and SpellSchool](https://mod.io/g/baldursgate3/r/adding-a-new-spell-projectile#heading-3)
- [Effect on Tooltips](https://mod.io/g/baldursgate3/r/adding-a-new-spell-projectile#heading-4)
- [Level](https://mod.io/g/baldursgate3/r/adding-a-new-spell-projectile#heading-5)
- [SpellSchool](https://mod.io/g/baldursgate3/r/adding-a-new-spell-projectile#heading-6)
- [SpellProperties](https://mod.io/g/baldursgate3/r/adding-a-new-spell-projectile#heading-7)
- [Summon: <template uuid>](https://mod.io/g/baldursgate3/r/adding-a-new-spell-projectile#heading-8)
- [Summon: <lifetime>](https://mod.io/g/baldursgate3/r/adding-a-new-spell-projectile#heading-9)
- [Summon: <spell override for ai>](https://mod.io/g/baldursgate3/r/adding-a-new-spell-projectile#heading-10)
- [Summon: <extendConcentration>](https://mod.io/g/baldursgate3/r/adding-a-new-spell-projectile#heading-11)
- [Summon: <stack id>](https://mod.io/g/baldursgate3/r/adding-a-new-spell-projectile#heading-12)
- [Summon: <status to be applied once it spawns>](https://mod.io/g/baldursgate3/r/adding-a-new-spell-projectile#heading-13)
- [Adjusting the Summon() Functor](https://mod.io/g/baldursgate3/r/adding-a-new-spell-projectile#heading-14)
- [TargetConditions](https://mod.io/g/baldursgate3/r/adding-a-new-spell-projectile#heading-15)
- [Trajectories](https://mod.io/g/baldursgate3/r/adding-a-new-spell-projectile#heading-16)
- [Icon, DisplayName, Description](https://mod.io/g/baldursgate3/r/adding-a-new-spell-projectile#heading-17)
- [Icon](https://mod.io/g/baldursgate3/r/adding-a-new-spell-projectile#heading-18)
- [Display Name, Description](https://mod.io/g/baldursgate3/r/adding-a-new-spell-projectile#heading-19)
- [CastTextEvent](https://mod.io/g/baldursgate3/r/adding-a-new-spell-projectile#heading-20)
- [UseCosts](https://mod.io/g/baldursgate3/r/adding-a-new-spell-projectile#heading-21)
- [Spell Animation](https://mod.io/g/baldursgate3/r/adding-a-new-spell-projectile#heading-22)
- [SpellFlags](https://mod.io/g/baldursgate3/r/adding-a-new-spell-projectile#heading-23)
- [PrepareEffect, CastEffect](https://mod.io/g/baldursgate3/r/adding-a-new-spell-projectile#heading-24)
- [PrepareSound, PrepareLoopSound, CastSound, VocalComponentSound](https://mod.io/g/baldursgate3/r/adding-a-new-spell-projectile#heading-25)
- [Testing Our Spell](https://mod.io/g/baldursgate3/r/adding-a-new-spell-projectile#heading-26)
- [Trajectory](https://mod.io/g/baldursgate3/r/adding-a-new-spell-projectile#heading-27)
- [Spell Animation, PrepareEffect, CastEffect](https://mod.io/g/baldursgate3/r/adding-a-new-spell-projectile#heading-28)
- [Summon()](https://mod.io/g/baldursgate3/r/adding-a-new-spell-projectile#heading-29)
- [StackID](https://mod.io/g/baldursgate3/r/adding-a-new-spell-projectile#heading-30)
- [What Next?](https://mod.io/g/baldursgate3/r/adding-a-new-spell-projectile#heading-31)
- [Discussion](https://mod.io/g/baldursgate3/r/adding-a-new-spell-projectile#discussion)

[English](https://mod.io/g/baldursgate3/r?tags=English) [Official](https://mod.io/g/baldursgate3/r?tags=Official) [Projectiles](https://mod.io/g/baldursgate3/r?tags=Projectiles) [Spells](https://mod.io/g/baldursgate3/r?tags=Spells) [Stats](https://mod.io/g/baldursgate3/r?tags=Stats)

This guide covers how to create a Projectile spell and test it in Game Mode.

Share

Report guide

---
# SOURCE: https://mod.io/g/baldursgate3/r/making-a-wall-spell
---

[Browse games](https://mod.io/g)

Browse games

[My library](https://mod.io/library)

My library

[My content](https://mod.io/content)

My content

My account

mod.io

mod.io

[All games](https://mod.io/g) [Baldur's Gate 3](https://mod.io/g/baldursgate3) [Guides](https://mod.io/g/baldursgate3/r) [Wall Spell](https://mod.io/g/baldursgate3/r?tags=Wall+Spell) Making a Wall Spell

Making a Wall Spell

Share

Report

Follow

Picture outlines the process. If you can't view the picture, this is the text:

01. Open the UUID Object Editor and navigate to SharedDev > ItemWallTemplates.
02. Figure out which wall most closely aligns with what you are trying to do.

    For example, if it's a physical wall, go with WallOfStone, or WallOfFire if you want to entities to walk over it.
03. Create an ItemWallTemplates file in your project, then copy the entire line from the spell you chose in SharedDev and paste it into yours.

    You can either re-name the one you pasted, or you can start a new one and use it as a reference.
04. Open the Stats Editor and navigate to SharedDev > StatusData > Status\_BOOST, then do a search for "WALLOF" to find the section for walls.
05. Copy all of the lines that have the name of your template, including the DAMAGE\_RECEIVED lines. Paste them to your project.

    Again, either re-name them or create new ones using them as a reference.
06. Rename everything to be what suits your spell, including all of the StackIds, AuraStatuses, and the OnApply content.

    Also change all of the properties, such as damage or statuses you want to apply.

    As a side note, WallOfFire has a function in its OnApplyRoll and OnTickRoll. You will need to create your own, but it's simple.

    Just copy the existing one from CommonConditionsDev.khn, paste it into your script file (if you don't have one there are guides for how to make one),

    and adjust it to fit your spell.
07. Make sure to clear the StatusEffect cell (BV)! If you don't and are using WallOfFire as your template, you will always have see a wall of fire.
08. Create your effects or modify existing ones, and make them usable. There are guides for how to do that.
09. In the toolkit's main window it's now time to create the objects you will use for your wall. Find the one you used as a template by searching

    for "wall\_spell". They all have 6 parts: HighLeft, HighMiddle, HighRight, LowLeft, LowMiddle, LowRight.
10. Select the HighLeft object, right click it, and click "Create new from selected..." For now, just rename it and then click "Create more."

    Using this option will let you create them all quickly, rather than one at a time. Rename each one to be your spell, but also make sure to change

    the part (HighLeft, HighMiddle, etc) so that you have all 6 for your spell.
11. Now go through each of them and change the "Visual Resource ID" to the effect you made in step 8.
12. One at a time, right click each of the new objects you made and select "Copy Name\_GUID to clipboard", then go back to your ItemWallTemplates file

    and paste them in the appropriate slots. HighLeft to HighLeft, etc.
13. Just to be thorough and make sure you didn't forget anything, look at the other wall spells in SharedDev and compare them to yours.
14. Double check all of your stuff for mistakes! A mistake can potentially cause the TK to crash. For testing purposes, just to make sure you

    got your wall spell working visually and physically, you should initially leave all of your OnApply/OnTick stuff empty. Test those after you get it working.
15. Save everything, make it so your class can use it, and then test it. If there are issues, consider restarting the TK. Sometimes it bugs.
16. Add in the things you want your wall to do. For example, my WallOfDust spell in the image forces a save or else get pushed back a distance based on

    and the caster's Athletics skill, and take Force damage based on the caster's History skill. Test your stuff until you're satisfied.
17. Job complete!

[![Steps to create a Wall Spell, with images.](https://image.modcdn.io/members/eb5c/50353450/profile/wallspelltutorial.png)](https://image.modcdn.io/members/eb5c/50353450/profile/wallspelltutorial.png)

[D\\
\\
Dakanmer](https://mod.io/g/baldursgate3/u/modiouser6533355/r)

Follow Dakanmer

Log in to join the discussion!

Last updated

117d

Reading time

4 min read

Views

82

Comments

0

[D\\
\\
Dakanmer](https://mod.io/g/baldursgate3/u/modiouser6533355/r)

Follow Dakanmer

- [Guide](https://mod.io/g/baldursgate3/r/making-a-wall-spell#guide)
- [Discussion](https://mod.io/g/baldursgate3/r/making-a-wall-spell#discussion)

[Wall Spell](https://mod.io/g/baldursgate3/r?tags=Wall+Spell)

Simple guide for how to create a Wall spell using existing wall spells as a template. Certain steps require other knowledge found in existing guides.

Share

Report guide

---
# SOURCE: https://mod.io/g/baldursgate3/r/how-to-extend-transmogrification-lite
---

[Browse games](https://mod.io/g)

Browse games

[My library](https://mod.io/library)

My library

[My content](https://mod.io/content)

My content

My account

mod.io

mod.io

[All games](https://mod.io/g) [Baldur's Gate 3](https://mod.io/g/baldursgate3) [Guides](https://mod.io/g/baldursgate3/r) [Armor](https://mod.io/g/baldursgate3/r?tags=Armor) How to Extend Transmogrification Lite

How to Extend Transmogrification Lite

Share

Report

Follow

This guide explains how to extend [Transmogrification Lite](https://mod.io/g/baldursgate3/m/transmogrification-lite) to add compatibility with modded equipment, as well as briefly covering a few other related topics.

Why is this necessary? Well, there's a lot of information that we need about each piece of equipment in order to transmogrify it, and I don't know of a way to get this information at runtime using only the official modding tools. Instead, my solution with Transmogrification Lite is to create duplicate equipment with the same appearance but none of the stats, and then create a status that  mimics its stats and can be applied to any character no matter what they're wearing. These two components (and a few other things) are then plugged into an Osiris script I wrote that lets the player mix-and-match any appearance with any status boost.

This system works, but it means that every single item needs to be broken down into its components and recorded in a database for Transmogrification Lite to be able to work with it. I've already done this for equipment in the base game, but equipment added by other mods still can't be transmogrified. There are two solutions to this:

1. The equipment mod author adds built-in compatibility. This would be ideal because there are no dependencies or extra mods required, but it's completely up to them whether they want to. We shouldn't assume that anyone will, and we also shouldn't pester them to change their mind if they decide not to.
2. Someone gets permission to create a dependency for the equipment mod in order to extend / add support for it. (More on this later.)

For the rest of this guide, I will assume that you have some basic BG3 modding knowledge. However, I've done my best to be thorough about where to go and how to do most things. If you have any questions, you're welcome to ask and I'll try to answer when I can.

This guide is also available in [the mod's GitHub repository](https://github.com/WorldWalker42/Transmogrification-Lite), where it's split into smaller parts, has more links between the various sections, and is next to other resources for extending the mod. I recommend reading it there, but you're also welcome to continue reading here!

## Permission to Extend Transmogrification Lite

You have my permission to create dependencies on Transmogrification Lite to extend support to more equipment, translate it to another language, add new features, change the original mod's behavior, etc., so long as you also have permission from the author of every other mod dependency your project has (if any). This permission includes adding default compatibility to your own mods without them needing to be literal dependencies.

I will do my best to support my mods for as long as I can, but if I am no longer active (i.e. I haven't replied to any comments or messages for 3+ months), then you also have my permission to reuse and change the Transmogrification Lite project files to publish a new standalone version of the mod so long as you meet the following requirements:

1. The fix / change / improvement to Transmogrification Lite cannot be accomplished with a dependency (that is, the _only way_ to do what you want to is by making another standalone mod)
2. You credit me for the original work and provide a link to the original mod page if it still exists
3. You allow your new version to be used / extended / reposted under these same conditions

The full project files are available in the Transmogrification Lite GitHub repository linked above.

## Extending Appearance-Only Support

Let's start adding transmogrification compatibility to new equipment. The easiest thing to do is to have your own equipment mod and add built-in support for creating transmogrifications with just the appearance (and not the stats) of your items. We'll add stats support in the next section.

At a high level, there are only two things you need to do for each item:

1. Create a duplicate Root Template that removes its stats
2. Fill out some values in a new line of an Osiris script

There's a little bit of one-time setup for each step, but once you're familiar with the process, it's all very easy to do. Let's go into more detail.

### Root Templates

The first step is to create new Root Templates that are identical to each piece of equipment that you want to support, except that their armor stats are replaced with ones that don't grant any bonuses.

#### One-Time Setup

Before we can start making the duplicate Root Templates, we need to prepare the empty stats that will be assigned to them. Because of the way armor stats work, we need to make one for each equipment slot. You can make your own, but I recommend copying the ones made in Transmogrification Lite so that, if they ever get updated, putting the equipment mod earlier in the load order will cause its version of the stats to be overwritten by the newer, correct version.

The easiest way to copy Transmogrification Lite's armor stats is to close the toolkit, paste some values into your mod's `Armor.stats` editor file, and then relaunch the toolkit. The file is probably located somewhere like this: `C:\Program Files (x86)\Steam\steamapps\common\Baldurs Gate 3\Data\Editor\Mods\[your mod name]\Stats\Stats\`

Open the file with any text editor and scroll down to the bottom. I recommend pasting the new values in the third-to-last line:

```xml
    </stat_object>
    !PASTE NEW VALUES HERE!
  </stat_objects>
</stats>
```

Here are the values to copy-paste:

```xml
    <stat_object is_substat="false">
      <fields>
        <field name="UUID" type="IdTableFieldDefinition" value="297dcf73-2dfc-4a16-85b2-b9279b8fb5f3" />
        <field name="Name" type="NameTableFieldDefinition" value="WW_TL_Base" />
        <field name="Using" type="BaseClassTableFieldDefinition" value="17fbd33d-6377-4ec4-b642-5c6e9b063366" />
        <field name="Weight" type="FloatTableFieldDefinition" value="0" />
        <field name="MinAmount" type="IntegerTableFieldDefinition" value="1" />
        <field name="MaxAmount" type="IntegerTableFieldDefinition" value="1" />
        <field name="Priority" type="IntegerTableFieldDefinition" value="1" />
        <field name="MinLevel" type="IntegerTableFieldDefinition" value="1" />
        <field name="Slot" type="EnumerationTableFieldDefinition" value="Breast" enumeration_type_name="Itemslot" version="1" />
        <field name="ValueUUID" type="GuidObjectTableFieldDefinition" value="8b2ad47c-891e-4a19-bab8-43cd5e964cb1" />
        <field name="Tags" type="StringTableFieldDefinition" value="WW_TL_TRANSMOGRIFIED" />
        <field name="RootTemplate" type="RootTemplateTableFieldDefinition" value="02ae5d88-8044-43df-8363-02a2900776db" />
        <field name="ArmorType" type="EnumerationTableFieldDefinition" value="Padded" enumeration_type_name="ArmorType" version="1" />
        <field name="Proficiency Group" type="EnumerationListTableFieldDefinition" value="None" enumeration_type_name="ProficiencyGroupFlags" version="1" />
      </fields>
    </stat_object>
    <stat_object is_substat="false">
      <fields>
        <field name="UUID" type="IdTableFieldDefinition" value="217b943a-e4bf-4ec8-81ae-48df9a495a26" />
        <field name="Name" type="NameTableFieldDefinition" value="WW_TL_Base_Helmet" />
        <field name="Using" type="BaseClassTableFieldDefinition" value="297dcf73-2dfc-4a16-85b2-b9279b8fb5f3" />
        <field name="Slot" type="EnumerationTableFieldDefinition" value="Helmet" enumeration_type_name="Itemslot" version="1" />
        <field name="RootTemplate" type="RootTemplateTableFieldDefinition" clear_inherited_value="true" value="" />
        <field name="ArmorClass" type="IntegerTableFieldDefinition" clear_inherited_value="true" value="" />
        <field name="ArmorType" type="EnumerationTableFieldDefinition" clear_inherited_value="true" value="" enumeration_type_name="ArmorType" version="1" />
      </fields>
    </stat_object>
    <stat_object is_substat="false">
      <fields>
        <field name="UUID" type="IdTableFieldDefinition" value="817a383b-23af-4595-81d7-8fdb46800a88" />
        <field name="Name" type="NameTableFieldDefinition" value="WW_TL_Base_Boots" />
        <field name="Using" type="BaseClassTableFieldDefinition" value="297dcf73-2dfc-4a16-85b2-b9279b8fb5f3" />
        <field name="RootTemplate" type="RootTemplateTableFieldDefinition" clear_inherited_value="true" value="" />
        <field name="Slot" type="EnumerationTableFieldDefinition" value="Boots" enumeration_type_name="Itemslot" version="1" />
        <field name="ArmorClass" type="IntegerTableFieldDefinition" clear_inherited_value="true" value="" />
        <field name="ArmorType" type="EnumerationTableFieldDefinition" clear_inherited_value="true" value="" enumeration_type_name="ArmorType" version="1" />
      </fields>
    </stat_object>
    <stat_object is_substat="false">
      <fields>
        <field name="UUID" type="IdTableFieldDefinition" value="ad252c9e-0353-40e4-9421-41340d3f502d" />
        <field name="Name" type="NameTableFieldDefinition" value="WW_TL_Base_Gloves" />
        <field name="Using" type="BaseClassTableFieldDefinition" value="297dcf73-2dfc-4a16-85b2-b9279b8fb5f3" />
        <field name="RootTemplate" type="RootTemplateTableFieldDefinition" clear_inherited_value="true" value="" />
        <field name="Slot" type="EnumerationTableFieldDefinition" value="Gloves" enumeration_type_name="Itemslot" version="1" />
        <field name="ArmorClass" type="IntegerTableFieldDefinition" clear_inherited_value="true" value="" />
        <field name="ArmorType" type="EnumerationTableFieldDefinition" clear_inherited_value="true" value="" enumeration_type_name="ArmorType" version="1" />
      </fields>
    </stat_object>
    <stat_object is_substat="false">
      <fields>
        <field name="UUID" type="IdTableFieldDefinition" value="bb8d47dd-7914-4901-bc0f-01aa32604434" />
        <field name="Name" type="NameTableFieldDefinition" value="WW_TL_Base_Cloak" />
        <field name="Using" type="BaseClassTableFieldDefinition" value="297dcf73-2dfc-4a16-85b2-b9279b8fb5f3" />
        <field name="RootTemplate" type="RootTemplateTableFieldDefinition" clear_inherited_value="true" value="" />
        <field name="Slot" type="EnumerationTableFieldDefinition" value="Cloak" enumeration_type_name="Itemslot" version="1" />
        <field name="ArmorClass" type="IntegerTableFieldDefinition" clear_inherited_value="true" value="" />
        <field name="ArmorType" type="EnumerationTableFieldDefinition" clear_inherited_value="true" value="" enumeration_type_name="ArmorType" version="1" />
      </fields>
    </stat_object>
```

Make sure to save these changes to the editor file. Now, when you reopen the toolkit, you will be able to see and use the armor stats like normal. Each of the stats corresponds with an equipment slot:

Chest: "WW\_TL\_Base"

Helmet: "WW\_TL\_Base\_Helmet"

Cloak: "WW\_TL\_Base\_Cloak"

Gloves: "WW\_TL\_Base\_Gloves"

Footwear: "WW\_TL\_Base\_Boots"

#### For Each Item

We're now ready to create new Root Templates for each item we want to support:

1. In the main toolkit window's Root Templates pane, right click on one of the items and choose "Create inherited from selected..."
2. In the popup window, add something to the end of the new template's name to indicate that it's the appearance-only version of the item.
3. Still in the popup, scroll down to the Item category and open the Stats field. Type `WW_TL_Base` into the filter and then choose the stats that correspond to this item's equipment slot.
4. Click "Create" to finalize this new template.
5. I recommend saving the project after creating each one, because it's _really_ not fun when the toolkit crashes and you lose a bunch of them at once.

If there are more pieces of equipment than you want to duplicate by hand, then make sure to read the **Automating This Process** section below.

### Database Entries

Now that we have templates for the equipment's appearance, we just need to connect them to the transmogrification system so that they can be used. This is done in an Osiris script, but don't worry if you haven't done anything with Osiris before - it's pretty easy to do.

#### One-Time Setup

First, we need to create an Osiris script. Open the Story Editor with this button in the main toolkit window:

[![Button to open Story Editor](https://image.modcdn.io/members/c344/35043001/profile/1storyeditorbutton.1.jpg)](https://image.modcdn.io/members/c344/35043001/profile/1storyeditorbutton.1.jpg)

Next, create a new top-level script by right-clicking on one of the items in the list and choosing "Add New Item".

[![Menu item to create new Osiris script](https://image.modcdn.io/members/c344/35043001/profile/2makingnewscript.jpg)](https://image.modcdn.io/members/c344/35043001/profile/2makingnewscript.jpg)

I recommend naming the script something like `GLO_Transmogrification_IDENTIFIER` where you replace `IDENTIFIER` with an abbreviation of your username and/or the mod's name (for example, the identifier I use for Transmogrification Lite is `WW_TL`, and the one I use for this Compatibility Example is `WW_CE`).

When you create the script, it should automatically open three text boxes on the right side of the window. If this doesn't happen automatically, you can find the name of your script in the list on the left (it probably went to the bottom) and double-click it.

#### For Each Item

In the topmost text box (called the INIT section), you will need to add the following line once for each piece of equipment and then fill in its values:

```scss
DB_WW_TL_ArmorComponents(_Template, _AppearanceTemplate, _StatsStatusName, _ArmorType, _DisplayAC, _Slot, _Unique, _AdditionalAttributesTooltip);
```

A lot of these values have to do with recreating equipment stats, which we don't care about right now. Instead, we can use the values for default stats (e.g. clothes with 10 AC for the chest slot and nothing for every other slot). To keep things simple, you can start with one of the following lines that are already mostly filled in:

For equipment in the chest slot:

```bash
DB_WW_TL_ArmorComponents(_Template, _AppearanceTemplate, "WW_TL_AC_10", 0, 10, "Breast", 0, 0);
```

For equipment in any other slot:

```scss
DB_WW_TL_ArmorComponents(_Template, _AppearanceTemplate, "NULL", 0, 0, _Slot, 0, 0);
```

Replace `_Template` with the Name\_GUID for the original item's Root Template (which you can get by right-clicking on it in the main window's Root Templates pane and select "Copy Name\_GUID to clipboard").

Replace `_AppearanceTemplate` with the Name\_GUID for the item's appearance-only Root Template that we created in the previous step.

If `_Slot` hasn't been filled in yet, replace it with `"Helmet"`, `"Gloves"`, `"Boots"`, or `"Cloak"` as appropriate for this item.

For example, here's what I did for a basic robe in the base game for Transmogrification Lite:

```bash
DB_WW_TL_ArmorComponents(ARM_Robe_B_69302808-57a0-4fbb-9938-137bce5421d1, ARM_Robe_B_WW_TL_01f1643b-363b-42e0-84c4-44fe7851b2c7, "WW_TL_AC_10", 0, 10, "Breast", 0, 0);
```

#### Finalizing the Script

Once you've added everything to your script, you MUST finalize it by 'building' the script (and fixing any errors it points out) so that it takes effect in the game. Do this by opening the "File" menu and choosing "Generate Definitions, Build and Reload".

The first time you do this after opening the toolkit, you will get a popup warning about orphan queries - this just means that you're adding facts to a database that isn't used anywhere, and it's letting you know about it in case this was a mistake. Because the database will be used by another mod - Transmogrification Lite - we want to ignore this warning.

To do this, close both popups and click on the "Ignore Orphan Queries" button toward the bottom of the window.

[![The buttons to click on to resolve orphan queries warning](https://image.modcdn.io/members/c344/35043001/profile/3ignoringorphanqueriespt1annota.jpg)](https://image.modcdn.io/members/c344/35043001/profile/3ignoringorphanqueriespt1annota.jpg)

A new window will open to let you choose which orphan queries you want to ignore. There should only be one for `DB_WW_TL_ArmorComponents`, so toggle on the checkbox next to it and press "OK" to finalize your choice.

[![The correct state for the orphan queries resolution window](https://image.modcdn.io/members/c344/35043001/profile/4ignoringorphanqueriespt2.jpg)](https://image.modcdn.io/members/c344/35043001/profile/4ignoringorphanqueriespt2.jpg)

Now that we've told the Story Editor to ignore this possible problem, choose "Generate Definitions, Build and Reload" again. Until the next time you close the toolkit, the process should complete without any warnings and your script is ready to work.

If you ever get tired of doing this, you can add a rule in the KB section that references the database but will never execute, like this:

```java
IF
LevelGameplayStarted(_, _)
AND
1 == 2 // always evaluates to false, which guarantees this rule will never execute
AND
DB_WW_TL_ArmorComponents(_,_,_,1000,_,_,_,_) // references the database
//AND
//[add more databases as needed]
THEN
DB_NOOP(1);
```

I recommend taking one last (optional) step to reduce the file size of your mod. For some reason, building any Osiris script will also put a copy of the entire game's scripts into your mod's project files, and unless you manually delete it before publishing the mod, it will add about 17 MB. (However, you also need to be aware that your script won't do anything _inside the toolkit_ after you delete the copy of the base game scripts. Without the copy, it will only work as a published .pak file being used with the actual game. So, only delete the files after testing in the toolkit and before you're ready to publish.)

To reduce your mod's size, navigate to your toolkit project files (most likely `C:\Program Files (x86)\Steam\steamapps\common\Baldurs Gate 3\Data` and then find this mod's Story files in `Mods\[mod_guid]\Story`. There will be a folder "RawFiles" and a bunch of other files. You MUST keep "RawFiles" but it should be safe to delete everything else.

### Complete Example

That's everything you need to do so that people can use the appearance of your equipment with the stats of any other supported item! It's perfectly fine to leave it this way if you don't want to add stats support - which gets more complicated - but I do recommend making it very clear in your mod description that the transmogrification support is appearance-only.

I've made a simple mod that just adds a few pieces of equipment with built-in appearance transmogrification support if you want to look at a complete example. The .pak and all project files for this example are available in Transmogrification Lite's GitHub repository: [https://github.com/WorldWalker42/Transmogrification-Lite/tree/main/Extension%20Resources/1.%20Appearance-Only%20Support](https://github.com/WorldWalker42/Transmogrification-Lite/tree/main/Extension%20Resources/1.%20Appearance-Only%20Support)

Although most of the **Updating The Mod** section isn't necessary for appearance-only support, it's still worth reading if you ever want to add support for more equipment in an update.

### Automating This Process

To make this process easier, I wrote a Python script that can do everything we've covered so far automatically. It's available in the mod's GitHub repository here: [https://github.com/WorldWalker42/Transmogrification-Lite/blob/main/Extension%20Resources/script.py](https://github.com/WorldWalker42/Transmogrification-Lite/blob/main/Extension%20Resources/script.py)

DISCLAIMER: I've found the script to be very helpful, but I DO NOT make any promises that it is perfect. Also, it was not written with any particular elegance or efficiency in mind - it's just something I threw together to help me, and I'm sharing it as-is. I do not plan to provide detailed support or troubleshooting for it.

That being said, if you have Python installed, all you should have to do is run the script and give it the mod's identifier and a few relative file paths. If the equipment has stats that the script doesn't recognize (and therefore doesn't know what equipment slot it goes into), then you might have to open the script in a text editor and add those stats to a list it uses.

Here's the process to use the script in more detail:

1\. Convert the Root Template .lsf files (which will be in the mod's Public -> RootTemplates directory) into .lsx files. Put these .lsx files into a different folder (which can be anywhere, like your desktop) and make sure the original .lsf files are still in the mod folder. (Note: This step has [more detail on GitHub](https://github.com/WorldWalker42/Transmogrification-Lite/tree/main/Extension%20Resources/1.%20Appearance-Only%20Support#automating-this-process).)

2\. Create another folder where the script's output can go.

3\. Open the terminal or command line application and change the directory to the location where you put the Python script. Run it with: `python3 script.py IDENTIFIER relative/path/to/lsx/files relative/path/to/armor/stats relative/path/to/output/directory` where you replace `IDENTIFIER` with your mod's unique identifier and the placeholder filepaths with the actual relative filepaths to the described location or file.

4\. In the output directory, check the "remainder.txt" file to see if any Root Templates were rejected by the script. Depending on the mod, it might be totally normal for there to be LOTS of rejected templates for things like weapons, containers, dyes, summons, etc. If any equipment that should have been supported was rejected, then refer to the script's output for the most up-to-date instructions on how to troubleshoot the problem.

5\. Copy the contents of "script\_init.txt" in the script output directory and paste it into your mod's Osiris script INIT section that you should create but not fill in as described above. Make sure to build and reload.

6\. Convert the .lsx files in the output directory's "templates" subdirectory back into .lsf files, and then move them into the project's Public -> RootTemplates directory along with the original .lsf files.

Keep in mind that every time you run the script, it generates new random GUIDs for each item. This means you need to be mindful of not keeping a Root Template from one time the script ran with the `DB_WW_TL_ArmorComponents` entry for the same item from another time the script ran, because they won't match.

## Extending Basic Stats Support

To also be able to create transmogrifications that use your equipment's basic stats, we need to do a couple more things:

1. Create a status effect that mimics the equipment's stats
2. Fill out the remaining values in the line added to the Osiris script

### BOOST Status

Let's start with creating the status effect (specifically a BOOST type status) that mimics the original item's Armor stats. This will allow Transmogrification Lite to freely apply it to any character without them having to equip a specific item.

#### One-Time Setup

First, we should create a parent status that all of the others will inherit from. This lets us set certain technical details one time (like not removing the status after a long rest) and then not have to worry about it again. Also, if we ever need to change something for every single status, we can do so very easily through the parent status.

In your mod's `Status_BOOST` file (which is in the Stats Editor, if you haven't worked with one before), create a new status that has this EXACT name: `WW_TL_ARMOR_STATS`

Next, assign it the following values:

\- `DisplayName` is "Transmogrified Equipment"

\- `Icon` is `PassiveFeature_LightlyArmored`

- `StatusPropertyFlags` are:

    \\* `IgnoreResting`

    \\* `DisableOverhead`

    \\* `DisableCombatlog`

    \\* `DisablePortraitIndicator`

    \\* `ApplyToDead`

If you're interested to know, the benefit of giving this status the exact same name as one that exists in Transmogrification Lite is that the mod that is loaded last will override the other versions of the status. So, Transmogrification Lite can be loaded after all equipment mods to have its most up-to-date version of the parent status be applied to all extensions automatically. This technically means you don't have to set the `StatusPropertyFlags` in your mod's version of the status, but I strongly recommend that you do because they're not strict dependencies and so it would be very easy to get the load order wrong, which would completely mess up the behavior of _every_ transmogrification without them being set.

#### For Each Item

Now you can create a BOOST status for each piece of equipment you want to add stats support for. This process is mostly a matter of copying and pasting cells between the Armor file and the Status\_BOOST file:

1\. Create a new status with the name of the armor stats you're recreating plus your mod's unique identifier (e.g. for the stats `MAG_DarkJusticiar_HalfPlate` I made the status `WW_TL_MAG_DarkJusticiar_HalfPlate`). If this is already the name for the armor stats, then you need to add something else (like `TL` for Transmogrification Lite compatibility), because it won't work if they have the same name.

2\. Set its parent to `WW_TL_ARMOR_STATS` that we created in the previous step

3\. Copy-paste the original `Boosts` column into the one for this status. If it has a penalty to stealth from being medium or heavy armor, don't copy the penalty, because this is handled automatically somewhere else.

4\. If the original stats has a value in the `ArmorClass` column (even if it's just inherited), add `AC(X);` to this status' `Boosts` column. For example, the Helldusk Armour has an AC 21 and the boost `UnlockSpell(Shout_MAG_Infernal_Fly)`, so the final boost for its status is `AC(21);UnlockSpell(Shout_MAG_Infernal_Fly)`.

5\. Copy-paste the original `Passives` column into the one for this status.

6\. If the original stats has a value in the `StatusOnEquip` column, then for each status is applies:

- Add `ApplyStatus(STATUS_NAME, 100, -1);` in this status' `OnApplyFunctors` column (make sure to replace `STATUS_NAME` with the name of the status).
- Add `RemoveStatus(STATUS_NAME);` in this status' `OnRemoveFunctors` column (again, replacing `STATUS_NAME`).
- For example, the original armor stats for the Boots of Persistence has the `StatusOnEquip` column `MAG_FREEDOM_OF_MOVEMENT;MAG_END_GAME_LONGSTRIDER`, and so the status that I made for it has the `OnApplyFunctors` column `ApplyStatus(MAG_FREEDOM_OF_MOVEMENT,100,-1);ApplyStatus(MAG_END_GAME_LONGSTRIDER,100,-1)` and the `OnRemoveFunctors` column `RemoveStatus(MAG_FREEDOM_OF_MOVEMENT);RemoveStatus(MAG_END_GAME_LONGSTRIDER)`

7\. I haven't seen any equipment stats using the `StatsFunctor` or other columns, but theoretically if one did then you should copy those too.

For a complete example, here's the original stats for the Armour of Persistence:

```wasm
new entry "MAG_EndGame_Plate_Armor"
type "Armor"
using "ARM_Plate_Body_2"
data "RootTemplate" "fb2ff6d1-3096-4904-813c-a448e3fbec4d"
data "ValueUUID" "adfdafe5-f4da-4c64-a1e6-a33d626437d2"
data "Rarity" "VeryRare"
data "PassivesOnEquip" "ARM_MagicalPlate_2_Passive;MAG_MAG_EndGame_Plate_Armor_Passive"
data "StatusOnEquip" "MAG_BLADE_WARD;MAG_END_GAME_RESISTANCE"
data "Unique" "1"
```

And here's the status I made to mimic it:

```wasm
new entry "WW_TL_MAG_EndGame_Plate_Armor"
type "StatusData"
data "StatusType" "BOOST"
using "WW_TL_ARMOR_STATS"
data "Boosts" "AC(20)"
data "Passives" "ARM_MagicalPlate_2_Passive;MAG_MAG_EndGame_Plate_Armor_Passive"
data "OnApplyFunctors" "ApplyStatus(MAG_BLADE_WARD,100,-1);ApplyStatus(MAG_END_GAME_RESISTANCE,100,-1)"
data "OnRemoveFunctors" "RemoveStatus(MAG_BLADE_WARD);RemoveStatus(MAG_END_GAME_RESISTANCE)"
```

Notice that the original stats doesn't have a `Boosts` column or an `ArmorClass` column, but for the status I had to add a `Boosts` column for the AC that the original inherits from `ARM_Plate_Body_2`.

If an item does nothing except provide a basic AC between 10-18, like the Simple Robe, then you can skip this step and use one of my pre-made statuses in the next step. If it adds an AC outside of this range, then you'll still need to make your own.

### Finishing the Database Entries

As before, in the INIT section of your Osiris script, you will need to have the following line with the values filled in for each piece of equipment:

```scss
DB_WW_TL_ArmorComponents(_Template, _AppearanceTemplate, _StatsStatusName, _ArmorType, _DisplayAC, _Slot, _Unique, _AdditionalAttributesTooltip);
```

If you already added this line for appearance-only support, don't add a second line for the same item - you just need to replace the default values with ones that are specific to this item's stats. This time, let's go over what every single value should be:

1\. Replace `_Template` with the Name\_GUID for the equipment's original Root Template.

2\. Replace `_AppearanceTemplate` with the Name\_GUID for the equipment's appearance-only Root Template.

3\. Replace `_StatsStatusName` with the name of the BOOST status we created in the previous step. Enter the name as a string (that is, it should be surrounded by quotation marks - the status `WW_TL_MAG_EndGame_Metal_Boots` should be entered as `"WW_TL_MAG_EndGame_Metal_Boots"`). If this item just adds an AC between 10-18, you can use `"WW_TL_AC_10"`, `"WW_TL_AC_11"`, ..., `"WW_TL_AC_18"`. If this item does not do anything, not even adding some AC, then enter `"NULL"`.

4\. Replace `_ArmorType` with a number indicating the type of armor it is:

- `-1` for camp clothes and shoes
- `0` for clothes
- `1` for light armor
- `2` for medium armor
- `3` for medium armor that applies disadvantage on stealth
- `4` for heavy armor
- `5` for medium armor that lets the wearer add their full Dexterity modifier to their AC (such as the Armour of Agility)

5\. Replace `_DisplayAC` with the number for its Armor Class bonus.

6\. Replace `_Slot` with `"Breast"`, `"Helmet"`, `"Gloves"`, `"Boots"`, or `"Cloak"` depending on which equipment slot this item goes into.

7\. Replace `_Unique` with `0` to let any number of copies of this item's stats be in use at the same time, or `1` to only let one of them be used at a time. The more items that are unique, the less that game balance is altered. At the very least, anything that grants a spell / ability with a cooldown should be set to unique or else there can be some weird behavior.

8\. Replace `_AdditionalAttributesTooltip` with `0` to not add the "Additional Attributes" description to this item's tooltip, or `1` to add it. (More on this in the **Extending Full Stats Support** section. In the meantime, you can leave it at `0`.)

Now that we've covered what every value means, let's take another look at the example used in the appearance-only section:

```bash
DB_WW_TL_ArmorComponents(ARM_Robe_B_69302808-57a0-4fbb-9938-137bce5421d1, ARM_Robe_B_WW_TL_01f1643b-363b-42e0-84c4-44fe7851b2c7, "WW_TL_AC_10", 0, 10, "Breast", 0, 0);
```

Let's break it down:

- The status `WW_TL_AC_10` gives the character 10 AC but does not grant any other bonuses
- The armor type is 0 because these robes are clothes
- The display AC is 10 to match the BOOST status's effect
- The slot is "Breast"
- It does not enforce unique stats because it's such a basic item that won't mess with game balance even if everyone uses it
- It does not use the "Additional Attributes" tooltip option because everything it does is described by its AC value

Let's look at another example of the Steelwatcher Helmet:

```bash
DB_WW_TL_ArmorComponents(MAG_Helmet_Watcher_A_c2ef4013-e6d1-48da-99f0-db486c223a90, MAG_Helmet_Watcher_A_WW_TL_faba36f5-6293-41eb-8f71-c59ce9861443, "WW_TL_MAG_Helmet_Human_Watcher", 2, 0, "Helmet", 1, 1);
```

Breaking it down:

- It uses a custom BOOST status `WW_TL_MAG_Helmet_Human_Watcher` to give the character Darkvision, immunity to blindness, and advantage on CON saves
- Its armor type is `2` because it's medium armor
- Its display AC is `0` because it does not provide an AC boost
- It has the helmet slot
- It only allows one copy of its stats to be used at a time because it has more meaningful bonuses that could alter game balance
- It uses the "Additional Attributes" tooltip option because Transmogrification Lite doesn't have tooltip categories to describe the item's Darkvision and status immunity (more on this later), so we need to indicate that it does more stuff

### Complete Example

Now players can also use the basic stats of your equipment with the appearance of any other supported item!

I've added basic stats support to my example mod and uploaded another version of the .pak and project files here: [https://github.com/WorldWalker42/Transmogrification-Lite/tree/main/Extension%20Resources/2.%20Basic%20Stats%20Support](https://github.com/WorldWalker42/Transmogrification-Lite/tree/main/Extension%20Resources/2.%20Basic%20Stats%20Support)

Notice that when you take the stats of one of these items, the tooltips of the transmogrifications will only show the armor type, AC, and maybe "Additional Attributes", but nothing else specific. This will be added in the next section. You can also have any character equip the item that should be limited to just the avatar by taking its stats for a transmogrification, as well as a few other subtle issues.

## Extending Full Stats Support

Although the basic stats for our equipment can now be used with a transmogrification, the tooltip still doesn't describe anything it does (which in my experience will make players think that it isn't working), and some types of stats won't work correctly in all circumstances without more customized support.

For example, one of the items in my example mod unlocks a spell with a Short Rest cooldown, but you can easily avoid the cooldown by re-transmogrifying it unless you hook the item up to Transmogrification Lite's cooldown enforcement system. Also, another item in my example should only be able to be equipped by avatars, but without adding special support for this restriction, anyone will be able to equip a transmogrification that uses its stats.

In this section, we'll discuss how to add full support for the most common issues with stats I've seen, and then I'll also describe some of the tools I've built into the core mod that you can use to make your own solutions to things not included here.

### Descriptions in Transmog Tooltips

Because we can't extract much information from an item with the official toolkit, we're also very limited in what we can do to recreate an item's descriptions for transmogrifications. Based on what we've done so far, the tooltip for transmogrified items will only show whether it's clothing or light/medium/heavy armor, its Armor Class, and it might also say "Additional Attributes" depending on the value you set for it in `DB_WW_TL_ArmorComponents`.

To be able to describe more of a transmogrification's stats, I built a system that applies descriptive statuses to the item so that they will appear in its tooltip. For example, the transmogrification's tooltip still can't say "Reduces Fire damage by 3", but it can show a status named "Damage Reduction" in order to broadly describe what it does.

[![Tooltips comparison for original item, basic transmog, and complete transmog](https://image.modcdn.io/members/c344/35043001/profile/5basicvsfulltooltips.jpg)](https://image.modcdn.io/members/c344/35043001/profile/5basicvsfulltooltips.jpg)

Adding these descriptors to the tooltip is very easy - we just need to add a couple values to a much simpler database in the INIT section of the Osiris script that we've already created.

The database we're going to be using this time is:

```scss
DB_WW_TL_TooltipStatuses(_StatsStatusName, _TooltipName);
```

Replace `_StatsStatusName` with the name of the BOOST status (in quotation marks) that applies the equipment's stats. It should match the third value used for this equipment's entry in the original database (`DB_WW_TL_ArmorComponents`).

Replace `_TooltipName` with the name of the category (in quotation marks) that you want applied to it. The following categories are available by default:

- `AC_CONDITIONAL` \- the wearer receives a bonus to their AC that changes or is only applied in certain situations.
- `SAVE_DC` \- the wearer's spell save DC is increased.
- `ATTACK` \- the wearer's attack rolls (melee or ranged, but NOT spell-based) are increased or made with advantage.
- `ATTACK_SPELL` \- the wearer's spell attack rolls (melee or ranged) are increased.
- `DAMAGE` \- the wearer deals additional damage or causes damage in new situations.
- `ABILITY` \- one or more of the wearer's ability scores are increased.
- `SAVE_THROW` \- one or more of the wearer's saving throws (including concentration checks) are increased.
- `RESISTANCE` \- the wearer becomes resistant to one or more types of damage.
- `REDUCE_DAMAGE` \- damage to the wearer is reduced (separate from being Resistant to a particular damage type).
- `SPELL` \- the wearer is granted one or more spells or abilities.

For example, the Gloves of Dexterity give +1 to attack rolls and set the wearer's Dexterity score to 18, so I used this for its tooltip:

```bash
DB_WW_TL_TooltipStatuses("WW_TL_MAG_BG_OfDexterity_Gloves", "ATTACK");
DB_WW_TL_TooltipStatuses("WW_TL_MAG_BG_OfDexterity_Gloves", "ABILITY");
```

And, because these two attributes fully describe the Gloves of Dexterity's stats, I set its line in `DB_WW_TL_ArmorComponents` to _not_ apply the "Additional Attributes" description.

Note: Each category can only be applied to an item one time, so even if it unlocks two spells when equipped, you should only add one line for it in this database with the `SPELL` category.

Also, the order of the facts in the database will be used for the order of the category descriptions in the tooltip. For consistency, I recommend keeping them in the order that I listed the categories above, but you're of course free to do otherwise.

If you want to create your own category, all you need to do is create a new BOOST status with:

1. A name that starts with `WW_TL_ARMOR_DISPLAY_` and ends with the name of the category (which I recommend to include your mod's identifier)
2. `StatusPropertyFlags` set to `IgnoreResting;DisableOverhead;DisableCombatlog`
3. A `DisplayName` and `Description` that lets the player know what this category describes.
4. It's very nice, but not required, to add a relevant icon.

Now you can use the name of your category with `DB_WW_TL_TooltipStatuses` and it should appear in the item tooltip!

### Enforcing Spell Cooldowns

It's common for equipment to grant the wearer a spell or ability with a cooldown. However, because transmogrification can be used to share equipment stats between lots of items, it's possible to trick the game into letting the player use the spell again before its cooldown is finished. This probably won't happen without intentionally trying to take advantage of it, but because it could be used to significantly alter game balance, I built a system into Transmogrification Lite that keeps track of spell cooldowns and interrupts an attempt to use something before it should be able to be.

In order to activate this system for a piece of equipment, we need to add a fact to 1-2 databases in the INIT section of the Osiris script that we've already made. Only do this for items that have their `_Unique` value set to `1` in `DB_WW_TL_ArmorComponents` because the spell cooldown is shared between all copies of the item, so if multiple copies can be in use at once then it's better not to enforce the cooldown.

The database you need to add to is:

```scss
DB_WW_TL_ArmorSpells(_StatsStatusName, _SpellName, _CooldownType);
```

Replace `_StatsStatusName` with the name of the BOOST status (in quotation marks) that applies the equipment's stats. It should match the third value used for this equipment's entry in the original database (`DB_WW_TL_ArmorComponents`). For example, I made the status `WW_TL_MAG_Martial_Exertion_Gloves` to recreate the bonuses from the Martial Exertion Gloves, so I would use the name of that status here to enforce its cooldown.

Replace `_SpellName` with the full technical name of the spell/ability (in quotation marks) that needs a cooldown. For example, the Martial Exertion Gloves grant the ability Martial Exertion that has the technical name `Shout_MAG_Martial_Exertion`.

Replace `_CooldownType` with the kind of cooldown this spell or ability has (also in quotation marks). The currently supported options are:

- Once per turn: `TURN`
- Once per combat: `COMBAT`
- Once per Short Rest: `SHORT`
- Once per Long Rest: `LONG`

Here's a complete example for the Martial Exertion ability, which can only be used once per Short Rest:

```bash
DB_WW_TL_ArmorSpells("WW_TL_MAG_Martial_Exertion_Gloves", "Shout_MAG_Martial_Exertion", "SHORT");
```

A couple of notes about this:

1. If a single piece of equipment unlocks multiple spells/abilities, then you would need to add a fact to the database for each one. The name of the BOOST status will be the same for all of them, but the spell name will be different, and the cooldown might need to change too.
2. Even if multiple pieces of equipment use the same BOOST status for their transmogrification stats, you don't need to add duplicate facts to this database for each one. This is because the cooldown enforcement systems looks for the status being used and not the specific item that's equipped.

#### Container Spells

Enforcing the cooldown for spells and abilities in a container has one more step. For example, Gortash's Gauntlet of the Tyrant unlocks Command, which is a container including five separate spells that can be cast. Casting any one of them needs to activate the cooldown for all of them.

For a spell container, follow the previous steps for JUST the spell container (NOT for any of the spells inside it), like this:

```bash
DB_WW_TL_ArmorSpells("WW_TL_MAG_Gortash_Gloves", "Target_MAG_Tyrant_Command_Container", "LONG");
```

Next, for each spell inside the container, we need to add a fact to this database:

```scss
DB_WW_TL_ArmorSpellContainers(_SpellContainerName, _ChildSpellName);
```

Replace `_SpellContainerName` with the full technical name of the container (in quotation marks) that we used for the other cooldown database. For this example, it would still be `"Target_MAG_Tyrant_Command_Container"`.

Replace `_ChildSpellName` with the full technical name of one of the spells/abilities inside the container (also in quotation marks).

For this example, the final result looks like this:

```cpp
// Container spell cooldown:
DB_WW_TL_ArmorSpells("WW_TL_MAG_Gortash_Gloves", "Target_MAG_Tyrant_Command_Container", "LONG");

// A list of the actual spells that might be used to trigger the container cooldown:
DB_WW_TL_ArmorSpellContainers("Target_MAG_Tyrant_Command_Container", "Target_MAG_Tyrant_Command_Halt");
DB_WW_TL_ArmorSpellContainers("Target_MAG_Tyrant_Command_Container", "Target_MAG_Tyrant_Command_Approach");
DB_WW_TL_ArmorSpellContainers("Target_MAG_Tyrant_Command_Container", "Target_MAG_Tyrant_Command_Drop");
DB_WW_TL_ArmorSpellContainers("Target_MAG_Tyrant_Command_Container", "Target_MAG_Tyrant_Command_Flee");
DB_WW_TL_ArmorSpellContainers("Target_MAG_Tyrant_Command_Container", "Target_MAG_Tyrant_Command_Grovel");
```

Now the cooldown should be properly enforced.

### Enforcing Unarmored-Only Bonuses

Some equipment should only grant AC or another kind of bonus when its wearer does not have any armor equipped. However, the game thinks every transmogrification is clothing even if it's using stats from heavy armor, and so by default the character can receive the unarmored-only bonuses when they're not supposed to.

To solve this, Transmogrification Lite applies the status `WW_TL_WEARING_ARMOR` to characters wearing a transmogrification with stats for light, medium, or heavy armor. We can use this two different ways to correctly enforce unarmored-only bonuses:

1. Anytime `not WearingArmor(context.Source)` is a boost condition, add `and not HasStatus('WW_TL_WEARING_ARMOR',context.Source)`. This is the cleanest solution, but if I would have to override a passive/status in the base game or another mod then I try to avoid it, because overriding resources limits compatibility with other mods that override the same resources.
2. Give the character a new passive whenever they have the status `WW_TL_WEARING_ARMOR` that will counteract the bonus if they're not wearing any normal armor that would disable it. That is, if you can't stop the equipment from giving them +3 AC, then you just need to also give them -3 AC so that 10 + 3 - 3 = 10. This is not a very clean solution and can't undo everything, but it has the broadest compatibility.

Let's look at the second solution in more detail.

First, we need to make the debuff passive, which can be used to undo more than one bonus. It needs to have the following settings:

1. `Properties` is `IsHidden` because the player shouldn't see this passive.
2. `BoostContext` is `OnEquip;OnCreate` so that the debuff is reevaluated every time the character (un)equips something.
3. `BoostConditions` is `not WearingArmor(context.Source)` so that we don't undo the buff if it's already been disabled by the character _also_ wearing normal armor. We only want to undo the buff if all the armor that the character is wearing has been transmogrified.
4. `Boosts` checks whether the character has one or more unarmored-only bonuses and does the opposite to cancel them out.

For example, this debuff passive undoes an imaginary +1 unarmored AC granted by the passive `IDENTIFIER_UnarmoredBonus` as well as a +3 unarmored AC granted by the passive `IDENTIFIER_UnarmoredBonus_Greater`:

```wasm
new entry "IDENTIFIER_ArmorDebuff"
type "PassiveData"
data "DisplayName" "hc81bdb92gb598g1751g9302g0cc4872aa860;3"
data "Properties" "IsHidden"
data "BoostContext" "OnEquip;OnCreate"
data "BoostConditions" "not WearingArmor(context.Source)"
data "Boosts" "IF(HasPassive('IDENTIFIER_UnarmoredBonus', context.Source)):AC(-1); IF(HasPassive('IDENTIFIER_UnarmoredBonus_Greater', context.Source)):AC(-3);"
```

As always, replace `IDENTIFIER` with your mod's unique identifier. Although, in this case you might want to completely rename the debuff passive to be more descriptive.

Next, you need to give the debuff passive to characters in your mod's Osiris script with these rules:

```java
IF
StatusApplied(_Character,"WW_TL_WEARING_ARMOR",_,_)
THEN
AddPassive(_Character,"IDENTIFIER_ArmorDebuff");

IF
StatusRemoved(_Character,"WW_TL_WEARING_ARMOR",_,_)
THEN
RemovePassive(_Character,"IDENTIFIER_ArmorDebuff");
```

Now the transmogrification's unarmored-only bonuses should _actually_ be limited to only unarmored characters.

### Custom Behaviors

Of course, part of why modded equipment is so much fun is because it can do entirely new and unexpected things. Unfortunately for adding transmogrification support, this means that I can't provide guidance on everything that might come up. However, I can tell you about some tools that are available for you to use and provide a couple of examples.

Most issues can probably be solved with Osiris scripting (either by doing something directly or by applying extra statuses / passives). If you don't have much experience with this kind of scripting and want to learn more, I recommend reading the official guide [Introduction to Osiris](https://mod.io/g/baldursgate3/r/introduction-to-osiris) and my guide [Understanding Osiris Rules](https://mod.io/g/baldursgate3/r/understanding-osiris-rules).

Transmogrification Lite implements two event-like procedures, a custom query, and several Osiris databases that you might find useful in your own script, the definitions of which are described below.

Note: The first time you reference each database in your own script, you will need to include the type of any values you leave unbound. Please see the **Examples** subsection below for reference.

#### Event-Like Procedures

The normal Osiris events `Equipped((ITEM)_Item, (CHARACTER)_Character)` and `Unequipped((ITEM)_Item, (CHARACTER)_Character)` will be triggered when a character (un)equips any kind of item, but it can be tricky to use them with transmogrifications due to a handful of small technical details. Instead, this mod calls the following procedures that you can use like the original events for transmogrifications:

`PROC_WW_TL_Event_Equipped((ITEM)_Armor, (CHARACTER)_Character)` when `_Character` equips the transmogrification `_Armor`.

`PROC_WW_TL_Event_Unequipped((ITEM)_Armor, (CHARACTER)_Character)` when `_Character` unequips the transmogrification `_Armor`.

You can add more rules to these procedures to use them just like events, like so:

```scss
// A character unequipped any item
IF
Unequipped(_Item, _Character)
AND
...
THEN
...

// A character unequipped a transmogrification
PROC
PROC_WW_TL_Event_Unequipped((ITEM)_Armor, (CHARACTER)_Character)
AND
...
THEN
...
```

#### Armor Type Query

There's also a custom query that returns the heaviest type of transmogrified armor that a character has equipped:

```scss
QRY_WW_TL_GetEquipmentHeaviness((GUIDSTRING)_Character)
```

This query is guaranteed to evaluate to true, and it stores one fact in each of the following databases:

1\. `DB_QRYRTN_WW_TL_GetEquipmentHeaviness_Overall((GUIDSTRING)_Character, (INTEGER)_Heaviness)` with the heaviest type of transmogrification equipped anywhere (if there is one). For example, a character with transmogrified light armor in one slot and transmogrified heavy armor in another slot would return the value for heavy armor.

2\. `DB_QRYRTN_WW_TL_GetEquipmentHeaviness_Chest((GUIDSTRING)_Character, (INTEGER)_Heaviness)` with the heaviness of the transmogrification equipped in the chest slot (if there is one).

Note that the heaviness / armor type is just a number, the same as we put into the fourth column of the main database when adding basic stats support.

You can use the query and its query-return databases like this:

```java
// A character has received a status that should also trigger something else if they're wearing transmogrified heavy armor
IF
StatusApplied(_Character, "TRIGGERS_IF_HEAVY_ARMOR", _, _)
AND
QRY_WW_TL_GetEquipmentHeaviness(_Character) // execute the query that will put the result in the QRYRTN databases
AND
DB_QRYRTN_WW_TL_GetEquipmentHeaviness_Overall(_Character, _Heaviness) // assign the result to _Heaviness
AND
_Heaviness == 4 // check if the result is heavy armor
THEN
...
```

If a character does not have _any_ transmogrifications equipped (even just clothes), then the query will still evaluate to true but the query-return databases will not have any facts stored in them. You can check for this situation with the condition: `NOT DB_QRYRTN_WW_TL_GetEquipmentHeaviness_Overall(_Character, _)`

If your equipment stats need this query to work but you don't want to make Transmogrification Lite a direct dependency, then you just need to define a simple version of the query in your own script. It won't be able to return any values without Transmogrification Lite also being loaded (which is fine because there won't be any transmogrifications without it either!), but this will allow the script to build and run independently:

```scss
QRY
QRY_WW_TL_GetEquipmentHeaviness((GUIDSTRING)_Character)
THEN
DB_NOOP(1);
```

#### All Transmogrifications Database

First, there's a database that tracks every transmogrified item that currently exists. It's important to remember that each transmogrification has a stats source and an appearance source, and they probably (but don't _have to_) come from different items.

```scss
DB_WW_TL_TransmogrifiedArmors((GUIDSTRING)_Item, (INTEGER)_Heaviness, (GUIDSTRING)_OriginalTemplateForStats, (STRING)_StatsBoost)
```

`_Item` is the Name\_GUID of the transmogrification's game object. This is an instantiation of the appearance source's Root Template.

`_Heaviness` is the same value as the stat source's `_ArmorType` in `DB_WW_TL_ArmorComponents`.

`_OriginalTemplateForStats` is the Name\_GUID of the stat source's Root Template (which will match the first column in `DB_WW_TL_ArmorComponents` for the stats source, and which can be used to get more information about it from that database).

`_StatsBoost` is the name of the BOOST status that applies the item's stats (it will match the third column in `DB_WW_TL_ArmorComponents` for the stats source).

In order to determine the appearance source of a transmogrification, use the `GetTemplate` Osiris query with `_Item` and match the result to the second column in `DB_WW_TL_ArmorComponents`.

#### Equipped Transmogrifications Database

There's also a database that tracks which transmogrifications each character has equipped:

```scss
DB_WW_TL_EquippedTransmogrifications((GUIDSTRING)_Character, (ITEM)_Item)
```

`_Character` is the Name\_GUID of the character who has equipped the transmogrification `_Item`. Each character might have multiple facts in this database if they have transmogrifications equipped in multiple slots at once.

Note that `_Item` should match a value for `_Item` in the previous database (`DB_WW_TL_TransmogrifiedArmors`).

Another important thing to know about this database is that there's a short delay between when a character equips a transmogrified item (which will trigger events like `Equipped(_Item, _Character)`) and when a fact is added to this database (which is also when the BOOST status with the item's stats is applied to the character). This means that, depending on the use case, you might want to use the normal event `Equipped` or a database condition for `DB_WW_TL_EquippedTransmogrifications` to trigger a rule, but you probably never want to use them both in a rule together because it's likely to cause issues.

#### Transmogrification Sources Database

Finally, there's a database that keeps a record of the original game object that a transmogrification used as its stats source. You can use `DB_WW_TL_TransmogrifiedArmors` to get the Root Template of a transmogrification's stats source, but not the specific item, so you'd need to use this database for that.

```scss
DB_WW_TL_TransmogrificationStatsSources((GUIDSTRING)_Source, (GUIDSTRING)_Transmogrification)
```

`_Source` is the Name\_GUID of the original game object used as the stats source.

`_Transmogrification` is the Name\_GUID of the transmogrified game object, which has been called `_Item` in the previous databases.

Note that if a transmogrification was made without a stats source (which happens when a character takes the appearance of an item for a slot they don't have anything equipped in), then it won't have a fact in this database.

Also, if a transmogrification is created with stats taken from another transmogrification, the new item's stats source is still considered to be the original non-transmogrified item.

#### Other Databases

There are two more databases you might want to know about, but they're used differently. Rather than writing Osiris rules that use these databases, instead you just need to add new facts to them in the INIT section of your own script.

For example, some statuses should be removed when a character is wearing armor, but this won't happen by default with transmogrified armor because the game doesn't recognize it as such. You could resolve this as described in the **Enforcing Unarmored-Only Bonuses** section, but using a status or passive to remove another status is kind of overkill when it can be removed directly by the Osiris rule instead. The rule to do this is already written in Transmogrification Lite's script, and so all you need to do is qualify another status to be removed by transmogrified armor by addding `DB_WW_TL_UnarmoredOnlyStatuses(_Status);` to the init section of your script, where `_Status` is replaced with the name of the status in quotation marks (e.g. `DB_WW_TL_UnarmoredOnlyStatuses("MAGE_ARMOR");`).

Similarly, most polymorph shapes are supposed to disable armor bonuses, but if you want to make one an exception to this behavior then you can also add a fact to the INIT section for the database `DB_WW_TL_PolymorphStatusExceptionsForAC(_PolymorphStatus)` where you replace `_PolymorphStatus` with the name of the polymorph status in quotation marks.

#### Tags

Because the AC calculations in Transmogrification Lite are so deeply woven into the mod, I made it so that you can turn certain parts of it on or off by applying different tags to a character.

This is mostly only helpful for supporting equipment that uses the `ACOverrideFormula(...)` boost, which will cause the normal AC calculation to stack on top of the transmog AC calculation unless we alert Transmogrification Lite that the AC is being overridden by using the tag(s).

Equipment can apply the following tags to its wearer:

1\. `WW_TL_CUSTOM_AC_OVERRIDE` (UUID: `44ca0460-b271-4118-a5a9-4c8756905d72`): This character will receive -10 AC to undo the base AC given from the formula override, and they will not receive a duplicate DEX bonus. If they are wearing armor, some or all of their DEX bonus will be undone.

2\. `WW_TL_MONK_AC_OVERRIDE` (UUID: `020c9b7b-dd2b-4ce5-a88b-9f42c7c5aa1a`): This character currently has a modded equivalent to Unarmoured Defense for Monks. They will receive the same debuffs as \`WW\_TL\_CUSTOM\_AC\_OVERRIDE\`, except their WIS bonus will also be undone if they are wearing armor.

3\. `WW_TL_BARB_AC_OVERRIDE` (UUID: `a0381c58-d848-4c6d-a4a4-f014eb056d77`): This character currently has a modded equivalent to Unarmoured Defense for Barbarians. They will receive the same debuffs as \`WW\_TL\_CUSTOM\_AC\_OVERRIDE\`, except their CON bonus will also be undone if they are wearing armor.

4\. `WW_TL_ALT_AC_MOD` (UUID: `fd51851b-3d8d-4e2e-baf6-e8fd0c480e91`): This character is currently using a different ability modifier than DEX for their primary AC bonus. This does not need to be used if another ability modifier is added on top of DEX, only if DEX shouldn't be added at all. Tagging a character with this basically disables all of the AC calculation passives so that you have a blank slate with which to work.

#### Examples

Let's take a look at a really quick example of adding support for an item that should only be able to be equipped by an avatar (even if its stats are being used in a transmogrification):

```scss
IF
Equipped(_Item, _Character) // this rule is triggered for evaluation when _Character equips _Item
AND
DB_WW_TL_TransmogrifiedArmors((GUIDSTRING)_Item, (INTEGER)_, WW_CE_ARM_Breastplate_WalkersPlate_c97df1d0-3011-47f4-b859-3ea9e3664997, (STRING)_) // _Item is a transmogrification using the stats we want to limit
AND
IsTagged((GUIDSTRING)_Character, (TAG)AVATAR_306b9b05-1057-4770-aa17-01af21acd650, 0) // _Character is NOT an avatar
AND
ResolveTranslatedString("WW_CE_AvatarOnlyErrorMessage", _ErrorMessage) // get an error message from a localization file
THEN
Unequip((CHARACTER)_Character, (ITEM)_Item); // unequip _Item from _Character because they shouldn't be able to use it
OpenMessageBox(_Character, _ErrorMessage); // put the error message on screen so the player understands what happens
```

This rule is fairly simple Osiris logic to unequip an item after a character equips it, but it can only know which items to unequip by checking the database `DB_WW_TL_TransmogrifiedArmors` to see whether the stats come from the restricted equipment.

Let's look at another example of how to implement set bonuses, where a character receives a status if they're wearing every piece of equipment in a set. This can usually be done just by checking that the character has equipped items instantiated from the Root Templates we want, but transmogrifying the equipment means that the Root Template will only correspond to the item's appearance, and we only care about its stats.

Instead, we can set up a custom query that checks whether a character is using a Root Template's stats by either having the original item or a transmogrification of it equipped:

```scss
// One way to satisfy the query is if _Character is wearing an item instantiated from the original Root Template
QRY
QRY_WW_CE_UsingStatsFromTemplate((CHARACTER)_Character, (GUIDSTRING)_Template)
AND
DB_WW_TL_ArmorComponents(_Template, _, _, _, _, _Slotname, _, _) // get the _Slotname that corresponds to _Template
AND
GetEquippedItem(_Character, _Slotname, _Item) // get the item currently equipped in that slot
AND
GetTemplate(_Item, _Template) // and then require that item to have been instantiated from _Template (i.e. it's the original item)
THEN
DB_NOOP(1);

// Another way to satisfy the query is if _Character is wearing a transmogrification using the stats that correspond to the original Root Template
QRY
QRY_WW_CE_UsingStatsFromTemplate((CHARACTER)_Character, (GUIDSTRING)_Template)
AND
DB_WW_TL_TransmogrifiedArmors(_Item, _, _Template, _) // get all the existing transmogrifications using _Template as its stats source
AND
DB_WW_TL_EquippedTransmogrifications((GUIDSTRING)_Character, (ITEM)_Item) // and then check if _Character has equipped any of them
THEN
DB_NOOP(1);
```

We can now use the custom query `QRY_WW_CE_UsingStatsFromTemplate` to easily check for what we want. For example, if there are two items in our equipment set, we can check for having them both equipped (regardless of whether they've been transmogrified) as follows:

```scss
QRY
QRY_WW_CE_EntireSetEquipped((CHARACTER)_Character)
AND
QRY_WW_CE_UsingStatsFromTemplate(_Character, WW_CE_ARM_Breastplate_WalkersPlate_c97df1d0-3011-47f4-b859-3ea9e3664997)
AND
QRY_WW_CE_UsingStatsFromTemplate(_Character, WW_CE_ARM_Boots_WalkersPlate_39001a4c-8a06-47d9-8e22-5b5a9b545a5b)
THEN
DB_NOOP(1);
```

All that's left to do is hook the custom query `QRY_WW_CE_EntireSetEquipped` into the relevant events and then apply/remove the set bonus status as needed. For a complete example, I recommend looking at my [example script for full stats support](https://github.com/WorldWalker42/Transmogrification-Lite/blob/main/Extension%20Resources/3.%20Full%20Stats%20Support/Mods%20folder/Story/RawFiles/Goals/GLO_Transmogrification_WW_CE.txt).

### Complete Example

As before, I've uploaded a complete example that has full stats support here: [https://github.com/WorldWalker42/Transmogrification-Lite/tree/main/Extension%20Resources/3.%20Full%20Stats%20Support](https://github.com/WorldWalker42/Transmogrification-Lite/tree/main/Extension%20Resources/3.%20Full%20Stats%20Support)

Note that the set bonus added to this version of my example mod does not actually apply any bonuses, it's just a visual effect to demonstrate that it's working.

### Automating This Process

The Python script discussed earlier can also do a pretty decent job at generating the BOOST statuses and tooltips database, but it's far from perfect at these tasks, so its output should be double-checked and probably needs to be manually completed.

Also, the script can't make the editor files for the BOOST statuses. It only makes the final / generated text file that gets packaged with the mod. If your mod doesn't have any other BOOST statuses, you will need to add `Stats\Generated\Data\Status_BOOST.txt` to your mod's Public directory. If this file already exists, you can just copy and paste the script's output into it, but be aware that whatever you paste in will be lost the next time you reload the project's stats in the toolkit because these statuses don't exist in the editor file. If you're still in active development, I recommend making these statuses manually in the toolkit to avoid them being overwritten.

To tell the script to generate stats, you just need to enter `1` after the previous arguments in the console command that runs it. Also, to get more complete tooltips, it's preferable to also give it a relative file path to a Passives file if the armor stats reference one.

The full console command to run the script with stats support ends up something like this:

```css
python3 script.py IDENTIFIER relative/path/to/lsx/files relative/path/to/armor/stats output_directory 1 relative/path/to/passives
```

Make sure to read the script's console output for directions on how to review and complete its work.

## Updating the Mod

It's likely that you will need to update your mod at some point to add support for new equipment or to change / fix ones you've already added support for. When you release an update, most of the changes should work just fine for players when they download it. However, the INIT section of the Osiris script only runs when the mod is first added to a game, and does not run again when the mod is updated. This means that any changes you make to the INIT section (like adding new equipment to the primary database, changing spell cooldowns, etc.) won't be applied to players' already-modded games unless we add some extra logic to the Osiris script.

It's possible to do this because any changes we make to the KB section of the Osiris script _will_ be immediately applied, even to already-modded games. This lets us check if the INIT section is out-of-date and, if so, execute a rule to add and remove the facts missing from the update.

Note: If you want to keep your original script cleaner, you can add these rules to a different Osiris script that's just for handling updates. It will work exactly the same.

To start, add `DB_IDENTIFIER_Ver(_Version);` to the INIT section, where `IDENTIFIER` is replaced with your mod's identifier and `_Version` is replaced by the current version number (`1` probably makes the most sense to start). Note that version numbers in this context can only be integers (e.g. `1`, `2`, `3`, ...) and CANNOT be any other format like `1.0.2`.

Next, add these rules to the KB section:

```scss
// Check if there's an update as soon as the game starts
IF
LevelGameplayStarted(_,_)
THEN
PROC_IDENTIFIER_CheckForUpdate();

// Compare the version number stored in a database by the INIT section (which won't be automatically updated)
// with the hard-coded version number in this rule (which will be automatically updated when you change it)
PROC
PROC_IDENTIFIER_CheckForUpdate()
AND
DB_IDENTIFIER_Ver(_Ver)
AND
_Ver < [version number] // update with current version number (e.g. '_Ver < 1')
THEN
PROC_IDENTIFIER_UpdateModVersion(_Ver);

// When the version numbers don't match and so we're going to perform an update, increment the version number
// stored in the database for this particular game so that it won't be repeated the next time it's loaded.
PROC
PROC_IDENTIFIER_UpdateModVersion(_Ver)
AND
IntegerSum(_Ver,1,_NewVer)
THEN
NOT DB_IDENTIFIER_Ver(_Ver);
DB_IDENTIFIER_Ver(_NewVer);

//REGION Version updates

// [UPDATES GO HERE]

//END_REGION

// Repeat the check for an update in case the player skipped one or more upgrades
PROC
PROC_WW_TL_UpdateModVersion(_)
THEN
PROC_WW_TL_CheckForUpdate();
```

Make sure to at least replace every use of `IDENTIFIER` with your mod's unique identifier, as well as to replace `[version number]` in `PROC_IDENTIFIER_CheckForUpdate()` with the same version number you put in the database in the INIT section.

After publishing your mod, you need to do the following things whenever you make changes to a script's INIT section:

1. Keep track of the changes you're making.
2. Increment the version number in the INIT section (which only newly-modded games will receive).
3. Update the version number in the KB section to the same value (which newly-modded AND updated games will receive).
4. Add a new rule to the "Version updates" region that applies the changes you made to the INIT section.

For example, let's say I want to update my mod with a new piece of equipment. I would add another fact to `DB_WW_TL_ArmorComponents` in the INIT section, increment the current version number in the INIT section _and_ KB section to `2`, and then write this new rule:

```scss
PROC_IDENTIFIER_UpdateModVersion(1) // the PROC's argument 1 indicates that we're updating from version 1 to version 2
THEN
DB_WW_TL_ArmorComponents(ExampleItem_c97df1d0-3011-47f4-b859-3ea9e3664997, ExampleItem_AppearanceOnly_fa942a7b-ea01-4562-be3c-19854ae8a255, "WW_CE_TL_ExampleItem", 1, 12, "Breast", 0, 0);
```

Let's say that this example item grants the wearer a spell, and that I forgot until after I released the update to add this to its tooltip and to enforce its cooldown. To fix this, I'd follow the steps again and end up with this additional rule:

```cpp
PROC_IDENTIFIER_UpdateModVersion(2) // the argument is now 2 to indicate that this rule should run when we're updating from v2 to v3
THEN
DB_WW_TL_TooltipStatuses("WW_CE_TL_ExampleItem", "SPELL");
DB_WW_TL_ArmorSpells("WW_CE_TL_ExampleItem", "Shout_ExampleSpell", "LONG");
```

Later, if I decide that a Long Rest cooldown is too much for this spell and I want to change it to a Short Rest, Transmogrification Lite won't let the player cast it again before a Long Rest unless I update its value in `DB_WW_TL_ArmorSpells`. Because we're now CHANGING an existing value instead of just adding a new one, it's extremely important to remove the old fact with `NOT` as well as adding the new fact, like this:

```cpp
PROC_IDENTIFIER_UpdateModVersion(3) // updating from v3 to v4
THEN
NOT DB_WW_TL_ArmorSpells("WW_CE_TL_ExampleItem", "Shout_ExampleSpell", "LONG"); // get rid of Long Rest cooldown
DB_WW_TL_ArmorSpells("WW_CE_TL_ExampleItem", "Shout_ExampleSpell", "SHORT"); // add Short Rest cooldown instead
```

Other than adding or removing entire facts from `DB_WW_TL_ArmorComponents`, I recommend trying to avoid _changing values_ in facts for that database because it will cause problems with how transmogrifications and their tooltips are updated. I think it would be fine if players destroy any existing transmogrifications of that item and then re-make them, but I'd be prepared to get bug reports about it even if you try to make sure everyone knows that this is necessary.

For a complete example of updating the INIT section, I recommend referencing the actual Transmogrification Lite script [GLO\_Transmogrification\_WW](https://github.com/WorldWalker42/Transmogrification-Lite/blob/main/Project%20Files/Mods%20folder/Story/RawFiles/Goals/GLO_Transmogrification_WW.txt). The relevant code is at the top of the KB section, or you can search for `PROC_WW_TL_CheckForUpdate()` to jump straight to it. To better organize the bigger updates, I defined the PROC `PROC_WW_TL_UpdateInitFacts(_Ver)` in a different script, [GLO\_TransmogrificationUpdates\_WW](https://github.com/WorldWalker42/Transmogrification-Lite/blob/main/Project%20Files/Mods%20folder/Story/RawFiles/Goals/GLO_TransmogrificationUpdates_WW.txt).

## Adding Support for Someone Else's Mod

So far, we've been focused on adding built-in transmogrification compatibility with your own equipment mod. Now let's talk about creating a dependency that extends support to someone else's mod.

The process is fundamentally the same (you still need to create duplicate Root Templates, BOOST statuses, add facts to databases, etc.), but there are a few extra steps to turn a mod into a dependency. Also, the workflow is a little different because we probably won't have access to the equipment mod's editor files.

### Getting Permission

First and foremost, I think it's incredibly important to make sure you have the original mod author's permission to create a dependency, as well as to be respectful if they say no. I recommend checking their mod description and comment section to see if they've already given an answer about making dependencies before contacting them so that they don't get flooded with duplicate requests.

Also, even though we have the option on mod.io to not allow dependencies, be aware that the option defaults to being turned on, so it shouldn't be taken as implied permission. Or, the mod author might only be comfortable with dependencies that translate the mod to other languages, and not for anything else. I have personally encountered this situation, where a very popular equipment mod had the setting enabled to allow dependencies but the author has declined most requests to make them (including to add compatibility with Transmogrification Lite), so please always ask.

### Setting Up the Project

Before we get started, make sure the .pak files for all mod dependencies are in the game's mod folder (which is _not_ the same as the toolkit's mod folder that we've used for most of this guide). If you downloaded the mods through the in-game mod manager then you don't need to worry about this step because it will put them there automatically.

Next, create a new project in the toolkit. I recommend using a name like `[abbreviation for your username]_TransmogLite_[abbreviation for the mod you're adding support for]`. Then open Project -> Project Settings, click on the Dependencies tab, and find the mod dependencies in the list on the left. Select one and click the right-facing arrow in between the two columns to set it as a dependency. The first time you do this, it's normal for lots of other items to move to the column on the right, like the dice sets, ModBrowser, SharedDev, etc. Make sure that Transmogrification Lite is one of the dependencies you set. Press Save in the bottom right, and then accept the toolkit's request to reload the level.

Restart the toolkit after adding dependencies to be able to see their Root Templates and Osiris scripts. Statuses, spells, and other files in the Stats Editor won't appear because their editor files aren't included in the mod's .pak file. You'd have to ask the mod author to give them to you directly or to upload all the project files to a GitHub repository.

### Adding Support for Each Item

From here, the things you need to make for a standalone extension are almost exactly the same as what you need to add to an equipment mod for built-in compatibility. However, you can skip some steps now that Transmogrification Lite is a formal dependency, which means you don't have to recreate its blank armor stats or parent BOOST status, etc.

The biggest difference in the process is that you won't be able to use the Stats Editor to directly access the equipment's stats when you're making the BOOST statuses. Instead, you will probably need to work directly with the mod's generated text files. Please refer to [this guide on GitHub](https://github.com/WorldWalker42/Transmogrification-Lite/tree/main/Extension%20Resources#adding-support-for-each-item) for more detail.

### Publishing

When the mod is ready to share and has been uploaded to mod.io, it's important to also set the dependencies on its mod page. From the mod's Admin page, choose the General Settings tab and then Dependencies. Type the name of each dependency into the search field and save them so that they will appear on the mod page.

## Adding Class Compatibility

Most of this guide is about adding transmogrification compatibility to new equipment, but it's worth noting that some modded classes can interfere with Transmogrification Lite's AC calculations unless they also have custom support.

For example, a caster class might also add the character's INT modifier to their AC when not wearing armor, just like Barbarians can add their CON modifier. This should be fixed like any other unarmored-only bonus, as described above.

Or, a class might use an ability other than DEX for their primary AC bonus, in which case Transmogrification Lite's AC calculations would need to be disabled for that character by applying the `WW_TL_ALT_AC_MOD` tag to them (also described above) before giving them new passives that perform the new AC calculation.

## Can You Make Extensions on a Mac?

Maybe? I haven't tried it, but (I think) it's theoretically possible.

Some people have tried to get the toolkit set up on a virtual Windows machine that's running on a Mac, and it sounds like this is very difficult but not entirely without success. You should be able to find discussions / threads where people share what they've tried and whether it worked on various modding Discord channels - I know it has come up at least on the official Larian Studios Discord.

However, my guess is that you'll get better results from using other techniques. Please refer to [this guide on GitHub](https://github.com/WorldWalker42/Transmogrification-Lite/tree/main/Extension%20Resources#can-you-make-extensions-on-a-mac) for more detail.

## Conclusion

If you're interested in extending Transmogrification Lite, I hope this guide helped. If you have any questions, you're welcome to ask and I'll try to answer when I can.

If you release an extension or compatible mod, I encourage you to reply to a pinned comment on Transmogrification Lite's mod page to let us know about it.

Happy modding!

[W\\
\\
WorldWalker42](https://mod.io/g/baldursgate3/u/worldwalker42/r)

Follow WorldWalker42

Log in to join the discussion!

Last updated

123d

Reading time

54 min read

Views

475

Comments

0

[W\\
\\
WorldWalker42](https://mod.io/g/baldursgate3/u/worldwalker42/r)

Follow WorldWalker42

- [Guide](https://mod.io/g/baldursgate3/r/how-to-extend-transmogrification-lite#guide)
- [Permission to Extend Transmogrification Lite](https://mod.io/g/baldursgate3/r/how-to-extend-transmogrification-lite#heading-1)
- [Extending Appearance-Only Support](https://mod.io/g/baldursgate3/r/how-to-extend-transmogrification-lite#heading-2)
- [Root Templates](https://mod.io/g/baldursgate3/r/how-to-extend-transmogrification-lite#heading-3)
- [One-Time Setup](https://mod.io/g/baldursgate3/r/how-to-extend-transmogrification-lite#heading-4)
- [For Each Item](https://mod.io/g/baldursgate3/r/how-to-extend-transmogrification-lite#heading-5)
- [Database Entries](https://mod.io/g/baldursgate3/r/how-to-extend-transmogrification-lite#heading-6)
- [One-Time Setup](https://mod.io/g/baldursgate3/r/how-to-extend-transmogrification-lite#heading-7)
- [For Each Item](https://mod.io/g/baldursgate3/r/how-to-extend-transmogrification-lite#heading-8)
- [Finalizing the Script](https://mod.io/g/baldursgate3/r/how-to-extend-transmogrification-lite#heading-9)
- [Complete Example](https://mod.io/g/baldursgate3/r/how-to-extend-transmogrification-lite#heading-10)
- [Automating This Process](https://mod.io/g/baldursgate3/r/how-to-extend-transmogrification-lite#heading-11)
- [Extending Basic Stats Support](https://mod.io/g/baldursgate3/r/how-to-extend-transmogrification-lite#heading-12)
- [BOOST Status](https://mod.io/g/baldursgate3/r/how-to-extend-transmogrification-lite#heading-13)
- [One-Time Setup](https://mod.io/g/baldursgate3/r/how-to-extend-transmogrification-lite#heading-14)
- [For Each Item](https://mod.io/g/baldursgate3/r/how-to-extend-transmogrification-lite#heading-15)
- [Finishing the Database Entries](https://mod.io/g/baldursgate3/r/how-to-extend-transmogrification-lite#heading-16)
- [Complete Example](https://mod.io/g/baldursgate3/r/how-to-extend-transmogrification-lite#heading-17)
- [Extending Full Stats Support](https://mod.io/g/baldursgate3/r/how-to-extend-transmogrification-lite#heading-18)
- [Descriptions in Transmog Tooltips](https://mod.io/g/baldursgate3/r/how-to-extend-transmogrification-lite#heading-19)
- [Enforcing Spell Cooldowns](https://mod.io/g/baldursgate3/r/how-to-extend-transmogrification-lite#heading-20)
- [Container Spells](https://mod.io/g/baldursgate3/r/how-to-extend-transmogrification-lite#heading-21)
- [Enforcing Unarmored-Only Bonuses](https://mod.io/g/baldursgate3/r/how-to-extend-transmogrification-lite#heading-22)
- [Custom Behaviors](https://mod.io/g/baldursgate3/r/how-to-extend-transmogrification-lite#heading-23)
- [Event-Like Procedures](https://mod.io/g/baldursgate3/r/how-to-extend-transmogrification-lite#heading-24)
- [Armor Type Query](https://mod.io/g/baldursgate3/r/how-to-extend-transmogrification-lite#heading-25)
- [All Transmogrifications Database](https://mod.io/g/baldursgate3/r/how-to-extend-transmogrification-lite#heading-26)
- [Equipped Transmogrifications Database](https://mod.io/g/baldursgate3/r/how-to-extend-transmogrification-lite#heading-27)
- [Transmogrification Sources Database](https://mod.io/g/baldursgate3/r/how-to-extend-transmogrification-lite#heading-28)
- [Other Databases](https://mod.io/g/baldursgate3/r/how-to-extend-transmogrification-lite#heading-29)
- [Tags](https://mod.io/g/baldursgate3/r/how-to-extend-transmogrification-lite#heading-30)
- [Examples](https://mod.io/g/baldursgate3/r/how-to-extend-transmogrification-lite#heading-31)
- [Complete Example](https://mod.io/g/baldursgate3/r/how-to-extend-transmogrification-lite#heading-32)
- [Automating This Process](https://mod.io/g/baldursgate3/r/how-to-extend-transmogrification-lite#heading-33)
- [Updating the Mod](https://mod.io/g/baldursgate3/r/how-to-extend-transmogrification-lite#heading-34)
- [Adding Support for Someone Else's Mod](https://mod.io/g/baldursgate3/r/how-to-extend-transmogrification-lite#heading-35)
- [Getting Permission](https://mod.io/g/baldursgate3/r/how-to-extend-transmogrification-lite#heading-36)
- [Setting Up the Project](https://mod.io/g/baldursgate3/r/how-to-extend-transmogrification-lite#heading-37)
- [Adding Support for Each Item](https://mod.io/g/baldursgate3/r/how-to-extend-transmogrification-lite#heading-38)
- [Publishing](https://mod.io/g/baldursgate3/r/how-to-extend-transmogrification-lite#heading-39)
- [Adding Class Compatibility](https://mod.io/g/baldursgate3/r/how-to-extend-transmogrification-lite#heading-40)
- [Can You Make Extensions on a Mac?](https://mod.io/g/baldursgate3/r/how-to-extend-transmogrification-lite#heading-41)
- [Conclusion](https://mod.io/g/baldursgate3/r/how-to-extend-transmogrification-lite#heading-42)
- [Discussion](https://mod.io/g/baldursgate3/r/how-to-extend-transmogrification-lite#discussion)

[Armor](https://mod.io/g/baldursgate3/r?tags=Armor)

An in-depth guide on how to add compatibility for transmogrifying modded equipment with Transmogrification Lite.

Share

Report guide

---
# SOURCE: https://mod.io/g/baldursgate3/r/how-to-make-a-custom-class-for-bg3
---

[Browse games](https://mod.io/g)

Browse games

[My library](https://mod.io/library)

My library

[My content](https://mod.io/content)

My content

My account

mod.io

mod.io

[All games](https://mod.io/g) [Baldur's Gate 3](https://mod.io/g/baldursgate3) [Guides](https://mod.io/g/baldursgate3/r) [beginner](https://mod.io/g/baldursgate3/r?tags=beginner) How to Make a Custom Class for BG3

How to Make a Custom Class for BG3

Share

Report

Follow

Getting started on modding Baldur's Gate 3 can be difficult. That is why I have focused my YouTube channel on easy to follow tutorials, geared for beginners.

[This tutorial will show you how to make a custom class for the game](https://youtu.be/aoVDqwvyZqk). I've included a text tutorial at the pinned comment, which you can access for free.

Have questions? Please leave comments on the YouTube tutorial, which I regularly monitor. I've turned off comments here to ensure they are directed to where you will get a response.

[I\\
\\
ImADoctorNotA1243](https://mod.io/g/baldursgate3/u/imadoctornota/r)

Follow ImADoctorNotA1243

Last updated

165d

Reading time

1 min read

Views

0

[I\\
\\
ImADoctorNotA1243](https://mod.io/g/baldursgate3/u/imadoctornota/r)

Follow ImADoctorNotA1243

- [Guide](https://mod.io/g/baldursgate3/r/how-to-make-a-custom-class-for-bg3#guide)

[beginner](https://mod.io/g/baldursgate3/r?tags=beginner) [Tutorial](https://mod.io/g/baldursgate3/r?tags=Tutorial)

Learn how to make custom subclasses.

Share

Report guide

---
# SOURCE: https://mod.io/g/baldursgate3/r/pommelstrikes-atlas-icons-photoshop-addon
---

[Browse games](https://mod.io/g)

Browse games

[My library](https://mod.io/library)

My library

[My content](https://mod.io/content)

My content

My account

mod.io

mod.io

[All games](https://mod.io/g) [Baldur's Gate 3](https://mod.io/g/baldursgate3) [Guides](https://mod.io/g/baldursgate3/r) [ATLAS](https://mod.io/g/baldursgate3/r?tags=ATLAS) ATLAS Skill/Item Icons Tool (Adobe Photoshop CC 2020+)

ATLAS Skill/Item Icons Tool (Adobe Photoshop CC 2020+)

Share

Report

Follow

## **pommelstrike's ATLAS Icon Stage Tool**    **This is to be used in conjunction with Item and Skills Icon Atlas guide :**  **[![](https://thumb.modcdn.io/articles/d1ee/1370/thumb_1020x2000/larian_mod_yt_thumbnail_043.jpg)](https://thumb.modcdn.io/articles/d1ee/1370/thumb_1020x2000/larian_mod_yt_thumbnail_043.jpg)**  **[https://mod.io/g/baldursgate3/r/adding-skill-and-item-icons](https://mod.io/g/baldursgate3/r/adding-skill-and-item-icons)**

[**Version:** 1.1.2](https://mod.io/g/baldursgate3/r/adding-skill-and-item-icons)

Visit my github [https://github.com/pommelstrike/bg3\_atlas\_icon\_export](https://github.com/pommelstrike/bg3_atlas_icon_export) for latest releases.

#### This guide is primary for Adobe Photoshop 2020+ user, If you use other Photo program beside Photoshop, then consider using my Python GUI Script, or Command Line Python script.

Blender version will be on it's own guide

## Overview

`BG3_ExportIcons` is a Photoshop JSX script designed to streamline the export of icons for the three resolutions needed to make BG3 UI icons in modkit. The script auto exports scaled-down versions for `380x380px`, `144x144px`, and `64x64px` resolutions needed for Tooltip and Controller UIs. It automatically organizes exported images into it's distinct folders. No more need of constant renaming and confusion of .png icon files in stage folders.

## Installation

1. Place the `ExportIcons.jsx` file in the Photoshop Scripts folder:

   - **Windows:**`C:\Program Files\Adobe\Adobe Photoshop 2023\Presets\Scripts`
   - Alternatively, save it in a location of your choice and load it manually (see "Usage").
2. Restart Photoshop to load the script into the `File > Scripts` menu.

## Usage

- ## **144 Items**

  - ## ControllerUIIcons/items\_png
- ## **380 Item** s

  - ## Tooltips/ItemIcons

Open the included Photoshop document Icon\_ATLAS\_PSTK\_TEMPLATE.psd, If you have your own, the .PSD needs to be in 1000x1000 resolution.

Run the script:

- **Menu:** Go to `File > Scripts > BG3_ExportIcons`.
- **Browse:** Alternatively, select `File > Scripts > Browse` and locate the script file.
- Follow the prompts:
- Select an project folder.
- Enter the base file name (e.g., `icon_base`).

The script will create the following structure:

```
Export Folder/
├── Original/
│   └── icon_base.png
├── GUI/
    ├── 380x380 Tooltip PNG/
    │   └── icon_base.png
    ├── 144x144 ControllerUI PNG/
    │   └── icon_base.png
    └── 64x64 PNG/
        └── icon_base.png
```

## Dependencies

- Photoshop CC 2020 or later.
- Tested on Adobe Photoshop 2023.

## Troubleshooting

### "Need Administrator Privileges" Error

If you're unable to copy the script to the Photoshop Scripts folder:

1. Run PowerShell as Administrator.
2. Use PowerShell to copy the file (update the command line to your version of Photoshop; Adobe Photoshop 2023 is used in this example):

`Copy-Item -Path "BG3_ExportIcons.jsx" -Destination "C:\Program Files\Adobe\Adobe Photoshop 2023\Presets\Scripts" -Force`

### Blurry Images

Ensure the original document resolution and canvas (1000x1000) are set appropriately before running the script.

[P\\
\\
pommelstrike](https://mod.io/g/baldursgate3/u/pommelstrike/r)

Follow pommelstrike

Log in to join the discussion!

Last updated

194d

Reading time

2 min read

Views

882

Comments

0

[P\\
\\
pommelstrike](https://mod.io/g/baldursgate3/u/pommelstrike/r)

Follow pommelstrike

- [Guide](https://mod.io/g/baldursgate3/r/pommelstrikes-atlas-icons-photoshop-addon#guide)
- [pommelstrike's ATLAS Icon Stage Tool](https://mod.io/g/baldursgate3/r/pommelstrikes-atlas-icons-photoshop-addon#heading-1)
- [This guide is primary for Adobe Photoshop 2020+ user, If you use other Photo program beside Photoshop, then consider using my Python GUI Script, or Command Line Python script.](https://mod.io/g/baldursgate3/r/pommelstrikes-atlas-icons-photoshop-addon#heading-2)
- [Overview](https://mod.io/g/baldursgate3/r/pommelstrikes-atlas-icons-photoshop-addon#heading-3)
- [Installation](https://mod.io/g/baldursgate3/r/pommelstrikes-atlas-icons-photoshop-addon#heading-4)
- [Usage](https://mod.io/g/baldursgate3/r/pommelstrikes-atlas-icons-photoshop-addon#heading-5)
- [144 Items](https://mod.io/g/baldursgate3/r/pommelstrikes-atlas-icons-photoshop-addon#heading-6)
- [ControllerUIIcons/items\_png](https://mod.io/g/baldursgate3/r/pommelstrikes-atlas-icons-photoshop-addon#heading-7)
- [380 Item](https://mod.io/g/baldursgate3/r/pommelstrikes-atlas-icons-photoshop-addon#heading-8)
- [Tooltips/ItemIcons](https://mod.io/g/baldursgate3/r/pommelstrikes-atlas-icons-photoshop-addon#heading-9)
- [Dependencies](https://mod.io/g/baldursgate3/r/pommelstrikes-atlas-icons-photoshop-addon#heading-10)
- [Troubleshooting](https://mod.io/g/baldursgate3/r/pommelstrikes-atlas-icons-photoshop-addon#heading-11)
- ["Need Administrator Privileges" Error](https://mod.io/g/baldursgate3/r/pommelstrikes-atlas-icons-photoshop-addon#heading-12)
- [Blurry Images](https://mod.io/g/baldursgate3/r/pommelstrikes-atlas-icons-photoshop-addon#heading-13)
- [Discussion](https://mod.io/g/baldursgate3/r/pommelstrikes-atlas-icons-photoshop-addon#discussion)

[ATLAS](https://mod.io/g/baldursgate3/r?tags=ATLAS) [icon items](https://mod.io/g/baldursgate3/r?tags=icon+items) [icon skill](https://mod.io/g/baldursgate3/r?tags=icon+skill) [Icons](https://mod.io/g/baldursgate3/r?tags=Icons) [photoshop](https://mod.io/g/baldursgate3/r?tags=photoshop) [UI](https://mod.io/g/baldursgate3/r?tags=UI)

This creates output UI folders for ease of Atlas editor loading and UI Assets Import If you make BG3 Actions or Items UI Icons in Adobe Photoshop CC 2020+ then you should use this.

Share

Report guide