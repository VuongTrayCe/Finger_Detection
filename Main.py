from turtle import onkeypress
import cv2
from face_detection import face_detection
from FaceMeshTrackingModule import FaceMeshTrackingModule
from manager2 import WindowManager, \
    ScreenManager
face_cascade = cv2.CascadeClassifier('./cascades/haarcascade_frontalface_alt.xml')
eye_cascade = cv2.CascadeClassifier('./cascades/haarcascade_eye_tree_eyeglasses.xml')
class Main(object):

    def __init__(self):
        self._windowManager = WindowManager('Cameo',
                                            self.onKeypress)
        self._ScreenManager = ScreenManager(
            cv2.VideoCapture(0))
        self._faceDetection = face_detection(face_cascade,eye_cascade)
        self._faceMesh = FaceMeshTrackingModule()
        self.couter = 0

    def run(self):
        """Run the main loop."""
        self._windowManager.createWindow()
        while self._windowManager.isWindowCreated:
            self._ScreenManager.enterFrame()
            frame = self._ScreenManager.frame
            frame = self._ScreenManager.display(frame)
            # frame = self._faceMesh.FaceMeshDetector(frame)
            # frame = self._faceDetection.ImageHandling(frame)
            



            if frame is not None:
                # TODO: Filter the frame (Chapter 3).
                pass
            self._windowManager.show(frame)
            self._ScreenManager.exitFrame()
            self._windowManager.processEvents()
            # self.keycode = cv2.waitKey(1)
            # self.onKeypress(self.keycode)
         
            

    def onKeypress(self, keycode):
        """Handle a keypress.
        escape -> Quit.
        """
        if keycode == 27:  # space
            self._windowManager.destroyWindow()


if __name__ == "__main__":
    Main().run()
