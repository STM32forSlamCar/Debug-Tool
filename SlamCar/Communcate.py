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
            self.__connectState = False
            self.__ser = serial.Serial()
        else:
            pass

    # def connect(self):
    #     # TODO 
    #     # open port ttyUSB0 115200bps
    #     # success return true
    #     # faild return false

    # def close(self):
    #     # TODO 
    #     # close serial port

    def receive(self):
        SerialPackage = DataPack()
        # TODO
        # serial receive msg to self.__SerialPack
        SerialPackage = DataPack()
        if SerialPack.Head.dataId == CmdId['STM32_FEED_BACK'] :
            self.__updateFeedback(SerialPack.bydata)
        else:
            print("dataId error")


    def sendCmd(self):
        db = DataBase()
        
        SerialPackage = DataPack(CmdId['DEBUG_QT_COMMOND'])
        SerialPackage.setDataLen()




    # def __read():

    # def __write():

    def __updateCmd(data):
        db = DataBase()
        db.cmdMsg = data

    def __updateFeedback(data):
        db = DataBase()
        db.feedbackMsg = data



 
# test this class
def test():
    McuCommuncate = Communcate()
    if McuCommuncate.connect():
        print("connect sucess")
    else:
        print("connect failed")
        return
    
    McuCommuncate.send()