# File05.py
uList = ['Hong','James','Tom','Alice','Jane']
# /Users/users03.txt
# open(w), write(), close()


with open('./Users/users03.txt','w') as f1:
    [f1.write('{}: {}\n'.format(i+1, name)) for i, name in enumerate(uList)]
