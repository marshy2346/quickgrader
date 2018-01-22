from PyQt5.QtWidgets import (
    QMessageBox,
    QInputDialog,
    QLineEdit,
    QFileDialog
)

def show_message(qt_widget, message):
    reply = QMessageBox.question(
        qt_widget, "Message", message, QMessageBox.Ok, QMessageBox.Ok
    )


def show_warning(qt_widget, warning):
    reply = QMessageBox.question(
        qt_widget, "Warning!", warning, QMessageBox.Ok | QMessageBox.Cancel, QMessageBox.Ok
    )
    return reply == QMessageBox.Ok


def show_request(qt_widget, request):
    text, ok_pressed = QInputDialog.getText(
        qt_widget, "Request", request, QLineEdit.Normal, ""
    )
    if ok_pressed:
        return text


def show_directory_request(qt_widget, title, root_path):
    opts = QFileDialog.ShowDirsOnly | QFileDialog.DontUseNativeDialog
    dirpath = str(QFileDialog.getExistingDirectory(
        qt_widget, title, root_path, opts
    ))
    return dirpath


def show_file_request(qt_widget, title, root_path):
    opts = QFileDialog.DontUseNativeDialog
    filepath = QFileDialog.getOpenFileName(
        qt_widget, title, root_path, options=opts
    )
    return filepath


def show_files_request(qt_widget, title, root_path):
    opts = QFileDialog.DontUseNativeDialog
    dialog = QFileDialog()
    dialog.setWindowTitle(title)
    dialog.setViewMode(QFileDialog.List)
    dialog.setOptions(opts)
    filenames = dialog.getOpenFileNames(qt_widget, title, root_path)
    return filenames[0]


