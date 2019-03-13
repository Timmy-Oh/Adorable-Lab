# Func07.py
def pSum(cmd, *args):
    return "{} {}".format(cmd, sum(args))

print(pSum('덧셈',20,10)) # 덧셈 30
print(pSum('덧셈',20,10,5)) # 덧셈 35
print(pSum('덧셈',20,10,5,2)) # 덧셈 37

a = [10,20,30,40,50]
print(pSum('덧셈',*a)) # 덧셈 150


