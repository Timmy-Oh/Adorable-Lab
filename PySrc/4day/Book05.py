# Book05.py

class Book:
    category = '소설'         #class 멤버 속성

    def __init__(self):
        self.title = '무제'   #instance 멤버 속성

    def pBook(self):
        print(self.title)   #instance 멤버 메소드

    @classmethod
    def pCate(cls):
        print(cls.category)     #class 멤버 메소드

    @staticmethod
    def test():
        print('요건 static 메소드 입니당!')

