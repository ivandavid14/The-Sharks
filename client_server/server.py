from socket import *
import sys
import os.path

HOST = ''
PORT = 80
ADDR = (HOST, PORT)
BUFSIZE = 4096

serv = socket(AF_INET, SOCK_STREAM)
serv.bind((ADDR))
serv.listen(5)

conn = None
addr = None

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
			command = msg.split(' ')

			if (len(command) == 3 and 'GET' in command) :
				
				print('ATTEMPTING TO OPEN FILE')
				f = None

				if(os.path.isfile('/tmp' + command[1])) :

					f = open('/tmp' + command[1])
					print("FILE OPENED")
					buf = None
						
					temp = 'HTTP/1.1 200 OK\n\n'
					buf = temp + f.read()
					print(buf)
					conn.send(buf)
					conn.close()
					break
			
				else :

					print("FILE CAN'T BE OPENED/FOUND")
					temp = 'HTTP/1.1 404 Not Found'	
					conn.send(temp)
					conn.close()
					break
		
	except :
		serv.close()
		if conn is not None :
			conn.close()
		sys.exit()
serv.close()
