# Str04.py

import datetime

dt = datetime.datetime.strptime('190312-1230', '%y%m%d-%H%M')
print('점심까지 {}'.format((dt - datetime.datetime.now())))

a = '   Hello'
b= 'Hello   '
c= '  Hello  '

print(a.strip())
print(b.strip())
print(c.lstrip())

d = 'Hello안녕12'

print(d.isalnum())

e = 'Hello 안녕12'
print(e.isalnum())


k = 'Java   C  SQL    Python'
m = k.split()
print(','.join(m))
