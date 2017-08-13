#coding=utf-8
import socket
sk=socket.socket()
ip_port=("127.0.0.1",9999)
sk.connect(ip_port)
while True:
	print "Computer:"
	str=raw_input()
	sk.sendall(str)
	server_reply=sk.recv(1024)
	print "Liuyunfei:"
	print server_reply
	sk.close()