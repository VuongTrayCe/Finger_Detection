from turtle import onkeypress
import cv2
from manager2 import WindowManager, \
    ScreenManager

class Main(object):

    def __init__(self):
        self._windowManager = WindowManager('Cameo',
                                            self.onKeypress)
        self._ScreenManager = ScreenManager(
            cv2.VideoCapture(0), self._windowManager, True)

    def run(self):
        """Run the main loop."""
        self._windowManager.createWindow()
        while self._windowManager.isWindowCreated:
            self._ScreenManager.enterFrame()
            frame = self._ScreenManager.frame
            frame = self._ScreenManager.displayHandCounter(frame)
            

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
