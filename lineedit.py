import sys
from PySide2.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Label Example")
        self.setGeometry(50, 50, 350, 350)
        self.UI()

    def UI(self):
        self.lineedit = QLineEdit(self)
        self.lineedit.setPlaceholderText('Please enter you pass')
        self.lineedit.setEchoMode(QLineEdit.Password)
        btn = QPushButton('Enter', self)
        self.lineedit.move(100, 50)
        btn.clicked.connect(self.btn_click)

        self.show()

    def btn_click(self):
        text = self.lineedit.text()
        self.setWindowTitle('Your text is -- {}'.format(text))


def main():
    App = QApplication(sys.argv)
    win = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
