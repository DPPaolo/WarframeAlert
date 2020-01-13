from PyQt5 import QtWidgets, QtGui, QtCore

from warframeAlert.components.common.Countdown import Countdown
from warframeAlert.services.translationService import translate
from warframeAlert.utils import timeUtils
from warframeAlert.utils.gameTranslationUtils import get_node


class HubEvent():

    def __init__(self):
        font = QtGui.QFont()
        font.setBold(True)

        self.HubName = QtWidgets.QLabel("N/D")
        self.HubInitLab = QtWidgets.QLabel(translate("hubEvent", "start"))
        self.HubInit = QtWidgets.QLabel("N/D")
        self.HubEndLab = QtWidgets.QLabel(translate("hubEvent", "end"))
        self.HubEnd = Countdown()
        self.HubNodeLab = QtWidgets.QLabel(translate("hubEvent", "node") + ": ")
        self.HubNode = QtWidgets.QLabel("N/D")
        self.HubCinematicLab = QtWidgets.QLabel(translate("hubEvent", "cinematic") + ": ")
        self.HubCinematic = QtWidgets.QLabel("N/D")
        self.HubCycleLab = QtWidgets.QLabel(translate("hubEvent", "cycle") + ": ")
        self.HubCycle = QtWidgets.QLabel("N/D")
        self.HubRepeatCycleLab = QtWidgets.QLabel(translate("hubEvent", "repeatCycle") + ": ")
        self.HubRepeatCycle = QtWidgets.QLabel("N/D")
        self.HubTrasmissionLab = QtWidgets.QLabel(translate("hubEvent", "transmission") + ": ")
        self.HubTrasmission = QtWidgets.QLabel("N/D")

        self.HubName.setAlignment(QtCore.Qt.AlignCenter)
        self.HubName.setFont(font)

        self.HubBox = QtWidgets.QVBoxLayout()

        hubhbox1 = QtWidgets.QHBoxLayout()
        hubhbox2 = QtWidgets.QHBoxLayout()
        hubhbox3 = QtWidgets.QHBoxLayout()
        hubhbox4 = QtWidgets.QHBoxLayout()

        hubhbox1.addWidget(self.HubInitLab)
        hubhbox1.addWidget(self.HubInit)
        hubhbox1.addWidget(self.HubEndLab)
        hubhbox1.addWidget(self.HubEnd.TimeLab)

        hubhbox2.addWidget(self.HubNodeLab)
        hubhbox2.addWidget(self.HubNode)
        hubhbox2.addWidget(self.HubCinematicLab)
        hubhbox2.addWidget(self.HubCinematic)

        hubhbox3.addWidget(self.HubCycleLab)
        hubhbox3.addWidget(self.HubCycle)
        hubhbox3.addWidget(self.HubRepeatCycleLab)
        hubhbox3.addWidget(self.HubRepeatCycle)

        hubhbox4.addWidget(self.HubTrasmissionLab)
        hubhbox4.addWidget(self.HubTrasmission)
        hubhbox4.addStretch(1)

        self.HubBox.addWidget(self.HubName)
        self.HubBox.addLayout(hubhbox1)
        self.HubBox.addLayout(hubhbox2)
        self.HubBox.addLayout(hubhbox3)
        self.HubBox.addLayout(hubhbox4)
        self.HubEnd.TimeOut.connect(self.hide)

    def set_hubevent_data(self, iniz, fin, tag, node, cinematic, interval, ciclo, trasmission):
        self.HubInit.setText(iniz)
        self.HubName.setText(tag)
        self.HubNode.setText(node[0] + " " + node[1])
        self.HubCinematic.setText(cinematic)
        self.HubRepeatCycle.setText(str(interval) + " " + translate("hubEvent", "seconds"))
        self.HubCycle.setText(str(ciclo) + " " + translate("hubEvent", "seconds"))
        self.HubTrasmission.setText(trasmission)

        self.HubEnd.set_countdown(fin[:10])
        self.HubEnd.start()

    def set_hub_name(self, name):
        self.HubName.setText(name)

    def get_name(self):
        return self.HubName.text()

    def hide(self):
        self.HubName.hide()
        self.HubInit.hide()
        self.HubInitLab.hide()
        self.HubEnd.hide()
        self.HubEndLab.hide()
        self.HubNodeLab.hide()
        self.HubNode.hide()
        self.HubCinematicLab.hide()
        self.HubCinematic.hide()
        self.HubRepeatCycleLab.hide()
        self.HubRepeatCycle.hide()
        self.HubCycleLab.hide()
        self.HubCycle.hide()
        self.HubTrasmissionLab.hide()
        self.HubTrasmission.hide()

    def is_expired(self):
        return (int(self.HubEnd.get_time()) - int(timeUtils.get_local_time())) < 0


def create_hub_event(hub):
    try:
        iniz = timeUtils.get_time(hub['Activation']['$date']['$numberLong'])
        end = hub['Expiry']['$date']['$numberLong']
    except KeyError:
        iniz = str((int(timeUtils.get_local_time()))*1000)
        end = str((int(timeUtils.get_local_time()) + 3600)*1000)
    try:
        node = get_node(hub['Node'])
    except KeyError:
        node = (translate("hubEvent", "none"))
    if ('CinematicTag' in hub):
        cinematic = hub['CinematicTag']
    else:
        cinematic = ""
    try:
        tag = hub['Tag']
    except KeyError:
        tag = translate("hubEvent", "eventNoName")
    interval = hub['RepeatInterval']
    if ('CycleFrequency' in hub):
        cycle = hub['CycleFrequency']
    else:
        cycle = 0
    if ('Transmissions' in hub):
        trasmission = hub['Transmissions'][0]
        for i in range(1, len(hub['Transmissions'])):
            trasmission += "\n" + hub['Transmissions'][i]
    else:
        trasmission = hub['Transmission']

    temp = HubEvent()
    temp.set_hubevent_data(iniz, end, tag, node, cinematic, interval, cycle, trasmission)
    return temp
