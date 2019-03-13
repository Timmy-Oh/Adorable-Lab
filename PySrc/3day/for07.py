# for07.py

a = [10,20,30,40,50]

for i in a : print(i)

for i in range(len(a)) : print(a[i])

######################

# 1 : 10

for i, v in enumerate(a):
    print("{} : {}".format(i+1,v))
