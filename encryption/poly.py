from monoalphabetic_class import *

symbolmap = 'abcdefghijklmnopqrstuvwxyz.,!? '

def poly_gen_key(size) :
    poly_key = []
    temp = mono_alpha()
    for x in range(size) :
      poly_key.append(''.join(temp.createkey()))
    return poly_key

def polyal(message, ikey, imode):
    oldmessage = message
    key = ikey
    mode = imode
    translated = translate(mode.lower(), key, oldmessage)
    file = open('messages.txt', 'a')
    file.seek(0,2)
    for symbol in translated:
        file.write(symbol)
    file.write('\n')
    file.close()

    print(translated)

def translate(mode, key, message):
    translated = []

    keyindex = 0

    for symbol in message:
        num = symbolmap.find(symbol)
        if num != -1:
            if mode == 'encrypt':
                num += symbolmap.find(key[keyindex])
            elif mode == 'decrypt':
                num -= symbolmap.find(key[keyindex])

            num %= len(symbolmap)

            translated.append(symbolmap[num])

            keyindex += 1
            if keyindex == len(key):
                keyindex = 0
        else:
            translated.append(symbol)
    translated_message = ''.join(translated)
    return translated_message


if __name__ == '__main__':
    import sys
    polyal(sys.argv[1], sys.argv[2], sys.argv[3])
