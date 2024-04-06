# coding=utf-8
from PyQt6 import QtGui, QtWidgets, QtCore

from warframeAlert.constants.warframeTypes import EndlessXpChoicesData
from warframeAlert.services.translationService import translate


class CircuitBox():

    def __init__(self) -> None:
        self.Font = QtGui.QFont()
        self.Font.setBold(True)

        self.StandardCircuitTitle = QtWidgets.QLabel(translate("circuitBox", "circuitTitle"))
        self.SteelPathCircuitTitle = QtWidgets.QLabel(translate("circuitBox", "steelPathCircuitTitle"))

        self.StandardCircuitTitle.setFont(self.Font)
        self.SteelPathCircuitTitle.setFont(self.Font)

        self.WarframeChoice1 = QtWidgets.QLabel("N/D")
        self.WarframeChoice2 = QtWidgets.QLabel("N/D")
        self.WarframeChoice3 = QtWidgets.QLabel("N/D")
        self.WeaponChoice1 = QtWidgets.QLabel("N/D")
        self.WeaponChoice2 = QtWidgets.QLabel("N/D")
        self.WeaponChoice3 = QtWidgets.QLabel("N/D")
        self.WeaponChoice4 = QtWidgets.QLabel("N/D")
        self.WeaponChoice5 = QtWidgets.QLabel("N/D")

        self.CircuitGrid = QtWidgets.QGridLayout()

        self.CircuitGrid.addWidget(self.StandardCircuitTitle, 0, 0)
        self.CircuitGrid.addWidget(self.WarframeChoice1, 1, 0)
        self.CircuitGrid.addWidget(self.WarframeChoice2, 1, 1)
        self.CircuitGrid.addWidget(self.WarframeChoice3, 1, 2)
        self.CircuitGrid.addWidget(self.SteelPathCircuitTitle, 2, 0)
        self.CircuitGrid.addWidget(self.WeaponChoice1, 3, 0)
        self.CircuitGrid.addWidget(self.WeaponChoice2, 3, 1)
        self.CircuitGrid.addWidget(self.WeaponChoice3, 3, 2)
        self.CircuitGrid.addWidget(self.WeaponChoice4, 4, 0)
        self.CircuitGrid.addWidget(self.WeaponChoice5, 4, 1)

        self.CircuitGrid.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

    def set_circuit_data(self, data: EndlessXpChoicesData) -> None:
        category = data['Category']
        choices = data['Choices']
        if (category == "EXC_NORMAL"):
            self.WarframeChoice1.setText(choices[0])
            self.WarframeChoice2.setText(choices[1])
            self.WarframeChoice3.setText(choices[2])
        elif (category == "EXC_HARD"):
            self.WeaponChoice1.setText(choices[0])
            self.WeaponChoice2.setText(choices[1])
            self.WeaponChoice3.setText(choices[2])
            self.WeaponChoice4.setText(choices[3])
            self.WeaponChoice5.setText(choices[4])

    def circuit_not_available(self) -> None:
        self.WarframeChoice1.setText("N/D")
        self.WarframeChoice2.setText("N/D")
        self.WarframeChoice3.setText("N/D")
        self.WeaponChoice1.setText("N/D")
        self.WeaponChoice2.setText("N/D")
        self.WeaponChoice3.setText("N/D")
        self.WeaponChoice4.setText("N/D")
        self.WeaponChoice5.setText("N/D")
