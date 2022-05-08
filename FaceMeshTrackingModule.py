
import cv2
import numpy as np
import  mediapipe as mp
import math
LEFT = [33,7,163,144,145,153,154,155,133,173,157,158,159,160,161,246]
RIGHT = [362,382,381,380,374,373,390,249,263,466,388,387,386,385]
CENTER = [61,146,91,181,84,17,314,405,321,375,291,409,270,269,267,0,37,39,40,185]
# Các điểm mốc quan trọng để kết nối các điểm lại trên miệng
moi =  [61,78,95,88,178,87,14,317,402,318,324,291,415,310,311,312,13,82,81,80,191]

class FaceMeshTrackingModule:
    def __init__(self):
        self.mp_faceMesh = mp.solutions.face_mesh   # Chọn giải pháp facemesh
        self.FaceMesh = self.mp_faceMesh.FaceMesh(max_num_faces =4)  # Tạo đối tượng facemesh để xử lý khuôn mặt
        self.mp_draw =mp.solutions.drawing_utils
        self.result = None
        self.mesh_point = None
        
        # Hàm thiết kế lưới khuôn mặt và xác định miệng của đối tượng
    def FaceMeshDetector(self,image):
        image_RGB = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)  # chuyển hình ảnh sang hình ảnh Rgb
        image_h,image_w = image.shape[:2]            # Lấy chiều cao và chiều rộng của hình ảnh 
        self.result =self.FaceMesh.process(image_RGB)   # trả về kết quả là số FaceMesh được phát hiện
        arr = []
        count = 0  # Biến dùng để đếm số khuôn mặt đang cười
        if self.result.multi_face_landmarks:  # Kiểm tra điều kiện xem có bằng Null ko
          for  landmarks in self.result.multi_face_landmarks:   # duyệt qua từng FaceMesh được phát hiện
              # Lưu tất cã 468 điểm trên khuôn mặt vào mảng mesh_point
              self.mesh_point =np.array([np.multiply([p.x,p.y],[image_w,image_h]).astype(int) for p in landmarks.landmark])
            #   cv2.polylines(image,[self.mesh_point[LEFT]],True,(0,255,0),1,cv2.LINE_AA)
            #   cv2.polylines(image,[self.mesh_point[RIGHT]],True,(0,255,0),1,cv2.LINE_AA)
            #   cv2.polylines(image,[self.mesh_point[CENTER]],True,(0,255,0),1,cv2.LINE_AA)
            #   cv2.polylines(image,[self.mesh_point[moi]],True,(0,255,0),1,cv2.LINE_AA)
              arr.append(self.mesh_point)
              # Các điểm dùng để xét điều kiện xem đang cười hay ko
              a = self.mesh_point[13]
              b = self.mesh_point[14]
              d = self.mesh_point[13]
              h = self.mesh_point[11]
              e = self.mesh_point[12]
              kc1 = int(math.sqrt(math.pow((a[0]-b[0]),2)+math.pow((a[1]-b[1]),2)))# Khoảng cách giữa điểm 13 và 14
              kc2 = int(math.sqrt(math.pow((d[0]-e[0]),2)+math.pow((d[1]-e[1]),2)))# Khoảng cách giữa điểm 13 và 12
              kc3 = int(math.sqrt(math.pow((d[0]-h[0]),2)+math.pow((d[1]-h[1]),2)))# Khoảng cách giữa điểm 13 và 11

              if self.mesh_point[61][0] < self.mesh_point[142][0] and kc1> kc3 and self.mesh_point[291][0] > self.mesh_point[371][0]+2 and self.mesh_point[17][1] < self.mesh_point[182][1]:
                  count = count+1  
              if self.mesh_point[61][0] < self.mesh_point[142][0] and self.mesh_point[291][0] > self.mesh_point[273][0]-1 and kc1> kc3 and self.mesh_point[17][1] < self.mesh_point[273][1]:
                  count =count+1
              if self.mesh_point[291][0] > self.mesh_point[371][0]-1 and self.mesh_point[61][0] < self.mesh_point[43][0] and kc1> kc3 and self.mesh_point[17][1] < self.mesh_point[43][1]:
                  count = count+1                 
                 
        return image,count