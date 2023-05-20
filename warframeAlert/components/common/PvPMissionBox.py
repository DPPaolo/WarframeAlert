# coding=utf-8
from typing import List

from PyQt6 import QtWidgets, QtGui

from warframeAlert.components.common.Countdown import Countdown
from warframeAlert.constants.pvp import PVP_MISSION_POINT
from warframeAlert.services.translationService import translate
from warframeAlert.utils import timeUtils
from warframeAlert.utils.gameTranslationUtils import get_pvp_mission_type


class PvPMissionBox():

    def __init__(self, pvp_id: str, generated: bool) -> None:
        self.Font = QtGui.QFont()
        self.Font.setBold(True)
        self.pvp_id = pvp_id
        self.generated = generated
        self.PvPMissionName = QtWidgets.QLabel("N/D")
        self.PvPMissionDesc = QtWidgets.QLabel("N/D")
        self.PvPMissionType = QtWidgets.QLabel("N/D")
        self.PvPMissionPoint = QtWidgets.QLabel("")
        self.PvPTime = Countdown()

        self.PvPMissionName.setFont(self.Font)
        self.PvPMissionType.setFont(self.Font)

        self.PvPMissionBox = QtWidgets.QHBoxLayout()
        self.PvPMissionBox = QtWidgets.QVBoxLayout()

        self.PvPMissionBox.addWidget(self.PvPMissionName)
        self.PvPMissionBox.addWidget(self.PvPMissionPoint)
        self.PvPMissionBox.addWidget(self.PvPMissionType)

        self.PvPMissionBox.addLayout(self.PvPMissionBox)
        self.PvPMissionBox.addWidget(self.PvPMissionDesc)

    def set_pvp_data(self, name: str, desc: str, mission: str, diff: int, time: int, sub_challenge: List[str]) -> None:
        if (diff == 2):
            name += " " + translate("pvpMissionBox", "hardMission")
        self.PvPMissionName.setText(name)
        self.PvPMissionDesc.setText(desc)
        self.PvPMissionType.setText(mission)
        if (mission == get_pvp_mission_type("PVPMODE_ALL")):
            self.PvPMissionPoint.setText("")
        elif (diff == -1):
            self.PvPMissionPoint.setText(get_pvp_mission_type("PVPChallengeTypeCategory_POWERUP"))
        elif (mission == get_pvp_mission_type("PVPMODE_SPEEDBALL")):
            self.PvPMissionPoint.setText(str(PVP_MISSION_POINT[diff] * 2) + " " + translate("pvpMissionBox", "points"))
        else:
            self.PvPMissionPoint.setText(str(PVP_MISSION_POINT[diff]) + " " + translate("pvpMissionBox", "points"))
        self.PvPTime.set_countdown(time[:10])
        self.PvPTime.start()

        if (sub_challenge != []):
            print(translate("pvpMissionBox", "subChallengePresents") + ": " + str(sub_challenge))

    def get_pvp_id(self) -> str:
        return self.pvp_id

    def is_expired(self) -> bool:
        return (int(self.PvPTime.get_time()) - int(timeUtils.get_local_time())) < 0

    def hide(self) -> None:
        self.PvPMissionName.hide()
        self.PvPMissionDesc.hide()
        self.PvPMissionType.hide()
        self.PvPMissionPoint.hide()
        self.PvPTime.hide()
