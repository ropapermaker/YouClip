import eel
import youtube_dl
import requests
import os
import random
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from datetime import datetime

eel.init('web')

now = datetime.now() # Need this for the output video title.


#        The below function checks if the link is valid and if it works or not using some ways,
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
        print("youtube.com in link not found")
        return("notyt")

vidTitle = "" # will globally store the video title


#            Downloads the video using youtube-dl as a command in the terminal with the best video and audio format,
#            This is not the best approach to this so I might change the downloadation method so it downloads the video
#            using only python itself.

@eel.expose
def download_video(videoURL):
    randNums = random.randint(1000, 9999)
    global vidTitle
    vidTitle = f"video{randNums}.mp4"
    print(vidTitle)
    try:
        os.system(f"youtube-dl --format 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4' -o '{vidTitle}' {videoURL}")
        return("downloaded")
    except:
        return("error")



#           Crops the video with moviepy; here are lots of stuff to handle so I tried to handle all I could think of.
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
            os.remove(vidTitle)
            return("greater60")

    total = sum(intval)

    if total == 0:
        os.remove(vidTitle)
        return("empty")
    else:
        pass

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    secondstart = intval[0] * 60 + intval[1]
    secondend = intval[2] * 60 + intval[3]

    if (secondstart < secondend):
        try:
            print(f"\n\nVideo Title: {vidTitle}\n\n")
            ffmpeg_extract_subclip(vidTitle, secondstart, secondend, targetname=f"croppedVideo_{current_time}.mp4")
            os.remove(vidTitle)
            return(f"croppedVideo_{current_time}.mp4")
        except:
            os.remove(vidTitle)
            return("fail")
    elif (secondstart == secondend):
        os.remove(vidTitle)
        return("equal")

    elif (secondstart > secondend):
        os.remove(vidTitle)
        return("greaterstart")


eel.start('index.html', size = (1000, 600)) # starts the app
