__author__ = 'hzengin'

from PySide import QtCore,QtGui
from ui.dialog_qt import *
import sys
from DirDialog import *
from MainWindow import *

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mainWindow=MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())


