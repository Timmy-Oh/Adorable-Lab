# ul01.py
from bs4 import BeautifulSoup
f1 = open('./ex00.html','r',encoding="utf-8")
bs = BeautifulSoup(f1,"html.parser")
#print(bs.prettify())
# fdata = f1.read()
# print(fbs)
print(bs)
print(type(bs))

print(bs.prettify())
f1.close()
