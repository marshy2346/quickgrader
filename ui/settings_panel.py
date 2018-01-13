import shutil

from PyQt5.QtWidgets import (
    QWidget,
    QListView,
    QDialog,
    QLineEdit,
    QHBoxLayout,
    QListWidget,
    QStackedWidget,
    QVBoxLayout,
    QGroupBox,
    QLabel,
    QPushButton,
    QListWidgetItem
)
from PyQt5.QtCore import (
    Qt
)

from utils.dialog import (
    show_message
)
from constants import (
    MESSAGE_SETTINGS_EDITOR_HELP
)


class EnvironmentPage(QWidget):
    def __init__(self, settings_manager, parent=None):
        super().__init__(parent)
        self.settings_manager = settings_manager

        editor_group = QGroupBox("Editor Configuration")  

        editor_label = QLabel("Editor:")
        self.editor_line = QLineEdit()

        update_button = QPushButton()
        update_button.setText("Update")
        update_button.clicked.connect(self.__update_editor)

        help_button = QPushButton()
        help_button.setText("Help")
        help_button.clicked.connect(self.__show_help)

        editor_layout = QHBoxLayout()
        editor_layout.addWidget(editor_label)
        editor_layout.addWidget(self.editor_line)
        editor_layout.addWidget(update_button)
        editor_layout.addWidget(help_button)

        config_layout = QVBoxLayout()
        config_layout.addLayout(editor_layout)
        editor_group.setLayout(config_layout)

        main_layout = QVBoxLayout()
        main_layout.addWidget(editor_group)
        main_layout.addStretch(1)

        self.__update_display()

        self.setLayout(main_layout)

    def __update_display(self):
        if self.settings_manager.default_editor == '':
            self.editor_line.setText("default")
        else:
            self.editor_line.setText(self.settings_manager.default_editor)

    def __show_help(self):
        show_message(self, MESSAGE_SETTINGS_EDITOR_HELP)

    def __update_editor(self):
        text = self.editor_line.text()
        if text is None or text == '' or text == 'default':
            self.settings_manager.default_editor = '' 
            self.settings_manager.save()
            show_message(self, "Default settings active.")
        elif shutil.which(text) is None:
            show_message(self, "Invalid executable path.")
        else:
            self.settings_manager.default_editor = text
            self.settings_manager.save()
            show_message(self, "Editor updated!")


class SettingsPanel(QDialog):
    def __init__(self, settings_manager, parent=None):
        super().__init__(parent)
        self.settings_manager = settings_manager
        self.contents_widget = QListWidget()
        self.contents_widget.setMovement(QListView.Static)
        self.contents_widget.setMaximumWidth(105)
        self.contents_widget.setSpacing(12)

        self.pages_widget = QStackedWidget()
        self.pages_widget.addWidget(EnvironmentPage(self.settings_manager))

        close_button = QPushButton("Close")

        self.__create_icons()
        self.contents_widget.setCurrentRow(0)

        close_button.clicked.connect(self.close)

        horizontal_layout = QHBoxLayout()    
        horizontal_layout.addWidget(self.contents_widget)
        horizontal_layout.addWidget(self.pages_widget, 1)

        buttons_layout = QHBoxLayout()
        buttons_layout.addStretch(1)
        buttons_layout.addWidget(close_button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(horizontal_layout)
        main_layout.addStretch(1)
        main_layout.addSpacing(12)
        main_layout.addLayout(buttons_layout)

        self.setLayout(main_layout)
        self.setWindowTitle("Settings Panel")

    def change_page(self, current, previous):
        if not current:
            current = previous
        self.pages_widget.setCurrentIndex(self.contents_widget.row(current))

    def __create_icons(self):
        environment_button = QListWidgetItem(self.contents_widget)
        environment_button.setText("Environment")
        environment_button.setTextAlignment(Qt.AlignHCenter)
        environment_button.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

