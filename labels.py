import sys
from PySide2.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Label Example")
        self.setGeometry(50, 50, 350, 350)
        self.UI()

    def UI(self):
        text01 = QLabel("Hello Window", self)
        text01 = QLabel("Hello Python", self)
        text01.move(100, 50)
        self.show()


def main():
    App = QApplication(sys.argv)
    win = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
