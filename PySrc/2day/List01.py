# List01.py

# ArrayList --> List(PYthon, R Scratch)

a = ['사과', '배', '바나나']
print(a, type(a))

a+= ['포도']
print(a, type(a))

a = a + ['딸기']
print(a, type(a))

a += [10]
print(a, type(a))
print(type(a[-1]))

b = [10, 'A', "안뇽", True, 3.14, [10, 20, 30]]
print(b)

print(b[0] is b[-1][0])

c = ['강', 10, 3.14, True, None, a]
print(len(c))
