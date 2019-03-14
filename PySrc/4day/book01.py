# Book01.py
'''
class
    member field
    member method
'''
# 서점 : 책( 제목(str), 저자(str), 가격(int) )

class Book():
    def __init__(self, title="무제", author="미상", price=0):
        self.title = title
        self.author = author
        self.price = price

    def pbook(self):
        print(self.title, self.author, self.price)

b1 = Book()
# b1.pbook()
# b1.title="파이썬"; b1.author="Tom"; b1.price=30000
# b1.pbook()

b2 = Book('파이썬')
# b2.title="자바"; b2.author="Jane"; b2.price=20000
# b2.pbook()

b3 = Book('자바', '이승엽')
b4 = Book('DB', '김연아', 30000)

b1.pbook();b2.pbook();b3.pbook();b4.pbook()
B=[b1, b2, b3, b4]
[i.pbook() for i in B]