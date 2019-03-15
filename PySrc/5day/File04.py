# File04.py

# 1. open() read() ==> 한줄 str

ori = ['Tom', 'Alice', 'Jane', '홍길동', 'Sophia','Hong', 'Ali']
with open('./Users/users01.txt','w') as f1:
    [f1.write('{}\n'.format(name)) for name in ori]

with open('./Users/users01.txt','r') as f1:
    users1 = f1.read()
    print("===== read : {}".format(type(users1)), "="*20)
    print(users1)
    f1.seek(0)

    users2 = f1.read()
    print("===== read : {}".format(type(users2)), "="*20)
    print(users2)
    f1.seek(0)

    users3 = f1.readlines()
    print("===== read : {}".format(type(users3)), "="*20)
    print(users3)
    f1.seek(0)
