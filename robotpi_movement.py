import time
from robotpi_Cmd import UPComBotCommand
from robotpi_serOp import serOp


class Movement():#命令操作

    def __init__(self):
        self.isOpen = True
        self.cmd = UPComBotCommand()
        self.action = serOp()

    def move(self,speed=200, turn=0, times=500):#移动
        if self.isOpen:
            command = self.cmd.Command(0, speed, turn, times)
            self.action.write_serial(command)
            return True
        return False

    def move_forward(self,speed=100):#直走
        if self.isOpen:
            command = self.cmd.Command(0, speed, 0, 500)
            self.action.write_serial(command)
            return True
        return False

    def move_left(self,speed=40,turn=0):#左移
        if self.isOpen:
            command = self.cmd.Command(90, speed, -turn, 500)
            self.action.write_serial(command)
            return True
        return False

    def move_right(self,speed=40,turn=0):#右移
        if self.isOpen:
            command = self.cmd.Command(270, speed, turn, 500)
            self.action.write_serial(command)
            return True
        return False

    def move_backward(self):#后退
        if self.isOpen:
            command = self.cmd.Command(180, 20, 0, 500)
            self.action.write_serial(command)
            return True
        return False

    def turn_left(self):#左拐
        if self.isOpen:
            command = self.cmd.Command(0, 100, 400, 1000)
            self.action.write_serial(command)
            return True
        return False

    def turn_right(self):#右拐
        if self.isOpen:
            command = self.cmd.Command(0, 100, -400, 1000)
            self.action.write_serial(command)
            return True
        return False
    
    def face_left(self):#左转
        if self.isOpen:
            command = self.cmd.Command(0, 0, 100, 1000)
            self.action.write_serial(command)
            return True
        return False

    def face_right(self):#右转
        if self.isOpen:
            command = self.cmd.Command(0, 0, -100, 1000)
            self.action.write_serial(command)
            return True
        return False
    
    def left_ward(self):#左倾
        if self.isOpen:
            command = self.cmd.Command(0, 100, 300, 1000)
            self.action.write_serial(command)
            return True
        return False

    def right_ward(self):#右倾
        if self.isOpen:
            command = self.cmd.Command(0, 100, -300, 1000)
            self.action.write_serial(command)
            return True
        return False
    
    def left_drift(self):#左漂移
        if self.isOpen:
            command = self.cmd.Command(0, 100, 100, 2000)
            self.action.write_serial(command)
            return True
        return False

    def right_drift(self):#右漂移
        if self.isOpen:
            command = self.cmd.Command(0, 100, -100, 2000)
            self.action.write_serial(command)
            return True
        return False

    def stop(self):#停止
        if self.isOpen:
            command = self.cmd.Command(0, 0, 0,200)
            self.action.write_serial(command)
            return True
        return False    
        
    def wave_hands(self):#举手
        if self.isOpen:
            command = self.cmd.wave_hands()
            self.action.write_serial(command)
            time.sleep(0.5)
            return True
        return False

    def hit(self):#击打
        if self.isOpen:
            command = self.cmd.hit()
            self.action.write_serial(command)
            time.sleep(1)
            return True
        return False