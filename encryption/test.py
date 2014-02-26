from homophonic import *
from poly import *
from monoalphabetic_class import *
import sys
sys.path.append('../cracking')
from mono_c import *

cipher = mono_alpha()

s = cipher.encrypt('hello how are you I am good thank you. how was your day today it was good thank you. Are you going to see the show, yes I will see the show. Cool I have to go now. Bye. WHy isnt this working. I have no idea, but it should. This class kinda sucks, its not as fun as i hought it would be')
d = cipher.decrypt(s)
print(d)
l = mono_crack(s)
print(l)
