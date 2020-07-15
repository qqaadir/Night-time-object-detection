# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 15:54:23 2020

@author: AliQadar
"""
import cv2
import numpy as np
import glob as glob
img_path = r"add_your_input_path_here"
output_path = r"add_your_out_path_here/"

files = glob.glob(img_path + "/"+ "*.png")

# image = cv2.imread(file_to_open)
filenames = []
for f in files:
    fname = f.split("/")[-1][22:]
    filenames.append(fname)

print(filenames)
#%%
for i, img in enumerate(files):
    image = cv2.imread(img)
    height, width = image.shape[:2]
    
    start_row, start_col = int(0), int(0)
    # get the left half pixel coordinates
    end_row, end_col = int(height), int(width * 0.5)
    cropped_left = image[start_row:end_row , start_col:end_col]
      
    # cv2.imshow("Cropped Left", cropped_left) 
    cv2.imwrite(output_path + "/" + "left_"+ filenames[i], cropped_left)
    print("Wrote left image: {0}".format(i) )    
    
    # Get the right half pixel coordiantes
    start_row, start_col = int(0), int(width * 0.5)
    # get the right half pixel coordinates 
    end_row, end_col = int(height), int(width)
    cropped_right = image[start_row:end_row , start_col:end_col]  
    # cv2.imshow("Cropped Right", cropped_right) 
    cv2.imwrite(output_path + "/" + "right_"+ filenames[i], cropped_right)
    print("Wrote Right image: {0}".format(i) )

print("Done !!")