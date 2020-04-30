# coding=utf-8
from PyQt5 import QtWidgets, QtCore


class MissionDropView():

    def __init__(self):

        self.ViewDropLabel1 = QtWidgets.QLabel("N/D")
        self.ViewDropLabel2 = QtWidgets.QLabel("N/D")
        self.ViewDropLabel3 = QtWidgets.QLabel("N/D")

        self.ViewDrop1 = QtWidgets.QLabel("N/D")
        self.ViewDrop2 = QtWidgets.QLabel("N/D")
        self.ViewDrop3 = QtWidgets.QLabel("N/D")

        self.ViewDropLabel1.setAlignment(QtCore.Qt.AlignTop)
        self.ViewDropLabel2.setAlignment(QtCore.Qt.AlignTop)
        self.ViewDropLabel3.setAlignment(QtCore.Qt.AlignTop)
        self.ViewDrop1.setAlignment(QtCore.Qt.AlignTop)
        self.ViewDrop2.setAlignment(QtCore.Qt.AlignTop)
        self.ViewDrop3.setAlignment(QtCore.Qt.AlignTop)

        droprotbox1 = QtWidgets.QVBoxLayout()
        droprotbox2 = QtWidgets.QVBoxLayout()
        droprotbox3 = QtWidgets.QVBoxLayout()

        self.DropBox = QtWidgets.QHBoxLayout()

        droprotbox1.addWidget(self.ViewDropLabel1)
        droprotbox1.addWidget(self.ViewDrop1)

        droprotbox2.addWidget(self.ViewDropLabel2)
        droprotbox2.addWidget(self.ViewDrop2)

        droprotbox3.addWidget(self.ViewDropLabel3)
        droprotbox3.addWidget(self.ViewDrop3)

        self.DropBox.addLayout(droprotbox1)
        self.DropBox.addLayout(droprotbox2)
        self.DropBox.addLayout(droprotbox3)

    def set_drop(self, num, name, drop):
        self.ViewDrop1.setText(drop[0])
        self.ViewDrop2.setText(drop[1])
        self.ViewDrop3.setText(drop[2])
        self.ViewDropLabel1.setText(name[0])
        if (num <= 2):
            self.ViewDropLabel3.hide()
            self.ViewDrop3.hide()
            if (num == 1):
                self.ViewDropLabel2.hide()
                self.ViewDrop2.hide()
            else:
                self.ViewDropLabel2.setText(name[1])
        else:
            self.ViewDropLabel2.setText(name[1])
            self.ViewDropLabel3.setText(name[2])