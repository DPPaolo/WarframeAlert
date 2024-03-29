# coding=utf-8
from typing import List

from PyQt6 import QtWidgets, QtCore


class MissionDropView():

    def __init__(self) -> None:

        self.ViewDropLabel1 = QtWidgets.QLabel("N/D")
        self.ViewDropLabel2 = QtWidgets.QLabel("N/D")
        self.ViewDropLabel3 = QtWidgets.QLabel("N/D")

        self.ViewDrop1 = QtWidgets.QLabel("N/D")
        self.ViewDrop2 = QtWidgets.QLabel("N/D")
        self.ViewDrop3 = QtWidgets.QLabel("N/D")

        self.ViewDropLabel1.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.ViewDropLabel2.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.ViewDropLabel3.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.ViewDrop1.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.ViewDrop2.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.ViewDrop3.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

        drop_rot_box1 = QtWidgets.QVBoxLayout()
        drop_rot_box2 = QtWidgets.QVBoxLayout()
        drop_rot_box3 = QtWidgets.QVBoxLayout()

        self.DropBox = QtWidgets.QHBoxLayout()

        drop_rot_box1.addWidget(self.ViewDropLabel1)
        drop_rot_box1.addWidget(self.ViewDrop1)

        drop_rot_box2.addWidget(self.ViewDropLabel2)
        drop_rot_box2.addWidget(self.ViewDrop2)

        drop_rot_box3.addWidget(self.ViewDropLabel3)
        drop_rot_box3.addWidget(self.ViewDrop3)

        self.DropBox.addLayout(drop_rot_box1)
        self.DropBox.addLayout(drop_rot_box2)
        self.DropBox.addLayout(drop_rot_box3)

    def set_drop(self, num: int, names: List[str], drop: List[str]) -> None:
        self.ViewDrop1.setText(drop[0])
        self.ViewDrop2.setText(drop[1])
        self.ViewDrop3.setText(drop[2])
        self.ViewDropLabel1.setText(names[0])
        if (num <= 2):
            self.ViewDropLabel3.hide()
            self.ViewDrop3.hide()
            if (num == 1):
                self.ViewDropLabel2.hide()
                self.ViewDrop2.hide()
            else:
                self.ViewDropLabel2.setText(names[1])
        else:
            self.ViewDropLabel2.setText(names[1])
            self.ViewDropLabel3.setText(names[2])
