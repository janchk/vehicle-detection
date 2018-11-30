import os
import numpy as np

PATH_TO_DOTA_LABELS = '../data/labelTxt/'
PATH_TO_IMGS = '../'
PATH_TO_OPENCV_LABELS = '../data/opencv/'
PROCESSED_CLASS = 'small-vehicle'

PATH_TO_VALSET = '../data/valset.txt'

lab_files = os.listdir(PATH_TO_DOTA_LABELS)

with open(PATH_TO_VALSET) as vs:
    desired_files = set(map(lambda lx: lx.strip(), vs.readlines()))

processed_strings = []

for filename in lab_files:
    if filename[:5] not in desired_files:
        continue
    with open(os.path.join(PATH_TO_DOTA_LABELS, filename), 'r') as f:
        flag = 0
        for line in f.readlines()[2:]:
            splitline = line.split()
            obj_class = splitline[8]
            if obj_class == PROCESSED_CLASS:
                flag += 1
        #print(filename, flag)
        if flag ==0 :
            s = '{}\n'.format(os.path.join(PATH_TO_IMGS, filename.replace('txt', 'png')))
            processed_strings.append(s)

try:
    os.mkdir(PATH_TO_OPENCV_LABELS)
except(OSError):
    pass

with open(os.path.join(PATH_TO_OPENCV_LABELS, 'bg-{}.dat'.format(PROCESSED_CLASS)), 'w') as info:
    for s in processed_strings:
        info.write(s)

