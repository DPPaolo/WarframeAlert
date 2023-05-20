# coding=utf-8
import json
import sys

from PyQt6 import QtCore, QtWidgets
from jsonschema import ValidationError

from warframeAlert.components.common.MessageBox import MessageBox, MessageBoxType
from warframeAlert.components.tab.AcolyteWidgetTab import AcolyteWidgetTab
from warframeAlert.components.tab.BaroWidgetTab import BaroWidgetTab
from warframeAlert.components.tab.BountyWidgetTab import BountyWidgetTab
from warframeAlert.components.tab.EventsWidgetTab import EventsWidgetTab
from warframeAlert.components.tab.FissureWidgetTab import FissureWidgetTab
from warframeAlert.components.tab.InvasionWidgetTab import InvasionWidgetTab
from warframeAlert.components.tab.NewsWidgetTab import NewsWidgetTab
from warframeAlert.components.tab.NightwaveWidgetTab import NightwaveWidgetTab
from warframeAlert.components.tab.OtherWidgetTab import OtherWidgetTab
from warframeAlert.components.tab.PvPWidgetTab import PvPWidgetTab
from warframeAlert.components.tab.SalesWidgetTab import SalesWidgetTab
from warframeAlert.components.tab.SortieWidgetTab import SortieWidgetTab
from warframeAlert.components.tab.SyndicateWidgetTab import SyndicateWidgetTab
from warframeAlert.components.tab.WeeklyWidgetTab import WeeklyWidgetTab
from warframeAlert.constants.warframeTypes import JsonData
from warframeAlert.services.optionHandlerService import OptionsHandler
from warframeAlert.services.translationService import translate
from warframeAlert.utils.commonUtils import print_traceback
from warframeAlert.utils.fileUtils import get_separator
from warframeAlert.utils.logUtils import LogHandler
from warframeAlert.utils.validatorUtils import check_json_data


