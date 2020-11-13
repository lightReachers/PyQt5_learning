from PySide2.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QMainWindow,
    QVBoxLayout,
    QPushButton
)
import sys
from PySide2.QtGui import QPixmap
from PySide2.QtCore import Qt, QSize


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Layout Test')
        self.setFixedSize(QSize(800, 700))

        label = QLabel()
        label.setPixmap(QPixmap("images/o_logo.jpg"))

        btn = QPushButton('Clickme!!')

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(btn)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec_()