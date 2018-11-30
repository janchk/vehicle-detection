import numpy as np
import cv2 as cv

hsmall_cascade = cv.CascadeClassifier('../data/opencv/h-small-cascade/cascade.xml')
vsmall_cascade = cv.CascadeClassifier('../data/opencv/v-small-cascade/cascade.xml')


img = cv.imread('../data/P0066.png')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cars = hsmall_cascade.detectMultiScale(gray, 1.3, 5)
vcars = vsmall_cascade.detectMultiScale(gray, 1.3, 5)

print(cars,vcars)
for (x,y,w,h) in vcars:
    cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    print(x,y,w,h)
for (x,y,w,h) in cars:
    cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    print(x,y,w,h)

cv.imwrite('img.png', img)
cv.waitKey(0)
cv.destroyAllWindows()
