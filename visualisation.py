import matplotlib.pyplot as plt
import cv2
def parse_pred(filename, img):
    objects = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        splitlines = [x.strip().split(' ') for x in lines]
        for splitline in splitlines:
            try:
                object_struct = {}
                # object_struct['name'] = splitline[8]
                # if (len(splitline) == 9):
                #     object_struct['difficult'] = 0
                # elif (len(splitline) == 10):
                #     object_struct['difficult'] = int(splitline[9])
                # object_struct['difficult'] = 0

                lu = (int(splitline[2]), int(splitline[3]))
                rb = (int(splitline[4]), int(splitline[5]))
                # ys = [splitline[1], splitline[3], splitline[5], splitline[7]]
                # xs = [splitline[0], splitline[2], splitline[4], splitline[6]]

                object_struct['bbox'] = [lu, rb]

                # object_struct['bbox'] = [int(float(splitline[0])),
                #                          int(float(splitline[1])),
                #                          int(float(splitline[4])),
                #                          int(float(splitline[5]))]
                # w = int(float(splitline[4])) - int(float(splitline[0]))
                # h = int(float(splitline[5])) - int(float(splitline[1]))
                # cv2.rectangle(img, (int(float(splitline[0])), int(float(splitline[1]))),
                #               (int(float(splitline[4])), int(float(splitline[5]))), (128, 1, 128), 4)
                cv2.rectangle(img, (lu), (rb), (128, 128, 0), 4)
                # object_struct['area'] = w * h
                # print('area:', object_struct['area'])
                # if object_struct['area'] < (15 * 15):
                #     #print('area:', object_struct['area'])
                #     object_struct['difficult'] = 1
                objects.append(object_struct)
            except Exception as e:
                print(e)

    while 1:
        cv2.imshow("output1", img)

        k = cv2.waitKey(33)
        if k == 27:
            break
    return objects

def parse_gt(filename, img):
    objects = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        splitlines = [x.strip().split(' ') for x in lines]
        for splitline in splitlines:
            try:
                object_struct = {}
                object_struct['name'] = splitline[8]
                if (len(splitline) == 9):
                    object_struct['difficult'] = 0
                elif (len(splitline) == 10):
                    object_struct['difficult'] = int(splitline[9])
                # object_struct['difficult'] = 0
                ys = [splitline[1], splitline[3], splitline[5], splitline[7]]
                xs = [splitline[0], splitline[2], splitline[4], splitline[6]]
                object_struct['bbox'] = [int(float(min(xs))),
                                         int(float(min(ys))),
                                         int(float(max(xs))),
                                         int(float(max(ys)))]
                # object_struct['bbox'] = [int(float(splitline[0])),
                #                          int(float(splitline[1])),
                #                          int(float(splitline[4])),
                #                          int(float(splitline[5]))]
                # w = int(float(splitline[4])) - int(float(splitline[0]))
                # h = int(float(splitline[5])) - int(float(splitline[1]))
                # cv2.rectangle(img, (int(float(splitline[0])), int(float(splitline[1]))),
                #               (int(float(splitline[4])), int(float(splitline[5]))), (128, 1, 128), 4)
                cv2.rectangle(img, (int(float(min(xs))), int(float(min(ys)))), (int(float(max(xs))),
                              int(float(max(ys)))), (128, 128, 0), 4)
                w = int(float(float(max(xs)) - float(min(xs))))
                h = int(float(float(max(ys)) - float(min(ys))))
                object_struct['area'] = w * h
                # print('area:', object_struct['area'])
                # if object_struct['area'] < (15 * 15):
                #     #print('area:', object_struct['area'])
                #     object_struct['difficult'] = 1
                objects.append(object_struct)
            except Exception as e:
                print(e)

    while 1:
        cv2.imshow("output2", img)

        k = cv2.waitKey(33)
        if k == 27:
            break
    return objects


def main():
    # detpath = r'E:\documentation\OneDrive\documentation\DotaEvaluation\evluation_task2\evluation_task2\faster-rcnn-nms_0.3_task2\nms_0.3_task\Task2_{:s}.txt'
    # annopath = r'I:\dota\testset\ReclabelTxt-utf-8\{:s}.txt'
    # imagesetfile = r'I:\dota\testset\va.txt'

    # detpath = r'detections/results_{:s}.txt'
    imgpath = r'data/{:s}.png'
    annopath = r'data/{:s}.txt'  # change the directory to the path of val/labelTxt, if you want to do evaluation on the valset
    pred_annopath = r'detections/results_small-vehicle.txt'
    imagesetfile = r'data/valset.txt'

    with open(imagesetfile, 'r') as f:
        lines = f.readlines()
    imagenames = [x.strip() for x in lines]

    recs = {}
    for i, imagename in enumerate(imagenames):
        dem_img = cv2.imread(imgpath.format(imagename))
        dem_img1 = dem_img.copy()
        recs[imagename] = parse_gt(annopath.format(imagename), dem_img)
        recs[imagename] = parse_pred(pred_annopath, dem_img1)

    print(recs)

    classnames = ['small-vehicle']
    classaps = []
    map = 0


if __name__ == '__main__':
    main()
