# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 11:16:50 2018

@author: Gehaha
"""
import sys
from SlamCar3 import Ui_MainWindow
import binascii
import threading
import stopThreading

import serial
import socket
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import QFileDialog ,QDialog,QWidget
sys.path.append('D:\Practice\10.2')
import serial.tools.list_ports
#逻辑部分
class SignalLogic(QtWidgets.QMainWindow,Ui_MainWindow):
    ser = serial.Serial()
  
    def __init__(self):  #析构函数，实例化后默认加载
        super(SignalLogic,self).__init__()  #超级加载
        self.setupUi(self)
        self.tcp_scoket = None
        self.server_th = None
        self.client_th = None
        self.client_socket_list = list()
        self.link = False # 用于标记是否开启连接
        
        self.OpenPort.clicked.connect(self.port_open)
        self.ClosePort.clicked.connect(self.port_close)
        self.CheckpushButton.clicked.connect(self.port_check)
        self.OpenFile.clicked.connect(self.open_file)
        self.SendFile.clicked.connect(self.send_file)
        self.Send.clicked.connect(self.send_data)
        self.OpenServer.clicked.connect(self.tcp_server_start)
        self.ConnectServer.clicked.connect(self.tcp_client_start)
        self.GetLocaButton.clicked.connect(self.get_location)
        self.sendMsgButton.clicked.connect(self.send_message)
        self.request_pushButton.clicked.connect(self.tcp_send)
        
        self.connect()
        
        
    def connect(self):
       # 控件的信号
        self.signal_write_msg.connect(self.write_msg)
    def write_msg(self,msg):
        #向接收区写入数据的方法
        self.RectextEdit.insertPlainText(msg)
        #滚动条移到结尾
        self.RectextEdit.moveCursor(QtGui.QTextCursor.End)
                                          
    #打开串口
    def port_open(self):
        self.ser.port = self.port_comboBox.currentText()
        self.ser.baudrate = self.Baud_comboBox.currentText()
        self.ser.bytesize = int(self.Data_comboBox.currentText())
        self.ser.stopbits = int(self.Stop_comboBox.currentText())
        self.ser.parity = self.Check_comboBox.currentText()
        self.ser.open()
        if (self.ser.isOpen()):
            self.OpenPort.setEnabled(False) #打开不成功
            self.CheckStaLab.setText("打开成功")
            self.t1 = threading.Thread(target = self.receive_data)
            #isdaemon()判断
            self.t1.setDaemon(True)
            self.t1.start()
        else:
            self.CheckStaLab.setText("打开失败")
            
    #关闭串口
    def port_close(self):
        self.ser.close()
        if (self.ser.isOpen()):
            self.CheckStaLab.setText("关闭失败")
        else:
            self.OpenPort.setEnabled(True)
            self.CheckStaLab.setText("关闭成功")
    #发送数据
    def send_data(self):
        #串口接收数据
        if(self.ser.isOpen):          
            if(self.Hex2_radioButton.isChecked()):
                self.ser.write(hex(self.SendtextEdit.toPlainText()))             
                #self.ser.write(binascii.b2a_hqx(self.SendtextEdit.toPlainText()))
            elif(self.ASCII2_radioButton.isChecked()):                
                self.ser.write(binascii.a2b_hex(self.SendtextEdit.toPlainText()))                
            else:
                self.ser.write(self.SendtextEdit.toPlainText().encode('utf-8'))
            self.CheckStaLab.setText("发送成功")
        else:
            self.CheckStaLab.setText("发送失败")
                  
    #接收数据
    def receive_data(self):
        print("receive data threading is start")
        res_data = ()
        #接收次数，初始为0，每接收一次增加一次
        num = 0 
        while(self.ser.isOpen()):
            size = self.ser.inWaiting()
            if size:
                res_data = self.ser.read_all()
                if(self.Hex_radioButton.isChecked()):
                    self.RectextEdit.append(binascii.b2a_hex(res_data).decode())             
                elif(self.ASCII1_radioButton.isChecked()):
                   self.RectextEdit.append(binascii.b2a_hex(res_data).decode())                                  
                else:
                    self.RectextEdit.append(res_data.decode())                 
                self.RectextEdit.moveCursor(QtGui.QTextCursor.End)
                self.ser.flushInput()
                num += 1
                self.CheckStaLab.setText("接收:" + str(num))
                
    #发送文件
    def send_file(self):
        if (self.ser.isOpen()):
            if(self.Hex2_radioButton.isChecked()):
                self.ser.write(binascii.a2b_hex(self.SendtextEdit.toPlainText()))
            else:
                self.ser.write(self.SendtextEdit.toPlainText().encode('utf-8'))
            self.CheckStaLab.setText("发送成功")
        else:
            self.CheckStaLab.setText("发送失败")
    #检查串口
    def port_check(self):
        Com_List = []
        port_list = list(serial.tools.list_ports.comports())
        #self.port_comboBox.clear()
        for port in port_list:
            Com_List.append(port[0])
            self.port_comboBox.addItem(port[0])
        if (len(Com_List) == 0):
            self.CheckStaLab.setText("没串口")
            
    #打开文件
    def open_file(self):
        filename = QFileDialog.getOpenFileName(self,"打开文件","./","All Files (*);;Text Files (*.)")
        if filename[0]:
            f = open(filename[0],'r')
            with f:
                data = f.read()
                self.SendtextEdit.setText(data)
                
                
    #作为客户端端，连接服务器   
    def connect_server(self):
        self.model = self.TCP_comboBox.currentText()
        self.BUFSIZE = 1024
        self.address = ('127.0.0.1')
        self.port = 8888# 服务器的端口
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)       
        #连接服务器
        self.client.connect((self.address,self.port))
        self.CheckStaLab.setText("连接成功")
    
    #功能函数，tcp服务端开启的方法
    def tcp_server_start(self):
        
        self.tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #取消主动断开连接四次握手后的TIME_WAIT状态
        self.tcp_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSERADDR,1)
        #设定套接字为非阻塞式
        self.tcp_socket.setblocking(False)
        try:
            port = int(self.PortlineEdit.text())
            self.tcp_socket.bind(('',port))
        except Exception as ret:
            msg = '请检查端口号\n'
            self.signal_write_msg.emit(msg)
        else:
            self.tcp_socket.listen()
            self.server_th = threading.Thread(target = self.tcp_server_concurrency)
            self.server_th.start()
            msg = 'TCP服务端正在监听端口：%s\n ' % str(port)
            self.signal_write_msg.emit(msg)
         
       
    def tcp_server_concurrenct(self):
        """
        功能函数，供创建线程的方法；
        使用子线程用于监听并创建连接，使主线程可以继续运行，以免无响应
        使用非阻塞式并发用于接收客户端消息，减少系统资源浪费，使软件轻量化
        """
        while True:
            try:
                client_socket ,client_address = self.tcp_scoket.accept()
            except Exception as ret:
                pass
            else:
                client_socket.setblocking(False)
                #将创建的客户端套接字存入列表，client_address 为ip和端口的元祖
                self.client_socket_list.append((client_socket,client_address))
                msg = 'TCP服务端连接IP:%s端口：%s\n'% client_address
                self.signal_write_msg.emit(msg)
        #轮询客户端套接字列表，接收数据
        for client,address in self.client_socket_list:
            try:
                recv_msg = client.recv(1024)
            except Exception as ret:
                pass
            if recv_msg:
                msg = recv_msg.decode('utf-8')
                msg = '来自IP:{}端口:{}:\n{}\n'.format(address[0], address[1], msg)
                self.signal_write_msg.emit(msg) 
            else:
                client.close() 
                self.client_socket_list.remove((client, address))
            
    def tcp_client_start(self):
        """
        功能函数，TCP客户端连接其他服务端的方法
        """
        self.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            address = (str(self.IPlineEdit.text()), int(self.PortlineEdit.text()))
        except Exception as ret:
            msg = '请检查目标IP，目标端口\n'
            self.signal_write_msg.emit(msg)
        else:
            try:
                msg = '正在连接目标服务器\n'
                self.signal_write_msg.emit(msg)
                self.tcp_socket.connect(address)
            except Exception as ret:
                msg = '无法连接目标服务器\n'
                self.signal_write_msg.emit(msg)
            else:
                self.client_th = threading.Thread(target=self.tcp_client_concurrency, args=(address,)) 
                self.client_th.start() 
                msg = 'TCP客户端已连接IP:%s端口:%s\n' % address 
                self.signal_write_msg.emit(msg)
    def tcp_client_concurrency(self,address):
        #功能函数，用于TCP客户端创建子线程的方法，阻塞式接收
        while True:
            recv_msg = self.tcp_socket.recv(1024) 
            if recv_msg: 
                msg = recv_msg.decode('utf-8') 
                msg = '来自IP:{}端口:{}:\n{}\n'.format(address[0], address[1], msg) 
                self.signal_write_msg.emit(msg) 
            else: 
                self.tcp_socket.close() 
                self.reset() 
                msg = '从服务器断开连接\n' 
                self.signal_write_msg.emit(msg)
                break
    def tcp_send(self):
        #用于TCP服务端和TCP客户端发送消息
        if self.link is False:
            msg = '请选择服务，并点击连接网络\n'
            self.signal_write_msg.emit(msg)
        else:
            try:
                send_msg =(str(self.SendtextEdit.toPlainText())).encode('utf-8')
                if self.Model_comboBox.currentIndex() == 0:
                    #向所有连接的客户端发送消息
                    
                    for client, address in self.client_socket_list:
                        client.send(send_msg)
                    msg = 'TCP服务端已发送\n'
                    self.signal_write_msg.emit(msg) 
                if self.comboBox_tcp.currentIndex() == 1: 
                    self.tcp_socket.send(send_msg) 
                    msg = 'TCP客户端已发送\n' 
                    self.signal_write_msg.emit(msg) 
            except Exception as ret:
                msg = '发送失败\n' 
                self.signal_write_msg.emit(msg)
    def  tcp_close(self):
        #关闭网络连接的方法
        if self.Model_comboBox.currentIndex() == 0:
            try:
                for client,address in self.client_socket_list:
                    client.close()
                    if self.link is True:
                        msg = '已断开网络\n'
                        self.singnal_write_msg.emit(msg)
            except Exception as ret:
                pass
            if self.Model_comboBox.currentIndex() == 1:
                try:
                    self.tcp_socket.close()
                    if self.link is True:
                        msg = '已断开网络\n'
                        self.signal_write_msg.emit(msg)
                except Exception as ret:
                    pass
            try:
                stopThreading.stop_thread(self.server_th)
            except Exception:
                pass
            try:
                stopThreading.stop_thread(self.client_th)
            except Exception:
                pass
            
     #得到位置信息
    def get_location(self):        
        #首先要检查出口是否打开
        if(self.ser.isOpen() ):        
            if(self.Hex2_radioButton.isChecked()):
                self.ser.write(binascii.a2b_hex(self.SendtextEdit.toPlainText('0x10')))
            else:
                self.ser.write(self.SendtextEdit.toPlainText('0x10').encode('utf-8'))
            self.CheckStaLab.setText("开始获取位置信息")
        else:
            self.CheckStaLab.setText("位置获取失败")
            
    def send_message(self):
        if(self.ser.isOpen()):
            if(self.Hex2_radioButton.isChecked()):
                self.ser.write(binascii.a2b_hex(self.angle_textEdit.toPlainText()))
                self.ser.write(binascii.a2b_hex(self.Coords_textEdit.toPlainText()))
                self.ser.write(binascii.a2b_hex(self.speed_textEdit.toPlainText()))
            else:
                self.ser.write(self.angle_textEdit.toPlainText().encode('utf-8'))
                self.ser.write(self.Coords_textEdit.toPlainText().encode('utf-8'))
                self.ser.write(self.speed_textEdit.toPlainText().encode('utf-8'))
            self.CheckLab.setText("发送成功")
        else:
            self.CheckLab.setText("发送失败")
#程序调用界面                
#调用程序    
if __name__ == '__main__':
    
    app = QtWidgets.QApplication(sys.argv) #外部参数列表
    MainWindow = QtWidgets.QMainWindow()  # 
    ui = SignalLogic()  
    ui.show() 
    sys.exit(app.exec_())  #退出中使用的消息循环，结束消息循环时就退出程序


