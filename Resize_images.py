# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 12:17:58 2020

@author: AliQadar
"""

import glob as glob
import cv2
import os

def resize_imgs(img_dir, extension, size):
    for img in glob.glob(img_dir + "*."+extension):
        image = cv2.imread(img)
        resized_img =cv2.resize(image, size)
        if not os.path.exists(img_dir + 'Resized'):
            os.makedirs(img_dir + 'Resized')
        foldername = "Resized/"
        folderlen = len(img_dir)
        cv2.imwrite(img_dir + foldername + img[folderlen:], resized_img)
        print('Image written : ' + img.split("\\")[1])


img_dir = "Path-to-images-directory"
extension = "jpg"
size = (1920, 1080)
resize_imgs(img_dir, extension, size)