import youtube_dl #downloads songs from youtube using link provided by youtubesearchpython
import os.path
from os import path
ydl_opts = {
    'outtmpl': 'song.mp3', #names downloaded file test.mp3 and places it in desired directory
    'format': 'bestaudio/best', #quality settings
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }]
}


def yt_download(url):
    if path.isfile('song.mp3') == True:
        os.remove("song.mp3")
    with youtube_dl.YoutubeDL(ydl_opts) as ydl: #youtube_dl stuff
        ydl.download(url) 
    
