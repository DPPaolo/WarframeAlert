# coding=utf-8
from PyQt6 import QtCore, QtWidgets

from warframeAlert.components.common.EmptySpace import EmptySpace
from warframeAlert.components.common.SimarisTarget import SimarisTarget
from warframeAlert.components.common.DailyDeals import DailyDeals
from warframeAlert.constants.warframeTypes import DailyDealsData, LibraryInfo, NodeOverrides
from warframeAlert.services.translationService import translate
from warframeAlert.utils import timeUtils
from warframeAlert.utils.gameTranslationUtils import get_item_name_en, get_node


class RelayStationWidget:
    def __init__(self) -> None:
        self.data = {'DailyDeals': [], 'LibraryInfo': []}

        self.dailyDeals = DailyDeals()
        self.simarisTarget = SimarisTarget()
        self.data['DailyDeals'].append(self.dailyDeals)
        self.data['LibraryInfo'].append(self.simarisTarget)

        self.relayStationWidget = QtWidgets.QWidget()

        self.gridRelay = QtWidgets.QGridLayout(self.relayStationWidget)

        self.RelayLabelDesc = QtWidgets.QLabel(translate("relayStationWidget", "destroyedStation") + ": ")
        self.RelayOtherLabelDesc = QtWidgets.QLabel(translate("relayStationWidget", "specialNode") + ": ")
        self.RelayLabel = QtWidgets.QLabel("")
        self.RelayOtherLabel = QtWidgets.QLabel(translate("relayStationWidget", "None"))

        self.gridRelay.addLayout(self.dailyDeals.DealsBox, 0, 0)
        self.gridRelay.addLayout(EmptySpace().SpaceBox, 1, 0)
        self.gridRelay.addLayout(self.simarisTarget.SimarisBox, 2, 0)
        self.gridRelay.addLayout(EmptySpace().SpaceBox, 3, 0)
        self.gridRelay.addWidget(self.RelayLabelDesc, 4, 0)
        self.gridRelay.addWidget(self.RelayLabel, 5, 0)
        self.gridRelay.addLayout(EmptySpace().SpaceBox, 6, 0)
        self.gridRelay.addWidget(self.RelayOtherLabelDesc, 7, 0)
        self.gridRelay.addWidget(self.RelayOtherLabel, 8, 0)

        self.gridRelay.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

        self.relayStationWidget.setLayout(self.gridRelay)

    def get_widget(self) -> QtWidgets.QWidget:
        return self.relayStationWidget

    def parse_simaris_target(self, simaris_data: LibraryInfo) -> None:
        self.data['LibraryInfo'][0].set_simaris_target(simaris_data['LastCompletedTargetType'])

    def parse_daily_deals(self, daily_deals_data: DailyDealsData) -> None:
        if (daily_deals_data):
            for deal in daily_deals_data:
                init = deal['Activation']['$date']['$numberLong']
                end = deal['Expiry']['$date']['$numberLong']
                remaining_time = int(end[:10]) - int(timeUtils.get_local_time())
                if (remaining_time >= 0 or remaining_time != translate("timeUtils", "Timed Out")):
                    q_sold = deal['AmountSold']
                    q_total = deal['AmountTotal']
                    sale = deal['Discount']
                    o_price = deal['OriginalPrice']
                    s_price = deal['SalePrice']
                    item = get_item_name_en(deal['StoreItem'])

                    self.data['DailyDeals'][0].set_deals_data(init, end, item, q_sold, q_total, o_price, sale, s_price)

    def parse_relay_station(self, data: NodeOverrides) -> None:
        self.reset_relay_node()
        spec = 0
        for nod in data:
            node = get_node(nod['Node'])
            if ('Hide' in nod):
                if (nod['Hide'] and 'Activation' not in nod):
                    self.set_relay_text(self.get_relay_text() + node[0] + " " + node[1] + "\n")
            elif ('CustomNpcEncounters' in nod):
                self.set_other_text(self.get_other_text() + translate("hubEvent", "event") +
                                    " " + node[0] + " " + node[1] + "\n")
                spec = 1
            elif ('Seed' in nod):
                self.set_other_text(self.get_other_text() + node[0] + " " + node[1] + "\n")
                spec = 1

        if (spec == 0):
            self.set_other_text(translate("hubEvent", "none"))

    def set_relay_text(self, text: str) -> None:
        self.RelayLabel.setText(text)

    def get_relay_text(self) -> str:
        return self.RelayLabel.text()

    def set_other_text(self, text: str) -> None:
        self.RelayOtherLabel.setText(text)

    def get_other_text(self) -> str:
        return self.RelayOtherLabel.text()

    def reset_relay_node(self) -> None:
        self.RelayLabel.setText("")
        self.RelayOtherLabel.setText("")
