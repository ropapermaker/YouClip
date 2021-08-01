# YouClip v1.0.6

## Table Of Contents:
- What Is YouClip
- Installation
- Usage
- Stuff To Fix
- Changelog

<br />

### What Is YouClip?
![image](https://user-images.githubusercontent.com/81928644/127772911-a80efc4a-2852-434d-a04f-71e9c349905a.png)

YouClip takes the video whose link you provided, downloads it and crops it in the timestamps given. <br /> It uses a fancy GUI using `HTML`, `CSS` and `Javascript`,
but don't expect too much; it was done in two days with me being a complete begginer in this GUI field. For the backend, `python` downloads and crops the video
which connects with the Javascript in the page using `eel module`. Pretty cool stuff.

<br />
<br />

### Installation
To install requirements for YouClip in Linux run these commands in the terminal:
- `sudo chmod +x install.sh`
- `./install.sh`

<br />

For windows just download the relase file in the [Relases](https://github.com/adornerz/YouClip/releases) and run it.
For Mac try the above commands of linux but I haven't tried nothing on Mac so no idea if it will work or not.
<!--
OLD INSTALLATION INSTRUCTIONS:

Python packages needed:
- `eel` => install with `pip install eel` 
- `moviepy` => install with `pip install moviepy`
- `youtube_dl` => install with `pip install youtube-dl`
- `datetime` install with `pip install datetime` <br />
on linux use `pip3`

You also need ffmpeg installed in your system. <br />
On linux ubuntu run `sudo apt install ffmpeg` and you're good to go. On manjaro ffmpeg is installed by default; not tried on other distros. <br />
For Windows, download [here](https://www.gyan.dev/ffmpeg/builds/) gyan.dev version of ffmpeg, extract the files somewhere and then add the `ffmpeg/bin` path to your
`PATH Variable`, if you don't know how look it up [here](https://helpdeskgeek.com/windows-10/add-windows-path-environment-variable/). I honestly don't know if it will run properly on Windows because ffmpeg installation
there is a pain in the ass, or atleast it has been for me and if you get it to run on Windows please contact me somehow.
-->

<br />

### Usage
Linux:
Just execute the script and you will be good to go. `python3 main.py` in the terminal.

Windows:
- If you installed using the installed on [Relases](https://github.com/adornerz/YouClip/releases)
- If you're using the source code execute `python main.py` in CMD.
<br />

### Stuff To Fix

- [x] Get The App Basicially Working.
- [x] Handle Most of The Errors.
- [x] Make An Installer For Linux.
- [x] Make an Installer For Windows.
- [x] Comment the code (update: I did, but poorly.)
- [x] Doesn't work on Windows; moviepy returns an error. (update: Now works; eliminated moviepy.)
- [ ] Add A Progress Bar Of Some Form on the GUI.

<br />
<br />
<br />


### Changelog

**v1.0.0**:
 - Uploaded the first somehow working version of the app, so basicially added all the stuff.
 <br />
 
**v1.0.1**:
 - Downloaded videos now get assigned a random generated number; this is to prevent if any leftover files from other sessions have been left in that same directory.
 - For the above reason now random module is needed.
 - Fixed the error where if the file wasn't mp4 it wouldn't crop, now all files are downloaded to mp4 or converted to mp4.
 
<br />

**v1.0.2**:
- Made installers for linx debian and arch. (with no error handling.)
- Commented the code a bit.

<br />

**v1.0.3**:
- Improved installer file; Has error handling and now only it's the only one needed. (Made by [ropapermaker](https://github.com/ropapermaker))
- Removed the previous installers.

<br />

**v1.0.4**:
- Removed moviepy as it returned errors on windows and it wasn't really needed as a package, now a local ffmpeg file is used.
- Created a seperate script for Windows.

<br />

**v1.0.5**:
- Improved window's main.py a lot.
- Window's installer now is fully working, and the scripts adapts to it.
- Published first stable build and installer for windows; you can find it [here](https://github.com/adornerz/YouClip/releases)

<br />

**v1.0.6**:
- Created other themes! You can see the Retro Theme as a branch of this repo.

