from turtle import onkeypress
import cv2
from manager2 import WindowManager, \
    CaptureManager


class Cameo(object):

    def __init__(self):
        self._windowManager = WindowManager('Cameo',
                                            self.onKeypress)
        self._captureManager = CaptureManager(
            cv2.VideoCapture(0), self._windowManager, True)

    def run(self):
        """Run the main loop."""
        self._windowManager.createWindow()
        while self._windowManager.isWindowCreated:
            self._captureManager.enterFrame()
            frame = self._captureManager.frame

            if frame is not None:
                # TODO: Filter the frame (Chapter 3).
                pass
            self._windowManager.show(frame)
            self._captureManager.exitFrame()
            self._windowManager.processEvents()
            # self.keycode = cv2.waitKey(1)
            # self.onKeypress(self.keycode)
         
            

    def onKeypress(self, keycode):
        """Handle a keypress.
        space  -> Take a screenshot.
        tab    -> Start/stop recording a screencast.
        escape -> Quit.
        """
        if keycode == 27:  # space
            self._windowManager.destroyWindow()


if __name__ == "__main__":
    Cameo().run()
