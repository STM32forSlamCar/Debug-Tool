# -*- coding: utf-8 -*-

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

# fixed for MODULEID  9.24  birthday
MODULEID = 0x039C 
# moduleId + dataId + dataLen + recvLen
DataHead = [MODULEID, 0x0000, 0x00, 0x00]

Head_ = DataHead
byData_ = [0x00000000,0x00000000]
check_ = 0x0000

SerialPackage = [Head_, byData_, check_]

# test
def test():
    pack = SerialPackage

    pack[0][1] = CmdId['DEBUG_QT_COMMOND']  # dataId
    pack[0][2] = 2                          # dataLen
    pack[0][3] = 0                          # recvLen

    # x100
    speed = 110  
    angle = 300  

    pack[1][0] = int(speed)
    pack[1][1] = int(angle)

    pack[2] = 0x1234
    # print("dataId: %X" %SerialPackage[0][1])
    print("dataId: %X" %pack[0][1])
    print("speed:",pack[1][0])
    print("angle:",pack[1][1])
    print("check: %X" %pack[2])

    # !!!
    # print(id(SerialPackage))
    # print(id(pack))


# test()