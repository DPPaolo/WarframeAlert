# coding=utf-8
from PyQt6 import QtWidgets, QtGui, QtCore

from warframeAlert.components.common.Countdown import Countdown
from warframeAlert.constants.warframeTypes import HubEventData
from warframeAlert.services.translationService import translate
from warframeAlert.utils import timeUtils
from warframeAlert.utils.gameTranslationUtils import get_node


class HubEvent():

    def __init__(self) -> None:
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
        self.HubTransmissionLab = QtWidgets.QLabel(translate("hubEvent", "transmission") + ": ")
        self.HubTransmission = QtWidgets.QLabel("N/D")

        self.HubName.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.HubName.setFont(font)

        self.HubBox = QtWidgets.QVBoxLayout()

        hub_h_box1 = QtWidgets.QHBoxLayout()
        hub_h_box2 = QtWidgets.QHBoxLayout()
        hub_h_box3 = QtWidgets.QHBoxLayout()
        hub_h_box4 = QtWidgets.QHBoxLayout()

        hub_h_box1.addWidget(self.HubInitLab)
        hub_h_box1.addWidget(self.HubInit)
        hub_h_box1.addWidget(self.HubEndLab)
        hub_h_box1.addWidget(self.HubEnd.TimeLab)

        hub_h_box2.addWidget(self.HubNodeLab)
        hub_h_box2.addWidget(self.HubNode)
        hub_h_box2.addWidget(self.HubCinematicLab)
        hub_h_box2.addWidget(self.HubCinematic)

        hub_h_box3.addWidget(self.HubCycleLab)
        hub_h_box3.addWidget(self.HubCycle)
        hub_h_box3.addWidget(self.HubRepeatCycleLab)
        hub_h_box3.addWidget(self.HubRepeatCycle)

        hub_h_box4.addWidget(self.HubTransmissionLab)
        hub_h_box4.addWidget(self.HubTransmission)
        hub_h_box4.addStretch(1)

        self.HubBox.addWidget(self.HubName)
        self.HubBox.addLayout(hub_h_box1)
        self.HubBox.addLayout(hub_h_box2)
        self.HubBox.addLayout(hub_h_box3)
        self.HubBox.addLayout(hub_h_box4)
        self.HubEnd.TimeOut.connect(self.hide)

    def set_hub_event_data(self, init: str, end: int, tag: str, node: tuple[str, str],
                           cinematic: str, interval: int, cycle: int, transmission: str) -> None:
        self.HubInit.setText(init)
        self.HubName.setText(tag)
        self.HubNode.setText(node[0] + " " + node[1])
        self.HubCinematic.setText(cinematic)
        self.HubRepeatCycle.setText(str(interval) + " " + translate("hubEvent", "seconds"))
        self.HubCycle.setText(str(cycle) + " " + translate("hubEvent", "seconds"))
        self.HubTransmission.setText(transmission)

        self.HubEnd.set_countdown(end[:10])
        self.HubEnd.start()

    def set_hub_name(self, name: str) -> None:
        self.HubName.setText(name)

    def get_name(self) -> str:
        return self.HubName.text()

    def hide(self) -> None:
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
        self.HubTransmissionLab.hide()
        self.HubTransmission.hide()

    def is_expired(self) -> bool:
        return (int(self.HubEnd.get_time()) - int(timeUtils.get_local_time())) < 0


def create_hub_event(hub: HubEventData) -> HubEvent:
    try:
        init = timeUtils.get_time(hub['Activation']['$date']['$numberLong'])
        end = hub['Expiry']['$date']['$numberLong']
    except KeyError:
        init = str((int(timeUtils.get_local_time()))*1000)
        end = str((int(timeUtils.get_local_time()) + 3600)*1000)
    try:
        node = get_node(hub['Node'])
    except KeyError:
        node = (translate("hubEvent", "none"), "")
    if ('CinematicTag' in hub):
        cinematic = hub['CinematicTag']
    else:
        cinematic = translate("hubEvent", "none")
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
        transmission = hub['Transmissions'][0]
        for i in range(1, len(hub['Transmissions'])):
            transmission += "\n" + hub['Transmissions'][i]
    else:
        transmission = hub['Transmission']

    temp = HubEvent()
    temp.set_hub_event_data(init, end, tag, node, cinematic, interval, cycle, transmission)
    return temp
