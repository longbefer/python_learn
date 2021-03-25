# import socket
# import sys

# # 创建socket对象
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # 获取本地主机名
# host = socket.gethostname()
# port = 9999

# # 绑定端口
# s.bind((host, 9999))

# # 设置最大连接数，超过后排队
# s.listen(5)

# while True:
#     print('waiting user to connect...')
#     # 获取客户区的链接
#     clientsocket, addr = s.accept()
#     # 发送给首次访问的客户
#     clientsocket.send('welcome visited the site.'.encode('utf-8'))
    
#     # 获取用户地址
#     print("user address： %s" % str(addr))
#     # 获取用户发送给客户端的内容
#     print("content: %s\n" % clientsocket.recv(1024).decode('utf-8'))

#     clientsocket.close()

#!/usr/bin/python3
# -*-coding:utf-8 -*-
from socket import *
import time
COD = 'utf-8'
HOST = gethostname() # '192.168.164.141' # 主机ip
PORT = 21566 # 软件端口号
BUFSIZ = 1024
ADDR = (HOST, PORT)
SIZE = 10 
tcpS = socket(AF_INET, SOCK_STREAM) # 创建socket对象
tcpS.setsockopt(SOL_SOCKET,SO_REUSEADDR,1) #加入socket配置，重用ip和端口
tcpS.bind(ADDR) # 绑定ip端口号
tcpS.listen(SIZE)  # 设置最大链接数
while True:
    print("服务器启动，监听客户端链接")
    conn, addr = tcpS.accept() 
    print("链接的客户端", addr)
    while True:
        try:
            data = conn.recv(BUFSIZ) # 读取已链接客户的发送的消息
        except Exception:
            print("断开的客户端", addr)
            break
        print("客户端发送的内容:",data.decode(COD))
        if not data:
            break
        msg = time.strftime("%Y-%m-%d %X") #获取结构化事件戳
        msg1 = '[%s]:%s' % (msg, data.decode(COD))
        conn.send(msg1.encode(COD)) #发送消息给已链接客户端
    conn.close() #关闭客户端链接
tcpS.closel()