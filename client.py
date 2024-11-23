#客服端服务器
# 导入socket模块包  自带模块无需安装
from socket import *
import threading
from threading import Thread
# 去连接服务器
s = socket() #准备一个套接字
s.connect(('192.168.2.9', 4444))
#给自己取一个名字，把名字告诉服务器
name = input('请给自己取一个名字：')
s.send(name.encode())
#子线程函数
def recv_msg(s):
    while True:
        print(s.recv(2048).decode())
#开启线程
threading,Thread(target = recv_msg, args = (s,)).start()

#主线程：给服务器发消息
while True:
    s.send(input('请输入你要发送的消息：').encode())
#主线程
#1.去连接服务器
# 2.开一个分身，分身去接收消息
# 3.循环给服务器发送消息就可以了
'''-----------使用步骤-------------'''
# 1.把你的ip改成你的服务器的ip地址
# 2.然后把客户端打包成exe就行了


