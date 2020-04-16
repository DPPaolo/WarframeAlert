# coding=utf-8
from PyQt5 import QtWidgets, QtGui, QtCore


class MissionDropViewWidget:
    viewDropWidget = None

    def __init__(self, parent, drop):
        self.viewDropWidget = QtWidgets.QWidget(parent)
        self.viewDropWidget.setWindowIcon(QtGui.QIcon("assets/icon/Warframe.ico"))

        self.gridViewDrop = QtWidgets.QGridLayout(self.viewDropWidget)
        self.gridViewDrop.addLayout(drop.DropBox, 0, 0)

        self.viewDropWidget.setLayout(self.gridViewDrop)
        self.gridViewDrop.setAlignment(QtCore.Qt.AlignTop)

    def get_widget(self):
        return self.viewDropWidget
