# -*- coding: utf-8 -*-
import Protocal
from Protocal import SerialPackage  

class DataPack():

    def __init__(self):
        self.__msg = Protocal.SerialPackage

    # def __init__(self, id):
    #     self.__msg = Protocal.SerialPackage
    #     self.__msg[0][1] = id
    #     self.__msg[0][3] = 0

    def setData(self, data):
        self.__msg[0][1] = data[0:2]
        self.setDataId(data[2:4])
        self.setLen(data[4])
        self.__msg[0][3] = data[5]
        self.setBody(data[6:6+data[4]])
        self.setCrc(data[6+data[4]:])

    def setDataId(self, id):
        self.__msg[0][1] = id

    def setLen(self, len):
        self.__msg[0][2] = len

    def setBody(self, bydata):
        self.__msg[1] = bydata

    def setCrc(self, crc):
        self.__msg[2] = crc
    
    def dataId(self):
        return self.__msg[0][1]

    def len(self):
        return self.__msg[0][2]

    def data(self):
        return self.__msg
        # Head = self.__msg[0][0] + self.__msg[0][1]
        # Head.append(self.__msg[0][2])
        # Head.append(self.__msg[0][3])
        
        # return Head + self.__msg[1] + self.__msg[2]


    def body(self):
        return self.__msg[1]
    
    def crc(self):
        return self.__msg[2]

    def size(self):
        # print(len(self.__msg[0]))
        # print(len(self.__msg[1]))
        # print(len(self.__msg[2]))
        return Protocal.HeadSize + len(self.__msg[1]) + Protocal.CrcSize

    def generateCrc(self):
        crc = self.__crcVerify()
        self.__msg[2] = crc
        print("crc: ",crc)

    def checkCrc(self):
        crc = self.__crcVerify()
        print (crc)
        return self.__msg[2] == crc

    def __crcVerify(self): 
        crc = 0
        for i in self.__msg[0][0]:
            crc += i
        
        for i in self.__msg[0][1]:
            crc += i

        crc += self.__msg[0][2]
        crc += self.__msg[0][3]
        
        for i in self.__msg[1]:
            crc += i
        return crc



# test this class
def test():

    data = [0x9c,0x03,0x10,0x50,0x08,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x07,0x01]
    msg = DataPack()  

    msg.setData(data)

    # print("dataId:", msg.dataId())
    # print("dataLen:", msg.len())
    # print("body:" ,msg.body())
    # print("crc:",msg.crc())
    # print("size:",msg.size())

    print("data:", msg.data())


# test()