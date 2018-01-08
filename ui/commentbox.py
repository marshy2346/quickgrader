from PyQt5.QtWidgets import QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QWidget

class CommentBox(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self._parent = parent
        self._setup_ui()

    def _setup_ui(self):
        title = QLabel("Comments")
        textedit = QTextEdit(self._parent)
        vlayout = QVBoxLayout()
        hlayout = QHBoxLayout()

        vlayout.addWidget(title)
        vlayout.addWidget(textedit)

        self.setLayout(vlayout)

