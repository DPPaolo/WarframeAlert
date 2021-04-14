# coding=utf-8
from PyQt5 import QtWidgets, QtCore

from warframeAlert.components.widget.GeneralInfoWidget import GeneralInfoWidget
from warframeAlert.components.widget.HubWidget import HubWidget
from warframeAlert.components.widget.RelayStationWidget import RelayStationWidget
from warframeAlert.components.widget.TwitchPromoWidget import TwitchPromoWidget
from warframeAlert.services.translationService import translate
from warframeAlert.utils import commonUtils
from warframeAlert.utils.logUtils import LogHandler


class OtherWidgetTab():

    def __init__(self):
        self.otherWidget = QtWidgets.QWidget()
        self.generalWidget = GeneralInfoWidget()
        self.relayStationWidget = RelayStationWidget()
        self.hubEventWidget = HubWidget()
        self.twitchPromoWidget = TwitchPromoWidget()

        self.OtherTabber = QtWidgets.QTabWidget(self.otherWidget)

        self.OtherTabber.insertTab(0, self.generalWidget.get_widget(), translate("otherWidgetTab", "general"))
        self.OtherTabber.insertTab(1, self.relayStationWidget.get_widget(), translate("otherWidgetTab", "relay"))
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

    def set_other_datas(self, version, mob_version, world_seed, force_logout_version, dtls):
        self.generalWidget.set_other_datas(version, mob_version, world_seed, force_logout_version, dtls)

    def update_prime_access(self, prime_access, prime_available):
        try:
            self.generalWidget.parse_prime_access(prime_access, prime_available)
        except Exception as er:
            LogHandler.err(translate("otherWidgetTab", "primeAccessUpdateError") + ": " + str(er))
            commonUtils.print_traceback(translate("otherWidgetTab", "primeAccessUpdateError") + ": " + str(er))
            self.generalWidget.reset_prime_access()

    def update_simaris_target(self, data):
        try:
            self.relayStationWidget.parse_simaris_target(data)
        except Exception as er:
            LogHandler.err(translate("otherWidgetTab", "simarisUpdateError") + ": " + str(er))
            commonUtils.print_traceback(translate("otherWidgetTab", "simarisUpdateError") + ": " + str(er))

    def update_daily_deals(self, data):
        try:
            self.relayStationWidget.parse_daily_deals(data)
        except Exception as er:
            LogHandler.err(translate("otherWidgetTab", "dailyDealsUpdateError") + ": " + str(er))
            commonUtils.print_traceback(translate("otherWidgetTab", "dailyDealsUpdateError") + ": " + str(er))

    def update_relay_station(self, data):
        try:
            self.relayStationWidget.parse_relay_station(data)
        except Exception as er:
            LogHandler.err(translate("otherWidgetTab", "relayStationUpdateError") + ": " + str(er))
            commonUtils.print_traceback(translate("otherWidgetTab", "relayStationUpdateError") + ": " + str(er))

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

    def update_experiment_recommended(self, data):
        try:
            self.get_widget()
            if (data != []):
                print(data)
        except Exception as er:
            LogHandler.err(translate("otherWidgetTab", "experimentUpdateError") + ": " + str(er))
            commonUtils.print_traceback(translate("otherWidgetTab", "experimentUpdateError") + ": " + str(er))
