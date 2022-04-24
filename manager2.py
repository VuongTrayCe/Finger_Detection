from tkinter import font
import cv2
from FaceMeshTrackingModule import FaceMeshTrackingModule
from HandTrackingModule import handDetector

class ScreenManager(object):

    def __init__(self, capture):
        self._capture = capture
        self._channel = 0
        self._enteredFrame = False
        self._frame = None
        self._handTracking = handDetector()
        self._faceMesh = FaceMeshTrackingModule()

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        if self._channel != value:
            self._channel = value
            self._frame = None

    @property
    def frame(self):
        if self._enteredFrame and self._frame is None:
            _, self._frame = self._capture.retrieve()
            
        return self._frame

    def display(self, img):
        img, index = self._handTracking.findHand(img)
        list = []
        count = []
        for i in range(0, index):
            list = self._handTracking.findPosition(img, i)
            index = [4, 8, 12, 16, 20]
            index2 = [3, 6, 10, 14, 18]
            if list[0][1] > list[1][1]:
                if list[index[0]][1] < list[index[0]-1][1]:
                    count.append(1)
            else:
                if list[index[0]][1] > list[index[0]-1][1]:
                    count.append(1)
            for id in range(1, 5):
                if list[index[id]][2] < list[index2[id]][2]:
                    count.append(1)

        img = cv2.putText(img, f'Number of fingers: {len(count)}', (
            10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        img =self._faceMesh.FaceMeshDetector(img)
        return img

    def enterFrame(self):
        """Capture the next frame, if any."""

        # But first, check that any previous frame was exited.
        if self._capture is not None:
            self._enteredFrame = self._capture.grab()

    def exitFrame(self):

        self._frame = None
        self._enteredFrame = False



class WindowManager(object):

    def __init__(self, windowName, keypressCallback=None):
        self.keypressCallback = keypressCallback

        self._windowName = windowName
        self._isWindowCreated = False

    @property
    def isWindowCreated(self):
        return self._isWindowCreated

    def createWindow(self):
        cv2.namedWindow(self._windowName)
        self._isWindowCreated = True

    def show(self, frame):
        cv2.imshow(self._windowName, frame)

    def destroyWindow(self):
        cv2.destroyWindow(self._windowName)
        self._isWindowCreated = False

    def processEvents(self):
        keycode = cv2.waitKey(1)
        if self.keypressCallback is not None and keycode != -1:
            self.keypressCallback(keycode)
