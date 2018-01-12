import os
import sys
import signal

from PyQt5.QtWidgets import (
    qApp,
    QApplication,
    QMainWindow,
    QAbstractItemView
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
from requirement import (
    RequirementModel
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
from utils.parsing import (
    replace_vars
)

class QuickGrader(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.project_manager = ProjectManager() 
        self.settings_manager = SettingsManager()
        self.stylesheet = None

        self.setupUi(self)
        self.__set_theme("default")

        self.requirement_model = RequirementModel()
        self.requirements_view.setModel(self.requirement_model)
        self.requirements_view.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.requirements_view.horizontalHeader().setStretchLastSection(True)
        self.requirements_view.setCornerButtonEnabled(False)
        self.__connect_actions()
        self.__make_workspace_folder()
        self.__signal_handlers()

    def __signal_handlers(self):
        signal.signal(signal.SIGINT, lambda: self.__save())

    def __is_project_loaded(self):
        submission = self.project_manager.get_current_submission()
        if submission == None:
            show_message(self, "No project is loaded.")
            return False
        else:
            return True

    def __set_theme(self, name):
        self.current_submission_label.setStyleSheet("QLabel { color: #1DE9B6 }")
        self.stylesheet = os.path.join("themes", name + ".stylesheet")
        style = replace_vars(os.path.join("themes", name + ".vars"), self.stylesheet)
        self.setStyleSheet(style)
        self.update()

    def __make_workspace_folder(self):
        if is_directory(WORKSPACE_PATH):
            return
        else:
            os.mkdir(WORKSPACE_PATH)

    def __connect_actions(self):
        self.file_view.itemDoubleClicked.connect(lambda list_item: self.__open_file(list_item.text()))

        self.action_new_project.triggered.connect(self.__new_project)
        self.action_open_project.triggered.connect(self.__open_project)
        self.action_exit.triggered.connect(self.__exit)

        self.previous_button.clicked.connect(self.__prev_submission)
        self.next_button.clicked.connect(self.__next_submission)

        self.add_requirement_button.clicked.connect(self.__add_requirement)
        self.remove_requirement_button.clicked.connect(self.__remove_requirement)

    def __update_fileview(self):
        if self.__is_project_loaded():
            submission = self.project_manager.get_current_submission()
            print("Submission Requirements ::: ")
            print(submission.requirements)
            self.requirement_model.replace_data(submission.requirements)
            self.current_submission_label.setText(os.path.basename(submission.path))

            self.file_view.clear()
            for f in os.listdir(submission.path):
                if f.startswith('_') or f.startswith('.'):
                    continue
                self.file_view.addItem(f)

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
                submission = self.project_manager.state['submissions'][0]

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
            
        submission = self.project_manager.get_current_submission()
        open_file(os.path.join(submission.path, path), editor)

    def __prev_submission(self):
        if self.__is_project_loaded():
            self.__update_submission_requirements()
            self.project_manager.prev_submission()
            self.__update_fileview()

    def __next_submission(self):
        if self.__is_project_loaded():
            self.__update_submission_requirements()
            self.project_manager.next_submission()
            self.__update_fileview() 

    def __add_requirement(self):
        if self.__is_project_loaded():
            self.requirement_model.add_requirement_row()

    def __remove_requirement(self):
        if self.__is_project_loaded():
            selections = self.requirements_view.selectionModel().selectedRows()
            self.requirement_model.remove_requirement_row(selections)

    def __update_submission_requirements(self):
        submission = self.project_manager.get_current_submission()
        if submission == None:
            return

        data = self.requirement_model.data[:]
        if len(data) == 0:
            return

        submission.requirements = data

    def __exit(self):
        print("__EXIT Called!")
        self.project_manager.save()
        qApp.exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    quickgrader = QuickGrader()
    quickgrader.show()
    app.exec_()
