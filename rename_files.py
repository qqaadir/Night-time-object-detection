# -*- coding: utf-8 -*-
"""
Created on Wed May 27 17:15:01 2020

@author: AliQadar
"""
# Use this to rename a bunch of files in a given directory
import os
imgs = r"images-path-goes-here"
for i, filename in enumerate(os.listdir(imgs)):
    os.rename(imgs + "//" +  filename, imgs + "//image_" + str(i + 1) + ".jpg")