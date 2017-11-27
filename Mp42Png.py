# https://www.cnblogs.com/kirito-c/p/5971988.html
# there is a problem that can not stop when the vedio is over
import numpy as np
import cv2
import os

cap = cv2.VideoCapture('BadApple.mp4')

num = 0
while (cap.isOpened()):
    print('pic',num)
    ret, frame = cap.read()
#    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(os.getcwd()+'\\pictures\\img%d.png' % num, frame)
    num += 1
print('finish')