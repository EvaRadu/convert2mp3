from __future__ import unicode_literals
import youtube_dl

print(" ---------- CONVERT TO MP3 ----------")
link = input ("Insert the URL : ")

video_info = youtube_dl.YoutubeDL().extract_info(url = link,download=False)
filename = f"{video_info['title']}.mp3"
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '720',
    }],
     'outtmpl':"downloads/"+filename,

}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])

