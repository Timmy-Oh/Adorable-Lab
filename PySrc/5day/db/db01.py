# db01.py
#커넥션 연결, 커서 연결, 처리, 커서해제, 커넥션 해제

import sqlite3

dbcon = sqlite3.connect('test01.db')
cursor = dbcon.cursor()

###########################################

sql = '''select * from T1'''
rows = cursor.execute(sql)

for row in rows:
    print(row)
###########################################
cursor.close()
dbcon.close()


