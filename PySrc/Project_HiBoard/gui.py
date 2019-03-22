import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit, QPushButton, QVBoxLayout


class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setWindowTitle('Hi Smart Board - 너목보')
        self.setWindowIcon(QIcon('./src/icon.png'))
        self.move(300, 300)
        self.resize(800, 400)

        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(QLabel('Topic'), 0, 0)
        grid.addWidget(QLabel('Article'), 0, 1)
        grid.addWidget(QLabel('Date'), 0, 2)

        grid.addWidget(QPushButton('Topic1', self), 1, 0)
        grid.addWidget(QPushButton('게시글1', self), 1, 1)
        grid.addWidget(QPushButton('2019-01-01', self), 1, 2)


        grid.addWidget(QPushButton('Topic2', self), 2, 0)
        grid.addWidget(QPushButton('게시글2', self), 2, 1)
        grid.addWidget(QPushButton('2019-01-02', self), 2, 2)

        grid.addWidget(QPushButton('Topic3', self), 3, 0)
        grid.addWidget(QPushButton('게시글3', self), 3, 1)
        grid.addWidget(QPushButton('2019-01-03', self), 3, 2)

        grid.addWidget(QPushButton('Topic3', self), 4, 0)
        grid.addWidget(QPushButton('게시글3', self), 4, 1)
        grid.addWidget(QPushButton('2019-01-03', self), 4, 2)

        grid.addWidget(QPushButton('Topic3', self), 5, 0)
        grid.addWidget(QPushButton('게시글3', self), 5, 1)
        grid.addWidget(QPushButton('2019-01-03', self), 5, 2)

        grid.addWidget(QPushButton('Topic3', self), 6, 0)
        grid.addWidget(QPushButton('게시글3', self), 6, 1)
        grid.addWidget(QPushButton('2019-01-03', self), 6, 2)
        self.setGeometry(300, 300, 300, 200)

        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())