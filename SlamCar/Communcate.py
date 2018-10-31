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
            # self.__ser = serial.Serial()
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
        # TODO
        # serial receive msg to self.__SerialPack
        msg = DataPack()
        if msg.dataId() == Procal.CmdId['STM32_FEED_BACK'] :
            self.__updateFeedback(msg)
        else:
            print("dataId error")


    def sendCmd(self):
        db = DataBase()
        db.cmdMsg = [0.1,20]
        
        SerialPackage = DataPack(Protocal.CmdId['DEBUG_QT_COMMOND'])
        SerialPackage.setLen(len(db.cmdMsg))
        SerialPackage.setBody(db.cmdMsg)
        SerialPackage.generateCrc()
        # print(SerialPackage.dataId())

        print('%x' %SerialPackage.dataId())
        print('%x' %len(db.cmdMsg))




    # def __read():

    # def __write():

    # def __updateCmd(data):
    #     db = DataBase()
    #     db.cmdMsg = data

    # def __updateFeedback(data):
    #     db = DataBase()
    #     db.feedbackMsg = data



 
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

