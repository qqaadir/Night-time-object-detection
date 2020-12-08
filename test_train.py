# -*- coding: utf-8 -*-
"""
Created on Sun May  3 22:54:17 2020

@author: AliQadar
"""
import os
from pathlib import Path
from glob import glob
import shutil
from sklearn.model_selection import train_test_split
# do test train splitting
#%%
# find image names
dataset_path = r"Path to images/*.jpg"
image_files = glob(dataset_path)
# image_files = [str(pp) for pp in dataset_path.glob("**/*.jpg")]
# remove file extension
image_names = [name.replace(".jpg","") for name in image_files]
# # Use scikit learn function for convenience
train_names, test_names = train_test_split(image_names, test_size=0.1)
#%%
# move files
def batch_move_files(file_list, destination_path):
    for file in file_list:
          image = file+'.jpg'
          xml = file+'.xml'
          shutil.copy2(image, destination_path)
          shutil.copy2(xml, destination_path)
    return

#%% Check for directory exists
test_dir = r"path-to-test-folder/test"
train_dir = r"path-to-train-folder/train"
if not (os.path.exists(test_dir) or os.path.exists(train_dir) ):
    os.mkdir(test_dir)
    os.mkdir(train_dir)
#%% Move file pairs to test and train folders
batch_move_files(train_names,  train_dir)
batch_move_files(test_names,  test_dir)


