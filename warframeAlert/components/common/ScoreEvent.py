# coding=utf-8
from typing import List

from PyQt6 import QtWidgets

from warframeAlert.components.common.Event import Event
from warframeAlert.services.translationService import translate


class ScoreEvent(Event):

    def __init__(self, event_id: str) -> None:
        super().__init__(event_id)
        self.TANodeAtt = QtWidgets.QLabel(translate("scoreEvent", "noEvent"))

        self.TAScoreLab = QtWidgets.QLabel(translate("scoreEvent", "globalScore") + ": ")
        self.TAScore = QtWidgets.QLabel("N/D")
        self.TABestLab = QtWidgets.QLabel(translate("scoreEvent", "bestScore") + ": ")
        self.TABest = QtWidgets.QLabel("N/D")

        self.TAPerAtt = QtWidgets.QProgressBar()

        self.TABarBox1 = QtWidgets.QHBoxLayout()
        self.TABarBox2 = QtWidgets.QHBoxLayout()

        self.TABarBox1.addWidget(self.TAScoreLab)
        self.TABarBox1.addWidget(self.TAScore)
        self.TABarBox1.addWidget(self.TABestLab)
        self.TABarBox1.addWidget(self.TABest)

        self.TABarBox2.addWidget(self.TAPerAtt)
        self.TABarBox2.addWidget(self.TANodeAtt)

        self.TADescVBox.addLayout(self.TABarBox1)
        self.TADescVBox.addLayout(self.TABarBox2)

    def set_perc_att(self, per: int, att_node: List[str]):
        self.TAPerAtt.reset()
        self.TAPerAtt.setMaximum(100)
        val = float(per)*100
        if (val > 100):
            self.TAPerAtt.setValue(100)
            self.TAPerAtt.setToolTip(str(100))
        elif (val <= 0):
            self.TAPerAtt.setValue(0)
            self.TAPerAtt.setToolTip(str(0))
        else:
            self.TAPerAtt.setValue(int(val))
            self.TAPerAtt.setToolTip(str(val))
        if (att_node != ""):
            self.TANodeAtt.setText(att_node[0])
        else:
            self.TANodeAtt.hide()

    def set_score_data(self, score: str, best: str) -> None:
        self.TAScore.setText(str(score))
        self.TABest.setText(best)
        if (score == ""):
            self.TAScoreLab.hide()
            self.TAScore.hide()
        if (best == ""):
            self.TABestLab.hide()
            self.TABest.hide()

    def set_score_optional_tooltip(self, optional_in_mission: str, upgrades_id: str, score_block_guilds: str) -> None:
        if (optional_in_mission != ""):
            self.EventReqItemLab.setToolTip(translate("scoreEvent", "optionalInMission") + ": " + optional_in_mission)
        if (upgrades_id != ""):
            self.TAScoreLab.setToolTip(translate("scoreEvent", "upgradesId") + ": " + upgrades_id)
        if (score_block_guilds != ""):
            self.EventScoreLab.setToolTip(translate("scoreEvent", "scoreBlockGuilds") + ": " + score_block_guilds)

    def hide(self) -> None:
        super().hide()
        self.TANodeAtt.hide()
        self.TAPerAtt.hide()
