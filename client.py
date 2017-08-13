#coding=utf-8
import socket
sk=socket.socket()
ip_port=("127.0.0.1",9999)
#the client connects,use connect(ip_port)
sk.connect(ip_port)
while True:
	print "Computer:"
	str=raw_input()
	#the client sends message to the server_reply
	sk.sendall(str)
	server_reply=sk.recv(1024)
	print "Liuyunfei:"
	print server_reply
        #do not forget to close the socket
	sk.close()
