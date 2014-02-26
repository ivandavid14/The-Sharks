from random import choice

#message = "i dont know what you are talking about"
key = {
    'a': ('9','91'),
    'b': ('8','81'),
    'c': ('7','71'),
    'd': ('6','61'),
    'e': ('5','51'),
    'f': ('4','41'),
    'g': ('3','31'),
    'h': ('2','21'),
    'i': ('1','10'),
    'j': ('99','991'),
    'k': ('88','881'),
    'l': ('77','771'),
    'm': ('66','661'),
    'n': ('55','551'),
    'o': ('44','441','4325'),
    'p': ('33','331'),
    'q': ('22','221'),
    'r': ('11','110'),
    's': ('999','9991'),
    't': ('888','8881'),
    'u': ('777','7771'),
    'v': ('666','6661'),
    'w': ('555','5551'),
    'x': ('444','4441'),
    'y': ('333','3331'),
    'z': ('222','2221'),
    ' ': ('111','1110'),
    '.': ('2314','3453'),
    ',': ('388', '488'),
    '!': ('987', '505'),
    '?': ('238', '42')
}


##ENCRYPTING++++++++++++
def encrypt(key, message) :
    encrypted_message = []
    for element in message:
        if not element.lower()[0:] in key.keys(): continue
        valueList = key[element.lower()][0:]
        encrypted_message.append(choice(valueList))
    encrypted_string = ' '.join(encrypted_message)
    return encrypted_string

##DECRYPTING++++++++++++
def decrypt(key, message) : 
    decrypted_message = []
    inverse_key = {v:k for k, v in key.items()}
    for number in message:
        if number == ' ':
            decrypted_message.append(' ')
            continue
        for key in inverse_key.keys():
            keyFragment = key[0:]
            for element in keyFragment:
                if element == number:
                    decrypted_message.append(inverse_key[key])
    decrypted_string = ''.join(decrypted_message)
    return decrypted_string
