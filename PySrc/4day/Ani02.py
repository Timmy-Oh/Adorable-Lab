# Ani02.py

class A:
    def __init__(self):
        self.type='A'

    def setTypeA(self):
        self.type = 'A'

    def printType(self):
        print('{}족이래요'.format(self.type))


class B:
    def __init__(self):
        self.type='B'

    def setTypeB(self):
        self.type = 'B'

    def printType(self):
        print('{}족이래요'.format(self.type))

class AB(A, B):
    pass

ab = AB()
ab.printType()
ab.setTypeB()
ab.printType()
ab.setTypeA()
ab.printType()

