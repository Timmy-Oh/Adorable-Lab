# Dict02.py

a = {'사과' : 'apple',
     '포도' : 'grape',
     '바나나' : 'banana',
     '컵' : 'cup',
     '물' : 'water'}

print(a['컵'])

a['강'] = 'river'
a['자바'] = 'java'

print(a)

e = a.pop('강')
print(e, a)

del a['자바']
print(a)

# key에서 바나나 존재
print( '바나나' in a.keys() )

# value 에서 grape가 존재
print( 'grape' in a.values() )

# item에서 '사과', 'apple' 존재
print( ('사과', 'apple') in a.items() )

a['강'] = 'river'
print(a)
b = {'불':'fire', '집':'house'}

a.update(b)
print(a)

a.setdefault('집', 'home')
a.setdefault('책', 'book')
print(a)

for z in a.items():
    print(z)

y = list(a.items())
print(y)

'''
####################################

#for item in a.items():
#    print(item)
'''
a_rev = {v:k for k,v in a.items()}
print(a_rev['grape'])
