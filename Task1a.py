import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from base64 import b64encode, b64decode



#public key
p=37
g=5

#pick private key random element of group 37
a = 7

# Alice sends A = g^a mod p
A = g**a % p

print("A:", A)

# pick private key random element of group 37
b = 16

#Bob sends alice B= g^a mod p
B = g**b % p

print("B: ", B)

#Alice computes s= B^a mod p
sa = B**a % p

print("sa", sa)

#Alice computes s= A^b mod p
sb = A**b % p

print("sb", sb)

#Alice computes k =SHA256(sa)

ka = hashlib.sha256(str(sa).encode()).hexdigest()
keya = ka[:64 - 48].encode()


print(keya)

#Bob computes k = SHA256(sb)

kb = hashlib.sha256(str(sb).encode()).hexdigest()
keyb = kb[:64 - 48].encode()


print(keyb)

#keys are the same

ma = "Hi Bob"




#ka = Fernet(ka)

cipher = AES.new(keya, AES.MODE_CBC)
ca = cipher.encrypt(pad(ma.encode(),AES.block_size)) 
#kb = Fernet(kb) 5:39 search for topic
iva = cipher.iv



print(f"ciphertext:{b64encode(ca).decode('utf-8')}")

cipher = AES.new(keya, AES.MODE_CBC, iva)
plaintext = unpad(cipher.decrypt(ca),16)
print("Original Message  A was: ", plaintext)


#second message
mb = "Hi Alice"


cipher = AES.new(keyb, AES.MODE_CBC)
cb = cipher.encrypt(pad(mb.encode(),AES.block_size))
ivb = cipher.iv
print(f"ciphertext:{b64encode(cb).decode('utf-8')}")


cipher = AES.new(keyb, AES.MODE_CBC, ivb)
plaintext = unpad(cipher.decrypt(cb),16)
print("Original Message B was: ", plaintext)





