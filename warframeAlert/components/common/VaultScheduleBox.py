# coding=utf-8
from PyQt6 import QtWidgets, QtGui

from warframeAlert.components.common.Countdown import Countdown
from warframeAlert.services.translationService import translate


class VaultScheduleBox():

    def __init__(self, item: str, end: int) -> None:
        self.item = item
        self.end = end
        self.VaultScheduleName = QtWidgets.QLabel(item)
        self.VaultScheduleEnd = Countdown(translate("salesBox", "end"))

        self.VaultScheduleEnd.set_countdown(end[:10])
        self.VaultScheduleEnd.start()

        self.Font = QtGui.QFont()
        self.Font.setBold(True)
        self.VaultScheduleName.setFont(self.Font)

        self.ScheduleBox = QtWidgets.QHBoxLayout()

        self.ScheduleBox.addWidget(self.VaultScheduleName)
        self.ScheduleBox.addWidget(self.VaultScheduleEnd.TimeLab)
