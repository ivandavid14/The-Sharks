from homophonic import *
from poly import *
from monoalphabetic_class import *
import sys
sys.path.append('../cracking')
import math

from mono_c import *
from gram import *

s = polygram('stevemorse', 'hell', 4, 'encrypt')
print s


d = polygram(s, 'hell', 4, 'decrypt')
print d
