#coding=utf-8
'''
the socket has 3 steps mainly
1.the server listening
2.the client connect
3.the connection established
'''
import socket
sk=socket.socket()
ip_port=("127.0.0.1",9999)
sk.bind(ip_port)
#sk.listen(5) starts server listening
sk.listen(5)
while True:
    #the server is waiting for the message from client,if not,it will keep waiting all the time...
	conn,addr=sk.accept()
	message=conn.recv(1024)
	print "Computer:"
	print message
	print "Liuyunfei:"
	str=raw_input()
	conn.sendall(str)
	conn.close()
