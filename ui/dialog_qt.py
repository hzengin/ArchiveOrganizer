# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created: Sat Aug  3 06:15:28 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(496, 78)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.btnSelectDir = QtGui.QPushButton(Dialog)
        self.btnSelectDir.setObjectName("btnSelectDir")
        self.gridLayout.addWidget(self.btnSelectDir, 0, 2, 1, 1)
        self.txtDirectory = QtGui.QLineEdit(Dialog)
        self.txtDirectory.setObjectName("txtDirectory")
        self.gridLayout.addWidget(self.txtDirectory, 0, 1, 1, 1)
        self.btnAccept = QtGui.QPushButton(Dialog)
        self.btnAccept.setObjectName("btnAccept")
        self.gridLayout.addWidget(self.btnAccept, 1, 1, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.btnAccept, QtCore.SIGNAL("clicked()"), Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Select Directory", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSelectDir.setText(QtGui.QApplication.translate("Dialog", "Select Dir", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAccept.setText(QtGui.QApplication.translate("Dialog", "Organize Directory", None, QtGui.QApplication.UnicodeUTF8))

