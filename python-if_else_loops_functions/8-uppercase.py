#!/usr/bin/python3

def uppercase(str):
    ouput = ''
    for ch in str:
        if ch >= 'a' and ch <= 'z':
            var1 = ord(ch)
            var2 = var1 - 32
            ouput = ouput+chr(var2)
        else:
            ouput = ouput+ch
    print("{}".format(ouput))

