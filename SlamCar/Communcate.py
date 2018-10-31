import DataBase
import SerialPackage
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

    def connect(self):
        # TODO 
        # open port ttyUSB0 115200bp
        # success return true
        # faild return false

    # def close(self):
        # TODO 
        # close serial port


    # omit a single 
    def receive(msg):
        # TODO
        # serial receive msg to self.__SerialPack



    def sendCmd(msg):
        # self.__ser.send()

    # def __read():

    # def __write():




 
# test this class
def test():
    McuCommuncate = Communcate()
    # if McuCommuncate.connect():
    #     print("connect sucess")
    # else:
    #     print("connect failed")
    #     return
    
    McuCommuncate.sendCmd()

test()
