# coding=utf-8
from PyQt6 import QtWidgets, QtGui

from warframeAlert.components.common.CommonLabelWithImage import CommonLabelWithImage
from warframeAlert.utils.fileUtils import get_separator


class VaultItemBox():

    def __init__(self, item: str, aya: int, regal_aya: int) -> None:
        self.item = item
        self.aya = aya
        self.regal_aya = regal_aya
        self.VaultItemName = QtWidgets.QLabel(item)
        regal_aya_image = "assets" + get_separator() + "icon" + get_separator() + "regalAya.png"
        self.VaultItemPriceRegalAya = CommonLabelWithImage(regal_aya_image, str(self.regal_aya))
        aya_image = "assets" + get_separator() + "icon" + get_separator() + "aya.png"
        self.VaultItemPriceAya = CommonLabelWithImage(aya_image, str(self.aya))

        if (self.regal_aya == 0):
            self.VaultItemPriceRegalAya.hide()
        if (self.aya == 0):
            self.VaultItemPriceAya.hide()

        self.Font = QtGui.QFont()
        self.Font.setBold(True)
        self.VaultItemName.setFont(self.Font)

        self.VaultItemLayoutBox = QtWidgets.QHBoxLayout()

        self.VaultItemLayoutBox.addWidget(self.VaultItemName)
        self.VaultItemLayoutBox.addLayout(self.VaultItemPriceRegalAya.LabelWithImage)
        self.VaultItemLayoutBox.addLayout(self.VaultItemPriceAya.LabelWithImage)
