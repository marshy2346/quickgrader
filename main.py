import sys

from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow
)

from design import (
    Ui_MainWindow
)
from constants import (
    VERSION
)

class QuickGrader(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
    def __update_fileview(self, new_path):
        self.file_view.clear()
        for f in os.listdir(new_path):
            if not f.startswith('_') and not f.startswith('.'):
                self.list.addItem(f)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    quickgrader = QuickGrader()
    quickgrader.show()
    app.exec_()
