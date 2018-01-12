from PyQt5.QtCore import (
    QVariant,
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

    def clear(self):
        self.data = []
        self.layoutChanged.emit()

    def replace_data(self, data):
        self.data = data
        self.layoutChanged.emit()

    def data(self, index, role):
        if index.isValid() and role == Qt.DisplayRole:
            return (self.data[index.row()][index.column()])

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.header[section]

    def add_requirement_row(self):
        self.data.append(["", "", ""])
        self.layoutChanged.emit()

    def remove_requirement_row(self, selections):
        if len(selections) == 0:
            return

        target = selections[0].row()
        new_data = []
        for r in range(0, self.rowCount()):
            if r != target:
                new_data.append(self.data[r])

        self.data = new_data
                
        self.layoutChanged.emit()


    def setData(self, index, value, role):
        self.data[index.row()][index.column()] = value
        return True

    def flags(self, index):
        return Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsSelectable



