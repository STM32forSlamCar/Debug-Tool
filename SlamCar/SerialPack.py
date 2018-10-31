# -*- coding: utf-8 -*-
import Protocal
from Protocal import SerialPackage  

class DataPack():

    # def __init__(self):
    #     self.__msg = Protocal.SerialPackage

    def __init__(self, id):
        self.__msg = Protocal.SerialPackage
        self.__msg[0][1] = id
        self.__msg[0][3] = 0
    
    def setDataId(self, id):
        self.__msg[0][1] = id

    def setLen(self, len):
        self.__msg[0][2] = len

    def setBody(self, bydata):
        self.__msg[1] = bydata
    
    def dataId(self):
        return self.__msg[0][1]

    def len(self):
        return self.__msg[0][2]

    def data(self):
        return self.__msg.data()

    def body(self):
        return self.__msg[1]

    def size():
        return HEADER_BYTESIZE + BODY_MAX_BYTESIZE + CRC_BYTESIZE

    def generateCrc(self):
        crc = self.__crcVerify()
        self.__msg[2] = crc
        print("crc: ",crc)

    def checkCrc(self):
        crc = self.__crcVerify()
        return self.__msg[2] == crc

    def __crcVerify(self): 
        crc = 0
        for i in self.__msg[0]:
            crc += i
        
        for i in self.__msg[1]:
            crc += i
        return crc



# test this class
def test():
    msg =  DataPack(Protocal.CmdId['DEBUG_QT_COMMOND'])
    print("dataId: %X" %msg.dataId())
    print("dataLen: %X" %msg.len())
    print("body:", msg.body())

    print('----------------------------------')

    msg.setDataId(Protocal.CmdId['DEBUG_TEST_COMMOND'])
    msg.setLen(2)
    msg.setBody([110, 200])
    msg.generateCrc()
    print("dataId: %X" %msg.dataId())
    print("dataLen: %X" %msg.len())
    print("body:", msg.body())

    msgTest = msg
    # msgTest.setBody([111, 200])
    print(msgTest.checkCrc())



test()