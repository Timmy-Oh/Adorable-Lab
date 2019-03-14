# Book04.py

class Book():
    category = '소설'

b1 = Book(); print(b1.category)
b2 = Book(); print(b2.category)
print(Book.category)

b2.category = 'IT'
print(b2.category); print(b1.category) ; print(Book.category)
Book.category='Romance'
print(b2.category); print(b1.category) ; print(Book.category)

