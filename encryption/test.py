from homophonic import *
from poly import *
from monoalphabetic_class import *
import sys
sys.path.append('../cracking')
import math
from polyal_crack import *

from mono_c import *
from gram import *

poly_key = poly_gen_key(3)

e = translate('encrypt', poly_key, 'hello how are you today')
d = translate('decrypt', poly_key, e)

s = crackpolyal(e)

print(s)
