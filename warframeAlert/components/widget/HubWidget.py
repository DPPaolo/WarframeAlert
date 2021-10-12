# coding=utf-8
from PyQt6 import QtWidgets, QtCore

from warframeAlert.components.common.HubEvent import create_hub_event
from warframeAlert.constants.warframeTypes import HubEvents
from warframeAlert.services.translationService import translate
from warframeAlert.utils import timeUtils
from warframeAlert.utils.commonUtils import remove_widget


class HubWidget:
    hubWidget = None

    def __init__(self) -> None:
        self.data = {'HubEvents': []}

        self.hubWidget = QtWidgets.QWidget()

        self.gridHub = QtWidgets.QGridLayout(self.hubWidget)

        self.NoHubLab = QtWidgets.QLabel(translate("hubWidget", "no_hub_event"))

        self.gridHub.addWidget(self.NoHubLab, 0, 0)

        self.NoHubLab.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.gridHub.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

        self.hubWidget.setLayout(self.gridHub)

    def get_widget(self) -> QtWidgets.QWidget:
        return self.hubWidget

    def parse_hub_event(self, json_data: HubEvents) -> None:
        self.reset_hub_event()
        n_hub = len(self.data['HubEvents'])
        if (json_data):
            for hub in json_data:
                end = hub['Expiry']['$date']['$numberLong']
                try:
                    tag = hub['Tag']
                except KeyError:
                    tag = translate("hubEvent", "eventNoName")
                remaining_time = int(end[:10]) - int(timeUtils.get_local_time())
                if (remaining_time > 0):
                    found = 0
                    for hub_event in self.data['HubEvents']:
                        if (hub_event.get_name() == tag):
                            found = 1

                    if (found == 0):
                        temp = create_hub_event(hub)
                        self.data['HubEvents'].append(temp)
                        del temp

        self.add_hub_event(n_hub)

    def add_hub_event(self, n_hub: int) -> None:
        for i in range(n_hub, len(self.data['HubEvents'])):
            if (not self.data['HubEvents'][i].is_expired()):
                self.gridHub.addLayout(self.data['HubEvents'][i].HubBox, self.gridHub.count(), 0)

        if (len(self.data['HubEvents']) > 0):
            self.NoHubLab.hide()

    def reset_hub_event(self) -> None:
        self.NoHubLab.show()
        cancelled_hub_event = []
        for i in range(0, len(self.data['HubEvents'])):
            if (self.data['HubEvents'][i].is_expired()):
                cancelled_hub_event.append(i)
        i = len(cancelled_hub_event)
        while i > 0:
            self.data['HubEvents'][cancelled_hub_event[i-1]].hide()
            remove_widget(self.data['HubEvents'][cancelled_hub_event[i-1]].HubBox)
            del self.data['HubEvents'][cancelled_hub_event[i-1]]
            i -= 1
