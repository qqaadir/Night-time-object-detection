# XML files with no  labels causes issue in creating csv file. To handle, this issue
#I moved all the files without labels to a separate folder named unlabelled for later use and to inspect images


import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET
import shutil

# move files
def batch_move_files(file, unlabelled):
     file = getname('.xml', file)
     image = file+'.jpg'
     xml = file+'.xml'
     shutil.move(image, unlabelled) # here its better to use copy instead of move, it cause problems when files exist in folder
     shutil.move(xml, unlabelled)                          
     return

#%% get name without extension
def getname(extension, file):
    name_without_ext = file.replace(extension,"")
    return name_without_ext
#%%
unlabelled = r"path-to-folder/unlabelled"
# In the following code, I made few changes to address my own problem mentioned at the top.
def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            if member.find("bndbox") is None:
               batch_move_files(xml_file,unlabelled)
               print(root.find("filename").text + " moved")
            else:
                value = (root.find('filename').text,
                         int(root.find('size')[0].text),
                         int(root.find('size')[1].text),
                         member[0].text,
                         int(member[4][0].text),
                         int(member[4][1].text),
                         int(member[4][2].text),
                         int(member[4][3].text)
                         )
                xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


def main():
    for folder in ['train','test']:
        image_path = os.path.join(os.getcwd(), ('China/' + folder))
        xml_df = xml_to_csv(image_path)
        xml_df.to_csv(('China/' + folder + '_labels.csv'), index=None)
        print('Successfully converted xml to csv.')


main()
