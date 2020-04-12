import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import QPixmap

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Label Example")
        self.setGeometry(50, 50, 1000, 1000)
        self.UI()

    def UI(self):
        self.img = QLabel(self)
        self.img.setPixmap(QPixmap('images/o_logo.jpg'))
        self.img.move(100, 50)
        btn_hide = QPushButton('Hide image', self)
        btn_hide.clicked.connect(self.hide_img)
        self.show()

    def hide_img(self):
        self.img.close()

def main():
    App = QApplication(sys.argv)
    win = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
