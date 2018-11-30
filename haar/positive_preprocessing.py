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
k = 0
i = 0
for filename in sorted(lab_files):
    if filename[:5] not in desired_files:
        continue
    with open(os.path.join(PATH_TO_DOTA_LABELS, filename), 'r') as f:
        objs = []
        for line in f.readlines()[2:]:
            splitline = line.split()
            obj_class = splitline[8]
            ys = list(map(int, [splitline[1], splitline[3], splitline[5], splitline[7]]))
            xs = list(map(int, [splitline[0], splitline[2], splitline[4], splitline[6]]))
            if obj_class == PROCESSED_CLASS:
                x = min(xs)
                y = min(ys)
                w = max(xs) - x
                h = max(ys) - y

                objs.append('{} {} {} {}'.format(x, y, w, h))
        if objs:
            k+= len(objs)
            i+=1
            s = '{}  {}  '.format(os.path.join(PATH_TO_IMGS, filename.replace('txt', 'png')), len(objs))
            for obj in objs:
                s += obj + '  '
            processed_strings.append(s)
            print(i, k)

try:
    os.mkdir(PATH_TO_OPENCV_LABELS)
except(OSError):
    pass

with open(os.path.join(PATH_TO_OPENCV_LABELS, 'info-{}.dat'.format(PROCESSED_CLASS)), 'w') as info:
    for s in processed_strings:
        info.write(s)
        info.write('\n')

