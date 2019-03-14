# Ani05.py
from abc import ABCMeta
from abc import abstractclassmethod

class Animal(metaclass=ABCMeta):
    def cry(self): print("으 앙") # 일반 method

    @abstractclassmethod
    def shout(self): pass # 추상(abstract) method

class Cat(Animal) :
    def shout(self):print("캬르릉~~♡")


c1 = Cat()
c1.cry()
c1.shout()