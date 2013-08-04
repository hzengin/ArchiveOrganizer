# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/mainwindow.ui'
#
# Created: Sat Aug  3 07:59:36 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(522, 574)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.btnTAGRating = QtGui.QPushButton(self.centralwidget)
        self.btnTAGRating.setObjectName("btnTAGRating")
        self.gridLayout.addWidget(self.btnTAGRating, 0, 2, 1, 1)
        self.btnTAGName = QtGui.QPushButton(self.centralwidget)
        self.btnTAGName.setObjectName("btnTAGName")
        self.gridLayout.addWidget(self.btnTAGName, 0, 1, 1, 1)
        self.btnTAGYear = QtGui.QPushButton(self.centralwidget)
        self.btnTAGYear.setObjectName("btnTAGYear")
        self.gridLayout.addWidget(self.btnTAGYear, 0, 3, 1, 1)
        self.btnClear = QtGui.QPushButton(self.centralwidget)
        self.btnClear.setObjectName("btnClear")
        self.gridLayout.addWidget(self.btnClear, 3, 2, 1, 1)
        self.btnPreview = QtGui.QPushButton(self.centralwidget)
        self.btnPreview.setObjectName("btnPreview")
        self.gridLayout.addWidget(self.btnPreview, 3, 3, 1, 1)
        self.txtNamePattern = QtGui.QLineEdit(self.centralwidget)
        self.txtNamePattern.setObjectName("txtNamePattern")
        self.gridLayout.addWidget(self.txtNamePattern, 3, 0, 1, 2)
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setFrameShape(QtGui.QFrame.StyledPanel)
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.CurrentChanged)
        self.tableWidget.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.tableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWidget.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerItem)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(250)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.gridLayout.addWidget(self.tableWidget, 6, 0, 1, 4)
        self.btnRenameAll = QtGui.QPushButton(self.centralwidget)
        self.btnRenameAll.setObjectName("btnRenameAll")
        self.gridLayout.addWidget(self.btnRenameAll, 7, 0, 1, 2)
        self.btnRenameAll_2 = QtGui.QPushButton(self.centralwidget)
        self.btnRenameAll_2.setObjectName("btnRenameAll_2")
        self.gridLayout.addWidget(self.btnRenameAll_2, 7, 2, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 522, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.btnClear, QtCore.SIGNAL("clicked()"), self.txtNamePattern.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Archive Directory Renamer", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "NAME TAGS:", None, QtGui.QApplication.UnicodeUTF8))
        self.btnTAGRating.setText(QtGui.QApplication.translate("MainWindow", "IMDB Rating", None, QtGui.QApplication.UnicodeUTF8))
        self.btnTAGName.setText(QtGui.QApplication.translate("MainWindow", "Movie Name", None, QtGui.QApplication.UnicodeUTF8))
        self.btnTAGYear.setText(QtGui.QApplication.translate("MainWindow", "Release Year", None, QtGui.QApplication.UnicodeUTF8))
        self.btnClear.setText(QtGui.QApplication.translate("MainWindow", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.btnPreview.setText(QtGui.QApplication.translate("MainWindow", "Preview Pattern", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("MainWindow", "Old Name", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("MainWindow", "New Name", None, QtGui.QApplication.UnicodeUTF8))
        self.btnRenameAll.setText(QtGui.QApplication.translate("MainWindow", "Rename All", None, QtGui.QApplication.UnicodeUTF8))
        self.btnRenameAll_2.setText(QtGui.QApplication.translate("MainWindow", "Rename Selected", None, QtGui.QApplication.UnicodeUTF8))
        self.txtNamePattern.setText("[TITLE] ([YEAR])")

