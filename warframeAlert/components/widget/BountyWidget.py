# coding=utf-8
from typing import Tuple

from PyQt6 import QtWidgets, QtCore

from warframeAlert.components.common.BountyBox import create_bounty_box
from warframeAlert.constants.warframeTypes import SyndicateMission
from warframeAlert.services.translationService import translate
from warframeAlert.utils.commonUtils import remove_widget
from warframeAlert.utils.gameTranslationUtils import get_syndicate


class BountyWidget:
    BountyWidget = None

    def __init__(self) -> None:
        self.alerts = {'Bounty': []}
        self.bountyInit: int = 0
        self.bountyEnd: int = 0
        self.BountyWidget = QtWidgets.QWidget()
        self.NoBountyMission = QtWidgets.QLabel(translate("bountyWidget", "noBounty"))
        self.NoBountyMission.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.BountyGrid = QtWidgets.QGridLayout(self.BountyWidget)
        self.BountyGrid.addWidget(self.NoBountyMission, 0, 0)
        self.BountyGrid.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

        self.BountyWidget.setLayout(self.BountyGrid)

    def get_widget(self) -> QtWidgets.QWidget:
        return self.BountyWidget

    def get_timer(self) -> Tuple[int, int]:
        return self.bountyInit, self.bountyEnd

    def parse_bounty(self, data: SyndicateMission, use_token: bool = False) -> None:
        if (data):
            is_bounty_present = False
            bounty_id = data['_id']['$oid']
            tag = data['Tag']

            # If the bounty has the same ID, it means that it's in the same group
            if (len(self.alerts['Bounty']) != 0):
                if (self.alerts['Bounty'][0].get_bounty_id() == bounty_id):
                    return
                else:
                    self.reset_bounty()

            self.bountyInit = data['Activation']['$date']['$numberLong']
            self.bountyEnd = data['Expiry']['$date']['$numberLong'][:10]

            if ('Jobs' in data):
                for i in range(0, len(data['Jobs'])):
                    bounty = create_bounty_box(data['Jobs'][i])
                    bounty.set_syndicate(get_syndicate(tag), i + 1, use_token)
                    bounty.set_bounty_id(bounty_id)
                    self.alerts['Bounty'].append(bounty)
                    del bounty
                is_bounty_present = True

            self.add_bounty(is_bounty_present)
        else:
            self.reset_bounty()

    def add_bounty(self, bounty: bool) -> None:
        if (bounty):
            for i in range(0, len(self.alerts['Bounty'])):
                self.BountyGrid.addLayout(self.alerts['Bounty'][i].BountyBox, self.BountyGrid.count(), 0)

        if (len(self.alerts['Bounty']) > 0):
            self.NoBountyMission.hide()

    def reset_bounty(self) -> None:
        self.NoBountyMission.show()
        for i in reversed(range(0, len(self.alerts['Bounty']))):
            self.alerts['Bounty'][i].hide()
            remove_widget(self.alerts['Bounty'][i].BountyBox)
            self.alerts['Bounty'][i].BountyBox.setParent(None)
            del self.alerts['Bounty'][i]
