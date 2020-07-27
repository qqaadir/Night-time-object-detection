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

ORIGINAL_DIR = "F:/Night-time_data/Datasets/Victoria/Sydney/"
OUTPUT_IMG_DIR = "F:/Night-time_data/Datasets/Victoria/Sydney_imgs/"
files=glob(ORIGINAL_DIR + "*.mp4")
len_files = len(files)
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
    print ("Done images for video !")

#%%
for i in range(len_files-1):
    for j in range(len_files):
        filename = files[j].split("\\")[1].split('.mp4')[0]
        extract_frames(files[j], OUTPUT_IMG_DIR, filename)
    
