# Func08.py

a=7

def Sum(*args):
    global a
    return sum(args)+a 

print(Sum(20, 10))


def test(i):
    global b
    b = i

b=0
test(200)
print(b)
