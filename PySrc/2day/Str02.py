# Str02.py
b= 20; c= '10';
print(b+int(c))
print(str(b)+c)

a = "Welcome to HPEducation"

print(a[:7])
print(a[3:10])
print(a[-11:])

import re
rea = re.sub('c', '*c', a)
print(rea.split('*'))

print('===========')
print('='*20)

print('HP' in a)
print('HP' not in a)
print(a.count('o'))
