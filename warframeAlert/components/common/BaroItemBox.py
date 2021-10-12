# coding=utf-8
from PyQt6 import QtGui, QtWidgets, QtCore

from warframeAlert.components.common.CommonImages import CommonImages
from warframeAlert.components.common.CommonLabelWithImage import CommonLabelWithImage
from warframeAlert.constants.files import UPDATE_SITE
from warframeAlert.utils.commonUtils import get_last_item_with_backslash
from warframeAlert.utils.fileUtils import get_separator


class BaroItemBox():

    def __init__(self) -> None:
        self.Font = QtGui.QFont()
        self.Font.setBold(True)

        self.BaroImage = CommonImages()
        self.BaroName = QtWidgets.QLabel("N/D")

        ducat_image = "assets" + get_separator() + "icon" + get_separator() + "ducats.png"
        self.BaroDucat = CommonLabelWithImage(ducat_image, "???")

        credit_image = "assets" + get_separator() + "icon" + get_separator() + "credit.png"
        self.BaroCredit = CommonLabelWithImage(credit_image, "???")

        self.BaroName.setFont(self.Font)
        self.BaroName.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.BaroBox = QtWidgets.QVBoxLayout()
        self.BaroImageBox = QtWidgets.QHBoxLayout()
        self.BaroHBox = QtWidgets.QHBoxLayout()

        self.BaroImageBox.addStretch(1)
        self.BaroImageBox.addWidget(self.BaroImage.image)
        self.BaroImageBox.addStretch(1)

        self.BaroHBox.addLayout(self.BaroDucat.LabelWithImage)
        self.BaroHBox.addStretch(1)
        self.BaroHBox.addLayout(self.BaroCredit.LabelWithImage)

        self.BaroBox.addLayout(self.BaroImageBox)
        self.BaroBox.addWidget(self.BaroName)
        self.BaroBox.addLayout(self.BaroHBox)

    def get_item_name(self) -> str:
        return self.BaroName.text()

    def set_baro_item(self, item: str, ducat: int, credit: int) -> None:
        self.BaroName.setText(item)
        if (ducat == 0):
            self.BaroDucat.hide()
        else:
            self.BaroDucat.set_before_text(str(ducat))
        if (credit == 0):
            self.BaroCredit.hide()
        else:
            self.BaroCredit.set_before_text(str(credit))

    def set_baro_image(self, url_image: str) -> None:
        image_name = get_last_item_with_backslash(url_image)

        site = UPDATE_SITE + "images" + get_separator() + image_name + ".png"
        site = site.replace("\\", "/")
        image_name += ".png"

        image_path = "images" + get_separator() + image_name
        self.BaroImage.set_image(image_path, site)
        self.BaroImage.set_image_dimension(65, 65, QtCore.Qt.KeepAspectRatio)

    def hide(self) -> None:
        self.BaroName.hide()
        self.BaroImage.hide()
        self.BaroDucat.hide()
        self.BaroCredit.hide()
