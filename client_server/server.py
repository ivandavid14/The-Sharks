from socket import *
import sys
import os.path

HOST = ''
PORT = 400
ADDR = (HOST, PORT)
BUFSIZE = 4096

serv = socket(AF_INET, SOCK_STREAM)
serv.bind((ADDR))
serv.listen(5)

conn = None
addr = None

f = open('/tmp/messages.txt', 'w+')

while True :
	try :
		conn,addr = serv.accept()
			
		print '...connected'

		while True :	

			msg = conn.recv(BUFSIZE)
			if len(msg) == 0 : 
				conn.close()
				serv.close()
				break

			#decrypt here

			print(msg)
			f.write(msg)
		
	except :
		serv.close()
		if conn is not None :
			conn.close()
		sys.exit()
serv.close()
