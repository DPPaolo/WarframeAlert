# coding=utf-8
from PyQt6 import QtWidgets, QtGui

from warframeAlert.services.translationService import translate


class EventReward():

    def __init__(self, mis: int) -> None:
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

        self.N_mis = mis

        self.TAItem.setFont(self.Font)
        self.TANode.setFont(self.Font)
        self.TAMisNumDesc.setFont(self.Font)

        self.TABox1 = QtWidgets.QHBoxLayout()
        self.TABox2 = QtWidgets.QHBoxLayout()
        self.TABox3 = QtWidgets.QHBoxLayout()
        self.TAVBox = QtWidgets.QVBoxLayout()

        self.TABox1.addWidget(self.TAMisNumDesc)
        self.TABox1.addWidget(self.TANode)

        self.TABox2.addWidget(self.TAScoreDesc)
        self.TABox2.addWidget(self.TAScore)
        self.TABox2.addWidget(self.TAScoreReqLab)
        self.TABox2.addWidget(self.TAScoreReq)

        self.TABox3.addWidget(self.TAItemDesc)
        self.TABox3.addWidget(self.TAItem)

        self.TAVBox.addLayout(self.TABox1)
        self.TAVBox.addLayout(self.TABox2)
        self.TAVBox.addLayout(self.TABox3)

    def set_reward_data(self, item: str, node: tuple[str, str], score: int, req: int,
                        mission_interval: int, mission_map_rotation: str) -> None:
        self.TAMisNumDesc.setText(translate("eventReward", "mission") + " " + str(self.N_mis))
        self.TAItem.setText(item)
        self.TANode.setText(translate("eventReward", "node") + ": " + node[0] + " " + node[1])
        self.TAScore.setText(str(score))
        self.TAScoreReq.setText(str(req))
        seconds = " " + translate("eventReward", "seconds")
        node_tooltip = ""
        if (mission_interval != 0):
            node_tooltip += translate("eventReward", "missionInterval") + ": " + str(mission_interval) + seconds + "\n"
        if (mission_map_rotation != ""):
            node_tooltip += translate("eventReward", "missionMapRotation") + " " + str(mission_map_rotation)
        if (node_tooltip != ""):
            self.TANode.setToolTip(node_tooltip)

    def hide(self) -> None:
        self.TAMisNumDesc.hide()
        self.TAItemDesc.hide()
        self.TAItem.hide()
        self.TANode.hide()
        self.TAScoreDesc.hide()
        self.TAScore.hide()
        self.TAScoreReqLab.hide()
        self.TAScoreReq.hide()
