# coding=utf-8
from PyQt6 import QtWidgets


class EmptySpace():

    def __init__(self) -> None:
        self.space = QtWidgets.QLabel("")

        self.SpaceBox = QtWidgets.QHBoxLayout()
        self.SpaceBox.addWidget(self.space)
