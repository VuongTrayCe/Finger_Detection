import cv2
from FaceMeshTrackingModule import FaceMeshTrackingModule
from HandTrackingModule import handDetector
from face_detection import face_detection
face_cascade = cv2.CascadeClassifier('./cascades/haarcascade_frontalface_alt.xml')
eye_cascade = cv2.CascadeClassifier('./cascades/haarcascade_eye_tree_eyeglasses.xml')
class ScreenManager(object):  # Class quản lý màn hình

    def __init__(self, capture):
        self._capture = capture    # Đây là đối tượng Videocapture
        self._enteredFrame = False    # thuộc tính Kiểm tra xem có đọc đc frame tiếp theo ko
        self._frame = None            # thuộc tính sẽ lưu frame chụp được. và nó là hình ảnh để hiển thị ra cửa số
        self._handTracking = handDetector()   #  Đối tượng để phát hiện và xử lý bàn tay
        self._faceMesh = FaceMeshTrackingModule()  # Đối tượng để phát hiện FaceMesh và xử lý nụ cười
        self.facedetect = face_detection(face_cascade,eye_cascade)
        self.smile_count = None

    @property
    def frame(self):         # function này sẽ trả về một frame mới
        if self._enteredFrame and self._frame is None:
            _, self._frame = self._capture.retrieve()
            
        return self._frame

    def display(self, img):     # Hàm xử lý và hiển thị trả về frame(Hình ảnh) mới sau khi được chỉnh sửa
        img, index = self._handTracking.findHand(img)  # img này chứa các bàn tay được phát hiện và index là số bàn tay được phát hiện

        list = []
        count = []  # Mảng dùng để lưu số ngón tay được phát hiện từ bàn táy
        for i in range(0, index):
            list = self._handTracking.findPosition(img, i)  # Dựa vào index để tìm ra 21 điểm của bàn tay có chỉ số đó
            # Đây là các mốc quan trọng (Ở đầu mút ngón tay và ở các khớp)
            index = [4, 8, 12, 16, 20]
            index2 = [3, 6, 10, 14, 18]
            # Kiểm tra só ngón tay đc phát hiển
            if list[0][1] > list[1][1]:
                if list[index[0]][1] < list[index[0]-1][1]:
                    count.append(1)
            else:
                if list[index[0]][1] > list[index[0]-1][1]:
                    count.append(1)
            for id in range(1, 5):
                if list[index[id]][2] < list[index2[id]][2]:
                    count.append(1)
        # In kết quả lên hình ảnh 
        cv2.putText(img, f'Number of fingers: {len(count)}', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
        img,self.smile_count =self._faceMesh.FaceMeshDetector(img)
        cv2.putText(img, f'Number of smiling faces: {self.smile_count}', (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
        img,face_count = self.facedetect.ImageHandling(img)
        cv2.putText(img, f'Number of faces: {face_count}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

        return img

    def enterFrame(self):
        # check xem frame tiếp theo có thể chụp được không
        if self._capture is not None:
            self._enteredFrame = self._capture.grab()

    def exitFrame(self):     # Đóng frame

        self._frame = None
        self._enteredFrame = False



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
