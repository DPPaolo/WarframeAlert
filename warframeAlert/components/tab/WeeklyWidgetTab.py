# coding=utf-8
from PyQt6 import QtWidgets, QtCore, QtGui

from warframeAlert.components.common.SortieBox import SortieBox
from warframeAlert.components.common.WeeklyMission import WeeklyMission, WeeklyMissionType
from warframeAlert.constants.warframeTypes import LiteSorties
from warframeAlert.services.optionHandlerService import OptionsHandler
from warframeAlert.services.translationService import translate
from warframeAlert.utils.commonUtils import print_traceback
from warframeAlert.utils.gameTranslationUtils import get_mission_type, get_node
from warframeAlert.utils.logUtils import LogHandler


class WeeklyWidgetTab():

    def __init__(self) -> None:
        self.WeeklyWidget = QtWidgets.QWidget()

        self.alerts: dict[str, tuple[str, int]] = {'LiteSorties': ("", 0)}

        self.arcon_box = SortieBox(True)
        self.ArchonWidget = QtWidgets.QWidget()
        self.OtherWidget = QtWidgets.QWidget()

        self.gridArchon = QtWidgets.QGridLayout()
        self.gridOther = QtWidgets.QGridLayout()

        self.WeeklyTabber = QtWidgets.QTabWidget()

        self.OtherScrollBar = QtWidgets.QScrollArea()

        self.OtherScrollBar.setWidgetResizable(True)
        self.OtherScrollBar.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.OtherScrollBar.setBackgroundRole(QtGui.QPalette.ColorRole.NoRole)

        self.ArchonWidget.setLayout(self.arcon_box.SortieBox)
        self.OtherWidget.setLayout(self.gridOther)

        self.OtherScrollBar.setWidget(self.OtherWidget)

        self.WeeklyTabber.insertTab(0, self.ArchonWidget, translate("weeklyWidget", "archon"))
        self.WeeklyTabber.insertTab(1, self.OtherScrollBar, translate("weeklyWidget", "other"))

        self.gridWeekly = QtWidgets.QGridLayout(self.WeeklyWidget)
        self.gridWeekly.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

        self.gridArchon.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.gridOther.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

        self.WeeklyWidget.setLayout(self.gridWeekly)

    def get_widget(self) -> QtWidgets.QWidget:
        return self.WeeklyTabber

    def update_lite_sortie(self, data: LiteSorties) -> None:
        if (OptionsHandler.get_option("Tab/Weekly") == 1):
            try:
                self.parse_other_weekly()
                self.parse_lite_sortie(data)
            except Exception as er:
                LogHandler.err(translate("weeklyWidget", "archonError") + ": " + str(er))
                print_traceback(translate("weeklyWidget", "archonError") + ": " + str(er))
                self.arcon_box.sortie_not_available()
        else:
            self.arcon_box.sortie_not_available()

    def parse_lite_sortie(self, data: LiteSorties) -> None:
        if (data):
            for lite_sortie in data:
                archon_id = lite_sortie['_id']['$oid']
                seed = lite_sortie['Seed']

                actual_archon_id: tuple[str, int] = (archon_id, seed)

                if (self.alerts['LiteSorties'] == actual_archon_id):
                    return

                init = lite_sortie['Activation']['$date']['$numberLong']
                end = lite_sortie['Expiry']['$date']['$numberLong']
                boss = lite_sortie['Boss']
                reward = lite_sortie['Reward']
                self.arcon_box.set_sortie_data(init, end[:10], boss, reward, [])

                num = 0
                for variant in lite_sortie['Missions']:
                    num += 1
                    mission = get_mission_type(variant['missionType'])
                    modifier = ""
                    node, planet = get_node(variant['node'])
                    tile_set = ""
                    self.arcon_box.set_mission_data(num, mission, modifier, node, planet, tile_set)

                self.alerts['LiteSorties'] = actual_archon_id

        else:
            self.arcon_box.SortieBox.sortie_not_available()

    def parse_other_weekly(self) -> None:
        if (self.gridOther.count() == 0):
            maroo_mission = WeeklyMission(WeeklyMissionType.MAROO)
            clem_mission = WeeklyMission(WeeklyMissionType.CLEM)

            self.gridOther.addLayout(maroo_mission.MissionBox, self.gridOther.count(), 0)
            self.gridOther.addLayout(clem_mission.MissionBox, self.gridOther.count(), 0)
