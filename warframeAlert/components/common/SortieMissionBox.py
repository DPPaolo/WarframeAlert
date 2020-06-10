# coding=utf-8
from PyQt5 import QtWidgets, QtGui

from warframeAlert.services.translationService import translate


class SortieMissionBox():
    def __init__(self, mission_number):
        self.Font = QtGui.QFont()
        self.Font.setBold(True)

        self.SortieName = QtWidgets.QLabel(translate("sortieMissionBox", "mission") + " " + str(mission_number))
        self.SortieMission = QtWidgets.QLabel("N/D")
        self.SortieModifier = QtWidgets.QLabel("N/D")
        self.SortieNode = QtWidgets.QLabel("N/D")
        self.SortieTile = QtWidgets.QLabel("N/D")

        self.SortieModifier.setFont(self.Font)
        self.SortieMission.setFont(self.Font)
        self.SortieNode.setFont(self.Font)

        self.SortieBoxData = QtWidgets.QHBoxLayout()

        self.SortieMissionBox = QtWidgets.QVBoxLayout()

        self.SortieBoxData.addWidget(self.SortieMission)
        self.SortieBoxData.addWidget(self.SortieModifier)
        self.SortieBoxData.addWidget(self.SortieNode)
        self.SortieBoxData.addWidget(self.SortieTile)

        self.SortieMissionBox.addWidget(self.SortieName)
        self.SortieMissionBox.addLayout(self.SortieBoxData)

    def to_string(self):
        return self.SortieMission.text() + " (" + self.SortieModifier.text() + ")"

    def set_mission_data(self, mission, modifier, node, planet, tileset):
        self.SortieMission.setText(mission)
        self.SortieModifier.setText(modifier)
        self.SortieNode.setText(node + " " + planet)
        self.SortieTile.setText(tileset)

    def sortie_not_available(self):
        self.SortieMission.setText("N/D")
        self.SortieModifier.setText("N/D")
        self.SortieNode.setText("N/D")
        self.SortieTile.setText("N/D")
