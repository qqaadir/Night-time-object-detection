# -*- coding: utf-8 -*-
"""
@author: AliQadar
"""
from lxml import etree
path = r"path-to-xml files"

files = glob.glob(path+ '/*.xml') # get all xml files

# Start adding new element in existing xml files and write them with same name
for file in files:    
    xmltree = etree.parse(file)
    root = xmltree.getroot()
    if root.find('size') is None:  # check if xml file has size element
        root.insert(4,etree.Element("size"))
        new_element = etree.SubElement(root[4], "width")
        new_element.text = '1920'
        new_element = etree.SubElement(root[4], "height")
        new_element.text = '1080'
        new_element = etree.SubElement(root[4], "depth")
        new_element.text = '3'
        # filename = file.split('\\')[-1]
        output = etree.tostring(root, pretty_print=True, encoding="UTF-8")
        open(file,'wb').write(output)
    else:
        print(file.split('\\')[-1] + 'has the size element')
        

print(etree.tostring(root[4],pretty_print=True,encoding='unicode')) # print newly added element