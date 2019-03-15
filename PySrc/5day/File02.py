# File02.py
# open() // 처리: write(), read() // close()  -> 'Hong'
# w : 신규, a : 추가
user='Hong'
with open('./Users/users01.txt', 'r', encoding='cp949') as f1:
    print(f1.readlines())

f2 = open(r'C:\yt_note\PySrc\5day\Users\users02.txt', 'r', encoding='utf8')
print(f2.readlines())

f1.close()
f2.close()


