#coding=utf-8
import socket
sk=socket.socket()
ip_port=("127.0.0.1",9999)
sk.bind(ip_port)
sk.listen(5)
while True:

	conn,addr=sk.accept()
	message=conn.recv(1024)
	print "Computer:"
	print message
	print "Liuyunfei:"
	str=raw_input()
	conn.sendall(str)
	conn.close()
