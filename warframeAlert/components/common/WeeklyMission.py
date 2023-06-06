# coding=utf-8
from enum import Enum

from PyQt6 import QtGui, QtWidgets, QtCore

from warframeAlert.components.common.CommonImages import CommonImages
from warframeAlert.components.common.EmptySpace import EmptySpace
from warframeAlert.constants.files import DEFAULT_ALERT_IMAGE
from warframeAlert.services.translationService import translate
from warframeAlert.utils.fileUtils import get_separator, check_assets_file
from warframeAlert.utils.gameTranslationUtils import get_weekly_mission_desc, get_node
from warframeAlert.utils.logUtils import LogHandler


class WeeklyMissionType(Enum):
    MAROO = 0,
    CLEM = 1


class WeeklyMission():

    def __init__(self, mission_type: WeeklyMissionType) -> None:
        self.image = None

        self.Font = QtGui.QFont()
        self.Font.setBold(True)

        self.MissionImg = CommonImages()

        self.MissionTitle = QtWidgets.QLabel("N/D")
        self.MissionLocation = QtWidgets.QLabel("N/D")
        self.AlertRew = QtWidgets.QLabel("N/D")

        self.MissionTitle.setFont(self.Font)
        self.MissionLocation.setFont(self.Font)
        self.AlertRew.setFont(self.Font)

        self.MissionVBox = QtWidgets.QVBoxLayout()
        self.MissionBox = QtWidgets.QHBoxLayout()

        self.MissionVBox.addWidget(self.MissionTitle)
        self.MissionVBox.addWidget(self.MissionLocation)
        self.MissionVBox.addWidget(self.AlertRew)
        self.MissionVBox.addLayout(EmptySpace().SpaceBox)

        self.MissionBox.addWidget(self.MissionImg.image)
        self.MissionBox.addLayout(self.MissionVBox)

        self.add_info(mission_type)

    def add_info(self, mission_type: WeeklyMissionType) -> None:
        mission_desc = get_weekly_mission_desc(mission_type.name)
        image = "???"
        match mission_type:
            case WeeklyMissionType.MAROO:
                image = "Maroo"
            case WeeklyMissionType.CLEM:
                image = "Clem"

        self.set_mission_data(mission_desc[0], mission_desc[1], mission_desc[2])
        self.set_mission_image(image)

    def set_mission_data(self, mission_title: str, mission_location: str, mission_rewards: str) -> None:
        self.MissionTitle.setText(mission_title)
        node, planet = get_node(mission_location)
        self.MissionLocation.setText(node + " " + planet)
        self.AlertRew.setText(mission_rewards)

    def set_mission_image(self, image_name: str) -> None:
        image_path = "assets" + get_separator() + "image" + get_separator() + image_name

        if (not check_assets_file(image_name)):
            self.set_default_mission_image()
            LogHandler.debug(translate("alert", "alertImgNotFound") + ": " + image_name)
        else:
            self.MissionImg.set_image(image_path)
            self.MissionImg.set_image_dimension(80, 80, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
            self.image = image_path

    def set_default_mission_image(self) -> None:
        image_name = "assets" + get_separator() + "image" + get_separator() + DEFAULT_ALERT_IMAGE
        self.MissionImg.set_image(image_name)
        self.MissionImg.set_image_dimension(80, 80, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.image = image_name
