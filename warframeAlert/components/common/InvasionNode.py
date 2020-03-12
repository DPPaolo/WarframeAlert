# coding=utf-8
from PyQt5 import QtWidgets

from warframeAlert.components.common.Countdown import Countdown
from warframeAlert.services.translationService import translate
from warframeAlert.utils import timeUtils


class InvasionNode():

    def __init__(self, node_id):
        self.node_id = node_id
        self.OccDesc = QtWidgets.QLabel(translate("invasionNode", "occupationDesc"))
        self.OccFaz = QtWidgets.QLabel("N/D")
        self.OccDescPlan = QtWidgets.QLabel(translate("invasionNode", "occupationNode") + " :")
        self.OccPlan = QtWidgets.QLabel("N/D")
        self.OccDescTime = QtWidgets.QLabel(translate("invasionNode", "occupationTimer"))
        self.OccTime = Countdown()

        self.InvasionNodeBox1 = QtWidgets.QHBoxLayout()
        self.InvasionNodeBox2 = QtWidgets.QHBoxLayout()

        self.InvasionNodeBox = QtWidgets.QVBoxLayout()

        self.InvasionNodeBox1.addWidget(self.OccDesc)
        self.InvasionNodeBox1.addWidget(self.OccFaz)

        self.InvasionNodeBox2.addWidget(self.OccDescPlan)
        self.InvasionNodeBox2.addWidget(self.OccPlan)
        self.InvasionNodeBox2.addWidget(self.OccDescTime)
        self.InvasionNodeBox2.addWidget(self.OccTime.TimeLab)

        self.InvasionNodeBox.addLayout(self.InvasionNodeBox1)
        self.InvasionNodeBox.addLayout(self.InvasionNodeBox2)
        self.InvasionNodeBox.addStretch(1)

        self.OccTime.TimeOut.connect(self.hide)

    def get_node_id(self):
        return self.node_id

    def is_expired(self):
        return (int(self.OccTime.get_time()) - int(timeUtils.get_local_time())) < 0

    def set_invasion_node_data(self, faction, node, time):
        self.OccFaz.setText(faction)
        self.OccPlan.setText(node[0] + " " + node[1])
        self.OccTime.set_countdown(time[:10])
        self.OccTime.start()

    def hide(self):
        self.OccDesc.hide()
        self.OccFaz.hide()
        self.OccDescPlan.hide()
        self.OccPlan.hide()
        self.OccDescTime.hide()
        self.OccTime.hide()