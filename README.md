# YouClip v1.0

## Table Of Contents:
- What Is YouClip
- Installation
- Usage
- Stuff To Fix

<br />

### What Is YouClip?

YouClip takes the video whose link you provided, downloads it and crops it in the timestamps given. <br /> It uses a fancy GUI using `HTML`, `CSS` and `Javascript`,
but don't expect too much; it was done in two days with me being a complete begginer in this GUI field. For the backend, `python` downloads and crops the video
which connects with the Javascript in the page using `eel module`. Pretty cool stuff.

<br />
<br />

### Installation

Python packages needed:
- `eel` => install with `pip install eel` 
- `moviepy` => install with `pip install moviepy`
- `youtube_dl` => install with `pip install youtube-dl`
- `datetime` install with `pip install datetime` <br />
*on linux use `pip3`

<br />
You also need ffmpeg installed in your system. <br />
On linux run `sudo apt install ffmpeg` and you're good to go. <br />
For Windows, download [here](https://www.gyan.dev/ffmpeg/builds/) gyan.dev version of ffmpeg, extract the files somewhere and then add the `ffmpeg/bin` path to your
`PATH Variable`, if you don't know how look it up [here](duckduckgo.com). I honestly don't know if it will run properly on Windows because ffmpeg installation
there is a pain in the ass, or atleast it has been for me and if you get it to run on Windows please contact me somehow.

<br />

### Usage

Just execute the script and you will be good to go. `python3 main.py` in linux terminal or `python main.py` in Window's CMD, in the folder's path of course.

<br />

### Stuff To Fix

Lots of things, honestly. <br />

- [x] Get The App Basicially Working.
- [x] Handle The Basic Errors.
- [ ] Doesn't work on Windows; moviepy returns an error (probably because of my ffmpeg setup).
- [ ] Make The GUI More Appealing.
- [ ] Add A Progress Bar Of Some Form.
- [ ] Make An Installer For Windows As .exe.
- [ ] Make The .exe App Borderless And Add A Close Button Cause It Bothers Me.
