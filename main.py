import os
import sys
import signal

from PyQt5.QtWidgets import (
    qApp,
    QApplication,
    QMainWindow, QAbstractItemView
)

from ui.design import (
    Ui_MainWindow
)
from constants import (
    WORKSPACE_PATH,
    MESSAGE_PROJECT_EXISTS,
    MESSAGE_PROJECT_NOTLOADED,
    MESSAGE_INVALID_NAME,
    MESSAGE_INVALID_SOURCE,
    MESSAGE_SAVE,
    MESSAGE_SAVE_ERROR,
    MESSAGE_ABOUT,
    DEFAULT_THEME
)
from models.requirement import (
    RequirementModel
)
from managers.project import (
    ProjectManager
)
from managers.settings import (
    SettingsManager
)
from ui.settings_panel import (
    SettingsPanel
)
from utils.dialog import (
    show_message,
    show_warning,
    show_request,
    show_directory_request
)
from utils.fs import (
    is_directory,
    overwrite,
    home,
    open_file
)
from utils.parsing import (
    replace_vars
)

# TODO: logic could be cleaned up


class QuickGrader(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.stylesheet = None
        self.project_manager = ProjectManager()
        self.settings_manager = SettingsManager()
        self.settings_manager.load()

        self.setupUi(self)
        self.__set_theme(DEFAULT_THEME)
        self.__setup_views()
        self.__connect_actions()
        self.__make_workspace_folder()
        self.__signal_handlers()
        self.__setup_keymappings()

    def __setup_views(self):
        self.requirement_model = RequirementModel()
        self.requirements_view.setModel(self.requirement_model)
        self.requirements_view.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.requirements_view.horizontalHeader().setStretchLastSection(True)
        self.requirements_view.setColumnWidth(0, 350)
        self.requirements_view.setColumnWidth(1, 50)
        self.requirements_view.setCornerButtonEnabled(False)

    def __setup_keymappings(self):
        self.action_open_project.setShortcut(self.settings_manager.keymap['Open Project'])
        self.action_new_project.setShortcut(self.settings_manager.keymap['New Project'])
        self.action_save.setShortcut(self.settings_manager.keymap['Save'])
        self.action_exit.setShortcut(self.settings_manager.keymap['Exit'])
        self.action_export.setShortcut(self.settings_manager.keymap['Export'])
        self.next_button.setShortcut(self.settings_manager.keymap['Next Submission'])
        self.previous_button.setShortcut(self.settings_manager.keymap['Previous Submission'])

    def __signal_handlers(self):
        signal.signal(signal.SIGINT, lambda: self.__exit())
        signal.signal(signal.SIGTERM, lambda: self.__exit())
        signal.signal(signal.SIGQUIT, lambda: self.__exit())

    def __is_project_loaded(self):
        submission = self.project_manager.get_current_submission()
        if submission is None:
            show_message(self, MESSAGE_PROJECT_NOTLOADED)
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
        self.action_save.triggered.connect(self.__save_project)
        self.action_settings.triggered.connect(self.__open_settings_panel)
        self.action_exit.triggered.connect(self.__exit)
        self.action_about.triggered.connect(self.__about)

        self.previous_button.clicked.connect(self.__prev_submission)
        self.next_button.clicked.connect(self.__next_submission)

        self.add_requirement.clicked.connect(self.__add_requirement)
        self.remove_requirement.clicked.connect(self.__remove_requirement)

    def __update_fileview(self):
        if self.__is_project_loaded():
            submission = self.project_manager.get_current_submission()

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
                show_message(self, MESSAGE_INVALID_NAME)
            elif name is None:
                return
            else:
                break

        full_path = os.path.join(WORKSPACE_PATH, name)

        if is_directory(full_path):
            yes = show_warning(self, MESSAGE_PROJECT_EXISTS)
            if yes:
                overwrite(full_path)
            else:
                return
        else:
            os.mkdir(full_path)

        while True:
            source_directory = show_directory_request(self, "Choose source directory", home())

            if source_directory is None or source_directory == '':
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
                    show_message(self, MESSAGE_INVALID_SOURCE)

    def __open_project(self):
        while True:
            source_directory = show_directory_request(self, "Choose project directory", WORKSPACE_PATH)

            if source_directory is None or source_directory == '':
                return
            else:
                success = self.project_manager.load(source_directory)

                if success:
                    message = "Project loaded!"
                    show_message(self, message)
                    self.__update_fileview()
                    return
                else:
                    show_message(self, MESSAGE_INVALID_SOURCE)

    def __save_project(self):
        if self.__is_project_loaded():
            success = self.project_manager.save()
            if success:
                show_message(self, MESSAGE_SAVE)
            else:
                show_message(self, MESSAGE_SAVE_ERROR)

    def __about(self):
        show_message(self, MESSAGE_ABOUT)

    def __open_file(self, path):
        project_path = self.project_manager.state['project_path']

        if project_path is None:
            show_message(self, MESSAGE_PROJECT_NOTLOADED)
            return

        editor = None
        if self.settings_manager.default_editor is not None:
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
            while True:
                res = show_request(self, "New requirement:")
                if res is None:
                    return
                elif res == '':
                    show_message(self, "Not a valid requirement.")
                else:
                    break

            submissions = self.project_manager.state['submissions']
            for i in range(0, len(submissions)):
                submissions[i].add_requirement(res)

            self.requirement_model.replace_data(self.project_manager.get_current_submission().requirements)

    def __remove_requirement(self):
        if self.__is_project_loaded():
            selections = self.requirements_view.selectionModel().selectedRows()
            if len(selections) == 0:
                return
            row = selections[0].row()
            submissions = self.project_manager.state['submissions']
            for i in range(0, len(submissions)):
                submissions[i].remove_requirement(row)
            self.requirement_model.replace_data(self.project_manager.get_current_submission().requirements)

    def __update_submission_requirements(self):
        submission = self.project_manager.get_current_submission()
        if submission is None:
            return
        submission.requirements = self.requirement_model.data[:]

    def __open_settings_panel(self):
        # TODO: this should not be hard-coded, styles should be the same across all components
        panel = SettingsPanel(self.settings_manager)
        style = replace_vars(os.path.join("themes", "default.vars"), self.stylesheet)
        panel.setStyleSheet(style)
        panel.exec_()

    def __exit(self):
        self.project_manager.save()
        qApp.exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    quickgrader = QuickGrader()
    quickgrader.show()
    app.exec_()
