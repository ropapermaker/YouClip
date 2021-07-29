# YouClip v1.0.3

## Table Of Contents:
- What Is YouClip
- Installation
- Usage
- Stuff To Fix
- Changelog

<br />

### What Is YouClip?
![image](https://user-images.githubusercontent.com/81928644/127146952-fd2cc23c-d50b-4deb-bd16-eb02bf4a7d42.png)

YouClip takes the video whose link you provided, downloads it and crops it in the timestamps given. <br /> It uses a fancy GUI using `HTML`, `CSS` and `Javascript`,
but don't expect too much; it was done in two days with me being a complete begginer in this GUI field. For the backend, `python` downloads and crops the video
which connects with the Javascript in the page using `eel module`. Pretty cool stuff.

<br />
<br />

### Installation
To install requirements for YouClip run these commands in the terminal:
- `sudo chmod +x install.sh`
- `./install.sh`
<br />
For windows I will work on an installer after I get my code to work properly there, stay tuned.

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

Just execute the script and you will be good to go. `python3 main.py` in linux terminal or `python main.py` in Window's CMD, in the folder's path of course.

<br />

### Stuff To Fix

- [x] Get The App Basicially Working.
- [x] Handle Most of The Errors.
- [x] Make An Installer For Linux.
- [x] Make an Installer For Windows.
- [x] Comment the code (update: I did, but poorly.)
- [ ] Doesn't work on Windows; moviepy returns an error.
- [ ] Add A Progress Bar Of Some Form.

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
