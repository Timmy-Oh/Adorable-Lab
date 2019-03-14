# Ani01.py

# --> 개 Dog, 고양이 Cat
class Animal():
    def __init__(self):
        self.name

    def cry(self):
        return '묭묭'

    def shout(self):
        return '킁킁'

    def status(self):
        print("{} cry like {} shout like {}".format(self.name, self.cry(), self.shout()))

class Dog(Animal):
    def __init__(self, name = '통통이'):
        self.name = name

class Cat(Animal):
    def __init__(self):
        self.name = '주인님'

c1 = Cat()
d1 = Dog()

c1.status()
d1.status()

d2 = Dog("지니")
d2.status()

