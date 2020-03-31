#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os
import re
import shutil
import sys
import zipfile
from PIL import Image

script_dir = os.path.dirname(__file__)


def splitValue(line):
    splitted = line.split(":", 1)
    return splitted[1].strip().replace("\"", "'")


if __name__ == '__main__':

    if len(sys.argv) < 3:
        print(os.path.basename(sys.argv[0]), "<pk3dir> <target_path_map_json> <target_path_images>")
        sys.exit(0)

    pk3Dir = sys.argv[1]
    mapJsonDir = sys.argv[2]
    imageDir = sys.argv[3]

    print("pk3dir:" + pk3Dir)
    print("mapJsonDir:" + mapJsonDir)
    print("imageDir:" + imageDir)

    pk3files = [f for f in os.listdir(pk3Dir) if f.endswith('.pk3')]

    custom_maps = []

    for pk3file in pk3files:
        print("file: " + pk3file)
        zip = zipfile.ZipFile(os.path.join(pk3Dir, pk3file))


        for item in zip.namelist():
            if item.endswith('.bsp'):
                map_name = os.path.basename(item).replace(".bsp", "")
            
                descriptors = [name for name in zip.namelist() if name.endswith(map_name + '.txt')]

                map = {}
                map['name'] = map_name
                map['description'] = ''
                custom_maps.append(map)

                if len(descriptors) >= 1:

                    for descriptor in descriptors:

                        data = zip.open(descriptor).readlines()

                        for line in data:
                            ll = line.decode("cp1252").strip()
                            if re.match(r'\s*title\s*:.+', ll.lower()):
                                map['title'] = splitValue(ll)

                            if re.match(r'\s*author\s*:.+', ll.lower()):
                                map['source'] = splitValue(ll)

                            if re.match(r'\s*description\s*:.+', ll.lower()):
                                map['description'] = splitValue(ll)

                        if 'title' in map:
                            break

                level_shots_jpg = [name for name in zip.namelist() if name.startswith('levelshots/') and name.endswith(map_name + '.jpg')]
                level_shots_tga = [name for name in zip.namelist() if name.startswith('levelshots/') and name.endswith(map_name + '.tga')]

                if len(level_shots_jpg) > 0:
                    source = zip.open(level_shots_jpg[0])
                    target = open(os.path.join(imageDir, map['name'] + ".jpg"), "wb")
                    with source, target:
                        shutil.copyfileobj(source, target)
                elif len(level_shots_tga) > 0:
                    print("converting tga: " + level_shots_tga[0])
                    source = zip.open(level_shots_tga[0])
                    im = Image.open(source)
                    im.save(os.path.join(imageDir, map['name'] + ".jpg"))

    with open('original_maps.json', 'r') as f:
        maps = json.load(f)
        maps.extend(custom_maps)

        with open(os.path.join(mapJsonDir, "all_maps.json"), 'w') as outfile:
            json.dump(maps, outfile, sort_keys=True, indent=4, separators=(',', ': '))


