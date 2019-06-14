#!/usr/bin/env python3
import binascii
from sympy.ntheory import isprime
import re
f = open("possibleprimes.txt", "w")

def unsed(pair,string):
    bindex=int(pair[0])
    tstr=pair[1]
    j=0
    for i in range(len(string)):
        if(i>=bindex and i<bindex+len(tstr)):
            # string[i]=tstr[j]
            string = string[:i] + tstr[j] + string[i+1:]
            j+=1
    return string
    # return True


# while(r<2000000):
#     if(isprime(i)):
#         print(i)
#         r+=1
#     i+=1
prime="""00fb40dc44ba03d15342f75908e0f9\
300596644ade94685e08e28c9ab164\
0c2f62c29ab9a239824b9ebeeb76ae\
6d8721a35e9ed98d7e57383e590934\
a578cdf72e895d5c3752eafdf631cc\
bad2d960e4451d6776d21f129c9dc9\
b1904551edd2fbddb674b499fbb10a\
d9b7c2be8b5707220a8e3a36ff6dc1\
1d6393afcb4ec0479f65bfdfe3f05f\
1e98614574ec36a7a5b1f18d3d976b\
5a82490900080d9dc274574e30a139\
682f22347113aa3bf2204f8e10ebd4\
d09bcd8cc2535f9d71130c0f21b66e\
133940d3a6b1eb74addd0a291481b1\
90ade053f089c800fedcad5659fc28\
1dc0cf5e08c0543324a352bbf32510\
43c373b8404ffc6b6b77bd5f2224eb\
fb15"""

pairs = [("7f","fb"), ("e1","66"), ("f4","12"), ("16","54"), ("a4","57"), ("b5","cd")] #sed operation
matches = []

for pair in pairs: #all the indexes and what to replace with
    ocur = re.finditer(pair[1],prime)
    for match in ocur:
            matches += [(match.start(),pair[0])]
num=len(matches)
max=pow(2,num)
r=0
for i in range(max):
    bins="{0:b}".format(max+i)[1:]
    buf=prime
    for j in range(num):
        if(bins[len(bins)-1-j] == '1'):
        # if(bins[j] == '1'):
            # print(matches[j])
            buf=unsed(matches[j],buf) #replace with replace function
    if(isprime(int(buf,16))):
        r+=1
        print(str(r)+":\n"+buf+"\n")
        f.write(buf+"\n")
        f.flush()
f.close()
