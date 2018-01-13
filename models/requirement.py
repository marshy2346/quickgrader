from PyQt5.QtCore import (
    Qt,
    QAbstractTableModel
)


class RequirementModel(QAbstractTableModel):
    def __init__(self):
        super().__init__()
        self.header = ["Requirement", "Value", "Comments"]
        self.data = []

    def rowCount(self, parent=None):
        return len(self.data)

    def columnCount(self, parent=None):
        return 3

    def replace_data(self, data):
        if data is None:
            return
        self.data = data
        self.layoutChanged.emit()

    def data(self, index, role):
        if index.isValid() and role == Qt.DisplayRole:
            return (self.data[index.row()][index.column()])

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.header[section]

    def setData(self, index, value, role):
        self.data[index.row()][index.column()] = value
        return True

    def flags(self, index):
        return Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsSelectable

