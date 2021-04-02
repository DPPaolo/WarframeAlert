# coding=utf-8
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import Qt

from warframeAlert.components.common.CommonImages import CommonImages
from warframeAlert.components.common.Countdown import Countdown
from warframeAlert.components.common.EmptySpace import EmptySpace
from warframeAlert.constants.files import DEFAULT_SITE_IMAGE, DEFAULT_ALERT_IMAGE, IMAGE_NAME
from warframeAlert.services.translationService import translate
from warframeAlert.utils import timeUtils
from warframeAlert.utils.commonUtils import get_last_item_with_backslash
from warframeAlert.utils.fileUtils import get_separator
from warframeAlert.utils.logUtils import LogHandler, LOG_FILE
from warframeAlert.utils.warframeUtils import get_image_path_from_export_manifest


class Alert():

    def __init__(self, id_allerta):
        self.alert_id = id_allerta
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

        self.Alerthbox0 = QtWidgets.QHBoxLayout()
        self.Alerthbox1 = QtWidgets.QHBoxLayout()
        self.Alerthbox2 = QtWidgets.QHBoxLayout()
        self.Alerthbox3 = QtWidgets.QHBoxLayout()
        self.Alerthbox4 = QtWidgets.QHBoxLayout()
        self.Alerthbox5 = QtWidgets.QHBoxLayout()
        self.Alertvbox = QtWidgets.QVBoxLayout()

        self.AlertBox = QtWidgets.QHBoxLayout()

        self.Alerthbox1.addStretch(1)
        self.Alerthbox1.addWidget(self.AlertHide)

        self.Alerthbox2.addWidget(self.AlertNode)
        self.Alerthbox2.addWidget(self.AlertPlanet)
        self.Alerthbox2.addStretch(1)
        self.Alerthbox2.addWidget(self.AlertLevel)
        self.Alerthbox2.addStretch(1)
        self.Alerthbox2.addWidget(self.AlertTime.TimeLab)

        self.Alerthbox3.addWidget(self.AlertMis)
        self.Alerthbox3.addWidget(self.AlertFaction)
        self.Alerthbox3.addStretch(1)
        self.Alerthbox3.addWidget(self.AlertWave)
        self.Alerthbox3.addStretch(1)
        self.Alerthbox3.addWidget(self.AlertLoc)

        self.Alerthbox4.addWidget(self.AlertRewLab)
        self.Alerthbox4.addWidget(self.AlertRew)
        self.Alerthbox4.addWidget(self.AlertSpace)

        self.Alertvbox.addLayout(self.Alerthbox0)
        self.Alertvbox.addLayout(self.Alerthbox1)
        self.Alertvbox.addLayout(self.Alerthbox2)
        self.Alertvbox.addLayout(self.Alerthbox3)
        self.Alertvbox.addLayout(self.Alerthbox4)
        self.Alertvbox.addLayout(self.Alerthbox5)
        self.Alertvbox.addLayout(EmptySpace().SpaceBox)

        self.AlertBox.addWidget(self.AlertImg.image)
        self.AlertBox.addLayout(self.Alertvbox)

        self.AlertTime.TimeOut.connect(self.hide)
        self.AlertHide.clicked.connect(self.hide_alert_data)

    def set_alert_data(self, node, planet, level, mis, faction, item, wave, loc):
        self.AlertNode.setText(node)
        self.AlertPlanet.setText(planet)
        self.AlertLevel.setText(translate("alert", "level") + ": " + level)
        self.AlertMis.setText(mis)
        self.AlertFaction.setText(faction)
        self.AlertRew.setText(item)
        self.AlertWave.setText(wave)
        self.AlertLoc.setText(translate("alert", "map") + ": " + loc)

    def set_alert_extra_data(self, difficulty, enemy_spec, extra_enemy_spec):
        self.AlertLevel.setToolTip(translate("alert", "difficulty") + ": " + str(difficulty))
        self.AlertLoc.setToolTip(translate("alert", "enemy_type") + ": " + get_last_item_with_backslash(enemy_spec))
        if (extra_enemy_spec != ""):
            self.AlertLoc.setToolTip(self.AlertLoc.text() + "\n" +
                                     translate("alert", "extra_enemy_type") + ": " +
                                     get_last_item_with_backslash(extra_enemy_spec))

    def get_title(self):
        return self.AlertNode.text() + " " + self.AlertPlanet.text()

    def to_string(self):
        text = self.AlertMis.text() + " " + self.AlertFaction.text() + " " + self.AlertLevel.text()
        text += "\n" + self.AlertRew.text()
        return text

    def set_alert_time(self, end, start):
        self.AlertTime.set_countdown(end[:10])
        self.AlertTime.start()
        self.AlertTime.set_tooltip(translate("alert", "init") + ": " + timeUtils.get_time(start[:10]))

    def set_alert_time_name(self, name):
        self.AlertTime.set_name(name)

    def set_alert_unlock(self, unlock):
        self.AlertNode.setToolTip(translate("alert", "unlock") + ":" + unlock)

    def hide_alert_data(self):
        self.hide()
        LogHandler.debug(translate("alert", "hidedAlert") + ":" + str(self.alert_id))

    def check_id(self):
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

    def get_alert_id(self):
        return self.alert_id

    def get_image(self):
        return self.image

    def get_ricompensa(self):
        return self.AlertRew.text()

    def is_expired(self):
        return (int(self.AlertTime.get_time()) - int(timeUtils.get_local_time())) < 0

    def is_hided(self):
        return self.HIDE

    def hide(self):
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

    def set_alert_image(self, url_image, item):
        if (item in IMAGE_NAME):
            img = IMAGE_NAME[item]
        elif ("Endo" in item):
            img = "/Lotus/Interface/Icons/Store/EndoIconRenderLarge.png"
        elif ("Riven" in item):
            img = "/Lotus/Interface/Cards/Images/OmegaMod.png"
        else:
            if (url_image):
                img = get_image_path_from_export_manifest(url_image)
            else:
                img = item
        image_name = "images" + get_separator() + get_last_item_with_backslash(img)
        self.AlertImg.set_image(image_name, DEFAULT_SITE_IMAGE + img)
        self.AlertImg.set_image_dimension(80, 80, Qt.KeepAspectRatio)
        self.image = image_name

    def set_default_alert_image(self):
        image_name = "images" + get_separator() + get_last_item_with_backslash(DEFAULT_ALERT_IMAGE)
        self.AlertImg.set_image(image_name, DEFAULT_SITE_IMAGE + DEFAULT_ALERT_IMAGE)
        self.AlertImg.set_image_dimension(80, 80, Qt.KeepAspectRatio)
        self.image = image_name
