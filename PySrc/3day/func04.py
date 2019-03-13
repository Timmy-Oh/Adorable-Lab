# Func04.py

def Sum(*args):
    return sum(args)

print(Sum(20, 10)) #30
print(Sum(20, 10, 5)) #35
print(Sum(20, 10, 5, 3)) #8

b = [10, 20, 30, 40, 50]

print(Sum(*b))
