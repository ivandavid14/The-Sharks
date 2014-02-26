##server.py
from socket import *
import sys
import os.path
import struct
import getopt
import time

sys.path.append('../encryption')
from monoalphabetic_class import *
from homophonic import *
from poly import *

HOST = ''
ciphertype = None
blockSize = 0
cipher = None
poly_key = []

try :
  opts, args = getopt.getopt(sys.argv[1:], "t:b:", ["type=", "block="])
except getopt.GetoptError:
  print 'server.py -t [ciphertype] -b [blockSize]'
  sys.exit(2)

for o, a in opts :
  if o in ("-t","--type") :
    ciphertype = a
  elif o in ("-b", "--block") :
    blocksize = int(a)
  else :
    assert False, "unhandled option"

if ciphertype == 'monoalphabetic' :
  cipher = mono_alpha()
elif ciphertype == 'polyalphabetic' :
  poly_key = poly_gen_key(blocksize)
print(str(len(poly_key)) + ' ' + str(blocksize))

PORT = 400
ADDR = (HOST, PORT)
BUFSIZE = 4096

serv = socket(AF_INET, SOCK_STREAM)
serv.bind((ADDR))
serv.listen(5)

conn = None
addr = None

f = None
log = None

f = open('messages.txt', 'w+')

if os.path.exists('log.txt') :
  log = open('log.txt', 'a')
else :
  log = open('log.txt', 'w+')

log.write('-----------------BEGINNING OF SEQUENCE OF MESSAGES--------------------\n')

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
      #decrypt here
      decrypted_message = None
      if ciphertype == 'monoalphabetic' :
        decrypted_message = cipher.decrypt(temp[1])
      elif ciphertype == 'homophonic' :
        l = temp[1].split(' ')
        decrypted_message = decrypt(key, l)
      elif ciphertype == 'polyalphabetic' :
        decrypted_message = translate('decrypt', poly_key, temp[1])
      else :
        decrypted_message = temp[1]
  
      print(str(temp[0]) + ': ' + decrypted_message)

      #write to file here
      log.write(str(temp[0]) + ': ' + decrypted_message + '\n')
      f.write(str(temp[0]) + ': ' + decrypted_message + '\n')
    
  except :
    serv.close()
    if conn is not None :
      conn.close()
    log.write('-----------------END OF SEQUENCE OF MESSAGES---------------------\n')
    f.close()
    log.close()
    serv.close()
    sys.exit()
f.close()
log.close()
serv.close()
