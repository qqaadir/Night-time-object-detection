# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 21:32:14 2020

@author: AliQadar
"""

import xmltodict
import os 
import json

path = r"your_images_path_here"


class Decoder(json.JSONDecoder):
    def decode(self, s):
        result = super().decode(s)  # result = super(Decoder, self).decode(s) for Python 2.x
        return self._decode(result)

    def _decode(self, o):
        if isinstance(o, str):
            try:
                return int(o)
            except ValueError:
                return o
        elif isinstance(o, dict):
            return {k: self._decode(v) for k, v in o.items()}
        elif isinstance(o, list):
            return [self._decode(v) for v in o]
        else:
            return o

for filename in os.listdir(path):
    if not filename.endswith('.xml'):
        continue

    fullname = os.path.join(path, filename)

    with open(fullname, 'r',encoding='utf-8') as f:
        xmlString = f.read()

    jsonString = json.dumps(xmltodict.parse(xmlString), indent=4)
    #Following two lines were custom for my dataset, you can coment them
    jsonString=jsonString.replace("annotation", "outputs")
    
    jsonString=jsonString.replace("filename", "path")
    

    with open(fullname[:-4] + ".json", 'w',encoding='utf-8') as f:
        D= json.loads(jsonString, cls=Decoder)
        D["path"] = D["outputs"].pop("path") # You can also comment this line if not needed
        
        json.dump(D, f,  indent = 4,
               ensure_ascii = False)
        print("Wrote JSON for :", filename)        
    