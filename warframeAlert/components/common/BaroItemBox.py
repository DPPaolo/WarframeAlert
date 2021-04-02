# coding=utf-8
from PyQt5 import QtGui, QtWidgets, QtCore

from warframeAlert.components.common.CommonImages import CommonImages
from warframeAlert.components.common.CommonLabelWithImage import CommonLabelWithImage
from warframeAlert.constants.files import UPDATE_SITE, DEFAULT_SITE_IMAGE
from warframeAlert.utils.commonUtils import get_last_item_with_backslash
from warframeAlert.utils.fileUtils import get_separator
from warframeAlert.utils.warframeUtils import get_baro_image_path_from_export_manifest


class BaroItemBox():

    def __init__(self):
        self.Font = QtGui.QFont()
        self.Font.setBold(True)

        self.BaroImage = CommonImages()
        self.BaroName = QtWidgets.QLabel("N/D")

        ducat_image = "assets" + get_separator() + "icon" + get_separator() + "ducats.png"
        self.BaroDucat = CommonLabelWithImage(ducat_image, "???")

        credit_image = "assets" + get_separator() + "icon" + get_separator() + "credit.png"
        self.BaroCredit = CommonLabelWithImage(credit_image, "???")

        self.BaroName.setFont(self.Font)
        self.BaroName.setAlignment(QtCore.Qt.AlignCenter)

        self.BaroBox = QtWidgets.QVBoxLayout()
        self.BaroImageBox = QtWidgets.QHBoxLayout()
        self.BarohBox = QtWidgets.QHBoxLayout()

        self.BaroImageBox.addStretch(1)
        self.BaroImageBox.addWidget(self.BaroImage.image)
        self.BaroImageBox.addStretch(1)

        self.BarohBox.addLayout(self.BaroDucat.LabelWithImage)
        self.BarohBox.addStretch(1)
        self.BarohBox.addLayout(self.BaroCredit.LabelWithImage)

        self.BaroBox.addLayout(self.BaroImageBox)
        self.BaroBox.addWidget(self.BaroName)
        self.BaroBox.addLayout(self.BarohBox)

    def get_item_name(self):
        return self.BaroName.text()

    def set_baro_item(self, item, ducat, credit):
        self.BaroName.setText(item)
        if (ducat == 0):
            self.BaroDucat.hide()
        else:
            self.BaroDucat.set_before_text(str(ducat))
        if (credit == 0):
            self.BaroCredit.hide()
        else:
            self.BaroCredit.set_before_text(str(credit))

    def set_baro_image(self, url_image):
        img = get_baro_image_path_from_export_manifest(url_image)
        image_name = get_last_item_with_backslash(img)

        if (img == url_image):
            site = UPDATE_SITE + "images" + get_separator() + image_name + ".png"
            site = site.replace("\\", "/")
            image_name += ".png"
        else:
            site = DEFAULT_SITE_IMAGE + img

        image_path = "images" + get_separator() + image_name
        self.BaroImage.set_image(image_path, site)
        self.BaroImage.set_image_dimension(65, 65, QtCore.Qt.KeepAspectRatio)

    def hide(self):
        self.BaroName.hide()
        self.BaroImage.hide()
        self.BaroDucat.hide()
        self.BaroCredit.hide()
