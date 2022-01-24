# coding=utf-8
from PyQt6 import QtWidgets, QtGui, QtCore

from warframeAlert.components.common.CommonImages import CommonImages
from warframeAlert.services.notificationService import NotificationService
from warframeAlert.services.translationService import translate
from warframeAlert.utils.commonUtils import get_last_item_with_backslash, create_pixmap
from warframeAlert.utils.fileUtils import get_separator
from warframeAlert.utils.gameTranslationUtils import get_mission_from_starchart


class Acolyte():

    def __init__(self, acc_id: str) -> None:
        self.acc_id = acc_id
        self.acc_health = 0
        self.acc_image = None

        self.AccImg = CommonImages()
        self.AccName = QtWidgets.QLabel("N/D")
        self.AccName.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.AccNode = QtWidgets.QLabel("N/D")
        self.AccPlanet = QtWidgets.QLabel("N/D")
        self.AccMis = QtWidgets.QLabel("N/D")
        self.AccLevel = QtWidgets.QLabel("N/D")
        self.AccTimeLabel = QtWidgets.QLabel(translate("acolyte", "init") + " ")
        self.AccTime = QtWidgets.QLabel("")
        self.AccFound = QtWidgets.QLabel("N/D")
        self.AccFlee = QtWidgets.QLabel("N/D")

        self.AccPer = QtWidgets.QProgressBar()

        font = QtGui.QFont()
        font.setBold(True)

        self.AccNode.setFont(font)
        self.AccPlanet.setFont(font)
        self.AccName.setFont(font)

        self.AccHBox1 = QtWidgets.QHBoxLayout()
        self.AccHBox2 = QtWidgets.QHBoxLayout()
        self.AccHBox3 = QtWidgets.QHBoxLayout()
        self.AccHBox4 = QtWidgets.QHBoxLayout()
        self.AccVBox = QtWidgets.QVBoxLayout()

        self.AccBox = QtWidgets.QHBoxLayout()

        self.AccHBox1.addWidget(self.AccName)

        self.AccHBox2.addWidget(self.AccLevel)
        self.AccHBox2.addWidget(self.AccNode)
        self.AccHBox2.addWidget(self.AccMis)

        self.AccHBox3.addWidget(self.AccTime)
        self.AccHBox3.addWidget(self.AccFound)
        self.AccHBox3.addWidget(self.AccFlee)

        self.AccHBox4.addWidget(self.AccPer)

        self.AccVBox.addLayout(self.AccHBox1)
        self.AccVBox.addLayout(self.AccHBox2)
        self.AccVBox.addLayout(self.AccHBox3)
        self.AccVBox.addLayout(self.AccHBox4)

        self.AccBox.addWidget(self.AccImg.image)
        self.AccBox.addLayout(self.AccVBox)

    def set_acc_data(self, name: str, level: float, icon: str, flee: float, ticket: str, loc_tag: str) -> None:
        self.AccName.setText(name)
        self.AccName.setToolTip(translate("acolyte", "inGameName") + " : " + loc_tag)
        self.AccLevel.setText(translate("acolyte", "level") + " : " + str(level))
        self.AccFlee.setText(translate("acolyte", "damageFlee") + " : " + str(flee))
        self.AccNode.setToolTip(translate("acolyte", "useTicket?") + " " + ticket)
        self.set_acc_image(icon)

    def set_acc_position(self, per: float, time: str, discovered: str, node: str, planet: str, region: str) -> None:
        change_detected = 0
        self.AccTime.setText(translate("acolyte", "init") + " " + time)
        self.AccPer.reset()
        self.acc_health = per
        if (per <= 0):
            self.AccPer.setValue(0)
            self.AccPer.setToolTip(str(0) + "%")
        else:
            self.AccPer.setValue(int(per * 100))
            self.AccPer.setToolTip(str(per * 100) + "%")
        old_found_node = self.AccFound.text()
        self.AccFound.setText(translate("acolyte", "found?") + " " + discovered)
        if (old_found_node != "N/D" and old_found_node != self.AccFound.text()):
            change_detected = 1
        old_found_node = self.AccNode.text()
        if (discovered == translate("commonUtils", "no")):
            if (region != translate("acolyteWidgetTab", "noRegion")):
                self.AccNode.setText(translate("acolyte", "founded") + " " + region)
            else:
                self.AccNode.setText(translate("acolyte", "positionUnknown"))
                self.AccMis.setText("")
        else:
            self.AccNode.setText(node + " " + planet)
            if (planet == ""):
                self.AccMis.setText("")
            else:
                self.AccMis.setText(get_mission_from_starchart(node, planet))
        if (old_found_node != "N/D" and old_found_node != self.AccNode.text()):
            change_detected = 1
        if (change_detected):

            NotificationService.send_notification(
                self.get_title(),
                self.to_string(),
                create_pixmap(self.acc_image))

    def set_acc_image(self, url_image: str) -> None:
        image_name = "assets" + get_separator() + "image" + get_separator() + get_last_item_with_backslash(url_image)
        self.AccImg.set_image(image_name)
        self.AccImg.set_image_dimension(120, 120, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.acc_image = image_name

    def get_acc_id(self) -> str:
        return self.acc_id

    def is_dead(self) -> bool:
        return self.acc_health <= 0

    def get_title(self) -> str:
        return self.AccName.text()

    def to_string(self) -> str:
        if (self.is_dead()):
            return translate("acolyte", "acolyteDead")
        else:
            text = self.AccNode.text() + " " + self.AccMis.text() + "\n"
            text += translate("acolyte", "health") + ": " + str(self.AccPer.value()) + "%"
            return text

    def get_image(self) -> str:
        return self.acc_image

    def hide(self) -> None:
        self.AccImg.hide()
        self.AccName.hide()
        self.AccLevel.hide()
        self.AccNode.hide()
        self.AccMis.hide()
        self.AccTime.hide()
        self.AccFound.hide()
        self.AccPer.hide()
        self.AccFlee.hide()
