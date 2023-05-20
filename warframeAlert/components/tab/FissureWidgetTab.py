# coding=utf-8
from typing import Tuple

from PyQt6 import QtWidgets, QtCore, QtGui

from warframeAlert.components.common.FissureBox import FissureBox
from warframeAlert.components.widget.RelicWidget import RelicWidget
from warframeAlert.constants.warframeTypes import VoidStorms, ActiveMissions
from warframeAlert.services.notificationService import NotificationService
from warframeAlert.services.optionHandlerService import OptionsHandler
from warframeAlert.services.translationService import translate
from warframeAlert.utils import timeUtils
from warframeAlert.utils.commonUtils import print_traceback, remove_widget
from warframeAlert.utils.gameTranslationUtils import get_node, get_mission_type, get_region
from warframeAlert.utils.logUtils import LogHandler


class FissureWidgetTab():

    def __init__(self) -> None:
        self.alerts = {'ActiveMissions': [], 'HardActiveMissions': [], 'VoidStorms': []}
        self.GeneralFissureWidget = QtWidgets.QWidget()

        self.FissureWidget = QtWidgets.QWidget()
        self.HardFissureWidget = QtWidgets.QWidget()
        self.VoidStormWidget = QtWidgets.QWidget()

        self.gridFissure = QtWidgets.QGridLayout()
        self.gridHardFissure = QtWidgets.QGridLayout()
        self.gridVoidStorm = QtWidgets.QGridLayout()

        self.FissureTabber = QtWidgets.QTabWidget()

        self.NoFissureLabel = QtWidgets.QLabel(translate("fissureWidgetTab", "NoFissure"))
        self.NoHardFissureLabel = QtWidgets.QLabel(translate("fissureWidgetTab", "NoHardFissure"))
        self.NoVoidStormLabel = QtWidgets.QLabel(translate("fissureWidgetTab", "NoVoidStorms"))

        self.gridFissure.addWidget(self.NoFissureLabel, 0, 0)
        self.gridHardFissure.addWidget(self.NoHardFissureLabel, 0, 0)
        self.gridVoidStorm.addWidget(self.NoVoidStormLabel, 0, 0)

        self.FissureScrollBar = QtWidgets.QScrollArea()
        self.HardFissureScrollBar = QtWidgets.QScrollArea()
        self.VoidStormScrollBar = QtWidgets.QScrollArea()

        self.FissureScrollBar.setWidgetResizable(True)
        self.HardFissureScrollBar.setWidgetResizable(True)
        self.VoidStormScrollBar.setWidgetResizable(True)

        self.FissureScrollBar.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.HardFissureScrollBar.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.VoidStormScrollBar.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.FissureScrollBar.setBackgroundRole(QtGui.QPalette.ColorRole.NoRole)
        self.HardFissureScrollBar.setBackgroundRole(QtGui.QPalette.ColorRole.NoRole)
        self.VoidStormScrollBar.setBackgroundRole(QtGui.QPalette.ColorRole.NoRole)

        self.FissureWidget.setLayout(self.gridFissure)
        self.HardFissureWidget.setLayout(self.gridHardFissure)
        self.VoidStormWidget.setLayout(self.gridVoidStorm)

        self.FissureScrollBar.setWidget(self.FissureWidget)
        self.HardFissureScrollBar.setWidget(self.HardFissureWidget)
        self.VoidStormScrollBar.setWidget(self.VoidStormWidget)

        self.FissureTabber.insertTab(0, self.FissureScrollBar, translate("fissureWidgetTab", "NormalFissure"))
        self.FissureTabber.insertTab(1, self.HardFissureScrollBar, translate("fissureWidgetTab", "HardFissure"))
        self.FissureTabber.insertTab(2, self.VoidStormScrollBar, translate("fissureWidgetTab", "VoidStorm"))

        self.RelicWidget = None
        self.RelicButton = QtWidgets.QPushButton(translate("fissureWidgetTab", "viewRelics"))
        self.RelicButton.clicked.connect(self.open_relics)

        self.gridFissure2 = QtWidgets.QGridLayout(self.GeneralFissureWidget)
        self.gridFissure2.addWidget(self.RelicButton, 0, 0)
        self.gridFissure2.addWidget(self.FissureTabber, 1, 0)
        self.gridFissure2.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

        self.gridFissure.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.gridHardFissure.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.gridVoidStorm.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.GeneralFissureWidget.setLayout(self.gridFissure2)

    def get_widget(self) -> QtWidgets.QWidget:
        return self.GeneralFissureWidget

    def update_fissure(self, fissure_data: ActiveMissions, void_storm_data: VoidStorms) -> None:
        if (OptionsHandler.get_option("Tab/Fissure") == 1):
            try:
                self.parse_fissure(fissure_data, void_storm_data)
            except Exception as er:
                LogHandler.err(translate("fissureWidgetTab", "errorRelics") + ": " + str(er))
                print_traceback(translate("fissureWidgetTab", "errorRelics") + ": " + str(er))
                self.reset_fissure()
                return
        else:
            self.reset_fissure()

    def parse_fissure(self, fissure_data: ActiveMissions, void_storm_data: VoidStorms) -> None:
        self.reset_fissure()
        n_fissure = len(self.alerts['ActiveMissions'])
        n_hard_fissure = len(self.alerts['HardActiveMissions'])
        n_void_storm = len(self.alerts['VoidStorms'])

        for fissure in fissure_data:
            fissure_id = fissure['_id']['$oid']
            init = fissure['Activation']['$date']['$numberLong']
            end = fissure['Expiry']['$date']['$numberLong']
            hard = fissure['Hard'] if ('Hard' in fissure) else False

            timer = int(end[:10]) - int(timeUtils.get_local_time())
            if (timer > 0):
                found = 0
                for old_fissure in self.alerts['ActiveMissions']:
                    if (old_fissure.get_fissure_id() == fissure_id):
                        found = 1
                for old_fissure in self.alerts['HardActiveMissions']:
                    if (old_fissure.get_fissure_id() == fissure_id):
                        found = 1

                if (found == 0):
                    node, plan = get_node(fissure['Node'])
                    mis = get_mission_type(fissure['MissionType'])

                    n_tier, tier = get_relic_tier(fissure['Modifier'])
                    seed = fissure['Seed']
                    region = get_region(fissure['Region'] + 1)

                    temp = FissureBox(fissure_id, seed)
                    temp.set_fissure_data(node, plan, mis, init, end, tier, region)
                    if (hard):
                        self.alerts['HardActiveMissions'].append(temp)
                    else:
                        self.alerts['ActiveMissions'].append(temp)
                    del temp

        for void_storm in void_storm_data:
            fissure_id = void_storm['_id']['$oid']
            init = void_storm['Activation']['$date']['$numberLong']
            end = void_storm['Expiry']['$date']['$numberLong']

            timer = int(end[:10]) - int(timeUtils.get_local_time())
            if (timer > 0):
                found = 0
                for old_void_storms in self.alerts['VoidStorms']:
                    if (old_void_storms.get_fissure_id() == fissure_id):
                        found = 1

                if (found == 0):
                    node, plan = get_node(void_storm['Node'])
                    mis = "Railjack"

                    n_tier, tier = get_relic_tier(void_storm['ActiveMissionTier'])

                    temp = FissureBox(fissure_id, -1)
                    temp.set_fissure_data(node, plan, mis, init, end, tier, "")
                    self.alerts['VoidStorms'].append(temp)
                    del temp

        self.add_fissure(n_fissure)
        self.add_hard_fissure(n_hard_fissure)
        self.add_void_storm(n_void_storm)

    def add_fissure(self, n_fissure: int) -> None:
        for i in range(n_fissure, len(self.alerts['ActiveMissions'])):
            if (not self.alerts['ActiveMissions'][i].is_expired()):
                self.gridFissure.addLayout(self.alerts['ActiveMissions'][i].FisBox, self.gridFissure.count(), 0)
                NotificationService.send_notification(
                    self.alerts['ActiveMissions'][i].get_title(),
                    self.alerts['ActiveMissions'][i].to_string(),
                    None)
        if (len(self.alerts['ActiveMissions']) > 0):
            self.NoFissureLabel.hide()

    def add_hard_fissure(self, n_fis: int) -> None:
        for i in range(n_fis, len(self.alerts['HardActiveMissions'])):
            if (not self.alerts['HardActiveMissions'][i].is_expired()):
                self.gridHardFissure.addLayout(self.alerts['HardActiveMissions'][i].FisBox,
                                               self.gridHardFissure.count(),
                                               0)
                NotificationService.send_notification(
                    self.alerts['HardActiveMissions'][i].get_title(),
                    self.alerts['HardActiveMissions'][i].to_string(),
                    None)
        if (len(self.alerts['HardActiveMissions']) > 0):
            self.NoHardFissureLabel.hide()

    def add_void_storm(self, n_fis: int) -> None:
        for i in range(n_fis, len(self.alerts['VoidStorms'])):
            if (not self.alerts['VoidStorms'][i].is_expired()):
                self.gridVoidStorm.addLayout(self.alerts['VoidStorms'][i].FisBox, self.gridVoidStorm.count(), 0)
                NotificationService.send_notification(
                    self.alerts['VoidStorms'][i].get_title(),
                    self.alerts['VoidStorms'][i].to_string(),
                    None)

        if (len(self.alerts['VoidStorms']) > 0):
            self.NoVoidStormLabel.hide()

    def reset_fissure(self) -> None:
        self.NoFissureLabel.show()
        self.NoHardFissureLabel.show()
        self.NoVoidStormLabel.show()

        cancelled_fissure = []
        for i in range(0, len(self.alerts['ActiveMissions'])):
            if (self.alerts['ActiveMissions'][i].is_expired()):
                cancelled_fissure.append(i)
        i = len(cancelled_fissure)
        while i > 0:
            self.alerts['ActiveMissions'][cancelled_fissure[i - 1]].hide()
            remove_widget(self.alerts['ActiveMissions'][cancelled_fissure[i - 1]].FisBox)
            del self.alerts['ActiveMissions'][cancelled_fissure[i - 1]]
            i -= 1

        cancelled_fissure = []
        for i in range(0, len(self.alerts['HardActiveMissions'])):
            if (self.alerts['HardActiveMissions'][i].is_expired()):
                cancelled_fissure.append(i)
        i = len(cancelled_fissure)
        while i > 0:
            self.alerts['HardActiveMissions'][cancelled_fissure[i - 1]].hide()
            remove_widget(self.alerts['HardActiveMissions'][cancelled_fissure[i - 1]].FisBox)
            del self.alerts['HardActiveMissions'][cancelled_fissure[i - 1]]
            i -= 1

        cancelled_fissure = []
        for i in range(0, len(self.alerts['VoidStorms'])):
            if (self.alerts['VoidStorms'][i].is_expired()):
                cancelled_fissure.append(i)
        i = len(cancelled_fissure)
        while i > 0:
            self.alerts['VoidStorms'][cancelled_fissure[i - 1]].hide()
            remove_widget(self.alerts['VoidStorms'][cancelled_fissure[i - 1]].FisBox)
            del self.alerts['VoidStorms'][cancelled_fissure[i - 1]]
            i -= 1

    def open_relics(self) -> None:
        self.RelicWidget = RelicWidget()
        self.RelicWidget.show()


def get_relic_tier(tier: str) -> Tuple[int, str]:
    match tier[-1]:
        case "1":
            return 1, "T1 Lith"
        case "2":
            return 2, "T2 Meso"
        case "3":
            return 3, "T3 Neo"
        case "4":
            return 4, "T4 Axi"
        case "5":
            return 5, "T5 Requiem"
        case _:
            print(translate("relicWidget", "unknownRelicTier") + ": " + tier)
            LogHandler.err(translate("relicWidget", "unknownRelicTier") + ": " + tier)
            return int(tier[-1]), tier
