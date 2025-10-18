# coding=utf-8
from typing import List

from PyQt6 import QtWidgets, QtGui

from warframeAlert.services.translationService import translate
from warframeAlert.utils.commonUtils import bool_to_yes_no


class InGameMarketBox:
    def __init__(self) -> None:
        self.SaleCategory= QtWidgets.QLabel("N/D")
        self.SaleName = QtWidgets.QLabel("N/D")
        self.SaleIcon = QtWidgets.QLabel("N/D")
        self.SaleAddToMenu = QtWidgets.QLabel(translate("inGameMarketBox", "addToMenu") + ": N/D")
        self.SaleItems = QtWidgets.QLabel(translate("inGameMarketBox", "isShow") + ": N/D")

        self.Font = QtGui.QFont()
        self.Font.setBold(True)
        self.SaleCategory.setFont(self.Font)

        self.MerBox = QtWidgets.QVBoxLayout()

        self.SalesBox1 = QtWidgets.QHBoxLayout()
        self.SalesBox2 = QtWidgets.QHBoxLayout()

        self.SalesBox1.addWidget(self.SaleCategory)
        self.SalesBox1.addWidget(self.SaleName)

        self.SalesBox2.addWidget(self.SaleIcon)
        self.SalesBox2.addWidget(self.SaleAddToMenu)

        self.MerBox.addLayout(self.SalesBox1)
        self.MerBox.addLayout(self.SalesBox2)
        self.MerBox.addWidget(self.SaleItems)

    def set_in_game_data(self, category_name: str, name: str, icon: str, add_to_menu: bool, items: List[str]) -> None:
        self.SaleCategory.setText(category_name)
        self.SaleName.setText(name)
        self.SaleIcon.setText(icon)
        self.SaleAddToMenu.setText(translate("inGameMarketBox", "addToMenu") + ": " + bool_to_yes_no(add_to_menu))

        item_list = ""
        for item in items:
            item_list += item + ", "

        self.SaleItems.setText(item_list[:-2])


    def hide(self) -> None:
        self.SaleName.hide()
        self.SaleCategory.hide()
        self.SaleIcon.hide()
        self.SaleAddToMenu.hide()
        self.SaleItems.hide()
