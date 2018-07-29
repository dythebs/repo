import requests
from socket import *  
import os
import time
import struct
import threading

nowmsgsize = 0
BUFFER = bytearray()
HOST = 'openbarrage.douyutv.com' 
PORT = 8601
BUFSIZ = 1024  
roomid = '67373'
ADDR = (HOST, PORT) 


tcpClientSock = socket(AF_INET, SOCK_STREAM)  
tcpClientSock.connect(ADDR)

url = 'http://open.douyucdn.cn/api/RoomApi/room/' + roomid

def pack_msg(msg):
	msglen = len(msg) + 8
	return struct.pack("iihbb",msglen,msglen,689,0,0) + msg.encode('utf-8')
def deserialization(msg):
	msg_dict = {}
	for array in msg.split('/') :
		keyandvalue = array.split('@=')
		if len(keyandvalue) == 2 :
			msg_dict[keyandvalue[0].replace('@S','/').replace('@A','@') ]= keyandvalue[1].replace('@S','/').replace('@A','@')
	if msg_dict['type'] == 'chatmsg':
		_str = danmuformat(msg_dict)
		print(_str)

def praser():
	global nowmsgsize
	global BUFFER
	while True :
		if nowmsgsize == 0 :
			if len(BUFFER) < 4 :
				return
			else :
				nowmsgsize = struct.unpack('i',BUFFER[0:4])[0]
				del BUFFER[0:4]


		if len(BUFFER) < nowmsgsize :
				return
		else :
			try:
				deserialization(BUFFER[8:nowmsgsize].decode())
			except UnicodeDecodeError as e:
				print(BUFFER[8:nowmsgsize])
			finally :
				del BUFFER[0:nowmsgsize]
				nowmsgsize = 0

def heartbeat():
	while True:
		tcpClientSock.send(pack_msg('type@=mrkl/' + '\0'))
		time.sleep(5)

def danmuformat(msg_dict):
	return '[弹幕] [%s] %s:%s' % ( time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())), msg_dict['nn'] ,msg_dict['txt'])

tcpClientSock.send(pack_msg('type@=loginreq/roomid@=' + roomid + '/' + '\0'))
tcpClientSock.send(pack_msg('type@=joingroup/rid@=' + roomid + '/gid@=-9999/' + '\0'))
threading.Thread(target=heartbeat).start()

while True :
	BUFFER += bytearray(tcpClientSock.recv(BUFSIZ))
	praser()