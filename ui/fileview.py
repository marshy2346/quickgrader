from PyQt5.QtWidgets import QListWidget, QWidget, QVBoxLayout, QLabel
import os

class FileView(QWidget):
    def __init__(self, parent, path, doubleclick_cb):
        super().__init__(parent)

        self._parent = parent 
        self.path = path

        if not os.path.isdir(path):
            raise ValueError("Path argument to FileView is not a directory.")

        self.list = QListWidget(parent)
        self.list.itemDoubleClicked.connect(doubleclick_cb)
        self._setup_ui()

    def _setup_ui(self):
        title = QLabel("Files")
        vlayout = QVBoxLayout()
        for f in os.listdir(self.path):
            if not f.startswith('_') and not f.startswith('.'):
                self.list.addItem(f)
        vlayout.addWidget(title)
        vlayout.addWidget(self.list)
        self.setLayout(vlayout)

    def update(self, path):
        self.path = path
        self.list.clear()
        for f in os.listdir(self.path):
            if not f.startswith('_') and not f.startswith('.'):
                self.list.addItem(f)
