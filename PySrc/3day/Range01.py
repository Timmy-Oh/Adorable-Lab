# Range01.py

# a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a= list(range(10))
print(a)

b= list(range(1, 11))
print(b)

c= list(range(0, 11, 2))
print(c)

d= list(range(10, 0, -1))
print(d)

f= a[1::2]
f= [i for i in a if i%2 ==1]
print(f)

# a에서 홀수만 제곱해서 g에 복사
g = [i**2 for i in a if i%2 ==1]
print("g is : {}".format(g))

# a에서 홀수만 제곱해서 h에 복사
h = {i:i**2 for i in a if i%2 == 1}
print("h is : {}".format(h))

x = 'ereefaerwthrtehberewfcredfdf'
# y= x에서 'abc'가 아닌 문자 중복제거후 정렬
y= sorted(set([c for c in x if c not in 'abc']))
print(y, type(y))


