#!/usr/bin/env python3
from sympy.ntheory import isprime
from egcd import egcd #modinv

import pyasn1.codec.der.encoder #generate RSA
import pyasn1.type.univ
import base64

def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m

def pempriv(n, e, d, p, q, dP, dQ, qInv):
    template = '-----BEGIN RSA PRIVATE KEY-----\n{}-----END RSA PRIVATE KEY-----\n'
    seq = pyasn1.type.univ.Sequence()
    for x in [0, n, e, d, p, q, dP, dQ, qInv]:
        seq.setComponentByPosition(len(seq), pyasn1.type.univ.Integer(x))
    der = pyasn1.codec.der.encoder.encode(seq)
    return template.format(base64.encodebytes(der).decode('ascii'))


modulus="""00cd5f8a24c7605008897a3c922c0e\
812e769de0a46442c350cb78c78685\
39f3d38aac80b3e6a506605910e859\
9806b4d1d148f2f6b81da04796a8a5\
aee18f29e83e16775a2a0a00870541\
f6574ed1438636ae0a0c116e07104f\
48f72094863a3869e1c8fc22062727\
8962fb22873e3156f18e55dec94e97\
0064ec7f4e0e88454012e2fd5dfe5f\
8d19bf170f9ccb3f46e0fd1019bcb0\
2d9083a0703c617f996379e6478354\
a73ae6e6acbce1f4333ecfaf24366a\
3e977d3cd3cbfe8d8a387bd876bfda\
b8488f6f47bf1fbe33010fd2d7e22b\
4db2e567783ce0b606db86b9375971\
4c4f6396a7fb9f74c4021043b0f3d4\
6d2633ebd43a877863df7d680f5065\
87c119dd64100ca831ce2af33d951b\
524c5f06b49f5bf2cb381e74181930\
d06a80505c06abd5bf4870f0c9fb58\
1bd80dba889660639f936edea8fe5d\
0c9eae58062ed693252583c71cc782\
ba613e01438e69b43f9e64eca84f9e\
a04e811ad7b39efd7876d1b6b501c4\
f48acce6f24239f6c04028788135cd\
88c3d15be0f2ebb7de9e9c19a7a930\
37005ee0a9a640bada332ec0d05ee9\
f08a832354a0487a927d5e88066e25\
69e6c5d4688e422bfa0b27c6171c6d\
7bf029bfd9165752af19aa71b33a1e\
a70b6c371fb21e47f527d80b7d04f5\
82ad9f9935af723682dc01ca988062\
1870decb7ad15648cdf4ef153016f3\
e6d87933b8ec54cfa1fdf87c467020\
a3e753"""
e = 0x10001

n=int(modulus,16)
f=open("./possibleprimes.txt")
for line in f:
    p=int(line,16)
    q=n//p
    if(isprime(q)):
        break
phi = (p -1)*(q-1)

d=modinv(e,phi)

dp = modinv(e,(p-1))
dq = modinv(e,(q-1))
qi = modinv(q,p)

key = pempriv(n,e,d,p,q,dp,dq,qi)
print(key)
