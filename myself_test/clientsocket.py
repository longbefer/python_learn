# import socket

# # af_inet 代表ipv4 
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# host = socket.gethostname()
# port = 9999


# while True:
#     # 连接服务器，需要服务器地址和端口
#     s.connect((host, port))

#     # 接收服务器数据
#     servermsg = s.recv(1024)
#     print('sever address: %s' % str(host))
#     print('%s\n' % servermsg.decode('utf-8'))

#     # 向服务器发送数据
#     sendmsg = input("send message to server: \n")
#     s.send(str(sendmsg).encode('utf-8'))

#     s.close()


#!/usr/bin/python3
# -*-coding:utf-8 -*-
from socket import *
from time import ctime
HOST = gethostname() # '192.168.164.141' #服务端ip
PORT = 21566 #服务端端口号
BUFSIZ = 1024
ADDR = (HOST, PORT)
tcpCliSock = socket(AF_INET, SOCK_STREAM) #创建socket对象
tcpCliSock.connect(ADDR) #连接服务器
while True:
    data = input('>>').strip()
    if not data:
        break
    tcpCliSock.send(data.encode('utf-8')) #发送消息
    data = tcpCliSock.recv(BUFSIZ) #读取消息
    if not data:
        break
    print(data.decode('utf-8'))
tcpCliSock.close() #关闭客户端