# -*- coding: utf-8 -*-
"""
@author: AliQadar
"""

import glob as glob
import codecs
from xml.dom import minidom


path=r"path to xml files"
files = glob.glob(path + "/*.xml")  # Getting all xml files

for j in range(len(files)):
    file_name = files[j].split("\\")[-1]  # Extract filename
    root = minidom.parse(file_name)       # Parsing xml file
    xmins = len(root.getElementsByTagName('xmin')) # Checking for number of available items in xmin
    if xmins > 0:

        for i in range(xmins):    
            root.getElementsByTagName('xmin')[i].firstChild.data=str(round(int(float(root.getElementsByTagName('xmin')[i].firstChild.data))))
            root.getElementsByTagName('xmax')[i].firstChild.data=str(round(int(float(root.getElementsByTagName('xmax')[i].firstChild.data))))
            root.getElementsByTagName('ymin')[i].firstChild.data=str(round(int(float(root.getElementsByTagName('ymin')[i].firstChild.data))))
            root.getElementsByTagName('ymax')[i].firstChild.data=str(round(int(float(root.getElementsByTagName('ymax')[i].firstChild.data))))
    
        with codecs.open(file_name, "w", encoding="utf-8", errors="xmlcharrefreplace") as xml_file:
             root.writexml(xml_file)   # writing out updated files
        print("updated file {}".format(file_name))
    else:
        print('corrupt file {} '.format(file_name))


print("updated total {} file".format(len(files)))