__author__ = 'hzengin'

from PySide import QtCore,QtGui
from ui.dialog_qt import *


class DirDialog(QtGui.QDialog):
    def __init__(self,parent=None):
        super(DirDialog,self).__init__(parent)
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.btnSelectDir,QtCore.SIGNAL('clicked()'),self.openFileDialog)


    def openFileDialog(self):
        dirUrl = QtGui.QFileDialog.getExistingDirectory(self,"Select Directory","/home/",QtGui.QFileDialog.ShowDirsOnly)
        self.ui.txtDirectory.setText(dirUrl)

