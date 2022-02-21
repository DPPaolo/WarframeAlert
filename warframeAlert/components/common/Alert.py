# coding=utf-8
from PyQt6 import QtGui, QtWidgets, QtCore

from warframeAlert.components.common.CommonImages import CommonImages
from warframeAlert.components.common.Countdown import Countdown
from warframeAlert.components.common.EmptySpace import EmptySpace
from warframeAlert.constants.files import DEFAULT_ALERT_IMAGE, IMAGE_NAME
from warframeAlert.services.translationService import translate
from warframeAlert.utils import timeUtils
from warframeAlert.utils.commonUtils import get_last_item_with_backslash
from warframeAlert.utils.fileUtils import get_separator, check_assets_file
from warframeAlert.utils.logUtils import LogHandler, LOG_FILE


class Alert():

    def __init__(self, alert_id: str) -> None:
        self.alert_id = alert_id
        self.image = None
        self.HIDE = self.check_id()

        self.Font = QtGui.QFont()
        self.Font.setBold(True)
        self.AlertImg = CommonImages()
        self.AlertNode = QtWidgets.QLabel("N/D")
        self.AlertPlanet = QtWidgets.QLabel("N/D")
        self.AlertLevel = QtWidgets.QLabel(translate("alert", "level") + ": N/D")
        self.AlertMis = QtWidgets.QLabel("N/D")
        self.AlertWave = QtWidgets.QLabel("")
        self.AlertFaction = QtWidgets.QLabel("N/D")
        self.AlertRewLab = QtWidgets.QLabel(translate("alert", "reward") + ": ")
        self.AlertRew = QtWidgets.QLabel("N/D")
        self.AlertSpace = QtWidgets.QLabel("")
        self.AlertLoc = QtWidgets.QLabel("N/D")
        self.AlertTime = Countdown()
        self.AlertHide = QtWidgets.QCheckBox(translate("alert", "hide"))

        self.AlertNode.setFont(self.Font)
        self.AlertPlanet.setFont(self.Font)
        self.AlertMis.setFont(self.Font)
        self.AlertFaction.setFont(self.Font)
        self.AlertRew.setFont(self.Font)

        self.AlertHBox0 = QtWidgets.QHBoxLayout()
        self.AlertHBox1 = QtWidgets.QHBoxLayout()
        self.AlertHBox2 = QtWidgets.QHBoxLayout()
        self.AlertHBox3 = QtWidgets.QHBoxLayout()
        self.AlertHBox4 = QtWidgets.QHBoxLayout()
        self.AlertHBox5 = QtWidgets.QHBoxLayout()
        self.AlertVBox = QtWidgets.QVBoxLayout()

        self.AlertBox = QtWidgets.QHBoxLayout()

        self.AlertHBox1.addStretch(1)
        self.AlertHBox1.addWidget(self.AlertHide)

        self.AlertHBox2.addWidget(self.AlertNode)
        self.AlertHBox2.addWidget(self.AlertPlanet)
        self.AlertHBox2.addStretch(1)
        self.AlertHBox2.addWidget(self.AlertLevel)
        self.AlertHBox2.addStretch(1)
        self.AlertHBox2.addWidget(self.AlertTime.TimeLab)

        self.AlertHBox3.addWidget(self.AlertMis)
        self.AlertHBox3.addWidget(self.AlertFaction)
        self.AlertHBox3.addStretch(1)
        self.AlertHBox3.addWidget(self.AlertWave)
        self.AlertHBox3.addStretch(1)
        self.AlertHBox3.addWidget(self.AlertLoc)

        self.AlertHBox4.addWidget(self.AlertRewLab)
        self.AlertHBox4.addWidget(self.AlertRew)
        self.AlertHBox4.addWidget(self.AlertSpace)

        self.AlertVBox.addLayout(self.AlertHBox0)
        self.AlertVBox.addLayout(self.AlertHBox1)
        self.AlertVBox.addLayout(self.AlertHBox2)
        self.AlertVBox.addLayout(self.AlertHBox3)
        self.AlertVBox.addLayout(self.AlertHBox4)
        self.AlertVBox.addLayout(self.AlertHBox5)
        self.AlertVBox.addLayout(EmptySpace().SpaceBox)

        self.AlertBox.addWidget(self.AlertImg.image)
        self.AlertBox.addLayout(self.AlertVBox)

        self.AlertTime.TimeOut.connect(self.hide)
        self.AlertHide.clicked.connect(self.hide_alert_data)

    def set_alert_data(self, node: str, planet: str, level: str, mis: str, faction: str,
                       item: str, wave: str, loc: str) -> None:
        self.AlertNode.setText(node)
        self.AlertPlanet.setText(planet)
        self.AlertLevel.setText(translate("alert", "level") + ": " + level)
        self.AlertMis.setText(mis)
        self.AlertFaction.setText(faction)
        self.AlertRew.setText(item)
        self.AlertWave.setText(wave)
        self.AlertLoc.setText(translate("alert", "map") + ": " + loc)

    def set_alert_extra_data(self, difficulty, enemy_spec, extra_enemy_spec) -> None:
        self.AlertLevel.setToolTip(translate("alert", "difficulty") + ": " + str(difficulty))
        self.AlertLoc.setToolTip(translate("alert", "enemy_type") + ": " + get_last_item_with_backslash(enemy_spec))
        if (extra_enemy_spec != ""):
            self.AlertLoc.setToolTip(self.AlertLoc.text() + "\n" +
                                     translate("alert", "extra_enemy_type") + ": " +
                                     get_last_item_with_backslash(extra_enemy_spec))

    def get_title(self) -> str:
        return self.AlertNode.text() + " " + self.AlertPlanet.text()

    def to_string(self) -> str:
        text = self.AlertMis.text() + " " + self.AlertFaction.text() + " " + self.AlertLevel.text()
        text += "\n" + self.AlertRew.text()
        return text

    def set_alert_time(self, end: int, start: int) -> None:
        self.AlertTime.set_countdown(end[:10])
        self.AlertTime.start()
        self.AlertTime.set_tooltip(translate("alert", "init") + ": " + timeUtils.get_time(start[:10]))

    def set_alert_time_name(self, name: str) -> None:
        self.AlertTime.set_name(name)

    def set_alert_unlock(self, unlock: str) -> None:
        self.AlertNode.setToolTip(translate("alert", "unlock") + ":" + unlock)

    def hide_alert_data(self) -> None:
        self.hide()
        LogHandler.debug(translate("alert", "hidedAlert") + ":" + str(self.alert_id))

    def check_id(self) -> bool:
        try:
            fp = open(LOG_FILE)
            data = fp.readlines()
        except FileNotFoundError:
            return False
        fp.close()
        for line in data:
            if (self.alert_id in line):
                return True
        return False

    def get_alert_id(self) -> str:
        return self.alert_id

    def get_image(self) -> str:
        return self.image

    def get_reward(self) -> str:
        return self.AlertRew.text()

    def is_expired(self) -> bool:
        return (int(self.AlertTime.get_time()) - int(timeUtils.get_local_time())) < 0

    def is_hidden(self) -> bool:
        return self.HIDE

    def hide(self) -> None:
        self.AlertImg.hide()
        self.AlertNode.hide()
        self.AlertPlanet.hide()
        self.AlertLevel.hide()
        self.AlertMis.hide()
        self.AlertFaction.hide()
        self.AlertRew.hide()
        self.AlertRewLab.hide()
        self.AlertWave.hide()
        self.AlertTime.hide()
        self.AlertLoc.hide()
        self.AlertSpace.hide()
        self.AlertHide.hide()

    def set_alert_image(self, url_image: str, item: str) -> None:
        if (item in IMAGE_NAME):
            img = IMAGE_NAME[item]
        elif ("Endo" in item):
            img = "EndoIconRenderLarge.png"
        elif ("Riven" in item):
            img = "OmegaMod.png"
        else:
            if (url_image):
                img = url_image
            else:
                img = item
        image_name = "assets" + get_separator() + "image" + get_separator() + get_last_item_with_backslash(img)
        if (not check_assets_file(get_last_item_with_backslash(img))):
            self.set_default_alert_image()
            LogHandler.debug(translate("alert", "alertImgNotFound") + ": " + image_name)
        else:
            self.AlertImg.set_image(image_name)
            self.AlertImg.set_image_dimension(80, 80, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
            self.image = image_name

    def set_default_alert_image(self) -> None:
        image_name = "assets" + get_separator() + "image" + get_separator() + DEFAULT_ALERT_IMAGE
        self.AlertImg.set_image(image_name)
        self.AlertImg.set_image_dimension(80, 80, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.image = image_name
