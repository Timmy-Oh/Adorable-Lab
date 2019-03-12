# List02.py

a= [10, 20, 30]
print(a)

a.append(40)
print(a)

a.append(20)
print(a, a.count(20))

a.insert(1, 50)
print(a)

a.pop(1)
print(a)

a.remove(20)
print(a)

a += [20]
print(a)

a.extend([50, 60])
print(a)

#print(a.index(20))

a.pop(-3)
print(a)

print('=' * 30)
