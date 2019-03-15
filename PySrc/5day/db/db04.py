# db04.py
import sqlite3
학생들 = {5:'Hong',6:'Sophia',7:'King'}
dbcon = sqlite3.connect('test01.db')
cursor = dbcon.cursor()
###########################################
sql = 'insert into T1 values(?,?)'

for k, v in 학생들.items():
    cursor.execute(sql, (k,v))
dbcon.commit()
###########################################
cursor.close()
dbcon.close()


