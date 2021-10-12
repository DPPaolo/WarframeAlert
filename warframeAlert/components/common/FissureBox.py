# coding=utf-8
from PyQt6 import QtGui, QtWidgets, QtCore

from warframeAlert.components.common.Countdown import Countdown
from warframeAlert.services.translationService import translate
from warframeAlert.utils import timeUtils


class FissureBox():

    def __init__(self, fissure_id: str, seed: int) -> None:
        # Label
        self.Font = QtGui.QFont()
        self.Font.setBold(True)

        self.FisNode = QtWidgets.QLabel("N/D")
        self.FisPlan = QtWidgets.QLabel("N/D")
        self.FisMis = QtWidgets.QLabel("N/D")
        self.FisTier = QtWidgets.QLabel("N/D")
        self.FisTime = Countdown()
        self.fissure_id = fissure_id
        self.seed = seed
        self.region = ""

        self.FisTier.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)

        self.FisMis.setFont(self.Font)
        self.FisTier.setFont(self.Font)

        self.FisBox = QtWidgets.QHBoxLayout()

        self.FisBox.addWidget(self.FisNode)
        self.FisBox.addWidget(self.FisPlan)
        self.FisBox.addWidget(self.FisMis)
        self.FisBox.addWidget(self.FisTime.TimeLab)
        self.FisBox.addWidget(self.FisTier)

        self.FisTime.TimeOut.connect(self.hide)

    def set_fissure_data(self, node: str, plan: str, mis: str, init: int, end: int, tier: str, region: str) -> None:
        self.region = region
        self.FisNode.setText(node)
        self.FisPlan.setText(plan)
        self.FisMis.setText(mis)
        self.FisTier.setText(tier)

        self.FisTime.set_countdown(end[:10])
        self.FisTime.set_tooltip(translate("fissureBox", "fissureStart") + " " + timeUtils.get_time(init[:10]))
        self.FisTime.start()

    def get_fissure_id(self) -> str:
        return self.fissure_id

    def get_title(self) -> str:
        return translate("fissureBox", "newFissure") + " " + self.FisTier.text()

    def to_string(self) -> str:
        return self.FisNode.text() + " " + self.FisPlan.text() + "\n" + self.FisMis.text()

    def is_expired(self) -> bool:
        return (int(self.FisTime.get_time()) - int(timeUtils.get_local_time())) < 0

    def hide(self) -> None:
        self.FisNode.hide()
        self.FisPlan.hide()
        self.FisMis.hide()
        self.FisTier.hide()
        self.FisTime.hide()
