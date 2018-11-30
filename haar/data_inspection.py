import os
import numpy as np
from matplotlib import pyplot as plt
from collections import Counter

PATH_TO_DOTA_LABELS = '../data/labelTxt/'
PATH_TO_IMGS = '../'
PATH_TO_OPENCV_LABELS = '../data/opencv/'
PROCESSED_CLASS = 'small-vehicle'
IGNORED_CLASS = 'large-vehicle'


PATH_TO_VALSET = '../data/valset.txt'

lab_files = os.listdir(PATH_TO_DOTA_LABELS)

with open(PATH_TO_VALSET) as vs:
    desired_files = set(map(lambda lx: lx.strip(), vs.readlines()))

processed_strings = []
lsc = Counter()
len_list = []
vertical_names = []
horizontal_names = []
m = 0
l = 0
k = 0
i = 0
for filename in sorted(lab_files):
    if filename[:5] not in desired_files:
        continue
    contains_not_cars = False
    with open(os.path.join(PATH_TO_DOTA_LABELS, filename), 'r') as f:
        objs = []
        ls = []
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
                long_side = np.linalg.norm([ys[1] - ys[2], xs[1] - xs[2]])

                objs.append('{} {} {} {}'.format(x, y, w, h))
                ls.append(long_side)


        if np.mean(ls) > 30:
            m+=1
            print("{}".format(filename.replace('.txt', '')))
            #print("{} >> 20, {}".format(filename.replace('.txt', ''), np.mean(ls)))
        else:
            l+=1
            #print("{}  20, {}".format(filename.replace('.txt', ''), np.mean(ls)))

        if objs:
            len_list.extend(ls)
            lsc.update(Counter(ls))
            k+= len(objs)
            i+=1
            s = '{}  {}  '.format(os.path.join(PATH_TO_IMGS, filename.replace('txt', 'png')), len(objs))
            for obj in objs:
                s += obj + '  '
            processed_strings.append(s)
            #print(i, k)

# print(lsc.most_common(100))
# print(len(lsc))
# plt.hist(len_list, bins=60)
# plt.show()
#
# print(np.sum(np.array(len_list)<12))

print("m {} l {}".format(m, l))