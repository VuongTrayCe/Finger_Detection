import cv2
import numpy as np




class face_detection:
       def __init__(self,face_cascade,eye_caseade):
         self.face_cascade=face_cascade
         self.eye_caseade = eye_caseade
         self.image = None
         self.face_list = None
         self.eye_rects = None
         self.eye_gray = None
         self.eye_color = None
         self.eye_list = None
      
      
       def face_detection_function(self,image):
         
         gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
         self.face_list = self.face_cascade.detectMultiScale(gray, 1.3, 4) #scaleFactor=1.3, minNeighbors=5
         return self.face_list
       
       
       def ImageHandling(self,image):
           faces = self.face_detection_function(image)
           gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
           for (x,y,w,h) in faces:
              image =  cv2.rectangle(image, (x,y), (x+w,y+h), (0,255,0), 3)
              eye_gray = gray_image[y:y+int(h/2), x:x+w] 
              eye_color = image[y:y+int(h/2), x:x+w]
              eyes = self.eye_cascade.detectMultiScale(eye_gray) 
              for (ex,ey,ew,eh) in eyes: 
                  cv2.rectangle(eye_color,(ex,ey),(ex+ew,ey+eh),(0,127,255),2)
                  
           return image
             
         
# face_cascade = cv2.CascadeClassifier('./cascades/haarcascade_frontalface_alt.xml')
# eye_cascade = cv2.CascadeClassifier('./cascades/haarcascade_eye_tree_eyeglasses.xml')
# s# scaling_factor = 0.5

# lower = np.array([120,1,1])
# upper = np.array([120,25,8])

   #  frame = cv2.resize(frame, None, fx=scaling_factor,fy=scaling_factor, interpolation=cv2.INTER_AREA)
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     face_rects = face_cascade.detectMultiScale(gray, 1.3, 4) #scaleFactor=1.3, minNeighbors=5
#     for (x,y,w,h) in face_rects:
#       frame =  cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3)
#       eye_gray1 = gray[y+22:y+int(h/2)+10, x+18:x+w-18] 
#       eye_color1 = frame[y+22:y+int(h/2)+10, x+18:x+w-18] 
#       eye_gray = gray[y:y+int(h/2), x:x+w] 
#       eye_color = frame[y:y+int(h/2), x:x+w]
#       gray_image = cv2.cvtColor(eye_color1,cv2.COLOR_BGR2GRAY)
#     # image = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#     # mask = cv2.inRange(image,lower,upper)
#       ret1, thresh1 = cv2.threshold(gray_image,60, 70, cv2.THRESH_BINARY)
#       # image = cv2.cvtColor(eye_color,cv2.COLOR_BGR2HSV)
#       # mask = cv2.inRange(image,lower,upper)
#       eyes = eye_cascade.detectMultiScale(eye_gray) 
#       for (ex,ey,ew,eh) in eyes: 
#             cv2.rectangle(eye_color,(ex,ey),(ex+ew,ey+eh),(0,127,255),2)
#       # coutours , hierarcchy = cv2.findContours(thresh1,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
#       # if len(coutours)!= 0:
#       #     for i,coutour in enumerate(coutours):
#       #       if cv2.contourArea(coutour)>500:
#       #         x,y,w,h = cv2.boundingRect(coutour)
#       #         cv2.rectangle(eye_color1,(x,y),(x+w,y+h),(0,0,255),3) 
    
#       # cv2.imshow('mask',thresh1)
#     cv2.imshow('Face Detector', frame)
#     c = cv2.waitKey(1)
#     if c == 27:
#        break
   
# cap.release()
# cv2.destroyAllWindows()