class TabService(QtCore.QObject):

    def __init__(self, tabber: QtWidgets.QTabWidget):
        super().__init__()
        self.mainTabber: QtWidgets.QTabWidget = tabber

        self.news_tab: NewsWidgetTab = NewsWidgetTab()
        self.nightwave_tab: NightwaveWidgetTab = NightwaveWidgetTab()
        self.event_tab: EventsWidgetTab = EventsWidgetTab()
        self.bounty_tab: BountyWidgetTab = BountyWidgetTab()
        self.invasion_tab: InvasionWidgetTab = InvasionWidgetTab()
        self.sortie_tab: SortieWidgetTab = SortieWidgetTab()
        self.weekly_tab: WeeklyWidgetTab = WeeklyWidgetTab()
        self.syndicate_tab: SyndicateWidgetTab = SyndicateWidgetTab()
        self.fissure_tab: FissureWidgetTab = FissureWidgetTab()
        self.baro_tab: BaroWidgetTab = BaroWidgetTab()
        self.pvp_tab: PvPWidgetTab = PvPWidgetTab()
        self.acolyte_tab: AcolyteWidgetTab = AcolyteWidgetTab()
        self.sales_tab: SalesWidgetTab = SalesWidgetTab()
        self.other_tab: OtherWidgetTab = OtherWidgetTab()

    def update_tabber(self) -> None:
        index: int = self.mainTabber.currentIndex()
        self.mainTabber.insertTab(0, self.news_tab.get_widget(), translate("tabService", "news"))
        self.mainTabber.insertTab(1, self.nightwave_tab.get_widget(), translate("tabService", "nightwave"))
        self.mainTabber.insertTab(2, self.event_tab.get_widget(), translate("tabService", "events"))
        self.mainTabber.insertTab(3, self.acolyte_tab.get_widget(), translate("tabService", "acolyte"))
        self.mainTabber.insertTab(4, self.bounty_tab.get_widget(), translate("tabService", "bounty"))
        self.mainTabber.insertTab(5, self.invasion_tab.get_widget(), translate("tabService", "invasion"))
        self.mainTabber.insertTab(6, self.sortie_tab.get_widget(), translate("tabService", "sortie"))
        self.mainTabber.insertTab(7, self.weekly_tab.get_widget(), translate("tabService", "weekly"))
        self.mainTabber.insertTab(8, self.syndicate_tab.get_widget(), translate("tabService", "syndicate"))
        self.mainTabber.insertTab(9, self.fissure_tab.get_widget(), translate("tabService", "fissure"))
        self.mainTabber.insertTab(10, self.baro_tab.get_widget(), translate("tabService", "baro"))
        self.mainTabber.insertTab(11, self.sales_tab.get_widget(), translate("tabService", "sales"))
        self.mainTabber.insertTab(12, self.pvp_tab.get_widget(), translate("tabService", "pvp"))
        self.mainTabber.insertTab(13, self.other_tab.get_widget(), translate("tabService", "other"))

        n_event: int = self.event_tab.get_length()
        n_acc: int = self.acolyte_tab.get_length()

        if (not OptionsHandler.get_option("Tab/News") == 1):
            self.mainTabber.removeTab(self.mainTabber.indexOf(self.news_tab.get_widget()))
        if (not OptionsHandler.get_option("Tab/Nightwave") == 1):
            self.mainTabber.removeTab(self.mainTabber.indexOf(self.nightwave_tab.get_widget()))
        if (not (n_event > 0) or not OptionsHandler.get_option("Tab/TactAll") == 1):
            self.mainTabber.removeTab(self.mainTabber.indexOf(self.event_tab.get_widget()))
        if (not (n_acc > 0) or not OptionsHandler.get_option("Tab/Acolyte") == 1):
            self.mainTabber.removeTab(self.mainTabber.indexOf(self.acolyte_tab.get_widget()))
        if (not OptionsHandler.get_option("Tab/Cetus") == 1):
            self.mainTabber.removeTab(self.mainTabber.indexOf(self.bounty_tab.get_widget()))
        if (not OptionsHandler.get_option("Tab/Invasion") == 1):
            self.mainTabber.removeTab(self.mainTabber.indexOf(self.invasion_tab.get_widget()))
        if (not OptionsHandler.get_option("Tab/Sortie") == 1):
            self.mainTabber.removeTab(self.mainTabber.indexOf(self.sortie_tab.get_widget()))
        if (not OptionsHandler.get_option("Tab/Weekly") == 1):
            self.mainTabber.removeTab(self.mainTabber.indexOf(self.weekly_tab.get_widget()))
        if (not OptionsHandler.get_option("Tab/Syndicate") == 1):
            self.mainTabber.removeTab(self.mainTabber.indexOf(self.syndicate_tab.get_widget()))
        if (not OptionsHandler.get_option("Tab/Fissure") == 1):
            self.mainTabber.removeTab(self.mainTabber.indexOf(self.fissure_tab.get_widget()))
        if (not OptionsHandler.get_option("Tab/Baro") == 1):
            self.mainTabber.removeTab(self.mainTabber.indexOf(self.baro_tab.get_widget()))
        if (not OptionsHandler.get_option("Tab/Market") == 1):
            self.mainTabber.removeTab(self.mainTabber.indexOf(self.sales_tab.get_widget()))
        if (not OptionsHandler.get_option("Tab/PVP") == 1):
            self.mainTabber.removeTab(self.mainTabber.indexOf(self.pvp_tab.get_widget()))
        if (not OptionsHandler.get_option("Tab/Other") == 1):
            self.mainTabber.removeTab(self.mainTabber.indexOf(self.other_tab.get_widget()))

        self.event_tab.update_tab()
        self.invasion_tab.update_tab()
        self.sales_tab.update_tab()
        self.other_tab.update_tab()
        self.pvp_tab.update_tab()

        self.mainTabber.setCurrentIndex(index)

    def update(self, path: str) -> str:
        if (not path):
            path: str = "data" + get_separator() + "allerte.json"
        try:
            fp = open(path, "rb")
            data = fp.readlines()
            data = data[0].decode('utf-8')
        except Exception as error:
            MessageBox("", translate("tabService", "alertError") + "\n" + str(error), MessageBoxType.ERROR)
            print_traceback(translate("tabService", "alertError") + str(error))
            LogHandler.err(str(error))
            return ""
        fp.close()

        # Parse and validate the file
        json_data: JsonData = json.loads(data)
        if (OptionsHandler.get_option("Debug") == 1):
            try:
                check_json_data(json_data)
            except ValidationError as validation_error:
                LogHandler.debug(translate("tabService", "validationError"))
                LogHandler.debug(str(validation_error.message))
                print(validation_error)
                sys.exit()

        build_label: str = json_data['BuildLabel']
        game_time: int = json_data['Time']

        # TODO: (if possible) try to parallelize

        self.fissure_tab.update_fissure(json_data['ActiveMissions'], json_data['VoidStorms'])
        self.event_tab.update_alert_mission(json_data['Alerts'])
        self.news_tab.update_news_info(build_label, game_time)
        self.other_tab.update_daily_deals(json_data['DailyDeals'])
        self.other_tab.update_experiment_recommended(json_data['ExperimentRecommended'])
        self.news_tab.update_news(json_data['Events'])
        self.other_tab.update_featured_dojo(json_data['FeaturedGuilds'])
        self.sales_tab.update_sales(json_data['FlashSales'])
        self.news_tab.update_global_upgrades(json_data['GlobalUpgrades'])
        self.event_tab.update_events(json_data['Goals'], json_data['ConstructionProjects'])
        self.other_tab.update_hub_event(json_data['HubEvents'])
        self.invasion_tab.update_invasion(json_data['Invasions'])
        self.other_tab.update_simaris_target(json_data['LibraryInfo'])
        self.weekly_tab.update_lite_sortie(json_data['LiteSorties'])
        self.other_tab.update_relay_station(json_data['NodeOverrides'])
        self.invasion_tab.update_node_override(json_data['NodeOverrides'])
        self.pvp_tab.update_pvp_tournament(json_data['PVPActiveTournaments'])
        self.pvp_tab.update_pvp_alternative_mission(json_data['PVPAlternativeModes'])
        self.pvp_tab.update_pvp_mission(json_data['PVPChallengeInstances'])
        self.acolyte_tab.update_acolyte(json_data['PersistentEnemies'])
        if ('PrimeTokenAvailability' in json_data and json_data['PrimeTokenAvailability']):
            self.event_tab.parse_prime_vault_traders(json_data['PrimeVaultTraders'])

        self.other_tab.update_prime_access(json_data['PrimeAccessAvailability'], json_data['PrimeVaultAvailabilities'])
        self.invasion_tab.update_invasion_project(json_data['ProjectPct'])
        if ('SeasonInfo' in json_data):
            self.nightwave_tab.update_nightwave_season(json_data['SeasonInfo'])
        else:
            self.nightwave_tab.season_not_available()
        self.sortie_tab.update_sortie(json_data['Sorties'])
        self.syndicate_tab.update_syndicate(json_data['SyndicateMissions'])
        self.bounty_tab.update_bounties(json_data['SyndicateMissions'])
        self.other_tab.update_twitch_promo(json_data['TwitchPromos'])
        self.baro_tab.update_baro(json_data['VoidTraders'])
        version: int = json_data['Version']
        mobile_version: str = json_data['MobileVersion']
        world_seed: str = json_data['WorldSeed']
        force_logout_version: int = json_data['ForceLogoutVersion']
        dtls: bool = json_data['DTLS'] if ('DTLS' in json_data) else False
        sentient_anomalies = json_data['Tmp']
        self.other_tab.set_other_datas(version, mobile_version, world_seed,
                                       force_logout_version, dtls, sentient_anomalies)

        self.update_tabber()
