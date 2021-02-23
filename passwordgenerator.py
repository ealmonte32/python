import itertools
import hashlib

#h = hashlib.sha1("abc")
#print (h)

res = itertools.product('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890', repeat=8)
#repeat is length of password letters

for i in res:
    result = ''.join(i)
    print(result)
