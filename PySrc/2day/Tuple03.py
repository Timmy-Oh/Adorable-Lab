# Tuple03.py

a = '사과', '배', '토메이도';
print(id(a))

d='토마토'

b,c,d = a # 투플 언팩

a = b,c,d # 투플 패킹
print(a, id(a))

z = 10, 20, 30
# z의 모든 숫자를 1씩 증가시키세요

print(z)
a,b,c = z
z = a+1, b+1, c+1
print(z)


z= z[0]+1, z[1]+1, z[2]+1
print(z)

z1, z2, z3 = map(str, z)
z= z1+'a', z2+'b', z3+'c'
print(z)

print(list(z))

