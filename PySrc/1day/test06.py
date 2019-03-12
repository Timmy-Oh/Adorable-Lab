# Test06.py

import time, datetime
print('Time is Ticking.... {}'.format(time.ctime()))

c = b = a = 10
print(a, id(a))
print(b, id(b))
print(c, id(c))

e=11; f=12; g=13;
print(e,f,g)

h=33
print(h,id(h))
h=None
print(h, id(h))
del h
