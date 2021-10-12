# coding=utf-8
from enum import Enum
from typing import List

from PyQt6 import QtWidgets, QtCore, QtGui

from warframeAlert.components.common.CommonImages import CommonImages
from warframeAlert.components.common.Countdown import Countdown
from warframeAlert.constants.files import UPDATE_SITE
from warframeAlert.services.translationService import translate
from warframeAlert.utils import timeUtils
from warframeAlert.utils.commonUtils import get_last_item_with_backslash
from warframeAlert.utils.fileUtils import get_separator
from warframeAlert.utils.gameTranslationUtils import get_item_name_en


class EventType(Enum):
    GENERAL = 0
    FOMORIAN = 1
    GHOUL = 2
    RECOSTRUCTION = 3
    SQUAD_LINK = 4


class Event():

    def __init__(self, event_id: str) -> None:
        self.event_id = event_id
        self.icon = ""
        self.event_type = EventType.GENERAL

        self.EventNameLab = QtWidgets.QLabel(translate("event", "event") + ":")
        self.EventName = QtWidgets.QLabel("N/D")
        self.EventStrLab = QtWidgets.QLabel(translate("event", "stratosEmblem") + ":")
        self.EventStr = QtWidgets.QLabel("No")
        self.EventInitLab = QtWidgets.QLabel(translate("event", "init"))
        self.EventInit = QtWidgets.QLabel("N/D")
        self.EventEndLab = QtWidgets.QLabel(translate("event", "end"))
        self.EventEnd = Countdown()
        self.EventPerLab = QtWidgets.QLabel(translate("event", "personalScore") + ":")
        self.EventPer = QtWidgets.QLabel("N/D")
        self.EventScoreLab = QtWidgets.QLabel(translate("event", "scoreLocked") + ":")
        self.EventScore = QtWidgets.QLabel("No")
        self.EventRegionLab = QtWidgets.QLabel(translate("event", "planet") + ":")
        self.EventRegion = QtWidgets.QLabel("N/D")
        self.EventSuccessLab = QtWidgets.QLabel(translate("event", "eventCompleted") + ":")
        self.EventSuccess = QtWidgets.QLabel("N/D")
        self.EventFactionLab = QtWidgets.QLabel(translate("event", "faction") + ":")
        self.EventFaction = QtWidgets.QLabel("N/D")
        self.EventReqItemLab = QtWidgets.QLabel(translate("event", "requiredItem"))
        self.EventReqItem = QtWidgets.QLabel("N/D")
        self.EventRoamingVipLab = QtWidgets.QLabel(translate("event", "vip_agent") + ":")
        self.EventRoamingVip = QtWidgets.QLabel("N/D")
        self.EventReqMisLab = QtWidgets.QLabel(translate("event", "eventRequired") + ":")
        self.EventReqMis = QtWidgets.QLabel("N/D")

        self.EventImg = CommonImages()

        self.TAInfoBox = QtWidgets.QVBoxLayout()
        self.TABaseInfoBox = QtWidgets.QHBoxLayout()
        self.TADescVBox = QtWidgets.QVBoxLayout()
        self.TAEventBox = QtWidgets.QHBoxLayout()

        self.TADescBox1 = QtWidgets.QHBoxLayout()
        self.TADescBox2 = QtWidgets.QHBoxLayout()
        self.TADescBox3 = QtWidgets.QHBoxLayout()
        self.TADescBox4 = QtWidgets.QHBoxLayout()
        self.TADescBox5 = QtWidgets.QHBoxLayout()

        self.TADescBox1.addWidget(self.EventNameLab)
        self.TADescBox1.addWidget(self.EventName)
        self.TADescBox1.addWidget(self.EventStrLab)
        self.TADescBox1.addWidget(self.EventStr)

        self.TADescBox2.addWidget(self.EventInitLab)
        self.TADescBox2.addWidget(self.EventInit)
        self.TADescBox2.addWidget(self.EventEndLab)
        self.TADescBox2.addWidget(self.EventEnd.TimeLab)

        self.TADescBox3.addWidget(self.EventPerLab)
        self.TADescBox3.addWidget(self.EventPer)
        self.TADescBox3.addWidget(self.EventScoreLab)
        self.TADescBox3.addWidget(self.EventScore)

        self.TADescBox4.addWidget(self.EventRegionLab)
        self.TADescBox4.addWidget(self.EventRegion)
        self.TADescBox4.addWidget(self.EventSuccessLab)
        self.TADescBox4.addWidget(self.EventSuccess)
        self.TADescBox4.addWidget(self.EventFactionLab)
        self.TADescBox4.addWidget(self.EventFaction)

        self.TADescBox5.addWidget(self.EventReqItemLab)
        self.TADescBox5.addWidget(self.EventReqItem)
        self.TADescBox5.addWidget(self.EventRoamingVipLab)
        self.TADescBox5.addWidget(self.EventRoamingVip)
        self.TADescBox5.addWidget(self.EventReqMisLab)
        self.TADescBox5.addWidget(self.EventReqMis)

        self.TAInfoBox.addStretch()
        self.TAInfoBox.addLayout(self.TADescBox1)
        self.TAInfoBox.addLayout(self.TADescBox2)
        self.TAInfoBox.addLayout(self.TADescBox3)
        self.TAInfoBox.addLayout(self.TADescBox4)
        self.TAInfoBox.addLayout(self.TADescBox5)
        self.TAInfoBox.addStretch()

        self.TABaseInfoBox.addWidget(self.EventImg.image)
        self.TABaseInfoBox.addLayout(self.TAInfoBox, 2)

        self.TADescVBox.addLayout(self.TABaseInfoBox)

        self.TAEventBox.addLayout(self.TADescVBox)

    def add_event_object(self, layout: QtWidgets) -> None:
        self.TADescVBox.addLayout(layout)

    def add_event_widget(self, layout: QtWidgets) -> None:
        self.TADescVBox.addWidget(layout)

    def set_event_name(self, name: str, desc: str, tooltip: str, icon: str, stratos_present: bool) -> None:
        if (icon != ""):
            image_name = "images" + get_separator() + get_last_item_with_backslash(icon)
            self.EventImg.set_image(image_name, UPDATE_SITE + "images/" + get_last_item_with_backslash(icon))
            self.EventImg.set_image_dimension(80, 80, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
            self.icon = image_name
        elif (stratos_present):
            image_name = "images" + get_separator() + "StratosEmblem.png"
            self.EventImg.set_image(image_name, UPDATE_SITE + "images/StratosEmblem.png")
            self.EventImg.set_image_dimension(80, 80, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
            self.icon = image_name
        elif (name == "HeatFissure"):
            image_name = "images" + get_separator() + "ThermiaFractureEmblem.png"
            self.EventImg.set_image(image_name, UPDATE_SITE + "images/ThermiaFractureEmblem.png")
            self.EventImg.set_image_dimension(80, 80, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
            self.icon = image_name
        else:
            self.EventImg.hide()

        event_name = desc or name or tooltip
        if (event_name == ""):
            self.EventName.setText("????")
        else:
            self.EventName.setText(event_name)

    def set_event_info(self, init: str, end: int, count: int, personal: str, score: str,
                       emblem: str, transmission: str, community: str) -> None:
        self.EventInit.setText(init)
        self.EventEnd.set_countdown(end[:10])
        self.EventEnd.start()
        name_tooltip = translate("event", "numEvent") + " " + str(count+1)
        if (transmission != ""):
            name_tooltip += "\n" + translate("event", "transmission") + ": " + transmission
        if (community):
            name_tooltip += "\n" + translate("event", "community") + ": " + community
        self.EventNameLab.setToolTip(name_tooltip)
        self.EventName.setToolTip(name_tooltip)
        self.EventPer.setText(personal)
        self.EventStr.setText(emblem)
        self.EventScore.setText(score)

    def set_optional_field(self, regions: str, success: str, faction: str,
                           item_required: str, roaming_vip: str, req_mis: List[str]) -> None:
        if (regions == ""):
            self.EventRegionLab.hide()
            self.EventRegion.hide()
        else:
            self.EventRegion.setText(regions)
        if (success == ""):
            self.EventSuccessLab.hide()
            self.EventSuccess.hide()
        else:
            self.EventSuccess.setText(success)
        if (faction == ""):
            self.EventFactionLab.hide()
            self.EventFaction.hide()
        else:
            self.EventFaction.setText(faction)
        if (item_required == ""):
            self.EventReqItemLab.hide()
            self.EventReqItem.hide()
        else:
            self.EventReqItem.setText(get_item_name_en(item_required))
        if (roaming_vip == ""):
            self.EventRoamingVipLab.hide()
            self.EventRoamingVip.hide()
        else:
            self.EventRoamingVip.setText(roaming_vip)
        if (req_mis == []):
            self.EventReqMisLab.hide()
            self.EventReqMis.hide()
        else:
            req_mission = ""
            for mission in req_mis:
                req_mission += mission + " "
                self.EventReqMis.setText(req_mission)

    def get_event_id(self) -> str:
        return self.event_id

    def set_event_type(self, event_type: EventType):
        self.event_type = event_type

    def get_event_type(self) -> EventType:
        return self.event_type

    def get_faction(self) -> str:
        return self.EventFactionLab.text()

    def is_expired(self) -> bool:
        return (int(self.EventEnd.get_time()) - int(timeUtils.get_local_time())) < 0

    def get_title(self) -> str:
        return self.EventName.text()

    def get_image(self) -> QtGui.QPixmap:
        return self.EventImg.pixmap

    def hide(self) -> None:
        self.EventNameLab.hide()
        self.EventName.hide()
        self.EventStrLab.hide()
        self.EventStr.hide()
        self.EventInitLab.hide()
        self.EventInit.hide()
        self.EventEndLab.hide()
        self.EventEnd.hide()
        self.EventScoreLab.hide()
        self.EventScore.hide()
        self.EventPerLab.hide()
        self.EventPer.hide()
        self.EventRegionLab.hide()
        self.EventRegion.hide()
        self.EventSuccessLab.hide()
        self.EventSuccess.hide()
        self.EventFactionLab.hide()
        self.EventFactionLab.hide()
        self.EventReqItemLab.hide()
        self.EventReqItem.hide()
        self.EventRoamingVipLab.hide()
        self.EventRoamingVip.hide()
        self.EventReqMisLab.hide()
        self.EventReqMis.hide()
