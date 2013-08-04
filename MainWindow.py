__author__ = 'hzengin'


from PySide import QtCore,QtGui
from ui.mainwindow_qt import *
from DirDialog import *
from NameFinder import *
from Movie import *
from NameParser import *



class MainWindow(QtGui.QMainWindow):
    dirUrl=""
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)

        self.finder=NameFinder()
        self.parser=NameParser()
        self.movies={}
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        QtCore.QObject.connect(self.ui.btnPreview,QtCore.SIGNAL('clicked()'),self.populateList)

        QtCore.QObject.connect(self.ui.btnTAGName,QtCore.SIGNAL('clicked()'),self.AddTAGTitle)
        QtCore.QObject.connect(self.ui.btnTAGRating,QtCore.SIGNAL('clicked()'),self.AddTAGRatinge)
        QtCore.QObject.connect(self.ui.btnTAGYear,QtCore.SIGNAL('clicked()'),self.AddTAGYear)


        dirDialog = DirDialog()
        dirDialog.exec_()
        self.dirUrl=dirDialog.ui.txtDirectory.text()
        self.getDirectories()
        self.getMovieData()
        self.populateList()


    def getDirectories(self):
        self.dirList=sub_dirs(self.dirUrl)

    def getMovieData(self):
        for name in self.dirList:
            movieData=self.finder.FindTitle(name)
            self.movies[name]=movieData

    def populateList(self):
        while(self.ui.tableWidget.rowCount() > 0):
            self.ui.tableWidget.removeRow(0)

        for old in self.movies.keys():
            insertRow = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(insertRow)
            item=QtGui.QTableWidgetItem(old)
            item.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
            self.ui.tableWidget.setItem(insertRow,0,item)
            item=QtGui.QTableWidgetItem(self.parser.parse(self.ui.txtNamePattern.text(),self.movies[old]))
            self.ui.tableWidget.setItem(insertRow,1,item)
            print(self.movies[old])

    def AddTAGTitle(self):
        self.ui.txtNamePattern.setText(self.ui.txtNamePattern.text()+"[TITLE]")

    def AddTAGYear(self):
        self.ui.txtNamePattern.setText(self.ui.txtNamePattern.text()+"[YEAR]")

    def AddTAGRatinge(self):
        self.ui.txtNamePattern.setText(self.ui.txtNamePattern.text()+"[RATING]")


