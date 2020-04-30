# coding=utf-8
from PyQt5 import QtWidgets, QtCore

from warframeAlert.components.common.Event import Event
from warframeAlert.services.translationService import translate
from warframeAlert.utils.gameTranslationUtils import get_region, get_node, get_task_type


def get_reconstruction_task(name, cons_relay):
    task = []
    for data in cons_relay:
        tag = data['Tag']
        if (tag == name):
            for tasks in data['Tasks']:
                task.append(get_task_type(tasks))
    return task


class ReconstructionRelayEvent(Event):
    def __init__(self, event_id):
        super().__init__(event_id)

        self.TARelayNode = QtWidgets.QLabel("N/D")
        self.TARelayNode.setAlignment(QtCore.Qt.AlignCenter)
        self.TARelaySpace1 = QtWidgets.QLabel("")
        self.TARelaySpace2 = QtWidgets.QLabel("")

        self.TAListRegion = QtWidgets.QLabel(translate("reconstrutionEvent", "resourcePlanet") + ":")
        self.TAListRegion.setAlignment(QtCore.Qt.AlignCenter)

        self.TARegion0 = QtWidgets.QLabel("N/D")
        self.TARegion1 = QtWidgets.QLabel("N/D")
        self.TARegion2 = QtWidgets.QLabel("N/D")
        self.TARegion3 = QtWidgets.QLabel("N/D")
        self.TARegion4 = QtWidgets.QLabel("N/D")

        self.TARegion0.setAlignment(QtCore.Qt.AlignCenter)
        self.TARegion1.setAlignment(QtCore.Qt.AlignCenter)
        self.TARegion2.setAlignment(QtCore.Qt.AlignCenter)
        self.TARegion3.setAlignment(QtCore.Qt.AlignCenter)
        self.TARegion4.setAlignment(QtCore.Qt.AlignCenter)

        self.TATask0 = QtWidgets.QLabel("N/D")
        self.TATask1 = QtWidgets.QLabel("N/D")
        self.TATask2 = QtWidgets.QLabel("N/D")
        self.TATask3 = QtWidgets.QLabel("N/D")
        self.TATask4 = QtWidgets.QLabel("N/D")

        self.TATask0.setAlignment(QtCore.Qt.AlignCenter)
        self.TATask1.setAlignment(QtCore.Qt.AlignCenter)
        self.TATask2.setAlignment(QtCore.Qt.AlignCenter)
        self.TATask3.setAlignment(QtCore.Qt.AlignCenter)
        self.TATask4.setAlignment(QtCore.Qt.AlignCenter)

        self.TAReconstructionBox = QtWidgets.QVBoxLayout()

        self.TAReconstructionhbox = QtWidgets.QHBoxLayout()

        self.TAReconstructionhbox.addWidget(self.TARegion0)
        self.TAReconstructionhbox.addWidget(self.TARegion1)
        self.TAReconstructionhbox.addWidget(self.TARegion2)
        self.TAReconstructionhbox.addWidget(self.TARegion3)
        self.TAReconstructionhbox.addWidget(self.TARegion4)

        self.TAReconstructionBox.addWidget(self.TARelayNode)
        self.TAReconstructionBox.addWidget(self.TARelaySpace1)
        self.TAReconstructionBox.addWidget(self.TAListRegion)
        self.TAReconstructionBox.addLayout(self.TAReconstructionhbox)
        self.TAReconstructionBox.addWidget(self.TARelaySpace2)
        self.TAReconstructionBox.addWidget(self.TATask0)
        self.TAReconstructionBox.addWidget(self.TATask1)
        self.TAReconstructionBox.addWidget(self.TATask2)
        self.TAReconstructionBox.addWidget(self.TATask3)
        self.TAReconstructionBox.addWidget(self.TATask4)

        self.TADescvbox.addLayout(self.TAReconstructionBox)

        self.TARegion4.hide()
        self.TATask4.hide()

    def add_relay_reconstruction(self, region, node, task):
        node = get_node(node)
        self.TARelayNode.setText(translate("reconstrutionEvent", "reconstructionNode") + " " + node[0] + " " + node[1])
        region_lenght = len(region)
        self.TARegion0.setText(get_region(region[0]))
        self.TARegion1.setText(get_region(region[1]))
        self.TARegion2.setText(get_region(region[2]))
        self.TARegion3.setText(get_region(region[3]))
        if (region_lenght > 4):
            self.TARegion4.show()
            self.TARegion4.setText(get_region(region[4]))
        task_lenght = len(task)
        self.TATask0.setText(str(task[0][1]) + "x " + task[0][0])
        self.TATask1.setText(str(task[1][1]) + "x " + task[1][0])
        self.TATask2.setText(str(task[2][1]) + "x " + task[2][0])
        self.TATask3.setText(str(task[3][1]) + "x " + task[3][0])
        if (task_lenght > 4):
            self.TATask4.show()
            self.TATask4.setText(str(task[4][1]) + "x " + task[4][0])

    def hide(self):
        super().hide()
        self.TARelayNode.hide()
        self.TARelaySpace1.hide()
        self.TAListRegion.hide()
        self.TARegion0.hide()
        self.TARegion1.hide()
        self.TARegion2.hide()
        self.TARegion3.hide()
        self.TARegion4.hide()
        self.TATask0.hide()
        self.TATask1.hide()
        self.TATask2.hide()
        self.TATask3.hide()
        self.TATask4.hide()
