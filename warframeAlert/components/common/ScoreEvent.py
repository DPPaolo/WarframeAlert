# coding=utf-8
from PyQt5 import QtWidgets

from warframeAlert.components.common.Event import Event
from warframeAlert.services.translationService import translate


class ScoreEvent(Event):

    def __init__(self, event_id):
        super().__init__(event_id)
        self.TANodeAtt = QtWidgets.QLabel(translate("scoreEvent", "noEvent"))

        self.TAScoreLab = QtWidgets.QLabel(translate("scoreEvent", "globalScore") + ": ")
        self.TAScore = QtWidgets.QLabel("N/D")
        self.TABestLab = QtWidgets.QLabel(translate("scoreEvent", "bestScore") + ": ")
        self.TABest = QtWidgets.QLabel("N/D")

        self.TAPerAtt = QtWidgets.QProgressBar()

        self.TABarbox1 = QtWidgets.QHBoxLayout()
        self.TABarbox2 = QtWidgets.QHBoxLayout()

        self.TABarbox1.addWidget(self.TAScoreLab)
        self.TABarbox1.addWidget(self.TAScore)
        self.TABarbox1.addWidget(self.TABestLab)
        self.TABarbox1.addWidget(self.TABest)

        self.TABarbox2.addWidget(self.TAPerAtt)
        self.TABarbox2.addWidget(self.TANodeAtt)

        self.TADescvbox.addLayout(self.TABarbox1)
        self.TADescvbox.addLayout(self.TABarbox2)

    def set_perc_att(self, per, attnode):
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
        if (attnode != ""):
            self.TANodeAtt.setText(attnode[0])
        else:
            self.TANodeAtt.hide()

    def set_score_data(self, score, best):
        self.TAScore.setText(str(score))
        self.TABest.setText(best)
        if (score == ""):
            self.TAScoreLab.hide()
            self.TAScore.hide()
        if (best == ""):
            self.TABestLab.hide()
            self.TABest.hide()

    def hide(self):
        super().hide()
        self.TANodeAtt.hide()
        self.TAPerAtt.hide()
