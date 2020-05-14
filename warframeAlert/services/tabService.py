# coding=utf-8
import json

from jsonschema import ValidationError

from warframeAlert.components.common.MessageBox import MessageBox, MessageBoxType
from warframeAlert.components.tab.AccolyteWidgetTab import AccolyteWidgetTab
from warframeAlert.components.tab.BountyWidgetTab import BountyWidgetTab
from warframeAlert.components.tab.EventsWidgetTab import EventsWidgetTab
from warframeAlert.components.tab.InvasionWidgetTab import InvasionWidgetTab
from warframeAlert.components.tab.NewsWidgetTab import NewsWidgetTab
from warframeAlert.components.tab.NightwaveWidgetTab import NightwaveWidgetTab
from warframeAlert.components.tab.OtherWidgetTab import OtherWidgetTab
from warframeAlert.components.tab.SyndicateWidgetTab import SyndicateWidgetTab
from warframeAlert.services.optionHandlerService import OptionsHandler
from warframeAlert.services.translationService import translate
from warframeAlert.utils.commonUtils import print_traceback
from warframeAlert.utils.fileUtils import get_separator
from warframeAlert.utils.logUtils import LogHandler
from warframeAlert.utils.validatorUtils import check_json_data


class TabService():

    def __init__(self, tabber):
        self.mainTabber = tabber

        self.news_tab = NewsWidgetTab()
        self.nightwave_tab = NightwaveWidgetTab()
        self.event_tab = EventsWidgetTab()
        self.bounty_tab = BountyWidgetTab()
        self.invasion_tab = InvasionWidgetTab()
        # self.tab_sortie = warframeClass.tab_sortie()
        self.syndicate_tab = SyndicateWidgetTab()
        # self.tab_fissure = warframeClass.tab_fissure()
        # self.tab_baro = warframeClass.tab_baro()
        # self.tab_pvp = warframeClass.tab_pvp()
        self.accolyte_tab = AccolyteWidgetTab()
        # self.tab_sconti = warframeClass.tab_sconti()
        self.other_tab = OtherWidgetTab()

        # Creazione Widget Tabber
        # self.SortieWidget = self.tab_sortie.get_widget()
        # self.FisWidget = self.tab_fissure.get_widget()
        # self.BaroWidget = self.tab_baro.get_widget()
        # self.PvPWidget = self.tab_pvp.get_widget()
        # self.MerWidget = self.tab_sconti.get_widget()

    def update_tabber(self):
        index = self.mainTabber.currentIndex()
        self.mainTabber.insertTab(0, self.news_tab.get_widget(), translate("tabService", "news"))
        self.mainTabber.insertTab(1, self.nightwave_tab.get_widget(), translate("tabService", "nightwave"))
        self.mainTabber.insertTab(2, self.event_tab.get_widget(), translate("tabService", "events"))
        self.mainTabber.insertTab(3, self.accolyte_tab.get_widget(), translate("tabService", "acolyte"))
        self.mainTabber.insertTab(4, self.bounty_tab.get_widget(), translate("tabService", "bounty"))
        self.mainTabber.insertTab(5, self.invasion_tab.get_widget(), translate("tabService", "invasion"))
        #self.mainTabber.insertTab(6, self.SortieWidget, translate("tabService", "sortie"))
        self.mainTabber.insertTab(7, self.syndicate_tab.get_widget(), translate("tabService", "syndicate"))
        #self.mainTabber.insertTab(8, self.FisWidget, translate("tabService", "fissure"))
        #self.mainTabber.insertTab(9, self.BaroWidget, translate("tabService", "baro"))
        #self.mainTabber.insertTab(10, self.MerWidget, translate("tabService", "sales"))
        #self.mainTabber.insertTab(11, self.PvPWidget, translate("tabService", "pvp"))
        self.mainTabber.insertTab(12, self.other_tab.get_widget(), translate("tabService", "other"))

        n_event = self.event_tab.get_lenght()
        n_acc = self.accolyte_tab.get_lenght()

        if (not OptionsHandler.get_option("Tab/News") == 1):
            self.mainTabber.removeTab(self.mainTabber.indexOf(self.news_tab.get_widget()))
        if (not OptionsHandler.get_option("Tab/Nightwave") == 1):
            self.mainTabber.removeTab(self.mainTabber.indexOf(self.nightwave_tab.get_widget()))
        if (not (n_event > 0) or not OptionsHandler.get_option("Tab/TactAll") == 1):
            self.mainTabber.removeTab(self.mainTabber.indexOf(self.event_tab.get_widget()))
        if (not (n_acc > 0) or not OptionsHandler.get_option("Tab/Accolyt") == 1):
            self.mainTabber.removeTab(self.mainTabber.indexOf(self.accolyte_tab.get_widget()))
        if (not OptionsHandler.get_option("Tab/Cetus") == 1):
            self.mainTabber.removeTab(self.mainTabber.indexOf(self.bounty_tab.get_widget()))
        if (not OptionsHandler.get_option("Tab/Invasion") == 1):
            self.mainTabber.removeTab(self.mainTabber.indexOf(self.invasion_tab.get_widget()))
        # if (not OptionsHandler.get_option("Tab/Sortie") == 1):
        #    self.mainTabber.removeTab(self.tabber.indexOf(self.SortieWidget))
        if (not OptionsHandler.get_option("Tab/Syndicate") == 1):
            self.mainTabber.removeTab(self.mainTabber.indexOf(self.syndicate_tab.get_widget()))
        # if (not OptionsHandler.get_option("Tab/Fissure") == 1):
        #    self.mainTabber.removeTab(self.tabber.indexOf(self.FisWidget))
        # if (not OptionsHandler.get_option("Tab/Baro") == 1):
        #    self.mainTabber.removeTab(self.tabber.indexOf(self.BaroWidget))
        # if (not OptionsHandler.get_option("Tab/Market") == 1):
        #    self.mainTabber.removeTab(self.tabber.indexOf(self.MerWidget))
        # if (not OptionsHandler.get_option("Tab/PVP") == 1):
        #    self.mainTabber.removeTab(self.tabber.indexOf(self.PvPWidget))
        if (not OptionsHandler.get_option("Tab/Other") == 1):
            self.mainTabber.removeTab(self.mainTabber.indexOf(self.other_tab.get_widget()))

        self.event_tab.update_tab()
        self.invasion_tab.update_tab()
        # self.tab_sconti.update_tab()
        self.other_tab.update_tab()
        # self.tab_pvp.update_tab()

        self.mainTabber.setCurrentIndex(index)

    def update(self, path):
        if (not path):
            path = "data" + get_separator() + "allerte.json"
        try:
            fp = open(path, "rb")
            data = fp.readlines()
        except Exception as error:
            MessageBox("", translate("tabService", "alertError") + "\n" + str(error), MessageBoxType.ERROR)
            print_traceback(translate("tabService", "alertError") + str(error))
            LogHandler.err(str(error))
            return
        fp.close()

        # Aggiorno ogni scheda
        data = data[0].decode('utf-8')
        json_data = json.loads(data)
        if (OptionsHandler.get_option("Debug") == 1):
            try:
                check_json_data(json_data)
            except ValidationError as validation_error:
                LogHandler.debug(translate("tabService", "validationError"))
                LogHandler.debug(validation_error)
                return

        build_label = json_data['BuildLabel']
        game_time = json_data['Time']

        #self.update_fissure(json_data['ActiveMissions'])

        self.event_tab.update_alert_mission(json_data['Alerts'])

        #self.update_dark_sector(json_data['BadlandNodes'])

        self.news_tab.update_news_info(build_label, game_time)
        self.other_tab.update_daily_deals(json_data['DailyDeals'])

        #self.update_sales(json_data['FlashSales'])

        self.event_tab.update_events(json_data['Goals'], json_data['ConstructionProjects'])
        self.news_tab.update_global_upgrades(json_data['GlobalUpgrades'])
        self.news_tab.update_news(json_data['Events'])
        self.other_tab.update_featured_dojo(json_data['FeaturedGuilds'])
        self.other_tab.update_hub_event(json_data['HubEvents'])
        self.invasion_tab.update_invasion(json_data['Invasions'])
        self.other_tab.update_simaris_target(json_data['LibraryInfo'])
        self.other_tab.update_relay_station(json_data['NodeOverrides'])
        self.invasion_tab.update_node_ovveride(json_data['NodeOverrides'])

        #self.update_PVP_tournament(json_data['PVPActiveTournaments'])
        #self.update_PVP_alternative_mission(json_data['PVPAlternativeModes'])
        #self.update_PVP_mission(json_data['PVPChallengeInstances'])

        self.accolyte_tab.update_accolyte(json_data['PersistentEnemies'])
        self.other_tab.update_prime_access(json_data['PrimeAccessAvailability'], json_data['PrimeVaultAvailabilities'])
        self.invasion_tab.update_invasion_project(json_data['ProjectPct'])
        if ('SeasonInfo' in json_data):
            self.nightwave_tab.update_nightwave_season(json_data['SeasonInfo'])
        else:
            self.nightwave_tab.season_not_available()

        #self.update_sortie(json_data['Sorties'])

        self.syndicate_tab.update_syndicate(json_data['SyndicateMissions'])
        self.bounty_tab.update_bounties(json_data['SyndicateMissions'])
        self.other_tab.update_twitch_promo(json_data['TwitchPromos'])

        #self.update_baro(json_data['VoidTraders'])

        version = json_data['Version']
        mob_version = json_data['MobileVersion']
        world_seed = json_data['WorldSeed']
        force_logout_version = json_data['ForceLogoutVersion']
        self.other_tab.set_other_datas(version, mob_version, world_seed, force_logout_version)

        self.update_tabber()