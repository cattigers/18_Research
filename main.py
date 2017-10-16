import cv2
import os
from pathlib import *


def extract(path, name):
    vid = Path(path, 'video', name)
    img = Path(path, 'frames', name)

    if not vid.exists():
        print('Path ' + str(vid) + ' Does not exists.\n')
        return

    cap = cv2.VideoCapture(str(vid))
    if not cap.isOpened():
        print("video not captured.")
        return

    if not img.exists():
        print('Making result directory...\n')
        os.mkdir(str(img))

    success, image = cap.read()
    count = 0
    while success:
        print('Writing %dth frame' % count)
        now = Path(img, '%05d.jpg' % count)
        cv2.imwrite(str(now), image)     # save frame as JPEG file
        count += 1
        success, image = cap.read()
    print("DONE!!\n")


def main():
    extract('/home/alpah/dev/AI/2017RnE/CCNN/Demo/Data/', 'sample.mp4')


main()
