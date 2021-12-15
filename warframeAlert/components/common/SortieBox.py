# coding=utf-8
from typing import List

from PyQt6 import QtWidgets, QtGui

from warframeAlert.components.common.Countdown import Countdown
from warframeAlert.components.common.EmptySpace import EmptySpace
from warframeAlert.components.common.SortieMissionBox import SortieMissionBox
from warframeAlert.components.common.SortieMissionDropView import SortieMissionDropView
from warframeAlert.components.common.Spoiler import Spoiler
from warframeAlert.services.notificationService import NotificationService
from warframeAlert.services.translationService import translate
from warframeAlert.utils import timeUtils
from warframeAlert.utils.gameTranslationUtils import get_sortie_boss
from warframeAlert.utils.logUtils import LogHandler
from warframeAlert.utils.warframeUtils import get_reward_from_sortie


class SortieBox():
    def __init__(self) -> None:
        self.Font = QtGui.QFont()
        self.Font.setBold(True)

        self.SortieTitle = QtWidgets.QLabel("")
        self.SortieInit = QtWidgets.QLabel("N/D")
        self.SortieEnd = Countdown(translate("sortieBox", "end") + ": ")
        self.SortieBoss = QtWidgets.QLabel("N/D")

        self.SortieBox1 = SortieMissionBox(1)
        self.SortieBox2 = SortieMissionBox(2)
        self.SortieBox3 = SortieMissionBox(3)

        self.SortieBoss.setFont(self.Font)

        self.SortieBoxData = QtWidgets.QHBoxLayout()

        self.SortieBoxData.addWidget(self.SortieInit)
        self.SortieBoxData.addWidget(self.SortieEnd.TimeLab)
        self.SortieBoxData.addWidget(self.SortieBoss)

        self.SortieBox = QtWidgets.QVBoxLayout()

        self.SortieBox.addLayout(self.SortieBoxData)
        self.SortieBox.addLayout(EmptySpace().SpaceBox)
        self.SortieBox.addLayout(self.SortieBox1.SortieMissionBox)
        self.SortieBox.addLayout(EmptySpace().SpaceBox)
        self.SortieBox.addLayout(self.SortieBox2.SortieMissionBox)
        self.SortieBox.addLayout(EmptySpace().SpaceBox)
        self.SortieBox.addLayout(self.SortieBox3.SortieMissionBox)
        self.SortieBox.addLayout(EmptySpace().SpaceBox)

        self.SortieReward = SortieMissionDropView()

        self.spoiler = Spoiler(translate("sortieBox", "reward"))

        sortie_reward = get_reward_from_sortie()
        self.SortieReward.set_drop(sortie_reward)
        self.spoiler.set_content_layout(self.SortieReward.DropBox)

        self.SortieBox.addWidget(self.spoiler)
        self.SortieBox.addStretch(1)

    def set_sortie_data(self, init: int, end: int, boss: str, reward: str, extra_reward: List[str]) -> None:
        self.SortieBoss.setText(translate("sortieBox", "boss") + ": " + get_sortie_boss(boss))
        self.SortieInit.setText(translate("sortieBox", "init") + ": " + timeUtils.get_time(init))
        self.SortieEnd.set_countdown(end)
        self.SortieEnd.start()
        if (reward != "/Lotus/Types/Game/MissionDecks/SortieRewards"):
            LogHandler.debug(translate("sortieBox", "newSortieRewards"))
            LogHandler.debug("/Lotus/Types/Game/MissionDecks/SortieRewards -> " + reward)
        if (len(extra_reward) > 0):
            sortie_reward = []
            for extra_rew in extra_reward:
                sortie_reward.append(extra_rew)
            self.SortieReward.set_drop(sortie_reward)
            self.spoiler.set_content_layout(self.SortieReward.DropBox)

        NotificationService.send_notification(
            translate("sortieBox", "sortie") + ": " + get_sortie_boss(boss),
            self.SortieBox1.to_string() + "\n" +
            self.SortieBox3.to_string() + "\n" +
            self.SortieBox1.to_string() + "\n",
            None)

    def set_mission_data(self, num: int, mission: str, modifier: str, node: str, planet: str, tileset: str) -> None:
        if (num == 1):
            self.SortieBox1.set_mission_data(mission, modifier, node, planet, tileset)
        elif (num == 2):
            self.SortieBox2.set_mission_data(mission, modifier, node, planet, tileset)
        elif (num == 3):
            self.SortieBox3.set_mission_data(mission, modifier, node, planet, tileset)

    def sortie_not_available(self) -> None:
        self.SortieInit.setText(translate("sortieBox", "init") + ": N/D")
        end = (int(timeUtils.get_local_time()) - 1) * 1000
        self.SortieEnd.set_countdown(end[:10])
        self.SortieEnd.start()
        self.SortieBoss.setText(translate("sortieBox", "boss") + ": " + translate("sortieBox", "noBoss"))

        self.SortieBox1.sortie_not_available()
        self.SortieBox2.sortie_not_available()
        self.SortieBox3.sortie_not_available()
