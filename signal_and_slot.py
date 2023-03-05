from PySide2.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QLabel
)

import sys


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("My App")
        button = QPushButton("Press Me")
        button.setCheckable(True)

        label = QLabel("This is the button")
        button.clicked.connect(self.the_button_was_clicked)

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(button)


        container = QWidget() 
        container.setLayout(layout)
        self.setCentralWidget(container)

    def the_button_was_clicked(self):
        print("Clicked")

app = QApplication(sys.argv)            
windows = MainWindow()
windows.show()
app.exec_()