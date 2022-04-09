#!/usr/bin/python

'''
Title:
    Youtube downloader and converter to .mp3
Explanation:
    Downloads the video in .mp4 audio only format and then converts to .mp3 in the current folder
Usage:
    python download_yt.py [youtube_url]
Dependences:
    pip install pytube
    pip install moviepy
Author:
    Prasanth Thangavel
Date edited:
    2021-04-09
'''

'''
Source: https://pytube.io/en/latest/user/streams.html#downloading-streams
'''

import sys

from pytube import YouTube

# import ipdb
print ('[INFO] Number of arguments:', len(sys.argv), 'arguments.')
print ('[INFO] Argument List:', str(sys.argv))

if sys.argv[1] is None:
    link = input("Enter the youtube video link: ")
else:
    link = sys.argv[1]
link = link.strip()
print (link)

yt = YouTube(link)

# Filtering streams
yt_streams = yt.streams.filter(only_audio=True)

# Slecting yt_streams
stream = yt_streams.get_by_itag(139)
assert "audio/mp4"  == stream.mime_type

# Downloading streams
path_to_saved_video = stream.download()
print ('[INFO] Download completed successfully.')


'''
Source: https://pytube.io/en/latest/api.html#pytube.Stream.download
'''
from moviepy.editor import *
def mp4_to_mp3(mp4, mp3):
    mp4_without_frames = AudioFileClip(mp4)
    mp4_without_frames.write_audiofile(mp3)
    mp4_without_frames.close()

# Convert .mp4 to .mp3
path_to_saved_audio = path_to_saved_video.replace(".mp4", ".mp3")
mp4_to_mp3(path_to_saved_video, path_to_saved_audio)


'''
Source: https://stackoverflow.com/questions/6996603/how-do-i-delete-a-file-or-folder-in-python
'''
import os
os.remove(path_to_saved_video)
