import re
import os
import sys
import pdb
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MyTableModel(QAbstractTableModel):
    def __init__(self, datain, headerdata, parent=None, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.arraydata=datain
        self.headerdata=headerdata
    def rowCount(self, parent):
        return len(self.arraydata)

    def columnCount(self,parent):
        return len(self.headerdata)

    def data(self, index,role):
        if not index.isValid():
            return QVariant()
        elif role != Qt.DisplayRole:
            return QVariant()
        return QVariant(self.arraydata[index.row()][index.column()])

    def getRow(self, idx):
        if idx< len(self.arraydata):
            return self.arraydata[idx]
    def setLabeled(self,idx):
        if idx<len(self.arraydata):
            self.arraydata[idx][1]="yes"
    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return QVariant(self.headerdata[col])
        return QVariant()

