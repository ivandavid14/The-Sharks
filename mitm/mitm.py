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
#must unbind whatever is in AF_INET first. if not then the program will
#not work
q.unbind(AF_INET)
if q.bind(AF_INET) != 0 :
	q.close()
	print("Error in binding to nfqueue")
	sys.exit()

q.set_callback(callback)
q.create_queue(0)

try :
	q.try_run()
except KeyboardInterrupt :
	print 'Exiting...'

q.unbind()
q.close()
