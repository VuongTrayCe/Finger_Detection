import cv2
from FaceMeshTrackingModule import FaceMeshTrackingModule
from HandTrackingModule import HandTrackingModule
from face_detection import face_detection

class WindowManager(object):     # Class quản lý cửa só của chúng ta

    def __init__(self, windowName, keypressCallback=None):
        self.keypressCallback = keypressCallback

        self._windowName = windowName
        self._isWindowCreated = False

    @property
    def isWindowCreated(self):   # Hàm trả về giá trị bool kiểm tra xem cửa sổ đã tạo chưa
        return self._isWindowCreated

    def createWindow(self):     # Hàm tạo cửa số window
        cv2.namedWindow(self._windowName)
        self._isWindowCreated = True

    def show(self, frame):       # Hàm hiển thị frame lên cửa số 
        cv2.imshow(self._windowName, frame)

    def destroyWindow(self):     # Đóng tất cã cửa số => thoát chương trình
        cv2.destroyWindow(self._windowName)
        self._isWindowCreated = False

    def processEvents(self):    # Hàm xử lý sự kiện
        keycode = cv2.waitKey(1)
        if self.keypressCallback is not None and keycode != -1:
            self.keypressCallback(keycode)
