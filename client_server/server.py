from socket import *
import sys
import os.path
import struct

HOST = ''
PORT = 400
ADDR = (HOST, PORT)
BUFSIZE = 4096

serv = socket(AF_INET, SOCK_STREAM)
serv.bind((ADDR))
serv.listen(5)

conn = None
addr = None

if os.path.exists('/tmp/messages.txt') :
	f = open('/tmp/messages.txt', 'a')
else :
	f = open('/tmp/messages.txt', 'w+')

f.write('-----------------BEGINNING OF SEQUENCE OF MESSAGES--------------------\n')

while True :
	try :
		conn,addr = serv.accept()
			
		print '...connected'

		while True :	

			data = conn.recv(BUFSIZE)
			if len(data) == 0 : 
				conn.close()
				serv.close()
				break

			temp = struct.unpack('i' + str(len(data) - 4) + 's', data)
			print(str(temp[0]) + ': ' + temp[1])
			#decrypt here

			#write to file here
			f.write(str(temp[0]) + ': ' + temp[1] + '\n')
		
	except :
		serv.close()
		if conn is not None :
			conn.close()
		f.write('-----------------END OF SEQUENCE OF MESSAGES---------------------\n')
		f.close()
		serv.close()
		sys.exit()
f.close()
serv.close()
