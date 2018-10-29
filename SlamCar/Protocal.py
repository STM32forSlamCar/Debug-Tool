# -*- coding: utf-8 -*-

HEADER_BYTESIZE = 6
BODY_MAX_BYTESIZE = 8
CRC_BYTESIZE = 2

MODULEID = 0x039C    # fixed for MODULEID  9.24  birthday

CmdId = {
    # TEST
    'DEBUG_TEST_COMMOND'   : 0x0001,

    # QT -> STM32
    'DEBUG_QT_COMMOND'     : 0xA010,

    # QT || IPC -> STM32
    'CMD_GET_VERSION'      : 0x1010,
    'CMD_IPC_COMMOND'      : 0x2010,
    'CMD_RESET'            : 0x2020,
    
    # STM32 -> IPC || QT
     
    'STM32_FEED_BACK'      : 0X5010,
    'STM32_HEART_BEAT'     : 0x6010,
    'STM32_TASK_FINISH'    : 0x7010,

}

class DataHead:
    def __init__(self):
        self.__moduleId__ = MODULEID    # fixed for MODULEID  9.24  birthday
        self.dataId   = 0x0000
        self.dataLen  = 0x00
        self.recvLen  = 0x00

class SerialPackage:
    def __init__(self):
        self.Head = DataHead()
        self.byData = []               # data content, max size is 
        self.check = 0x0000



# test this class
def test():
    pass