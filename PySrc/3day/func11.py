# Func11.py

def calc(n,m):
    return [n+m, n-m, n*m, n/m]


print(calc(20, 10))

a,b,c,d = calc(20,10)
print(a,b,c,d) # + - * /

def swap(n,m):
    return m, n

x= 200
y= 100
x,y = swap(x,y)
print(x,y) # 100, 200


