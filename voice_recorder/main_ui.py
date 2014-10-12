# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Sun Oct 12 10:29:33 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(533, 346)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pause_button = QtGui.QPushButton(self.centralwidget)
        self.pause_button.setObjectName(_fromUtf8("pause_button"))
        self.gridLayout.addWidget(self.pause_button, 3, 3, 1, 1)
        self.username = QtGui.QLineEdit(self.centralwidget)
        self.username.setObjectName(_fromUtf8("username"))
        self.gridLayout.addWidget(self.username, 0, 2, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 0, 6, 1, 1)
        self.recorded_minutes_and_seconds = QtGui.QLabel(self.centralwidget)
        self.recorded_minutes_and_seconds.setObjectName(_fromUtf8("recorded_minutes_and_seconds"))
        self.gridLayout.addWidget(self.recorded_minutes_and_seconds, 3, 0, 1, 2)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 3, 1, 1)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 1, 5, 1, 2)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.password = QtGui.QLineEdit(self.centralwidget)
        self.password.setEchoMode(QtGui.QLineEdit.Password)
        self.password.setObjectName(_fromUtf8("password"))
        self.gridLayout.addWidget(self.password, 0, 4, 1, 2)
        self.textEdit_2 = Qsci.QsciScintilla(self.centralwidget)
        self.textEdit_2.setMaximumSize(QtCore.QSize(16777215, 100))
        self.textEdit_2.setToolTip(_fromUtf8(""))
        self.textEdit_2.setWhatsThis(_fromUtf8(""))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.gridLayout.addWidget(self.textEdit_2, 4, 0, 1, 8)
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout.addWidget(self.lineEdit_2, 0, 7, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 1, 1, 1, 4)
        self.textEdit = Qsci.QsciScintilla(self.centralwidget)
        self.textEdit.setToolTip(_fromUtf8(""))
        self.textEdit.setWhatsThis(_fromUtf8(""))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.gridLayout.addWidget(self.textEdit, 2, 0, 1, 8)
        self.start_button = QtGui.QPushButton(self.centralwidget)
        self.start_button.setObjectName(_fromUtf8("start_button"))
        self.gridLayout.addWidget(self.start_button, 3, 2, 1, 1)
        self.resume_button = QtGui.QPushButton(self.centralwidget)
        self.resume_button.setObjectName(_fromUtf8("resume_button"))
        self.gridLayout.addWidget(self.resume_button, 3, 4, 1, 1)
        self.stop_button = QtGui.QPushButton(self.centralwidget)
        self.stop_button.setObjectName(_fromUtf8("stop_button"))
        self.gridLayout.addWidget(self.stop_button, 3, 5, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 533, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName(_fromUtf8("menu"))
        self.menu_2 = QtGui.QMenu(self.menubar)
        self.menu_2.setObjectName(_fromUtf8("menu_2"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.start = QtGui.QAction(MainWindow)
        self.start.setObjectName(_fromUtf8("start"))
        self.pause = QtGui.QAction(MainWindow)
        self.pause.setObjectName(_fromUtf8("pause"))
        self.resume = QtGui.QAction(MainWindow)
        self.resume.setObjectName(_fromUtf8("resume"))
        self.stop = QtGui.QAction(MainWindow)
        self.stop.setObjectName(_fromUtf8("stop"))
        self.open = QtGui.QAction(MainWindow)
        self.open.setObjectName(_fromUtf8("open"))
        self.exit = QtGui.QAction(MainWindow)
        self.exit.setObjectName(_fromUtf8("exit"))
        self.menu.addAction(self.open)
        self.menu.addAction(self.exit)
        self.menu_2.addAction(self.start)
        self.menu_2.addAction(self.pause)
        self.menu_2.addAction(self.resume)
        self.menu_2.addAction(self.stop)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pause_button.setText(_translate("MainWindow", "Pause", None))
        self.label.setText(_translate("MainWindow", "Username:", None))
        self.label_4.setText(_translate("MainWindow", "Note name:", None))
        self.recorded_minutes_and_seconds.setText(_translate("MainWindow", "000:00", None))
        self.label_2.setText(_translate("MainWindow", "Password:", None))
        self.pushButton.setText(_translate("MainWindow", "Browser", None))
        self.label_3.setText(_translate("MainWindow", "Path:", None))
        self.start_button.setText(_translate("MainWindow", "Start", None))
        self.resume_button.setText(_translate("MainWindow", "Resume", None))
        self.stop_button.setText(_translate("MainWindow", "Stop", None))
        self.menu.setTitle(_translate("MainWindow", "文件", None))
        self.menu_2.setTitle(_translate("MainWindow", "动作", None))
        self.start.setText(_translate("MainWindow", "开始", None))
        self.pause.setText(_translate("MainWindow", "暂停", None))
        self.resume.setText(_translate("MainWindow", "继续", None))
        self.stop.setText(_translate("MainWindow", "停止", None))
        self.open.setText(_translate("MainWindow", "打开", None))
        self.exit.setText(_translate("MainWindow", "退出", None))

from PyQt4 import Qsci
