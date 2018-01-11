import os
import sys

from PyQt5.QtWidgets import (
    qApp,
    QApplication,
    QMainWindow
)

from design import (
    Ui_MainWindow
)
from constants import (
    VERSION,
    WORKSPACE_PATH,
    PROJECT_EXISTS_MESSAGE,
    INVALID_NAME_MESSAGE,
    INVALID_SOURCE_MESSAGE
)
from project import (
    ProjectManager
)
from settings import (
    SettingsManager
)
from dialog import (
    show_message,
    show_warning,
    show_request,
    show_directory_request
)
from utils.fs import (
    is_directory,
    overwrite,
    home,
    is_hidden_file,
    open_file
)

class QuickGrader(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.__connect_actions()
        self.__make_workspace_folder()
        self.project_manager = ProjectManager() 
        self.settings_manager = SettingsManager()

    def __make_workspace_folder(self):
        if is_directory(WORKSPACE_PATH):
            return
        else:
            os.mkdir(WORKSPACE_PATH)

    def __update_fileview(self, submission):
        self.file_view.clear()
        for s in os.listdir(submission):
            if not is_hidden_file(s):
                self.file_view.append(s)

    def __connect_actions(self):
        self.file_view.itemDoubleClicked.connect(lambda list_item: self.__open_file(list_item.text()))
        self.action_new_project.triggered.connect(self.__new_project)
        self.action_open_project.triggered.connect(self.__open_project)
        self.action_exit.triggered.connect(self.__exit)
        self.previous_button.clicked.connect(self.__prev_submission)
        self.next_button.clicked.connect(self.__next_submission)

    def __update_fileview(self):
        submission = self.project_manager.get_current_submission()
        if submission == None:
            show_message(self, "No project is loaded.")
            return
        self.file_view.clear()
        for f in os.listdir(submission.path):
            if not f.startswith('_') and not f.startswith('.'):
                self.file_view.addItem(os.path.join(submission.path, f))

    def __new_project(self):
        while True:
            name = show_request(self, "New Project Name")
            if name == '':
                show_message(self, INVALID_NAME_MESSAGE)
            elif name == None:
                return
            else:
                break

        full_path = os.path.join(WORKSPACE_PATH, name)

        if is_directory(full_path):
            yes = show_warning(self, PROJECT_EXISTS_MESSAGE)
            if yes:
                overwrite(full_path)
            else:
                return
        else:
            os.mkdir(full_path)

        while True:
            source_directory = show_directory_request(self, "Choose source directory", home())

            if source_directory == None or source_directory == '':
                if os.path.isdir(full_path):
                    os.rmdir(full_path)
                break
            else:
                success = self.project_manager.new(full_path, source_directory)

                if success:
                    message = "Project setup complete!"
                    show_message(self, message)
                    self.__update_fileview()
                    return
                else:
                    if os.path.isdir(full_path):
                        os.rmdir(full_path)
                    show_message(self, INVALID_SOURCE_MESSAGE)

    def __open_project(self):
        while True:
            source_directory = show_directory_request(self, "Choose project directory", WORKSPACE_PATH)

            if source_directory == None or source_directory == '':
                return
            else:
                success = self.project_manager.load(source_directory)

                if success:
                    message = "Project loaded!"
                    show_message(self, message)
                    self.__update_fileview()
                    return
                else:
                    show_message(self, INVALID_SOURCE_MESSAGE)

    def __open_file(self, path):
        project_path = self.project_manager.state['project_path']
        if project_path == None:
            show_message(self, "No project is open.")
            return
        editor = None
        if self.settings_manager.default_editor != None:
            editor = self.settings_manager.default_editor
        open_file(path, editor)

    def __prev_submission(self):
        self.project_manager.prev_submission()
        self.__update_fileview()

    def __next_submission(self):
        self.project_manager.next_submission()
        self.__update_fileview()

    def __exit(self):
        qApp.exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    quickgrader = QuickGrader()
    quickgrader.show()
    app.exec_()
