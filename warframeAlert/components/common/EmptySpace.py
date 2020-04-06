# coding=utf-8
from PyQt5 import QtWidgets


class EmptySpace():

    def __init__(self):
        self.space = QtWidgets.QLabel("")

        self.SpaceBox = QtWidgets.QHBoxLayout()
        self.SpaceBox.addWidget(self.space)
