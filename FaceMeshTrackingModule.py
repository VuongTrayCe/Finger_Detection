
import cv2
import numpy as np
import  mediapipe as mp
import math

LEFT = [33,7,163,144,145,153,154,155,133,173,157,158,159,160,161,246]
RIGHT = [362,382,381,380,374,373,390,249,263,466,388,387,386,385]
CENTER = [61,146,91,181,84,17,314,405,321,375,291,409,270,269,267,0,37,39,40,185]
moi =  [61,78,95,88,178,87,14,317,402,318,324,291,415,310,311,312,13,82,81,80,191]

class FaceMeshTrackingModule:
    def __init__(self):
        self.mp_faceMesh = mp.solutions.face_mesh
        self.FaceMesh = self.mp_faceMesh.FaceMesh()
        self.mp_draw =mp.solutions.drawing_utils
        self.result = None
        self.mesh_point = None
        
        
    def FaceMeshDetector(self,image):
        image_RGB = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        image_h,image_w = image.shape[:2]
        self.result =self.FaceMesh.process(image_RGB)
        arr = []
        if self.result.multi_face_landmarks:
          for  landmarks in self.result.multi_face_landmarks:
              
              self.mesh_point =np.array([np.multiply([p.x,p.y],[image_w,image_h]).astype(int) for p in landmarks.landmark])
              cv2.polylines(image,[self.mesh_point[LEFT]],True,(0,255,0),1,cv2.LINE_AA)
              cv2.polylines(image,[self.mesh_point[RIGHT]],True,(0,255,0),1,cv2.LINE_AA)
              cv2.polylines(image,[self.mesh_point[CENTER]],True,(0,255,0),1,cv2.LINE_AA)
              cv2.polylines(image,[self.mesh_point[moi]],True,(0,255,0),1,cv2.LINE_AA)
            #   arr.append(self.mesh_point)
            #   a = self.mesh_point[13]
            #   b = self.mesh_point[14]
            #   d = self.mesh_point[13]
            #   h = self.mesh_point[11]
            #   e = self.mesh_point[12]
            #   arr1 = int(math.sqrt(math.pow((a[0]-b[0]),2)+math.pow((a[1]-b[1]),2)))
            #   arr2 = int(math.sqrt(math.pow((d[0]-e[0]),2)+math.pow((d[1]-e[1]),2)))
            #   arr3 = int(math.sqrt(math.pow((d[0]-h[0]),2)+math.pow((d[1]-h[1]),2)))

            #   if self.mesh_point[61][0] < self.mesh_point[142][0]-2 and arr1> arr2 and self.mesh_point[291][0] > self.mesh_point[371][0]+2 and self.mesh_point[17][1] < self.mesh_point[182][1]:  
            #      image = cv2.putText(image, f'dang cuoi', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
            #   if self.mesh_point[61][0] < self.mesh_point[142][0]-2 and self.mesh_point[291][0] > self.mesh_point[273][0] and arr1> arr3 and self.mesh_point[17][1] < self.mesh_point[273][1]:
            #      image = cv2.putText(image, f'dang cuoi', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
            #   if self.mesh_point[291][0] > self.mesh_point[371][0]-2 and self.mesh_point[61][0] < self.mesh_point[43][0] and arr1> arr3 and self.mesh_point[17][1] < self.mesh_point[43][1]:
            #      image = cv2.putText(image, f'dang cuoi', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
                 
                 
        return image
# # cap = cv2.VideoCapture(0)
# FaceMesh = mp_faceMesh.FaceMesh()
# mp_draw = mp.solutions.drawing_utils
# LEFT = [33,7,163,144,145,153,154,155,133,173,157,158,159,160,161,246]
# RIGHT = [362,382,381,380,374,373,390,249,263,466,388,387,386,385]
# CENTER = [61,146,91,181,84,17,314,405,321,375,291,409,270,269,267,0,37,39,40,185]
# moi =  [61,78,95,88,178,87,14,317,402,318,324,291,415,310,311,312,13,82,81,80,191]
# while True:
#     ret, frame = cap.read()
#     frame_RGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
#     frame_h,frame_w = frame.shape[:2]
#     result =FaceMesh.process(frame_RGB)
#     if result.multi_face_landmarks:
#         mesh_point =np.array([np.multiply([p.x,p.y],[frame_w,frame_h]).astype(int) for p in result.multi_face_landmarks[0].landmark])
#         cv2.polylines(frame,[mesh_point[LEFT]],True,(0,255,0),1,cv2.LINE_AA)
#         cv2.polylines(frame,[mesh_point[RIGHT]],True,(0,255,0),1,cv2.LINE_AA)
#         cv2.polylines(frame,[mesh_point[CENTER]],True,(0,255,0),1,cv2.LINE_AA)
#         cv2.polylines(frame,[mesh_point[moi]],True,(0,255,0),1,cv2.LINE_AA)

#         a = mesh_point[13]
#         b = mesh_point[14]
#         d = mesh_point[13]
#         h = mesh_point[11]
#         e = mesh_point[12]
#         h190 = mesh_point[190]
#         a1 = mesh_point[386]
#         b1 = mesh_point[414]
#         px = int((a[0]+b[0])/2)
#         py = b[1]
#         # cv2.circle(frame,(mesh_point[273][0],mesh_point[273][1]),2,(0,255,0),1,cv2.LINE_AA)
#         # cv2.circle(frame,(mesh_point[106][0],mesh_point[106][1]),2,(0,255,0),1,cv2.LINE_AA)
#         # cv2.circle(frame,(mesh_point[43][0],mesh_point[43][1]),2,(0,255,0),1,cv2.LINE_AA)
#         # cv2.circle(frame,(mesh_point[182][0],mesh_point[182][1]),2,(0,255,0),1,cv2.LINE_AA)

#         # cv2.circle(frame,(mesh_point[17][0],mesh_point[17][1]),2,(0,255,0),1,cv2.LINE_AA)
#         arr1 = int(math.sqrt(math.pow((a[0]-b[0]),2)+math.pow((a[1]-b[1]),2)))
#         arr2 = int(math.sqrt(math.pow((d[0]-e[0]),2)+math.pow((d[1]-e[1]),2)))
#         arr3 = int(math.sqrt(math.pow((d[0]-h[0]),2)+math.pow((d[1]-h[1]),2)))

#         if mesh_point[61][0] < mesh_point[142][0]-2 and arr1> arr2 and mesh_point[291][0] > mesh_point[371][0]+2 and mesh_point[17][1]<mesh_point[182][1]:  
#             frame = cv2.putText(frame, f'dang cuoi', (
#             100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
#         if mesh_point[61][0] < mesh_point[142][0]-2 and mesh_point[291][0] > mesh_point[273][0] and arr1> arr3 and mesh_point[17][1]<mesh_point[273][1]:
#              frame = cv2.putText(frame, f'dang cuoi', (
#             100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
#         if mesh_point[291][0] > mesh_point[371][0]-2 and mesh_point[61][0] < mesh_point[43][0] and arr1> arr3 and mesh_point[17][1]<mesh_point[43][1]:
#             frame = cv2.putText(frame, f'dang cuoi', (
#             100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
#         # if mesh_point[61][0] < mesh_point[43][0] and mesh_point[291][0] < mesh_point[273][0]:  
#         #     print("Dang cuoi")

       
            
#         # print(f'{c1,c,c1-c}')
#         # print(f'Vuuong dep trai {c1}')
    


#     cv2.imshow("hello",frame)   
#     key = cv2.waitKey(1)
#     if key == ord('q'):
#         break
    
# cap.release()
# cv2.destroyAllWindows() 