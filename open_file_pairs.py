# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 16:38:17 2020
This script checks for a pair of files with different extentions. It can also check if 
there is some extraneous file.
USAGE:
    Simply pass the extensions of your files and path to directory with these files.
@author: AliQadar
"""

import os
from collections import defaultdict

EXTENSIONS = {'.xml', '.jpg'} # Change extensions for your own needs

directory = r"your-directory-path-here"

grouped_files = defaultdict(int)

for f in os.listdir(directory):
    name, ext = os.path.splitext(os.path.join(directory, f))
    if ext in EXTENSIONS:
        grouped_files[name] += 1

for name in grouped_files:
    if grouped_files[name] == len(EXTENSIONS):
        with open('{}.jpg'.format(name)) as jpg_file, \
                open('{}.xml'.format(name)) as xml_file:
            # Check for processed files
            print(jpg_file, xml_file)
            
    else:
        print(name, ext)