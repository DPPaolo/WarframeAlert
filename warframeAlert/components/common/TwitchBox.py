from PyQt5 import QtGui, QtWidgets, QtCore

from warframeAlert.components.common.Countdown import Countdown
from warframeAlert.services.translationService import translate
from warframeAlert.utils import timeUtils
from warframeAlert.utils.gameTranslationUtils import get_enemy_name


class TwitchBox:

    def __init__(self):
        font = QtGui.QFont()
        font.setBold(True)

        self.TwitchInit = QtWidgets.QLabel(translate("twitchBox", "init") + ": N/D")
        self.TwitchEnd = Countdown(translate("twitchBox", "countdown_label"))
        self.TwitchType = QtWidgets.QLabel(translate("twitchBox", "promo_type") + " N/D")
        self.TwitchStreamers = QtWidgets.QLabel(translate("twitchBox", "streamer") + " N/D")

        self.TwitchType.setFont(font)
        self.TwitchType.setAlignment(QtCore.Qt.AlignCenter)

        twitchbox = QtWidgets.QHBoxLayout()

        self.TwitchBox = QtWidgets.QVBoxLayout()

        twitchbox.addWidget(self.TwitchInit)
        twitchbox.addWidget(self.TwitchEnd.TimeLab)

        self.TwitchBox.addLayout(twitchbox)
        self.TwitchBox.addWidget(self.TwitchType)
        self.TwitchBox.addWidget(self.TwitchStreamers)

        self.TwitchEnd.TimeOut.connect(self.hide)

    def set_twitch_data(self, iniz, fin, twitch_type, agent_type, spawn, cooldown, achievement, streamers):
        self.TwitchEnd.set_countdown(fin[:10])
        self.TwitchEnd.start()
        self.TwitchInit.setText(translate("twitchBox", "init") + ": " + iniz)
        if (streamers != []):
            streamers_ids = ""
            for stream in streamers:
                streamers_ids += stream + " "
            self.TwitchStreamers.setText(translate("twitchBox", "streamer") + ": " + streamers_ids)
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
            print(translate("twitchBox", "unknown") + ": " + twitch_type)

    def is_expired(self):
        return (int(self.TwitchEnd.get_time()) - int(timeUtils.get_local_time())) < 0

    def get_iniz(self):
        return self.TwitchInit.text().split(" ")[1]

    def hide(self):
        self.TwitchInit.hide()
        self.TwitchEnd.hide()
        self.TwitchType.hide()
        self.TwitchStreamers.hide()
