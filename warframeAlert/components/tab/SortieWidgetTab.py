# coding=utf-8
from PyQt5 import QtWidgets

from warframeAlert.components.common.SortieBox import SortieBox
from warframeAlert.services.optionHandlerService import OptionsHandler
from warframeAlert.services.translationService import translate
from warframeAlert.utils.commonUtils import print_traceback
from warframeAlert.utils.gameTranslationUtils import get_mission_type, get_map_type, get_node, get_sortie_modifier
from warframeAlert.utils.logUtils import LogHandler


class SortieWidgetTab():

    def __init__(self):
        self.alerts = {'Sorties': (0, 0, False)}

        self.SortieWidget = QtWidgets.QWidget()

        self.SortieBox = SortieBox()

        self.gridSortie = QtWidgets.QGridLayout(self.SortieWidget)
        self.gridSortie.addLayout(self.SortieBox.SortieBox, 0, 0)

        self.SortieWidget.setLayout(self.gridSortie)

    def get_widget(self):
        return self.SortieWidget

    def update_sortie(self, data):
        if (OptionsHandler.get_option("Tab/Sortie") == 1):
            try:
                self.parse_sortie(data)
            except Exception as er:
                LogHandler.err(translate("sortieWidgetTab", "sortieError") + ": " + str(er))
                print_traceback(translate("sortieWidgetTab", "sortieError") + ": " + str(er))
                self.SortieBox.sortie_not_available()
        else:
            self.SortieBox.sortie_not_available()

    def parse_sortie(self, data):
        if (data):
            for sortie in data:
                sortie_id = sortie['_id']['$oid']
                seed = sortie['Seed']
                twitter = sortie['Twitter'] if ('Twitter' in sortie) else False

                actual_sortie_id = (sortie_id, seed, twitter)

                if (self.alerts['Sorties'] == actual_sortie_id):
                    return

                init = sortie['Activation']['$date']['$numberLong']
                end = sortie['Expiry']['$date']['$numberLong']
                boss = sortie['Boss']
                reward = sortie['Reward']
                extra_reward = sortie['ExtraDrops']
                self.SortieBox.set_sortie_data(init, end[:10], boss, reward, extra_reward)

                num = 0
                for variant in sortie['Variants']:
                    num += 1
                    mission = get_mission_type(variant['missionType'])
                    modifier = get_sortie_modifier(variant['modifierType'])
                    node, planet = get_node(variant['node'])
                    tileset = get_map_type(variant['tileset'])
                    self.SortieBox.set_mission_data(num, mission, modifier, node, planet, tileset)

                self.alerts['Sorties'] = actual_sortie_id

        else:
            self.SortieBox.sortie_not_available()
