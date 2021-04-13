# coding=utf-8
from PyQt5 import QtWidgets, QtGui

from warframeAlert.components.common.Countdown import Countdown
from warframeAlert.constants.pvp import PVP_MISSION_POINT
from warframeAlert.services.translationService import translate
from warframeAlert.utils import timeUtils
from warframeAlert.utils.gameTranslationUtils import get_pvp_mission_type


class PvPMissionBox():

    def __init__(self, pvp_id, generated):
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

        self.PvPMissionbox = QtWidgets.QHBoxLayout()
        self.PvPMissionBox = QtWidgets.QVBoxLayout()

        self.PvPMissionbox.addWidget(self.PvPMissionName)
        self.PvPMissionbox.addWidget(self.PvPMissionPoint)
        self.PvPMissionbox.addWidget(self.PvPMissionType)

        self.PvPMissionBox.addLayout(self.PvPMissionbox)
        self.PvPMissionBox.addWidget(self.PvPMissionDesc)

    def set_pvp_data(self, name, desc, mission, diff, time, sub_challenge):
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
            print(translate("pvpMissionBox", "subChallengPresents") + ": " + sub_challenge)

    def get_pvp_id(self):
        return self.pvp_id

    def is_expired(self):
        return (int(self.PvPTime.get_time()) - int(timeUtils.get_local_time())) < 0

    def hide(self):
        self.PvPMissionName.hide()
        self.PvPMissionDesc.hide()
        self.PvPMissionType.hide()
        self.PvPMissionPoint.hide()
        self.PvPTime.hide()
