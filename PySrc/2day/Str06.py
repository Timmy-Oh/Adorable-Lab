# Str06.py

a1 = 'Welcome to Korea Education'
a2 = 'Welcome to Korea Education'

print(id(a1), id(a2))
print(a1 is a2)
print(a1 == a2)

b1 = 'skhi'
# b2 = input('skhi 입력 바람')
b3 = 'skhi'
b4 = b1
b5 = b1[:-1]

#print('b1 == b2 : ', b1 == b2)
#print('b1 is b2 : ', b1 is b2)
#print('id_b1 : {}, id_b2 : {}'.format(id(b1), id(b2)))

print('b1 == b3 : ', b1 == b3)
print('b1 is b3 : ', b1 is b3)
print('id_b1 : {}, id_b3 : {}'.format(id(b1), id(b3)))

print('b1 == b4 : ', b1 == b4)
print('b1 is b4 : ', b1 is b4)
print('id_b1 : {}, id_b4 : {}'.format(id(b1), id(b4)))

print('b1 == b5 : ', b1 == b5)
print('b1 is b5 : ', b1 is b5)
print('id_b1 : {}, id_b5 : {}'.format(id(b1), id(b5)))

print('b3 == b4 : ', b3 == b4)
print('b3 is b4 : ', b3 is b4)
print('id_b3 : {}, id_b4 : {}'.format(id(b3), id(b4)))
