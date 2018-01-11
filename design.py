import os 

from PyQt5 import (
    QtCore,
    QtGui,
    QtWidgets
)

from utils.parsing import (
   replace_vars 
) 

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 628)
        MainWindow.setWindowOpacity(1.0)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalWidget_2.setObjectName("verticalWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalWidget_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalFrame = QtWidgets.QFrame(self.verticalWidget_2)
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.file_view_label = QtWidgets.QLabel(self.verticalFrame)
        self.file_view_label.setObjectName("file_view_label")
        self.verticalLayout.addWidget(self.file_view_label)
        self.file_view = QtWidgets.QListWidget(self.verticalFrame)
        self.file_view.setObjectName("file_view")
        self.verticalLayout.addWidget(self.file_view)
        self.verticalLayout_2.addWidget(self.verticalFrame)
        self.requirements_label = QtWidgets.QLabel(self.verticalWidget_2)
        self.requirements_label.setObjectName("requirements_label")
        self.verticalLayout_2.addWidget(self.requirements_label)
        self.requirements_view = QtWidgets.QTableView(self.verticalWidget_2)
        self.requirements_view.setObjectName("requirements_view")
        self.verticalLayout_2.addWidget(self.requirements_view)
        self.groupBox_2 = QtWidgets.QGroupBox(self.verticalWidget_2)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.previous_button = QtWidgets.QPushButton(self.groupBox_2)
        self.previous_button.setObjectName("previous_button")
        self.horizontalLayout_3.addWidget(self.previous_button)
        self.next_button = QtWidgets.QPushButton(self.groupBox_2)
        self.next_button.setObjectName("next_button")
        self.horizontalLayout_3.addWidget(self.next_button)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.verticalLayout_3.addWidget(self.verticalWidget_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        self.file_menu = QtWidgets.QMenu(self.menubar)
        self.file_menu.setObjectName("file_menu")
        self.about_menu = QtWidgets.QMenu(self.menubar)
        self.about_menu.setObjectName("about_menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_open_project = QtWidgets.QAction(MainWindow)
        self.action_open_project.setObjectName("action_open_project")
        self.action_new_project = QtWidgets.QAction(MainWindow)
        self.action_new_project.setObjectName("action_new_project")
        self.action_export = QtWidgets.QAction(MainWindow)
        self.action_export.setObjectName("action_export")
        self.action_exit= QtWidgets.QAction(MainWindow)
        self.action_exit.setObjectName("action_exit")
        self.file_menu.addAction(self.action_open_project)
        self.file_menu.addAction(self.action_new_project)
        self.file_menu.addAction(self.action_export)
        self.file_menu.addAction(self.action_exit)
        self.menubar.addAction(self.file_menu.menuAction())
        self.menubar.addAction(self.about_menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.stylesheet = None
        self.setTheme("default")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def setTheme(self, name):
        self.stylesheet = os.path.join("themes", name + ".stylesheet")
        style = replace_vars(os.path.join("themes", name + ".vars"), self.stylesheet)
        self.setStyleSheet(style)
        self.update()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QuickGrader"))
        self.file_view_label.setText(_translate("MainWindow", "File View"))
        self.requirements_label.setText(_translate("MainWindow", "Requirements"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Toolbar"))
        self.previous_button.setText(_translate("MainWindow", "Previous"))
        self.next_button.setText(_translate("MainWindow", "Next"))
        self.file_menu.setTitle(_translate("MainWindow", "File"))
        self.about_menu.setTitle(_translate("MainWindow", "About"))
        self.action_open_project.setText(_translate("MainWindow", "Open Project"))
        self.action_new_project.setText(_translate("MainWindow", "New Project"))
        self.action_export.setText(_translate("MainWindow", "Export"))
        self.action_exit.setText(_translate("MainWindow", "Exit"))

