# Robot-Fighting-Competition-Humanoid-Visual
2020 China Intelligent Robot Fighting Competition humanoid vision against A

系统概述： 
仿人视觉对抗项目通过设置不同难度的任务，逐步提高机器视觉 
及运动控制在机器人格斗对抗中的应用水平，本次任务是攻击标靶，机器人通过视觉识别道路并沿着赛道自行走到靶区，在靶区击倒标靶。 

系统环境： 
1）	硬件环境： 
UP 格斗机器人，树莓派背包，摄像头，PC 机或笔记本 

2）	软件环境： 
Linux，shell，python，nomachine，opencv 

3）	测试环境： 
统一部件组仿人视觉对抗比赛场地

硬件设计： 
基于博创尚和公司的智元素-格斗机器人，设计一套自动驾驶系统，用于参加统一部件组仿人视觉对抗比赛。自动驾驶系统底盘采用的是双排三轮全向底盘，相比单排全方位轮，双板的全方位轮滚筒之间没有死区，底盘通过 arduino 编程可以实现在各个不同的方向移动，同时 arduino 也是作为整个格斗机器人的控制系统。   
自动驾驶系统的视觉识别部分，是通过格斗机器人提供的树莓派背包来实现的，树莓派通过连接一个外接 USB 摄像头，采集赛场数据， 然后通过USB 口发送给树莓派，树莓派接收到赛场图像数据后，对赛场数据进行处理，赛道是白色的，其余部分为黑色，本系统中采用二值化处理，将赛道的白色单独显示出来，同时也没有分析整个摄像头范围，而是选取图像中的一行像素进行处理，通过算法，让小车一直朝着跑道中点矫正。    
关于算法的实现，通过调用 opencv 接口，实现对图像的采集以及数据处理。树莓派与 arduino 之间通过串口进行通信，树莓派对图像进行处理后的转向控制命令，通过调用博创尚和公司提供的一组接口来进行，最终实现对整个系统的控制。  

系统框架：
auto_move为主文件，运行时由此进入
found接受帧返回角度，auto由此判断判定后续行走路线
robot_Cmd收集各种参数（角度，速度，转向，时间）生成各种动作命令
robot_serOp将命令传送给机器人
robot_movement调动Cmd和SerOp，一个方法对应一套参数一个命令
 
软件策略： 
软件编程方面，采用 Python 语言，需要在开始引入 cv2、robotPi、 robotpi_movement 等多个库，其中 cv2 用于 opencv 的引入，用来实现 USB 摄像头的图像采集，并对采集的图像进行处理，主要涉及的函数如下:   
self.cap = cv2.VideoCapture(self.CAM_NUM) #用于获取摄像头数据   
ret, frame = self.cap.read() #获取视频中的图像帧  
gray = cv.cvtColor(img,cv.COLOR_RGB2GRAY) #转换为灰度图像并进行二值化   
dst = cv.dilate(dst,None,iterations=2) 	#放大白色区域     
find_angel(self,gray):#寻路算法,然后找到4个白点位置，根据白点位置设计算法，控制底盘直行，左转， 右转，并最终走到目标去， 最后在目标去挥动。  
robotPi_Cmd 、 robotpi_serOp 和 robotpi_movement #用于机器人控制和底盘的运动，控制指令通过树莓派的串口发送给 arduino，再由 arduino 接收后，控制机器人执行各种移动和击打等动作。   
