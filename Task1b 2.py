import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from base64 import b64encode, b64decode

p ="B10B8F96 A080E01D DE92DE5E AE5D54EC 52C99FBC FB06A3C69A6A9DCA 52D23B61 6073E286 75A23D18 9838EF1E 2EE652C013ECB4AE A9061123 24975C3C D49B83BF ACCBDD7D 90C4BD7098488E9C 219A7372 4EFFD6FA E5644738 FAA31A4F F55BCCC0A151AF5F 0DC8B4BD 45BF37DF 365C1A65 E68CFDA7 6D4DA708DF1FB2BC 2E4A4371"
p = int.from_bytes(p.encode(), 'big')

#print(p)

g = "A4D1CBD5 C3FD3412 6765A442 EFB99905 F8104DD2 58AC507F D6406CFF 14266D31 266FEA1E 5C41564B 777E690F 5504F213160217B4 B01B886A 5E91547F 9E2749F4 D7FBD7D3 B9A92EE1909D0D22 63F80A76 A6A24C08 7A091F53 1DBF0A01 69B6A28AD662A4D1 8E73AFA3 2D779D59 18D08BC8 858F4DCE F97C2A24855E6EEB 22B3B2E5"
g = int.from_bytes(g.encode(), 'big')

#print(g)

#random element of group p
a = "AAADSASA SDASDSAE EQWKASDN SAKEOWQW SAWDEQSA"
a = int.from_bytes(a.encode(), 'big')

print(a)

#random element of group g
b = "AAOSPAEA AJSNCDJS AJSNDNFS ANSMDJAS ASNWENSA RSJAUENB HSJAKSJD" 
b = int.from_bytes(b.encode(), 'big')

# Alice sends A = g^a mod p
#A = pow(int.from_bytes(g.encode(), 'big'), int.from_bytes(a.encode(), 'big')) % int.from_bytes(p.encode(), 'big')


def exponentiation(bas, exp):
    t = 1;
    while(exp > 0):
 
        # for cases where exponent
        # is not an even value
        if (exp % 2 != 0):
            t = (t * bas) % p;
 
        bas = (bas * bas) % p;
        exp = int(exp / 2);
    return t % p;

# Alice sends A = g^a mod p
A = exponentiation(g, a)

#print(A)

# Bob sends B = g^b mod p
B = exponentiation(g, b)

#print(B)

#Now that alice has B she can compute sa = B^a mod p
sa = exponentiation(B, a)

print(sa)

#Now that alice has A she can compute sb = A^a mod p
sb = exponentiation(B, b)
print(sb)

ka = hashlib.sha256(str(sa).encode()).hexdigest()
keya = ka[:64 - 48].encode()

print(keya)

kb = hashlib.sha256(str(sb).encode()).hexdigest()
keyb = kb[:64 - 48].encode()

print(keyb)




