from PySide2.QtWidgets import QApplication, QWidget
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle('First Qt Window')
        self.setFixedSize(300, 400)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    app.exec_()