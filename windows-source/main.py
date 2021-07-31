import eel
import youtube_dl
import requests
import os
import random
from datetime import datetime

eel.init('web')
appdataLocal = os.getenv('LOCALAPPDATA')
desktopPath = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
now = datetime.now() # Need this for the output video title.


#        findBrowser() is used to find which browser to use when launching the app
#        This is to prevent crashing if user doesn't have chrome installed
#        Which is the default browser; though firefox and edge opens as a browser tab
#        It gets the work done.
browser = ""
def findBrowser():
    if os.path.isdir("C:\Program Files\Google\Chrome"):
        l = 'chrome'
    elif os.path.isdir("C:\Program Files\Mozilla Firefox"):
        l = 'firefox'
    elif os.path.isdir("C:\Program Files (x86)\Microsoft\Edge"):
        l = 'edge'

#       appdataFolder() Checks if the folder in appdata/local/YouClip exists, and if not
#       it creates it. Useful when running the app for the first time and if the folder
#       has been modified/removed by the user.
def appdataFolder():
    if os.path.isdir(f"{appdataLocal}\YouClip"):
        pass
    else:
        os.mkdir(f"{appdataLocal}\YouClip")


#        check_video_url function checks if the link is valid and if it works or not using some ways,
#        first if youtube.com is in the link at all,
#        missing schema is when the link doesn't contain the 'https://' part
#        If both conditions are met, it stores the page text in the r variable and checks if
#        'video unavailable' text is in it; if not then the link is valid.

@eel.expose
def check_video_url(url):
    if ("youtube.com/" in url) or ("youtu.be/" in url):
        try:
            r = requests.get(url)
            if ("Video unavailable" in r.text):
                return("invalid")
            else:
                return("valid")

        except requests.exceptions.MissingSchema:
            return("schema")
        except:
            return("unknownerror")

    else:
        return("notyt")

vidTitle = "" # will globally store the video title
vidFormat = ""


#            Downloads the video using youtube-dl as a command in the terminal with the best video and audio format,
#            This is not the best approach to this so I might change the downloadation method so it downloads the video
#            using only python itself.

@eel.expose
def download_video(videoURL):
    randNums = random.randint(1000, 9999)
    global vidTitle
    global vidFormat
    vidTitle = f"video{randNums}"
    try:
        os.system(f"youtube-dl -o {appdataLocal}/YouClip/{vidTitle} {videoURL}")
        if (os.path.isfile(f"{appdataLocal}/YouClip/{vidTitle}.mkv")):
            vidFormat = ".mkv"
        elif os.path.isfile(f"{appdataLocal}/YouClip/{vidTitle}.mp4"):
            vidFormat = ".mp4"
        elif os.path.isfile(f"{appdataLocal}/YouClip/{vidTitle}.webm"):
            vidFormat = ".webm"
        else:
            return("fail")
        return("downloaded")
    except:
        return("error")

#           Crops the video with ffmpeg; here are lots of stuff to handle so I tried to handle all I could think of.
@eel.expose
def crop_video(startmin, startsec, endmin, endsec):
    seconds = [startmin, startsec, endmin, endsec]
    intval = []

    for second in seconds:
        if second == '':
            second = 0
        intval.append(int(second))

    for second in intval:
        if second > 60:
            os.remove(f"{appdataLocal}/YouClip/{vidTitle}{vidFormat}")
            return("greater60")

    total = sum(intval)

    if total == 0:
        os.remove(f"{appdataLocal}/YouClip/{vidTitle}{vidFormat}")
        return("empty")
    else:
        pass

    now = datetime.now()
    current_time = now.strftime("%H-%M")

    startsecond = intval[0] * 60 + intval[1]
    endsecond = intval[2] * 60 + intval[3]

    if (startsecond < endsecond):
        try:
            os.system(f"ffmpeg.exe -i {appdataLocal}/YouClip/{vidTitle}{vidFormat} -ss {startsecond} -to {endsecond} -c copy {desktopPath}/croppedVideo_{current_time}{vidFormat}")
            os.remove(f"{appdataLocal}/YouClip/{vidTitle}{vidFormat}")
            return(f"croppedVideo-{current_time}{vidFormat}")
        except:
            os.remove(f"{appdataLocal}/YouClip/{vidTitle}{vidFormat}")
            return("fail")

    elif (startsecond == endsecond):
        os.remove(f"{appdataLocal}/YouClip/{vidTitle}{vidFormat}")
        return("equal")

    elif (startsecond > endsecond):
        os.remove(f"{appdataLocal}/YouClip/{vidTitle}{vidFormat}")
        return("greaterstart")

findBrowser()
appdataFolder()

eel.start('index.html', size = (1000, 600), mode="chrome") # starts the app
