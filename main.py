import sys

from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow
)

from ui.design import (
    Ui_MainWindow
)
from constants import (
    VERSION
)

class QuickGrader(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    quickgrader = QuickGrader()
    quickgrader.show()
    app.exec_()
