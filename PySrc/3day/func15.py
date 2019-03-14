# Func15.py

a = ['콜라','사이다','씨그램','우유','활명수']
b = [1000,900,600,700,800]
c = list(zip(a,b))
print(c)
d = dict(zip(a,b))
print(d)

e = '1001'
print(e,type(e))
f = int(e,base=10)
print(f,type(f))

g = int(e,base=2)
print(g,type(g))

from functools import partial
DecFromBin = partial(int,base=2)
print(DecFromBin('1001'))
