# db02.py
import sqlite3

dbcon = sqlite3.connect('test01.db')
cursor = dbcon.cursor()

###########################################

sql = '''insert into T1 values(40, 'James')'''

cursor.execute(sql)
dbcon.commit()


###########################################
cursor.close()
dbcon.close()


