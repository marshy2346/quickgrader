from PyQt5.QtWidgets import QMessageBox, QInputDialog, QLineEdit, QFileDialog


def show_message(parent, content):
    reply = QMessageBox.question(
        parent, "Message", content, QMessageBox.Ok, QMessageBox.Ok
    )

def show_warning(parent, content):
    reply = QMessageBox.question(
        parent, "Warning", content,
        QMessageBox.Ok | QMessageBox.Cancel, QMessageBox.Cancel
    )
    return reply == QMessageBox.Ok

def request_info(parent, request_str):
    text, ok = QInputDialog.getText(parent, "Request", request_str, QLineEdit.Normal, "")
    if ok:
        return text
    else:
        return None
    
def request_directory(parent, title, root):
    opts = QFileDialog.ShowDirsOnly | QFileDialog.DontUseNativeDialog
    dirpath = str(
        QFileDialog.getExistingDirectory(
            parent,
            title,
            root,
            opts
        )
    )
    if dirpath != '':
        return dirpath
    else:
        return None
