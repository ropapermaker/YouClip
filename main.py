import eel
import youtube_dl
import requests
import os
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from datetime import datetime

eel.init('web')
now = datetime.now()


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

@eel.expose
def download_video(videoURL):
    try:
        print(videoURL)
        os.system(f"youtube-dl -o 'video6932.mp4' " + videoURL)
        return("downloaded")
    except:
        return("error")
    

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
            os.remove('video6932.mp4')
            return("greater60")
    
    total = sum(intval)
    
    if total == 0:
        os.remove('video6932.mp4')
        return("empty")
    else:
        pass
    
    zeroitems = 0
    for item in intval:
        if item == 0:
            zeroitems += 1
    
    if zeroitems < 2:
        return("less")
    
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    
    secondstart = intval[0] * 60 + intval[1]
    secondend = intval[2] * 60 + intval[3]
    

    if (secondstart < secondend):
        try:
            ffmpeg_extract_subclip("video6932.mp4", secondstart, secondend, targetname=f"croppedVideo_{current_time}.mp4")
            os.remove('video6932.mp4')
            return(f"croppedVideo_{current_time}.mp4")
        except:
            os.remove('video6932.mp4')
            return("fail")
    elif (secondstart == secondend):
        os.remove('video6932.mp4')
        return("equal")
    
    elif (secondstart > secondend):
        os.remove('video6932.mp4')
        return("greaterstart")
    
    
eel.start('index.html', size = (1000, 600))