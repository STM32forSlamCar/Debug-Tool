import serial

class Communcate(object):
    """communcate with mcu"""

    __instance = None
    __isFirstInit = False

    def __new__(cls):
        if not cls.__instance:
            Communcate.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        if not self.__isFirstInit:
            # self.__connectState = False
            self.__ser = serial.Serial()
        else:
            pass

    def  __del__(self):
        self.__ser.close()

    def connect(self):
        self.__ser.baudrate = 115200
        self.__ser.port = "/dev/ttyUSB0"
        self.__ser.bytesize = serial.EIGHTBITS
        self.__ser.stopbits = serial.STOPBITS_ONE
        self.__ser.parity =  serial.PARITY_NONE
        self.__ser.open()
        if(self.__ser.isOpen()):
            print("open serial success")
            return True
        else:
            print("open serial faild !!!")
            return False  
        # open port ttyUSB0 115200bp
        # success return true
        # faild return false

    def close(self):
        # TODO 
        # close serial portrint
        self.__ser.close()
    
    # omit a single 
    def receive(self):
        # TODO
        res_data = ()
        while(self.__ser.isOpen()):
            size = self.__ser.inWaiting()
            if size:
                # print(size) 
                res_data = self.__ser.read_all()
                # print("%X" %res_data[2])
                # print("%X" %res_data[3])
                return res_data
                self.__ser.flushInput()
            
    def send(msg):
     # self.__ser.send()
        self.__ser.write(msg)

    # def __read():


    # def __write():

 
# test this class
def test():
    McuCommuncate = Communcate()
    McuCommuncate.connect()

    while True:
        msg = McuCommuncate.receive()
        # for i in msg:
            # print("%X" %i)


test()
