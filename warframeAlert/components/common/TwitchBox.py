# coding=utf-8
from typing import List

from PyQt6 import QtGui, QtWidgets, QtCore

from warframeAlert.components.common.Countdown import Countdown
from warframeAlert.services.translationService import translate
from warframeAlert.utils import timeUtils
from warframeAlert.utils.gameTranslationUtils import get_enemy_name
from warframeAlert.utils.logUtils import LogHandler
from warframeAlert.utils.stringUtils import divide_for_n


class TwitchBox:

    def __init__(self) -> None:
        font = QtGui.QFont()
        font.setBold(True)

        self.TwitchInit = QtWidgets.QLabel(translate("twitchBox", "init") + ": N/D")
        self.TwitchEnd = Countdown(translate("twitchBox", "countdown_label"))
        self.TwitchType = QtWidgets.QLabel(translate("twitchBox", "promo_type") + " N/D")

        self.TwitchType.setFont(font)
        self.TwitchType.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        twitchBox = QtWidgets.QHBoxLayout()

        self.TwitchBox = QtWidgets.QVBoxLayout()

        twitchBox.addWidget(self.TwitchInit)
        twitchBox.addWidget(self.TwitchEnd.TimeLab)

        self.TwitchBox.addLayout(twitchBox)
        self.TwitchBox.addWidget(self.TwitchType)

        self.TwitchEnd.TimeOut.connect(self.hide)

    def set_twitch_data(self, init: str, end: int, twitch_type: str, agent_type: List[str], spawn: int,
                        cooldown: int, achievement: str, streamers: List[str]) -> None:
        self.TwitchEnd.set_countdown(end[:10])
        self.TwitchEnd.start()
        self.TwitchInit.setText(translate("twitchBox", "init") + ": " + init)
        if (streamers != []):
            streamers_ids = ""
            for stream in streamers:
                streamers_ids += stream + " "
            streamer_divided = divide_for_n(streamers_ids, 30, " ")
            streamers_ids = ""
            for stream in streamer_divided:
                streamers_ids += stream + "\n"
            self.TwitchType.setToolTip(translate("twitchBox", "streamer") + ": " + streamers_ids)
        if (twitch_type == 'SpecificAchievement'):
            self.TwitchType.setText(translate("twitchBox", "achievement") + ": " + achievement)
        elif (twitch_type == 'Cumulative'):
            self.TwitchType.setText(translate("twitchBox", "vision"))
        elif (twitch_type == 'MarkedEnemy'):
            enemy = ""
            for elem in agent_type:
                enemy += get_enemy_name(elem) + " "
            text = translate("twitchBox", "kill") + " " + enemy
            text += " ( " + translate("twitchBox", "spawn") + " " + str(spawn)
            text += translate("twitchBox", "perc_spawn") + " " + str(cooldown) + "s)"
            self.TwitchType.setText(text)
        else:
            self.TwitchType.setText(translate("twitchBox", "unknown"))
            LogHandler.debug(translate("twitchBox", "unknown") + ": " + twitch_type)

    def is_expired(self) -> bool:
        return (int(self.TwitchEnd.get_time()) - int(timeUtils.get_local_time())) < 0

    def get_init(self) -> str:
        return self.TwitchInit.text().split(" ")[1]

    def hide(self) -> None:
        self.TwitchInit.hide()
        self.TwitchEnd.hide()
        self.TwitchType.hide()
