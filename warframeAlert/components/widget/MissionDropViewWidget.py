# coding=utf-8
from PyQt6 import QtWidgets, QtGui, QtCore

from warframeAlert.components.common import MissionDropView


class MissionDropViewWidget:
    viewDropWidget = None

    def __init__(self, drop: MissionDropView) -> None:
        self.viewDropWidget = QtWidgets.QWidget()
        self.viewDropWidget.setWindowIcon(QtGui.QIcon("assets/icon/Warframe.ico"))

        self.gridViewDrop = QtWidgets.QGridLayout(self.viewDropWidget)
        self.gridViewDrop.addLayout(drop.DropBox, 0, 0)

        self.viewDropWidget.setLayout(self.gridViewDrop)
        self.gridViewDrop.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

    def get_widget(self) -> QtWidgets.QWidget:
        return self.viewDropWidget
