# coding=utf-8
from PyQt5 import QtWidgets, QtGui

from warframeAlert.services.translationService import translate
from warframeAlert.utils.gameTranslationUtils import get_simaris_target


class SimarisTarget():
    def __init__(self) -> None:
        font = QtGui.QFont()
        font.setBold(True)

        self.SimarisLab = QtWidgets.QLabel(translate("simarisTarget", "actualSimarisTarget") + ": ")
        self.Simaris = QtWidgets.QLabel("N/D")

        self.Simaris.setFont(font)

        self.SimarisBox = QtWidgets.QHBoxLayout()

        self.SimarisBox.addWidget(self.SimarisLab)
        self.SimarisBox.addWidget(self.Simaris)

    def set_simaris_target(self, simaris: str) -> None:
        self.Simaris.setText(get_simaris_target(simaris))
