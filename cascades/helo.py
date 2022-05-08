import cv2
import numpy as np


cam = cv2.VideoCapture(0)
ret, frame = cam.read()

while True:
    ret, frame = cam.read()
    cv2.imshow("Vuong",frame)
    cv2.waitKey(1)