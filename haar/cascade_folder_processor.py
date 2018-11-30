import cv2 as cv
import numpy as np
from tqdm import tqdm_notebook
import os
import time


PATH_TO_DATA = '../data'
PATH_TO_RESULTS = '../detections'
PATH_TO_VALSET = '../data/valset.txt'

small_cascade = cv.CascadeClassifier('../data/opencv/small-cascade-40/cascade.xml')

try:
    os.mkdir(PATH_TO_RESULTS)
except(OSError):
    pass

with open(PATH_TO_VALSET) as vs:
    desired_files = set(map(lambda lx: lx.strip(), vs.readlines()))



def process_pic(img_name):
    path = os.path.join(PATH_TO_DATA, img_name)
    gray = cv.cvtColor(cv.imread(path), cv.COLOR_BGR2GRAY)

    # imgname score xmin ymin xmax ymax
    cars = small_cascade.detectMultiScale(gray, 1.3, 5)
    l = len(cars)+2
    i = 1
    for (x, y, w, h) in cars:
        score = i/l
        yield "{} {:.5} {} {} {} {}\n".format(img_name.replace('.png', ''), score, x, y, x + w, y + h)


def process_dir(dir_path=PATH_TO_DATA, filename='results_small-vehicle.txt'):
    now = time.time()

    img_names = sorted(os.listdir(dir_path))
    f = open(os.path.join(PATH_TO_RESULTS, filename), 'w+')
    ii=0
    for iname in tqdm_notebook(img_names):
        if iname[:5] not in desired_files:
            continue
        if not iname.endswith('.png'):
            continue
        i = 0
        for line in process_pic(iname):
            f.write(line)
            i += 1
        ii+=1
        print('{} cars detected on img {}'.format(i, iname))
        if ii%20 == 0:
            print('done {}/{} in {} msec'.format(ii, len(img_names), time.time()-now))

    f.close()

process_dir()
