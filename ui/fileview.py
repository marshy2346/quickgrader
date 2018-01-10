from PyQt5.QtWidgets import (
    QLabel
    QListWidget,
    QWidget, 
    QVBoxLayout,
) 

from utils.fs import (
    is_hidden_file
)

class FileView(QWidget):
    TITLE = "Files"

    def __init__(self, parent):
        super().__init__(parent)
        self.list = QListWidget(parent)
        self.__ui_setup()

    def __ui_setup(self):
        title = QLabel(FileView.TITLE)
        vlayout = QVBoxLayout()
        vlayout.addWidget(title)
        vlayout.addWidget(self.list)
        self.setLayout(vlayout)

    def update(self, path):
        self.list.clear()
        for f in os.listdir(self.path):
            if not is_hidden_file(f):
                self.list.addItem(f)

