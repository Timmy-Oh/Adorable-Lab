# File02.py
# open() // 처리: write(), read() // close()  -> 'Hong'
# w : 신규, a : 추가
user='Ali'

with open('./Users/users01.txt', 'a+', encoding='cp949') as f1:
    f1.write('\n' + user)
    f1.seek(0)
    contents = f1.readlines()
    print(contents)
    [f1.write(cont) for cont in  contents[:5]]
    contents = f1.readlines()
    print(contents)





