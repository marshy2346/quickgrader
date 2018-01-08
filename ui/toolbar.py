from PyQt5.QtWidgets import QWidget, QHBoxLayout, QToolBar, QAction

class Toolbar(QWidget):
    def __init__(self,  parent):
        super().__init__(parent)
        self._parent = parent
        self.actions = []

    def setup_ui(self):
        toolbar = QToolBar(self._parent)
        for a in self.actions:
            toolbar.addAction(a)

        hlayout = QHBoxLayout()
        hlayout.addWidget(toolbar)

        self.setLayout(hlayout)

    def add_action(self, name, shortcut, handler):
        action = QAction(name, self)
        action.setShortcut(shortcut)
        action.triggered.connect(handler)
        self.actions.append(action)

