# coding=utf-8
from PyQt5 import QtWidgets, QtGui, QtCore

from warframeAlert.components.common.CommonImages import CommonImages
from warframeAlert.components.common.Countdown import Countdown
from warframeAlert.services.translationService import translate
from warframeAlert.utils import timeUtils
from warframeAlert.utils.fileUtils import get_separator
from warframeAlert.utils.gameTranslationUtils import get_upgrade_type
from warframeAlert.warframeData import UPGRADE_TYPE_IMAGE


class GlobalUpgrade():
    def __init__(self, upgrade_id):
        self.id = upgrade_id
        self.upgrade_image = None
        font = QtGui.QFont()
        font.setBold(True)

        self.UpgradeImage = CommonImages()
        self.UpgradeText = QtWidgets.QLabel("N/D")
        self.UpgradeInit = QtWidgets.QLabel("N/D")
        self.UpgradeEnd = Countdown(translate("globalUpgrade", "end"))

        self.UpgradeText.setFont(font)

        self.Upgradehbox = QtWidgets.QHBoxLayout()
        self.Upgradevbox = QtWidgets.QVBoxLayout()

        self.UpgradeBox = QtWidgets.QHBoxLayout()

        self.Upgradehbox.addWidget(self.UpgradeInit)
        self.Upgradehbox.addWidget(self.UpgradeEnd.TimeLab)

        self.Upgradevbox.addLayout(self.Upgradehbox)
        self.Upgradevbox.addWidget(self.UpgradeText)

        self.UpgradeBox.addWidget(self.UpgradeImage.image)
        self.UpgradeBox.addLayout(self.Upgradevbox)
        self.UpgradeBox.addStretch(1)

    def set_upgrade_data(self, init, end, upgrade_type, operation, value, node):
        nodes = ""
        for nod in node:
            nodes += nod[0] + " " + nod[1] + " "
        self.UpgradeEnd.set_countdown(end[:10])
        self.UpgradeEnd.start()
        self.UpgradeInit.setText(translate("globalUpgrade", "init") + ": " + init)
        self.UpgradeText.setText(get_upgrade_type(upgrade_type) + operation + str(value) + " " + nodes)
        self.set_image(upgrade_type)

    def set_other_data(self, tag, desc, valid_type):
        tooltip = ""
        if (tag != ""):
            tooltip += tag + " "
        if (desc != ""):
            tooltip += desc + " "
        if (valid_type != ""):
            tooltip += valid_type
        if (tooltip != ""):
            self.UpgradeImage.set_tooltip(tooltip)

    def to_string(self):
        return self.UpgradeText.text()

    def is_expired(self):
        return (int(self.UpgradeEnd.get_time()) - int(timeUtils.get_local_time())) < 0

    def get_id(self):
        return self.id

    def get_image(self):
        return self.upgrade_image

    def hide(self):
        self.UpgradeImage.hide()
        self.UpgradeText.hide()
        self.UpgradeInit.hide()
        self.UpgradeEnd.hide()

    def set_image(self, upgrade_type):
        if (upgrade_type in UPGRADE_TYPE_IMAGE):
            image = UPGRADE_TYPE_IMAGE[upgrade_type]
        else:
            print(translate("gameTranslation", "unknownupgradeType"))
            return

        image_name = "assets" + get_separator() + "image" + get_separator() + image
        self.UpgradeImage.set_image(image_name)
        self.UpgradeImage.set_image_dimension(32, 32, QtCore.Qt.KeepAspectRatio)
        self.upgrade_image = image_name
