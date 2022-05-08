import cv2
import numpy as np




class face_detection:  # class phát hiện khuôn mặt
       def __init__(self,face_cascade,eye_cascade):
         self.face_cascade=face_cascade
         self.eye_cascade = eye_cascade
         self.image = None
         self.face_list = None
        #  self.eye_rects = None
        #  self.eye_gray = None
        #  self.eye_color = None
        #  self.eye_list = None
      
      
       def face_detection_function(self,image):  # trả về số khuôn mặt được phát hiện
         
         gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
         self.face_list = self.face_cascade.detectMultiScale(gray, 1.3, 4) #scaleFactor=1.3, minNeighbors=5
         return self.face_list
       
       
       def ImageHandling(self,image):  # vẽ hình vuông bao quanh khuôn mặt được phát hiện
           count = 0
           gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
           gray_image = cv2.bilateralFilter(gray_image,5,1,1)
           faces = self.face_detection_function(image)
           for (x,y,w,h) in faces:
              cv2.rectangle(image, (x,y), (x+w,y+h), (0,255,0), 3)
              # eye_gray = gray_image[y:y+int(h/2), x:x+w] 
              # eye_color = image[y:y+int(h/2), x:x+w]
              # eyes = self.eye_cascade.detectMultiScale(eye_gray)
              # if len(eyes)>= 2:
                 
              #   for (ex,ey,ew,eh) in eyes: 
              #     cv2.rectangle(eye_color,(ex,ey),(ex+ew,ey+eh),(0,127,255),2)
              #   flag = True
              # else:
              #   flag = False
              
              # if flag == False:
              count +=1
                
           return image,count