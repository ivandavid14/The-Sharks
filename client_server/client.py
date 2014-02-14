##client.py
from socket import *
import sys
import os.path
import time
import struct

HOST = None

if len(sys.argv) != 2 :
	print('Please enter a server name, exiting...')
	sys.exit()

HOST = sys.argv[1]

PORT = 400
ADDR = (HOST,PORT)
BUFSIZE = 4096

sequence_number = 0

while True : 
	try :
		client = socket(AF_INET, SOCK_STREAM)
		client.connect((ADDR))
	
	except gaierror, (value, message) :
		if(client) :
			client.close()
		print('Bad server name, exiting...')
		sys.exit()	

	msg = None
	f = None

	while True :
		path = raw_input('Enter messages file (full path): ')	
		if(os.path.isfile(path)) :
			f = open(path)
			break
		else :
			print("File doesn't exist, try again")

	while True :
		#read data from file here
		#ask teacher to see if the messages end in a newline char or
		#if they don't end in a newline char, then they are 100 bytes
		#including newline character
		line = f.readline(100)
		if len(line) == 0 :
			client.close()
			sys.exit()
	
		data = None
		if '\n' in line :
			data = line[0:len(line) - 1]
		else :
			data = line[0:len(line)]

		#encrypt here

		#put a sequence number here
		msg = struct.pack('i' + str(len(data)) + 's', sequence_number, data)
		print(msg[1:])
		sequence_number = sequence_number + 1
		
		#send
		client.send(msg)

		#sleep here
		time.sleep(2)
f.close()
client.close()
