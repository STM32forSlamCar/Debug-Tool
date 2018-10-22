# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 21:52:28 2018

@author: Gehaha
"""
from struct import*
import serial

#打包数据包
class SerialPackage:
    """
    规定包头占6个字节
    数据段不超过50个字节
    crc校验码2个字节
    
    """
    
    def __init__(self,bs = None):
        """
        如果bs为None则代表需要创建一个数据包
        否则代表需要解析一个数据包
        """
        if bs:
            self.bs = bytearray(bs) #bytearray 方法返回一个新字节数组
        else:
            self.bs = bytearray(0)
    #       
    def get_int32(self):
        try:
            ret = self.bs[:6]
            self.bs = self.bs[6:]
            return int.from_bytes(ret, byteorder ='little')
        except:
            raise Exception("数据异常！")
    def get_str(self):
        try:
            #拿到字符串字节长度(字符串长度位2字节)            
            length = int.from_bytes(self.bs[:2],byteorder = 'little')
            #再拿字符串
            ret = self.bs[2:length + 2]
            # 删掉取出来的部分
            self.bs = self.bs[2 + length:]
            return ret.decode(encoding='utf8')
        except:
            raise Exception("数据异常！")
 
    def add_int32(self, val):
        bytes_val = bytearray(val.to_bytes(4, byteorder='little'))
        self.bs += bytes_val
 
    def add_str(self, val):
        bytes_val = bytearray(val.encode(encoding='utf8'))
        bytes_length = bytearray(len(bytes_val).to_bytes(2, byteorder='little'))
        self.bs += (bytes_length + bytes_val)
 
    def get_pck_not_head(self):
        return self.bs
 
    def get_pck_has_head(self):
        bytes_pck_length = bytearray(len(self.bs).to_bytes(4, byteorder='little'))
        return bytes_pck_length + self.bs
 
 
if __name__ == '__main__':
    p = SerialPackage()
 
    p.add_int32(666)
    p.add_str("你好啊")
    p.add_str("hello")
    p.add_int32(888)
 
    r =SerialPackage(p.get_pck_not_head())
 
    print(r.get_int32())
    print(r.get_str())
    print(r.get_str())
    print(r.get_int32())

            
    
