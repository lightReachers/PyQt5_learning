from PySide2.QtCore import QAbstractListModel, Qt
from PySide2.QtWidgets import *
from PySide2.QtGui import QColor

import sys

cmplt_status = QColor('green')


class TodoModel(QAbstractListModel):
    def __init__(self, todos=None):
        super().__init__()
        self.todos = todos or []

    def data(self, index, role):
        if role == Qt.DisplayRole:
            status, text = self.todos[index.row()]
            return text
        if role == Qt.DecorationRole:
            status, text = self.todo[index.row()]
            if status:
                return cmplt_status
    
    def rowCount(self, index):
        return len(self.todos)    


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("To Do List")

        self.model = TodoModel()

        self.todoView = QListView()
        self.todoView.setModel(self.model)

        self.delBtn = QPushButton("Delete")
        self.cmpltBtn = QPushButton("Complete")
        self.todoEdit = QLineEdit()
        self.addBtn = QPushButton("Add Todo")

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.todoView)

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.delBtn)
        btn_layout.addWidget(self.cmpltBtn)

        main_layout.addLayout(btn_layout)
        main_layout.addWidget(self.todoEdit)
        main_layout.addWidget(self.addBtn)

        container = QWidget() 
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        self.addBtn.pressed.connect(self.add)
        self.delBtn.pressed.connect(self.delete)
        self.cmpltBtn.pressed.connect(self.complete)


    def add(self):
        text = self.todoEdit.text()
        text = text.strip()
        if text:
            self.model.todos.append((False, text))
            self.model.layoutChanged.emit()
            self.todoEdit.setText("")

    def delete(self):
        indexes = self.todoView.selectedIndexes()
        if indexes:
            index = indexes[0]
            del self.model.todos[index.row()]    
            self.model.layoutChanged.emit()
            self.todoView.clearSelection()

    def complete(self):
        indexes = self.todoView.selectedIndexes()
        if indexes:
            index = indexes[0]
            row = index.row()
            status, text = self.model.todos[row]
            self.model.todos[row] = (True, text)
            self.model.dataChanged.emit(index, index)
            self.todoView.clearSelection()         



app = QApplication(sys.argv)            
windows = MainWindow()
windows.show()
app.exec_()



