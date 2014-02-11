##client.py
from socket import *
import sys

HOST = None

if len(sys.argv) != 2 :
	print('Please enter a server name, exiting...')
	sys.exit()

HOST = sys.argv[1]

PORT = 80
ADDR = (HOST,PORT)
BUFSIZE = 4096

while True : 
	try :
		client = socket(AF_INET, SOCK_STREAM)
		client.connect((ADDR))
	
	except gaierror, (value, message) :
		if(client) :
			client.close()
		print('Bad server name, exiting...')
		sys.exit()

	print('CONNECTION STARTED\n')

	msg = raw_input('Enter the name of the file you would like to get \n' + \
			'format is filename.html, you must type .html :')
	if msg == 'done' :
		client.close()
		break

	print('')

	new_msg = 'GET ' + '/' + msg + ' HTTP/1.1'

	client.send(new_msg)
	data = []
	while True :
		temp = client.recv(BUFSIZE)
		data.append(temp)
		if len(temp) == 0 :
			client.close()
			print('CONNECTION ENDED\n')
			break

	message = ''.join(data)
	print('Writing to /tmp/' + msg + '\n')
	
	write_file = open('/tmp/' + msg, 'w+')
	write_file.write(message)
	write_file.close()
	print('Done writing\n')

	temp = raw_input('Do you want to print the file to standard out (y/n)?')
	if temp == 'y' or temp == 'Y' :
		print(message + '\n')

client.close()
