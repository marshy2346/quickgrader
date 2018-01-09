import sys
import os

from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QVBoxLayout, QWidget, QSplitter
from PyQt5.QtCore import Qt

import constants
import project
import settings
from models.submission import Submission
from ui.dialog import show_warning, show_message
from ui.editor import Editor
from ui.fileview import FileView
from ui.toolbar import Toolbar
from ui.commentbox import CommentBox

g_settings_manager = settings.SettingsManager()
g_project_manager = project.ProjectManager()

class Menu:
    def __init__(self, _qmainwindow):
        self.main_window = _qmainwindow
        self.menu = _qmainwindow.menuBar()
        self.__setup_file_menu()

    def __get_new_menu_action(self, key, handler):
        action = QAction(key, self.main_window)
        action.setShortcut(g_settings_manager.keymap[key])
        action.triggered.connect(handler)
        return action

    def __setup_file_menu(self):
        file_menu = self.menu.addMenu('&File')
        file_menu.addAction(self.__get_new_menu_action("Exit", self.__handle_exit))
        file_menu.addAction(self.__get_new_menu_action("Start Project", self.__handle_new_project))
        file_menu.addAction(self.__get_new_menu_action("Open Project", self.__handle_open_project))

    def __handle_exit(self):
        g_project_manager.save(self.main_window)
        qApp.quit()

    def __handle_new_project(self):
        if g_project_manager.new(self.main_window):
            show_message(self.main_window, "Project setup complete.")
            self.main_window.setup_project_ui()
        else:
            show_message(self.main_window, "Oops! Error occurred. Try again.")

    def __handle_open_project(self):
        if g_project_manager.open(self.main_window):
            show_message(self.main_window, "Project opened successfully.")
            self.main_window.setup_project_ui()
        else:
            show_message(self.main_window, "Oops! Error occurred. Try Again.")


class QuickGrader(QMainWindow):
    TITLE = "QuickGrader V{}".format(constants.VERSION)

    def __init__(self, dimensions, position):
        super().__init__()
        self.menu = Menu(self)
        self.__init_ui(dimensions, position)

    def __init_ui(self, dimensions, position): 
        self.__make_workspace_ifnoexist()
        self.setGeometry(
            position[0],
            position[1],
            dimensions[0],
            dimensions[1]
        )
        self.setWindowTitle(QuickGrader.TITLE)
        self.show()

    def setup_project_ui(self):
        submission_path = g_project_manager.current_submission().path
        editor = Editor(self, submission_path)
        fileview = FileView(self, submission_path, editor.set_view)

        # TODO: find a way to make this more elegant, remember that this application needs to be extensible
        def load_toolbar_actions(toolbar):

            def prev_submission():
                g_project_manager.prev_submission()
                new_path = g_project_manager.current_submission().path
                editor.root_path = new_path
                fileview.update(new_path)
            def next_submission():
                g_project_manager.next_submission()
                new_path = g_project_manager.current_submission().path
                editor.root_path = new_path
                fileview.update(new_path)

            toolbar.add_action(
                "Previous Submission",
                g_settings_manager.keymap["Previous Submission"],
                prev_submission
            )

            toolbar.add_action(
                "Next Submission",
                g_settings_manager.keymap["Next Submission"],
                next_submission
            )

            toolbar.setup_ui()


        toolbar = Toolbar(self)
        load_toolbar_actions(toolbar)

        commentbox = CommentBox(self)

        vlayout = QVBoxLayout()
        container = QWidget()
        hsplit = QSplitter(self)
        vsplit = QSplitter(self)
        vsplit.setOrientation(Qt.Vertical)

        hsplit.addWidget(fileview)
        hsplit.addWidget(editor)
        hsplit.addWidget(commentbox)

        vlayout.addWidget(hsplit)
        container.setLayout(vlayout)

        vsplit.addWidget(container)
        vsplit.addWidget(toolbar)

        self.setCentralWidget(vsplit)

    def __make_workspace_ifnoexist(self):
        if not os.path.isdir(constants.WORKSPACE_PATH):
            os.mkdir(constants.WORKSPACE_PATH)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    rect = app.desktop().screenGeometry()
    dim = (rect.width(), rect.height())
    pos = (0, 0)
    quickgrader = QuickGrader(dim, pos)
    sys.exit(app.exec_())

