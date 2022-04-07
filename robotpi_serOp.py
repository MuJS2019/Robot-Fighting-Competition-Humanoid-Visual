import serial

class serOp():#端口操作

    ser = serial.Serial(
            port="/dev/ttyUSB0",#端口
            baudrate=115200,#波特率
            bytesize=8,#字节大小
            parity='E',#校验位
            stopbits=1,#停止位
            timeout=2)#超时设置
    isOpen = True

    def __int__(self):
        self.isOpen = True
        
    def open(self):#打开端口
        self.ser.open()
        if(serOp.ser.isOpen):
            self.isOpen = True
            print ("open")
        else:
            self.isOpen = False

    def serial_listen(self):#返回端口监听数据
        data = []
        while serOp.ser.inWaiting() > 0:#获取接收到的数据长度大于0
            k = serOp.ser.read()#从串口的缓冲区取出并读取一个Byte的数据
            data.append(int.from_bytes(k, byteorder='big', signed=False))
            #data二进制转int，正序原码，添加到data列表里
        return data

    def serial_string(self):#返回监听数据6位之后的数据
        data = b''
        while serOp.ser.inWaiting() > 0:
            k = serOp.ser.read()
            data += k
        return data[5:-1]

    def write_serial(self, command):#发送命令数据
        self.ser.write(command)
