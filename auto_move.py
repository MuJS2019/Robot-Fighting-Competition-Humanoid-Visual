__author__ = 'Avi'

from robotpi_movement import Movement
from found import Found
import numpy as np
import cv2 as cv

class auto(object):

    def __init__(self):
        self.mv = Movement()
        self.fod=Found()
        self.handle()


    def rev_cam(self,frame):#摄像头倒转
        (h, w)=frame.shape[:2]
        center=(w / 2, h / 2)
        M=cv.getRotationMatrix2D(center, 180, 1)  # 旋转缩放矩阵：(旋转中心，旋转角度，缩放因子)
        rotated=cv.warpAffine(frame, M, (w, h))
        
        return rotated
    
    
    def to_gray(self,img):
        high,weight=img.shape[:2]
        high,weight=int(high/5),int(weight/5)
        img=cv.resize(img,(weight,high))
        gray = cv.cvtColor(img,cv.COLOR_RGB2GRAY)   #要二值化图像，要先进行灰度化处理
        ret, binary = cv.threshold(gray,75,255,cv.THRESH_BINARY)# | cv.THRESH_OTSU)
        
        return binary
   
    
    def handle(self):
        cap = cv.VideoCapture(0)#从摄像机中读取视频
        self.mv.wave_hands()#举手，示意开始
        while cap.isOpened():#当摄像头开启的时候
            _, frame = cap.read()#获取视频中的图像帧
            frame=frame[:240,320:]#截取frame右上1/4部分，倒转后为实际图像的左下1/4部分
            res=self.to_gray(frame)#转灰度图 
            res = self.rev_cam(res)#摄像头倒转添加
            cv.imshow("review", res)# 在窗口显示截取的图像
            command =self.fod.find_angel(res)#接受处理好的角度并根据角度转向
            if cv.waitKey(1)==27:#中途随时可以按esc结束
                cap.release()
            if command == 1:#前进
                self.mv.move_forward()
                print("前进")
            if command == 2:#逼进
                self.mv.move_forward(20)
                print("逼进")
            elif command == -1:#后退
                self.mv.move_backward()
                print("后退")
            elif command == -15:#左漂移
                self.mv.left_drift()
                print("左漂移")
            elif command == 15:#右漂移
                self.mv.right_drift()
                print("右漂移")
            elif command == -45:#左倾
                self.mv.left_ward()
                print("左倾")
            elif command == 45:#右倾
                self.mv.right_ward()
                print("右倾")
            elif command == -60:#左转
                self.mv.face_left()
                print("左转")
            elif command == 60:#右转
                self.mv.face_right()
                print("右转") 
            elif command == -90:#左拐
                self.mv.left_ward()
                print("左拐")
            elif command == 90:#右拐
                self.mv.right_ward()
                print("右拐")            
            elif command == 999:#停止
                self.mv.stop()
                print("停止")
                break
        cv.destroyAllWindows()#关闭这个窗口，进入找圆阶段
        while cap.isOpened():#当摄像头开启的时候
            _, frame = cap.read()#获取视频中的图像帧
            frame=frame[240:,:]#截取frame上半部分，倒转后为实际图像下半部分
            res=self.to_gray(frame)#转灰度图 
            res = self.rev_cam(res)#摄像头倒转添加
            cv.imshow("review_circle", res)# 在窗口显示截取的图像
            command =self.fod.find_circle(res) #接受处理好的指令
            if cv.waitKey(1)==27:#中途随时可以按esc结束
                cap.release()
            if command == 1:#前进
                self.mv.move_forward(10)
                print("前进")
            elif command == -361:#左移
                self.mv.move_left(10)
                print("左移")
            elif command == 361:#右移
                self.mv.move_right(10)
                print("右移")
            elif command == 777:#击打
                self.mv.hit()
                print("击打")
                break
        cap.release()#关闭摄像头
        cv.destroyAllWindows()#销毁所有窗口，程序结束
        
        return



if __name__ == '__main__':#main函数
	auto()
