# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 13:47:23 2020

@author: AliQadar
"""
'''The script will first create a directory in in your video files directory
and then will write video files without audio while retaining original files names.
'''
from moviepy.editor import VideoFileClip, AudioFileClip
import moviepy.editor as mpe
import glob
import os

VIDEO_DIR = "Path-to-video-files-here/"
video_files=glob.glob(VIDEO_DIR + "*.mp4")

def remove_audio(video_files):
    path = video_files[0].split("\\")[0]
    
    for vid in video_files:
        videoclip = VideoFileClip(vid)
        if not os.path.exists(path + '/NoAudio'):
            os.makedirs(path + '/NoAudio')
        foldername = "/NoAudio/"
        
        folderlen = len(path)
        videoclip.write_videofile(path + foldername + vid[folderlen:],  audio=False)


remove_audio(video_files)