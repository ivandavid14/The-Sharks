#man in the middle program
#HOW TO RUN
#before running the program, run this on the commandline
#sudo apt-get install -y nfqueue-bindings-python
#you will probably have to do this every time you run an experiment 
#then in the command line rune
#sudo iptables -A FORWARD -p tcp -j NFQUEUE
#then just run
#sudo python mitm.pu

#i will put a link to some documentation of iptables and some
#documentation just in case you want to play with this

#you need the sudo commands or else things won't work because we
#dont necessarily have the right permissions
import sys
import nfqueue
from socket import AF_INET, AF_INET6, inet_ntoa

def callback(i, payload) :
	data = payload.get_data()
	print(data)
	payload.set_verdict(nfqueue.NF_ACCEPT)

q = nfqueue.queue()
q.open()
q.bind(AF_INET)
q.set_callback(callback)
q.create_queue(0)

try :
	q.try_run()
except KeyboardInterrupt :
	print 'Exiting...'

q.unbind()
q.close()
