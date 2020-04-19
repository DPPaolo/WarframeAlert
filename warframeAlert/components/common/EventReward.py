# coding=utf-8
from PyQt5 import QtWidgets, QtGui

from warframeAlert.services.translationService import translate


class EventReward():

    def __init__(self, mis):
        self.Font = QtGui.QFont()
        self.Font.setBold(True)

        self.TAMisNumDesc = QtWidgets.QLabel(translate("eventReward", "mission"))
        self.TAItemDesc = QtWidgets.QLabel(translate("eventReward", "reward") + ":")
        self.TAItem = QtWidgets.QLabel(translate("eventReward", "noItem") + "Nessuna")
        self.TANode = QtWidgets.QLabel("N/D (???)")
        self.TAScoreDesc = QtWidgets.QLabel(translate("eventReward", "scoreRequired") + ":")
        self.TAScore = QtWidgets.QLabel("N/D")
        self.TAScoreReqLab = QtWidgets.QLabel(translate("eventReward", "scoreRequiredUnlock") + ":")
        self.TAScoreReq = QtWidgets.QLabel("0")

        self.Nmis = mis

        self.TAItem.setFont(self.Font)
        self.TANode.setFont(self.Font)
        self.TAMisNumDesc.setFont(self.Font)

        self.TAbox1 = QtWidgets.QHBoxLayout()
        self.TAbox2 = QtWidgets.QHBoxLayout()
        self.TAbox3 = QtWidgets.QHBoxLayout()
        self.TAvbox = QtWidgets.QVBoxLayout()

        self.TAbox1.addWidget(self.TAMisNumDesc)
        self.TAbox1.addWidget(self.TANode)

        self.TAbox2.addWidget(self.TAScoreDesc)
        self.TAbox2.addWidget(self.TAScore)
        self.TAbox2.addWidget(self.TAScoreReqLab)
        self.TAbox2.addWidget(self.TAScoreReq)

        self.TAbox3.addWidget(self.TAItemDesc)
        self.TAbox3.addWidget(self.TAItem)

        self.TAvbox.addLayout(self.TAbox1)
        self.TAvbox.addLayout(self.TAbox2)
        self.TAvbox.addLayout(self.TAbox3)

    def set_reward_data(self, item, node, score, req):
        self.TAMisNumDesc.setText(translate("eventReward", "mission") + " " + str(self.Nmis))
        self.TAItem.setText(item)
        self.TANode.setText(translate("eventReward", "node") + ": " + node[0] + " " + node[1])
        self.TAScore.setText(str(score))
        self.TAScoreReq.setText(str(req))

    def hide(self):
        self.TAMisNumDesc.hide()
        self.TAItemDesc.hide()
        self.TAItem.hide()
        self.TANode.hide()
        self.TAScoreDesc.hide()
        self.TAScore.hide()
        self.TAScoreReqLab.hide()
        self.TAScoreReq.hide()
