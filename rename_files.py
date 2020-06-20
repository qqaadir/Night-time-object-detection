# -*- coding: utf-8 -*-
"""
Created on Wed May 27 17:15:01 2020

@author: AliQadar
"""

import os
imgs = r"F:/Night-time_data/annotate/images"
for i, filename in enumerate(os.listdir(imgs)):
    os.rename(imgs + "//" +  filename, imgs + "//image_" + str(i + 1) + ".jpg")