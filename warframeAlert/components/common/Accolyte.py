# coding=utf-8
from PyQt5 import QtWidgets, QtGui, QtCore

from warframeAlert.components.common.CommonImages import CommonImages
from warframeAlert.services.notificationService import NotificationService
from warframeAlert.services.translationService import translate
from warframeAlert.utils.commonUtils import get_last_item_with_backslash, create_pixmap
from warframeAlert.utils.fileUtils import get_separator, get_cur_dir
from warframeAlert.utils.gameTranslationUtils import get_mission_from_starchart


class Accolyte():

    def __init__(self, acc_id):
        self.acc_id = acc_id
        self.acc_health = 0
        self.acc_image = None

        self.AccImg = CommonImages()
        self.AccName = QtWidgets.QLabel("N/D")
        self.AccName.setAlignment(QtCore.Qt.AlignCenter)
        self.AccNode = QtWidgets.QLabel("N/D")
        self.AccPlanet = QtWidgets.QLabel("N/D")
        self.AccMis = QtWidgets.QLabel("N/D")
        self.AccLevel = QtWidgets.QLabel("N/D")
        self.AccTimeLabel = QtWidgets.QLabel(translate("accolyt", "init") + " ")
        self.AccTime = QtWidgets.QLabel("")
        self.AccFound = QtWidgets.QLabel("N/D")
        self.AccFlee = QtWidgets.QLabel("N/D")

        self.AccPer = QtWidgets.QProgressBar()

        font = QtGui.QFont()
        font.setBold(True)

        self.AccNode.setFont(font)
        self.AccPlanet.setFont(font)
        self.AccName.setFont(font)

        self.Acchbox1 = QtWidgets.QHBoxLayout()
        self.Acchbox2 = QtWidgets.QHBoxLayout()
        self.Acchbox3 = QtWidgets.QHBoxLayout()
        self.Acchbox4 = QtWidgets.QHBoxLayout()
        self.Accvbox = QtWidgets.QVBoxLayout()

        self.AccBox = QtWidgets.QHBoxLayout()

        self.Acchbox1.addWidget(self.AccName)

        self.Acchbox2.addWidget(self.AccLevel)
        self.Acchbox2.addWidget(self.AccNode)
        self.Acchbox2.addWidget(self.AccMis)

        self.Acchbox3.addWidget(self.AccTime)
        self.Acchbox3.addWidget(self.AccFound)
        self.Acchbox3.addWidget(self.AccFlee)

        self.Acchbox4.addWidget(self.AccPer)

        self.Accvbox.addLayout(self.Acchbox1)
        self.Accvbox.addLayout(self.Acchbox2)
        self.Accvbox.addLayout(self.Acchbox3)
        self.Accvbox.addLayout(self.Acchbox4)

        self.AccBox.addWidget(self.AccImg.image)
        self.AccBox.addLayout(self.Accvbox)

    def set_acc_data(self, name, level, icon, flee, ticket, loctag):
        self.AccName.setText(name)
        self.AccName.setToolTip(translate("accolyt", "inGameName") + " : " + loctag)
        self.AccLevel.setText(translate("accolyt", "level") + " : " + str(level))
        self.AccFlee.setText(translate("accolyt", "damageFlee") + " : " + str(flee))
        self.AccNode.setToolTip(translate("accolyt", "useTicket?") + " " + ticket)
        self.set_acc_image(icon)

    def set_acc_position(self, per, time, discoved, node, planet, region):
        change_detected = 0
        self.AccTime.setText(translate("accolyt", "init") + " " + time)
        self.AccPer.reset()
        self.acc_health = per
        if (per <= 0):
            self.AccPer.setValue(0)
            self.AccPer.setToolTip(str(0) + "%")
        else:
            self.AccPer.setValue(per * 100)
            self.AccPer.setToolTip(str(per * 100) + "%")
        old_found_node = self.AccFound.text()
        self.AccFound.setText(translate("accolyt", "found?") + " " + discoved)
        if (old_found_node != "N/D" and old_found_node != self.AccFound.text()):
            change_detected = 1
        old_found_node = self.AccNode.text()
        if (discoved == translate("commonUtils", "no")):
            if (region != translate("accolyteWidgetTab", "noRegion")):
                self.AccNode.setText(translate("accolyt", "founded") + " " + region)
            else:
                self.AccNode.setText(translate("accolyt", "positionUnknown"))
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

    def set_acc_image(self, url_image):
        image_name = "images" + get_separator() + get_last_item_with_backslash(url_image)
        self.AccImg.set_image(image_name)
        self.AccImg.set_image_dimension(120, 120, QtCore.Qt.KeepAspectRatio)
        self.acc_image = image_name

    def get_acc_id(self):
        return self.acc_id

    def is_dead(self):
        return self.acc_health <= 0

    def get_title(self):
        return self.AccName.text()

    def to_string(self):
        if (self.is_dead()):
            return translate("accolyt", "accolytDead")
        else:
            text = self.AccNode.text() + " " + self.AccMis.text() + "\n"
            text += translate("accolyt", "health") + ": " + str(self.AccPer.value()) + "%"
            return text

    def get_image(self):
        return self.acc_image

    def hide(self):
        self.AccImg.hide()
        self.AccName.hide()
        self.AccLevel.hide()
        self.AccNode.hide()
        self.AccMis.hide()
        self.AccTime.hide()
        self.AccFound.hide()
        self.AccPer.hide()
        self.AccFlee.hide()
