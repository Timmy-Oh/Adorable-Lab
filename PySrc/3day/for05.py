# for05.py
'''
1: *
2: **
3: ***
4: ****
5: *****
'''

for i in range(1,6): print("{}: {}".format(i, "*"*i))

print("\n{}\n".format("="*30))

for i in range(1, 21):
    print(i, end=' ')
    if i%5==0: print()

print("\n{}\n".format("="*30))

for i in range(1,21,5):
    for j in range(i,i+5):
        print(j, end=' ')
    print()

