import sys
from PySide2.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(100, 100, 300, 450)
        self.setWindowTitle('This is First Window')

        self.show()


App = QApplication(sys.argv)
win = Window()
sys.exit(App.exec_())
