# coding=utf-8
from PyQt5 import QtWidgets, QtGui

from warframeAlert.services.translationService import translate


class SortieMissionBox():
    def __init__(self, mission_number: int) -> None:
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

    def to_string(self) -> str:
        return self.SortieMission.text() + " (" + self.SortieModifier.text() + ")"

    def set_mission_data(self, mission: str, modifier: str, node: str, planet: str, tileset: str) -> None:
        self.SortieMission.setText(mission)
        self.SortieModifier.setText(modifier)
        self.SortieNode.setText(node + " " + planet)
        self.SortieTile.setText(tileset)

    def sortie_not_available(self) -> None:
        self.SortieMission.setText("N/D")
        self.SortieModifier.setText("N/D")
        self.SortieNode.setText("N/D")
        self.SortieTile.setText("N/D")
