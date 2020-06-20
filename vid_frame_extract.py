"""Created on Tue Mar 17 10:39:36 2020

@author: AliQadar
"""
#Simple script to extract and save video frames
import cv2
import numpy as np
import imageio as io
from matplotlib import pyplot as plt
import os
from glob import glob
import math

ORIGINAL_DIR = 'F:/Night-time_data/Group33/'
OUTPUT_IMG_DIR = 'F:/Night-time_data/Group33/images3/'
folders=os.listdir(ORIGINAL_DIR)
len_folders = len(folders)
#%%    
def extract_frames(videoFile, dest, fname):

    cap = cv2.VideoCapture(videoFile)
    seconds = 1
    # frameRate = cap.get(10) #frame rate
    fps = cap.get(cv2.CAP_PROP_FPS) # Gets the frames per second
    frameRate = fps * seconds
    while(cap.isOpened()):
        frameId = int(round(cap.get(1)))  #current frame number
        ret, frame = cap.read()
        if (ret != True):
            break
        if (frameId % math.floor(frameRate) == 0):
            filename = dest + fname + '_' +  str(int(frameId)) + ".jpg"
            cv2.imwrite(filename, frame)
            print(" Frame written:", ret)
    cap.release()
    print ("Done!")

#%%
for i in range(len_folders-1):
    vid_paths = os.path.join(ORIGINAL_DIR + folders[i], '*.MP4')
    vid_files = glob(vid_paths)
    for j in range(len(vid_files)):
        filename = vid_files[j][-22:-4]
        extract_frames(vid_files[j], OUTPUT_IMG_DIR, filename)
    
    
