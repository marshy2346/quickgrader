import sys
from enum import Enum
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, qApp, QMessageBox
from PyQt5.QtCore import QCoreApplication, pyqtSlot

# TODO: setup packaging with cx_freeze
# TODO: setup plugin system

CURRENT_VERSION = "2.0"

KEYMAP = {
    'New Workspace': 'Ctrl+N',
    'Open Workspace': 'Ctrl+O',
    'Exit': 'Ctrl+Q'
}

def show_message(parent, content):
    reply = QMessageBox.question(
        parent, "Message", content, QMessageBox.Ok, QMessageBox.Ok
    )

def show_warning(parent, content, ok_cb, cancel_cb):
    reply = QMessageBox.question(
        parent, "Warning", content,
        QMessageBox.Ok | QMessageBox.Cancel, QMessageBox.Cancel
    )
    if reply == QMessageBox.Ok:
        if ok_cb != None:
            ok_cb()
    elif reply == QMessageBox.Cancel:
        if cancel_cb != None:
            cancel_cb()


class QuickGrader(QMainWindow):

    #TODO: setup icon

    def __init__(self):
        super().__init__()
        self._setup_ui()

    def _get_title(self):
        return "QuickGrader" + " V" + CURRENT_VERSION

    def _setup_ui(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle(self._get_title())

        self._setup_menu()

        self.show()

    def _new_action(self, name, shortcut, handler):
        action = QAction(name, self)
        action.setShortcut(shortcut)
        action.triggered.connect(handler)
        return action

    def _setup_menu(self):
        main_menu = self.menuBar()

        file_menu = main_menu.addMenu('&File')
        file_menu.addAction(
            self._new_action("Exit", KEYMAP['Exit'], self._handle_exit)
        )
        file_menu.addAction(
            self._new_action("New Workspace", KEYMAP['New Workspace'], self._handle_new_workspace)
        )
        file_menu.addAction(
            self._new_action("Open Workspace", KEYMAP['Open Workspace'], self._handle_open_workspace)
        )

    def _handle_exit(self):
        show_warning(self,
            "Are you sure you want to quit?",
            lambda: qApp.quit(),
            None
        )

    def _handle_new_workspace(self):
        print("New Workspace")

    def _handle_open_workspace(self):
        print("Open workspace")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    quickgrader = QuickGrader()
    sys.exit(app.exec_())

