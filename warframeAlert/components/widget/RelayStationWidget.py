from PyQt5 import QtCore, QtWidgets

from warframeAlert.components.common.SimarisTarget import SimarisTarget
from warframeAlert.components.common.DailyDeals import DailyDeals
from warframeAlert.services.translationService import translate
from warframeAlert.utils import timeUtils
from warframeAlert.utils.gameTranslationUtils import get_item_name_en


class RelayStationWidget:
    def __init__(self):
        self.data = {'DailyDeals': [], 'LibraryInfo': []}

        self.dailyDeals = DailyDeals()
        self.simarisTarget = SimarisTarget()
        self.data['DailyDeals'].append(self.dailyDeals)
        self.data['LibraryInfo'].append(self.simarisTarget)

        self.relayStationWidget = QtWidgets.QWidget()

        self.gridRelay = QtWidgets.QGridLayout(self.relayStationWidget)

        self.labelRelayDesc = QtWidgets.QLabel(translate("relayStationWidget", "destroyedStation") + ": ")
        self.labelOtherDesc = QtWidgets.QLabel(translate("relayStationWidget", "specialNode") + ": ")
        self.labelRelay = QtWidgets.QLabel("")
        self.labelOther = QtWidgets.QLabel(translate("relayStationWidget", "None"))
        self.RelaySpace1 = QtWidgets.QLabel("")
        self.RelaySpace2 = QtWidgets.QLabel("")
        self.RelaySpace3 = QtWidgets.QLabel("")

        self.gridRelay.addLayout(self.dailyDeals.DealsBox, 0, 0)
        self.gridRelay.addWidget(self.RelaySpace1, 1, 0)
        self.gridRelay.addLayout(self.simarisTarget.SimarisBox, 2, 0)
        self.gridRelay.addWidget(self.RelaySpace2, 3, 0)
        self.gridRelay.addWidget(self.labelRelayDesc, 4, 0)
        self.gridRelay.addWidget(self.labelRelay, 5, 0)
        self.gridRelay.addWidget(self.RelaySpace3, 6, 0)
        self.gridRelay.addWidget(self.labelOtherDesc, 7, 0)
        self.gridRelay.addWidget(self.labelOther, 8, 0)

        self.gridRelay.setAlignment(QtCore.Qt.AlignTop)

        self.relayStationWidget.setLayout(self.gridRelay)

    def get_widget(self):
        return self.relayStationWidget

    def parse_simaris_target(self, simaris_data):
        self.data['LibraryInfo'][0].set_simaris_target(simaris_data['LastCompletedTargetType'])

    def parse_daily_deals(self, daily_deals_data):
        if (daily_deals_data):
            for deal in daily_deals_data:
                try:
                    init = deal['Activation']['$date']['$numberLong']
                    end = deal['Expiry']['$date']['$numberLong']
                except KeyError:
                    init = str((int(timeUtils.get_local_time())) * 1000)
                    end = str((int(timeUtils.get_local_time()) + 3600) * 1000)
                tempo = int(end[:10]) - int(timeUtils.get_local_time())
                if (tempo >= 0 or tempo != translate("timeUtils", "Timed Out")):
                    q_sold = deal['AmountSold']
                    q_total = deal['AmountTotal']
                    sale = deal['Discount']
                    o_price = deal['OriginalPrice']
                    s_price = deal['SalePrice']
                    item = get_item_name_en(deal['StoreItem'])

                    self.data['DailyDeals'][0].set_deals_data(init, end, item, q_sold, q_total, o_price, sale, s_price)
