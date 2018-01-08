from PyQt5.QtWidgets import QTextEdit, QWidget, QVBoxLayout, QLabel
from ui.dialog import show_message
import os

class Editor(QWidget):
    def __init__(self, parent, root_path):
        super().__init__(parent)
        self._parent = parent
        self.root_path = root_path
        self.editor = QTextEdit(parent)
        self.editor.textChanged.connect(self._handle_text_changed)
        self._setup_ui()

    def _setup_ui(self):
        vlayout = QVBoxLayout()
        title = QLabel("File Editor")
        vlayout.addWidget(title)
        vlayout.addWidget(self.editor)
        self.setLayout(vlayout)

    def set_view(self, list_widget):
        f_path = os.path.join(self.root_path, list_widget.text())

        if not os.path.isfile(f_path):
            show_message(self._parent, "Selection must be a file.")
            return

        with open(f_path, 'r') as f:
            text = f.read()
            self.editor.setText(text)

    def _handle_text_changed(self):
        print("text changed")
