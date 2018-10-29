# -*- coding: utf-8 -*-
import Protocal
from Protocal import SerialPackage 

class ProtocalPack:

    def data(self):
        pass
    
    def size(self):
        pass
    
    def crcVerify(self, buf, size): 
        wCrc = 0
        for i in range(0, size):
            wCrc += buf[i]
        return wCrc 

class DataPack(ProtocalPack):
    
    def __init__(self, id):
        self.__msg = SerialPackage()
        self.__msg.Head.dataId = id
    
    def setDataId(self, id):
        self.__msg.dataId = id

    def setLen(self, len):
        self.__msg.dataLen = len

    def setBody(self, data):
        self.__msg.byData = data
    
    def dataId(self):
        return self.__msg.dataId

    def len(self):
        return self.__msg.Head.dataLen

    def data(self):
        return self.__msg

    def body(self):
        return self.byData

    def size():
        return HEADER_BYTESIZE + BODY_MAX_BYTESIZE + CRC_BYTESIZE

    def generateCrc(self):
        crc = crcVerify(buf, size)
        self.__msg.check = crc

    def checkCrc(self):
        crc = self.crcVerify(buf,size)
        return self.__msg.check == crc




# test this class
def test():
    pass