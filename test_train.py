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
dataset_path = r"F:/Night-time_data/Snow_20200420/images1/g1_snow/*.jpg"
# dataset_path = r"F:/Night-time_data/Object_detection_nighttime/dataset/*.jpg" 
image_files = glob(dataset_path)
# image_files = [str(pp) for pp in dataset_path.glob("**/*.jpg")]
# remove file extension
image_names = [name.replace(".jpg","") for name in image_files]
# # Use scikit learn function for convenience
train_names, test_names = train_test_split(image_names, test_size=0.1)
#%%

def batch_move_files(file_list, destination_path):
    for file in file_list:
          image = file+'.jpg'
          xml = file+'.xml'
          shutil.copy2(image, destination_path)
          shutil.copy2(xml, destination_path)
          
         
    return

#%%
test_dir = r"F:/Night-time_data/Object_detection_nighttime/test_images_snow"
train_dir = r"F:/Night-time_data/Object_detection_nighttime/training_images_snow"

batch_move_files(train_names,  train_dir)

batch_move_files(test_names,  test_dir)

# source = source_dir
# dest = test_dir
# files = os.listdir(source)
# for f in test_names:
#     image = f+'.jpg'
#     xml = f+'.xml'
#     shutil.copy2(image, dest)
#     shutil.copy2(xml, dest)
    

# for filename in os.listdir(test_names):
    
        # shutil.move( dir_src + filename, dir_dst)



