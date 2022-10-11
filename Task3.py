#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 16:30:36 2022

@author: stevenhartinger
"""
from Crypto.PublicKey import RSA
from Crypto.Util import number
import math
from sympy.ntheory.factor_ import totient
import binascii



#key generation
n = 1024 #for rsa 2048 we need 1024 bit keys
e = 65537

p = number.getPrime(n)
print()
q = number.getPrime(n)
N = p * q
phiN = (p-1) * (q-1)
if math.gcd(e, phiN) != 1:
    print(math.gcd(e, phiN))
    print("fehler")

d = pow(e, -1, phiN)
        
string = "aif an adversary were able to learn that key. And, that’s what we’re about to do. One of textbook RSA’s great weaknesses is its malleability"
# ascii 
m = binascii.hexlify(string.encode())
print(m)
print(type(m))
m = int(m, 16)
print("small m", m)

#encryption
C = pow(m, e, N)

M = pow(C, d, N)
print(type(M))
print("big m", M)

if M == m:
    print("correctly decrypted")




#M = binascii.unhexlify(M).decode()

#M = bytes.fromhex(M).decode('utf-16')

        
        
    



