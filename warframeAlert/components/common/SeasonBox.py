# coding=utf-8
from PyQt6 import QtWidgets, QtGui

from warframeAlert.components.common.Countdown import Countdown
from warframeAlert.services.translationService import translate
from warframeAlert.utils import timeUtils
from warframeAlert.utils.stringUtils import divide_message


class SeasonBox():
    def __init__(self, id_nightwave: str) -> None:
        self.id_nightwave = id_nightwave
        self.image = None
        self.Font = QtGui.QFont()
        self.Font.setBold(True)

        self.ChallengeTitle = QtWidgets.QLabel("N/D")
        self.ChallengeDesc = QtWidgets.QLabel("N/D")
        self.ChallengePoint = QtWidgets.QLabel("N/D")
        self.ChallengeType = QtWidgets.QLabel("N/D")
        self.ChallengeTitle.setFont(self.Font)
        self.ChallengeEnd = Countdown()

        self.Seasonhbox1 = QtWidgets.QHBoxLayout()
        self.Seasonhbox2 = QtWidgets.QHBoxLayout()

        self.SeasonBox = QtWidgets.QVBoxLayout()

        self.Seasonhbox1.addWidget(self.ChallengeTitle)
        self.Seasonhbox1.addStretch(1)
        self.Seasonhbox1.addWidget(self.ChallengeType)

        self.Seasonhbox2.addWidget(self.ChallengeEnd.TimeLab)
        self.Seasonhbox2.addStretch(1)
        self.Seasonhbox2.addWidget(self.ChallengePoint)

        self.SeasonBox.addLayout(self.Seasonhbox1)
        self.SeasonBox.addWidget(self.ChallengeDesc)
        self.SeasonBox.addLayout(self.Seasonhbox2)
        self.SeasonBox.setContentsMargins(10, 10, 10, 10)

    def get_challenge_id(self) -> str:
        return self.id_nightwave

    def is_expired(self) -> bool:
        return (int(self.ChallengeEnd.get_time()) - int(timeUtils.get_local_time())) < 0

    def get_title(self) -> str:
        return self.ChallengeTitle.text()

    def to_string(self) -> str:
        return self.ChallengeDesc.text()

    def set_data(self, init: int, end: int, challenge: tuple[str, str, int], daily) -> None:
        challenge_start = timeUtils.get_time(init)
        self.ChallengeTitle.setToolTip(translate("seasonBox", "init") + " " + challenge_start)
        self.ChallengeEnd.set_countdown(end[:10])
        self.ChallengeEnd.start()
        self.ChallengeTitle.setText(challenge[0])
        self.ChallengeDesc.setText(divide_message(challenge[1], 26))
        self.ChallengePoint.setText(str(challenge[2]) + " " + translate("seasonBox", "points"))
        if (daily):
            temp = translate("seasonBox", "daily").upper()
        elif (challenge[2] == 1000):
            temp = translate("seasonBox", "daily").upper()
        elif (challenge[2] == 4500):
            temp = translate("seasonBox", "weekly").upper()
        elif (challenge[2] == 7000):
            temp = translate("seasonBox", "weeklyElite").upper()
        else:
            temp = translate("seasonBox", "unkown").upper()
        self.ChallengeType.setText(temp)

    def hide(self) -> None:
        self.ChallengeTitle.hide()
        self.ChallengeDesc.hide()
        self.ChallengePoint.hide()
        self.ChallengeType.hide()
        self.ChallengeEnd.hide()
