import mediapipe as mp
import cv2  
 
class handDetector():
    def __init__(self):
        self.mpHands = mp.solutions.hands  # Sử dụng giải pháp hand
        self.hands = self.mpHands.Hands(max_num_hands =4)   # tạo đối tượng để xử lý bàn tay
        self.mp_draw = mp.solutions.drawing_utils
        
        
    def findHand(self,img):
        img_RGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)  # Chuyển hình ảnh sang không gian màu RGB
        self.result = self.hands.process(img_RGB)  # kết quả trả về các đôí tượng là bàn tay được phát hiện
        hand_count = 0
        if self.result.multi_hand_landmarks:
          for hand_landmarks in self.result.multi_hand_landmarks: # Đi qua từng đối tượng bàn tay
            index = [4,8,12,16,20]
            for id,lm in enumerate(hand_landmarks.landmark):   # Lấy id và tọa độ của 21 điểm trên bàn tay đó
                h,w,c = img.shape 
                cx,cy = int(lm.x*w),int(lm.y*h)
                # print(cx,cy)
                
                if id in index:                  # vẽ một vòng tròn trên các đỉnh ngón tay
                    cv2.circle(img,(cx,cy),10,(255,0,0),cv2.FILLED)
                            
            self.mp_draw.draw_landmarks(img,hand_landmarks,self.mpHands.HAND_CONNECTIONS)
            hand_count = hand_count+1
        return img,hand_count
    
    def findPosition(self,img,handIndex=0):  # Hàm lấy 21 điểm của bàn tay trong danh sách bàn tay được phát hiện
        point_list = []
        if self.result.multi_hand_landmarks:
          myHand = self.result.multi_hand_landmarks[handIndex]   # Đối tượng bàn tay tương ứng với chỉ số thứ tự được truyền vào
          # Lưu 21 điểm của bàn tay cần tìm vào point_list
          for id,lm in enumerate(myHand.landmark):    
                h,w,c = img.shape
                cx,cy = int(lm.x*w),int(lm.y*h)
                point_list.append([id,cx,cy])
                # print(cx,cy)
                
        return point_list
    
    
    def finger_Counter(self,img,index):
        list = []
        count = []
        for i in range(0, index):
            list = self.findPosition(img, i)  # Dựa vào index để tìm ra 21 điểm của bàn tay có chỉ số đó
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
        return count