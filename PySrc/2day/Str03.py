# Str03.py

import datetime
a = '20190311Mon'

dt = datetime.datetime.strptime( a, "%Y%m%d%a")
weekday = ['월요일', '화요일' ,',수요일', '목요일', '금요일', '토요일', '일요일']

print("일시는 %s 이구용" % dt.date())
print("요일은 %s 입니당" % weekday[dt.weekday()])


b = 'Pithon'
#b = b.replace('i', 'y')
b = b[:1] + 'y' + b[2:]
print(b)
