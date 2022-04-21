import mediapipe as mp
import cv2 
import time
 
 
class handDetector():
    def __init__(self):
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands()
        self.mp_draw = mp.solutions.drawing_utils
        
        
    def findHand(self,img):
        img_RGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.result = self.hands.process(img_RGB)
        i = 0
        if self.result.multi_hand_landmarks:
          for hand_landmarks in self.result.multi_hand_landmarks:  # đi qua từng cột mốc để nối lại
            index = [4,8,12,16,20]
            for id,lm in enumerate(hand_landmarks.landmark):
                h,w,c = img.shape
                cx,cy = int(lm.x*w),int(lm.y*h)
                # print(cx,cy)
                
                if id in index:
                    cv2.circle(img,(cx,cy),10,(255,0,0),cv2.FILLED)
                            
            self.mp_draw.draw_landmarks(img,hand_landmarks,self.mpHands.HAND_CONNECTIONS)
            i = i+1
        
        return img,i
    
    def findPosition(self,img,handIndex=0):
        list = []
        if self.result.multi_hand_landmarks:
          myHand = self.result.multi_hand_landmarks[handIndex]  # đi qua từng cột mốc để nối lại
          for id,lm in enumerate(myHand.landmark):
                h,w,c = img.shape
                cx,cy = int(lm.x*w),int(lm.y*h)
                list.append([id,cx,cy])
                # print(cx,cy)
                
        return list