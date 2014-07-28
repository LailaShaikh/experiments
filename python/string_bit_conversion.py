# -*- coding: utf-8 -*-

a="Hello WORLD"

def toBigInt(s):
    ret=0
    for i,j in enumerate(s):
        ret+= ord(j)<<(i * 8)
    return ret

def fromBigInt(i):
    s=""
    while i>0:
        s+=chr(i & 0xff)
        i=i>>8
    return s

i = toBigInt(a)
print i
print fromBigInt(i)
