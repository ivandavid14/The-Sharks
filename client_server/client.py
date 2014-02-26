## client.py
from socket import *
import sys
import os.path
import time
import struct
import getopt
sys.path.append('../encryption')
from monoalphabetic_class import *
from homophonic import *
from poly import *
from gram import *

HOST = None
ciphertype = None
blockSize = 0
poly_key = []
try:
	opts, args = getopt.getopt(sys.argv[1:], "h:t:b:", ["host=", "type=", "block="])
except getopt.GetoptError:
      	#sys.exit(2)
      	print 'client.py -h [hostname] -t [ciphertype] -b [blockSize or number of maps]'
        sys.exit(2)

for o, a in opts:
        if o in ("-h", "--host"):
		HOST = a
        elif o in ("-t", "--type"):
            	ciphertype = a
        elif o in ("-b", "--block"):
            	blockSize = int(a)
        else:
            	assert False, "unhandled option"

if HOST == None: 
      	print "HOST needs to be specified"
	print 'client.py -h [hostname] -t [ciphertype] -b [blockSize or number of maps]'
        sys.exit(2)

PORT = 400
ADDR = (HOST,PORT)
BUFSIZE = 4096

sequence_number = 0

cipher = None
if ciphertype == 'monoalphabetic' :
	cipher = mono_alpha()
if ciphertype == 'polyalphabetic' :
	poly_key = poly_gen_key(blockSize)

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

		encrypted_message = None

		print(data)

                #encrypt here
		if ciphertype == 'monoalphabetic' :
			encrypted_message = cipher.encrypt(data)
		elif ciphertype == 'homophonic' :
			encrypted_message = encrypt(key, data)
		elif ciphertype == 'polyalphabetic' :
			encrypted_message = translate('encrypt', poly_key, data)
		elif ciphertype == 'polygram' :
			encrypted_message = polygram(data, 'hell', blockSize, 'encrypt')
			print('encrypted_message: ' + encrypted_message)
			
		elif ciphertype == None :
			encrypted_message = data

                #put a sequence number here
                msg = struct.pack('i' + str(len(encrypted_message)) + 's', sequence_number, encrypted_message)
                sequence_number = sequence_number + 1

                #send
                client.send(msg)

                #sleep here
                time.sleep(2)
f.close()
client.close()
