# coding=utf-8
from PyQt5 import QtWidgets, QtGui, QtCore

from warframeAlert.components.common.CommonImages import CommonImages
from warframeAlert.components.common.Countdown import Countdown
from warframeAlert.constants.events import UPGRADE_TYPE_IMAGE
from warframeAlert.services.translationService import translate
from warframeAlert.utils import timeUtils
from warframeAlert.utils.fileUtils import get_separator
from warframeAlert.utils.gameTranslationUtils import get_upgrade_type
from warframeAlert.utils.logUtils import LogHandler


class GlobalUpgrade():
    def __init__(self, upgrade_id: str) -> None:
        self.id = upgrade_id
        self.upgrade_image = None
        font = QtGui.QFont()
        font.setBold(True)

        self.UpgradeImage = CommonImages()
        self.UpgradeText = QtWidgets.QLabel("N/D")
        self.UpgradeInit = QtWidgets.QLabel("N/D")
        self.UpgradeEnd = Countdown(translate("globalUpgrade", "end"))

        self.UpgradeText.setFont(font)

        self.UpgradeHBox = QtWidgets.QHBoxLayout()
        self.UpgradeVBox = QtWidgets.QVBoxLayout()

        self.UpgradeBox = QtWidgets.QHBoxLayout()

        self.UpgradeHBox.addWidget(self.UpgradeInit)
        self.UpgradeHBox.addWidget(self.UpgradeEnd.TimeLab)

        self.UpgradeVBox.addLayout(self.UpgradeHBox)
        self.UpgradeVBox.addWidget(self.UpgradeText)

        self.UpgradeBox.addWidget(self.UpgradeImage.image)
        self.UpgradeBox.addLayout(self.UpgradeVBox)
        self.UpgradeBox.addStretch(1)

    def set_upgrade_data(self, init: str, end: int, upgrade_type: str,
                         operation: str, value: int, node: list[tuple[str, str]]) -> None:
        nodes = ""
        for nod in node:
            nodes += nod[0] + " " + nod[1] + " "
        self.UpgradeEnd.set_countdown(end[:10])
        self.UpgradeEnd.start()
        self.UpgradeInit.setText(translate("globalUpgrade", "init") + ": " + init)
        self.UpgradeText.setText(get_upgrade_type(upgrade_type) + operation + str(value) + " " + nodes)
        self.set_image(upgrade_type)

    def set_other_data(self, tag: str, desc: str, valid_type: str) -> None:
        tooltip = ""
        if (tag != ""):
            tooltip += tag + " "
        if (desc != ""):
            tooltip += desc + " "
        if (valid_type != ""):
            tooltip += valid_type
        if (tooltip != ""):
            self.UpgradeImage.set_tooltip(tooltip)

    def to_string(self) -> str:
        return self.UpgradeText.text()

    def is_expired(self) -> bool:
        return (int(self.UpgradeEnd.get_time()) - int(timeUtils.get_local_time())) < 0

    def get_id(self) -> str:
        return self.id

    def get_image(self) -> str:
        return self.upgrade_image

    def hide(self) -> None:
        self.UpgradeImage.hide()
        self.UpgradeText.hide()
        self.UpgradeInit.hide()
        self.UpgradeEnd.hide()

    def set_image(self, upgrade_type: str) -> None:
        if (upgrade_type in UPGRADE_TYPE_IMAGE):
            image = UPGRADE_TYPE_IMAGE[upgrade_type]
        else:
            LogHandler.debug(translate("gameTranslation", "unknownUpgradeType"))
            return

        image_name = "assets" + get_separator() + "image" + get_separator() + image
        self.UpgradeImage.set_image(image_name)
        self.UpgradeImage.set_image_dimension(32, 32, QtCore.Qt.KeepAspectRatio)
        self.upgrade_image = image_name
