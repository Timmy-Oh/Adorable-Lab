# Book02.py
class Book:
    def __init__(self,t='무제',a='미상',p=0): # 멤버 생성자 <-- 메모리 로드, 호출
        self.title = t   # instance 멤버 속성
        self.author = a
        self.price = p
    def pBook(self):          # instance 멤버 메소드
        print(self.title, self.author, self.price)

b1 = Book()
b2 = Book('파이썬')
b3 = Book('자바','이승엽')
b4 = Book('DB','김연아',30000)
b1.pBook();b2.pBook();b3.pBook();b4.pBook()
