#man in the middle program
#HOW TO RUN

#before running the program, run some stuff on the command line, since
#every time we load up the experiment, we won't have the right files in place

#must do these commands to get the right files
#sudo-apt get install python-scapy
#sudo apt-get install -y nfqueue-bindings-python

#you will probably have to do this every time you run an experiment 
#then in the command line rune
#sudo iptables -A FORWARD -p tcp -j NFQUEUE
#then just run
#sudo python mitm.py

#i will put a link to some documentation of iptables and some
#documentation just in case you want to play with this

#you need the sudo commands or else things won't work because we
#dont necessarily have the right permissions
import sys
import nfqueue

from socket import AF_INET, AF_INET6, inet_ntoa
from scapy.all import *
import struct
import os.path
import threading
from multiprocessing import Process, Queue
sys.path.append('../cracking')
from mono_c import *

ciphertype = None
blocksize = 0

try :
	opts, args = getopt.getopt(sys.argv[1:], "t:b:", ["type=", "block="])
except getopt.GetoptError :
	sys.exit(2)
	
for o, a in opts :
	if o in ('-t', '--type')
		ciphertype = a
	elif o in ('-b', '--block')
		blocksize = int(a)

s = threading.Semaphore(0)
queue = Queue()
f = None
if os.path.exists('messages.txt') :
	f = open('messages.txt', 'a')
else :
	f = open('messages.txt', 'w+')

def crack(queue, write_file, cipher, block) :
	#DO CRACKING IN THE WHILE LOOP
	#SINCE THIS IS A DIFFERENT PROCESS, WE CAN DO SWITCHING OF CRACKING METHODS
	#ON THE FLY
	while True :
		try :
			if(cipher == 'mono')
				messages = []
				temp = queue.get(block=True)
				messages.append(temp)
				t = mono_crack(''.join(messages))
				for d in temp :
					write_file.write(str(ord(d)) + ' ')
				write_file.write('\n')
			elif(cipher == 'homo') :

			elif(cipher == 'polyalpha') :
				temp = queue.get(block=True)
				t = crackpolyal(temp)
				for d in temp :
					write_file.write(str(ord(d)) + ' ')
				write_file.write('\n')
			
			elif(cipher == 'gram') :
			
		except :
			write_file.close()
			print('fuck')
			return -1

def callback(i, payload) :
	pkt = IP(payload.get_data())
	if pkt.haslayer(Raw) == True: 
		temp = pkt.getlayer(Raw).load
		global queue
		global s
		queue.put(temp)
		print('put data in queue')
	payload.set_verdict(nfqueue.NF_ACCEPT)

q = nfqueue.queue()
q.open()
q.unbind(AF_INET)
if q.bind(AF_INET) != 0 :
	q.close()
	print("Error in binding to nfqueue")
	sys.exit()

q.set_callback(callback)
q.create_queue(0)

p = Process(target=crack, args=(queue,f,ciphertype,blocksize))
p.start()

try :
	q.try_run()
except KeyboardInterrupt :
	print 'Exiting...'
	q.unbind(AF_INET)
	q.close()
