from PyQt5 import QtWidgets, QtCore

from warframeAlert.components.widget.GeneralInfoWidget import GeneralInfoWidget
from warframeAlert.components.widget.HubWidget import HubWidget
from warframeAlert.components.widget.TwitchPromoWidget import TwitchPromoWidget
from warframeAlert.services.translationService import translate
from warframeAlert.utils import commonUtils
from warframeAlert.utils.logUtils import LogHandler


class OtherWidgetTab():

    def __init__(self):
        #  Darvo's Deals and Simaris Target
        self.alerts = {'DailyDeals': [], 'LibraryInfo': []}

        self.otherWidget = QtWidgets.QWidget()
        self.generalWidget = GeneralInfoWidget()
        self.relayStationWidget = QtWidgets.QWidget() #RelayStationWidget(self)
        self.hubEventWidget = HubWidget()
        self.twitchPromoWidget = TwitchPromoWidget()

        self.OtherTabber = QtWidgets.QTabWidget(self.otherWidget)

        self.OtherTabber.insertTab(0, self.generalWidget.get_widget(), translate("otherWidgetTab", "general"))
        self.OtherTabber.insertTab(1, self.relayStationWidget, translate("otherWidgetTab", "relay"))
        self.OtherTabber.insertTab(2, self.hubEventWidget.get_widget(), translate("otherWidgetTab", "hub"))
        self.OtherTabber.insertTab(3, self.twitchPromoWidget.get_widget(), translate("otherWidgetTab", "twitchPromo"))

        self.otherGrid = QtWidgets.QGridLayout(self.otherWidget)

        self.otherGrid.addWidget(self.OtherTabber, 0, 0)

        self.otherWidget.setLayout(self.otherGrid)

        self.otherGrid.setAlignment(QtCore.Qt.AlignTop)

    def get_widget(self):
        return self.otherWidget

    def update_tab(self):
        self.OtherTabber.insertTab(2, self.hubEventWidget.get_widget(), translate("otherWidgetTab", "hub"))
        self.OtherTabber.insertTab(3, self.twitchPromoWidget.get_widget(), translate("otherWidgetTab", "twitchPromo"))
        if (not (len(self.hubEventWidget.data['HubEvents']) > 0)):
            self.OtherTabber.removeTab(self.OtherTabber.indexOf(self.hubEventWidget.get_widget()))
        if (not (len(self.twitchPromoWidget.data['TwitchPromos']) > 0)):
            self.OtherTabber.removeTab(self.OtherTabber.indexOf(self.twitchPromoWidget.get_widget()))

    def set_other_datas(self, version, mob_version, world_seed):
        self.generalWidget.set_other_datas(version, mob_version, world_seed)

    def update_prime_access(self, prime_access, prime_available):
        try:
            self.generalWidget.parse_prime_access(prime_access, prime_available)
        except Exception as er:
            LogHandler.err(translate("otherWidgetTab", "primeAccessUpdateError") + ": " + str(er))
            commonUtils.print_traceback(translate("otherWidgetTab", "primeAccessUpdateError") + ": " + str(er))
            self.generalWidget.reset_prime_access()

    def update_twitch_promo(self, data):
        try:
            self.twitchPromoWidget.parse_twitch_promo(data)
        except Exception as er:
            LogHandler.err(translate("otherWidgetTab", "twitchPromoUpdateError") + ": " + str(er))
            commonUtils.print_traceback(translate("otherWidgetTab", "twitchPromoUpdateError") + ": " + str(er))
            self.twitchPromoWidget.reset_twitch_promo()

    def update_featured_dojo(self, data):
        try:
            self.generalWidget.parse_featured_dojo(data)
        except Exception as er:
            LogHandler.err(translate("otherWidgetTab", "featureDojoUpdateError") + ": " + str(er))
            commonUtils.print_traceback(translate("otherWidgetTab", "featureDojoUpdateError") + ": " + str(er))
            self.generalWidget.reset_featured_dojo()

    def update_hub_event(self, data):
        try:
            self.hubEventWidget.parse_hub_event(data)
        except Exception as er:
            LogHandler.err(translate("otherWidgetTab", "hubEventUpdateError") + ": " + str(er))
            commonUtils.print_traceback(translate("otherWidgetTab", "hubEventUpdateError") + ": " + str(er))
            self.hubEventWidget.reset_hub_event()



def RelayStationWidget(self):
    RelayWidget = QtWidgets.QWidget()  # Widget Altro Stazioni

    gridRelay = QtWidgets.QGridLayout(RelayWidget)

    DailyDeals = warframeClass.daily_deals()
    SimTarget = warframeClass.simaris_target()
    self.labelRelayDesc = QtWidgets.QLabel("Stazioni Distrutte:")
    self.labelOtherDesc = QtWidgets.QLabel("Atri Nodi Speciali:")
    self.labelRelay = QtWidgets.QLabel("")
    self.labelOther = QtWidgets.QLabel("Nessuno")
    self.RelaySpazio1 = QtWidgets.QLabel("")
    self.RelaySpazio2 = QtWidgets.QLabel("")
    self.RelaySpazio3 = QtWidgets.QLabel("")

    self.alerts['DailyDeals'].append(DailyDeals)
    self.alerts['LibraryInfo'].append(SimTarget)

    gridRelay.addLayout(DailyDeals.DealsBox, 0, 0)
    gridRelay.addWidget(self.RelaySpazio1, 1, 0)
    gridRelay.addLayout(SimTarget.SimarisBox, 2, 0)
    gridRelay.addWidget(self.RelaySpazio2, 3, 0)
    gridRelay.addWidget(self.labelRelayDesc, 4, 0)
    gridRelay.addWidget(self.labelRelay, 5, 0)
    gridRelay.addWidget(self.RelaySpazio3, 6, 0)
    gridRelay.addWidget(self.labelOtherDesc, 7, 0)
    gridRelay.addWidget(self.labelOther, 8, 0)

    gridRelay.setAlignment(QtCore.Qt.AlignTop)

    RelayWidget.setLayout(gridRelay)

    return RelayWidget