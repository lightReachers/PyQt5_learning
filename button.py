import sys
from PySide2.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Label Example")
        self.setGeometry(50, 50, 350, 350)
        self.UI()

    def UI(self):
        self.text01 = QLabel("Hello Window", self)
        btn = QPushButton('Enter', self)
        self.text01.move(100, 50)
        btn.clicked.connect(self.btn_click)

        self.show()

    def btn_click(self):
        self.text01.setText('You clicked, Enter!!!')
        self.text01.resize(150, 20)


def main():
    App = QApplication(sys.argv)
    win = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
