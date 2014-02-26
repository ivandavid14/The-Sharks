import random

class mono_alpha:
  keybase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
         'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
         'v', 'w', 'x', 'y', 'z', '.', ',','!','?',' ']

  def __init__(self) :
    random.seed(1)
    self.key = self.createkey()
    self.inverse_key = {v:k for k, v in self.key.items()}

  def createkey(self) :
    usedletters = []
    key = {}
    count = 0
    while len(key) < 31 :
      rand = random.randint(0,30)
      if not rand in usedletters :
        usedletters.append(rand)
        key[self.keybase[count]] = self.keybase[rand]
        count += 1
    return key
 
  def encrypt(self, message) :
    encrypted_message = []
    for letter in message :
      encrypted_message.append(self.key[letter.lower()])
    encrypted_string = ''.join(encrypted_message)
    return encrypted_string

  def decrypt(self, data) :
   decrypted_message = []
   for letter in data :
    try :
      decrypted_message.append(self.inverse_key[letter])
    except KeyError :
      decrypted_message.append(letter)
   decrypted_string = ''.join(decrypted_message)
   return decrypted_string

