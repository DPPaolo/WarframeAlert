# coding=utf-8
from PyQt5 import QtWidgets, QtCore

from warframeAlert.components.common.FissureBox import FissureBox
from warframeAlert.components.widget.RelicWidget import RelicWidget
from warframeAlert.services.notificationService import NotificationService
from warframeAlert.services.optionHandlerService import OptionsHandler
from warframeAlert.services.translationService import translate
from warframeAlert.utils import timeUtils
from warframeAlert.utils.commonUtils import print_traceback, remove_widget
from warframeAlert.utils.gameTranslationUtils import get_node, get_mission_type, get_region
from warframeAlert.utils.logUtils import LogHandler


class FissureWidgetTab():

    def __init__(self):
        self.alerts = {'ActiveMissions': []}

        self.FissureWidget = QtWidgets.QWidget()
        self.RelicWidget = None

        self.gridFissure = QtWidgets.QGridLayout()

        self.RelicButton = QtWidgets.QPushButton(translate("fissureWidgetTab", "viewRelics"))
        self.RelicButton.clicked.connect(self.open_relics)

        self.FissureBox = QtWidgets.QVBoxLayout()

        self.FissureBox.addLayout(self.gridFissure)
        self.FissureBox.addWidget(self.RelicButton)
        self.FissureBox.addStretch(1)

        self.gridFissureWidget = QtWidgets.QGridLayout(self.FissureWidget)
        self.gridFissureWidget.addLayout(self.FissureBox, 0, 0)

        self.FissureWidget.setLayout(self.gridFissureWidget)

        self.gridFissure.setAlignment(QtCore.Qt.AlignTop)
        self.gridFissureWidget.setAlignment(QtCore.Qt.AlignTop)

    def get_widget(self):
        return self.FissureWidget

    def update_fissure(self, data):
        if (OptionsHandler.get_option("Tab/Fissure") == 1):
            try:
                self.parse_fissure(data)
            except Exception as er:
                LogHandler.err(translate("fissureWidgetTab", "errorRelics") + ": " + str(er))
                print_traceback(translate("fissureWidgetTab", "errorRelics") + ": " + str(er))
                self.reset_fissure()
                return
        else:
            self.reset_fissure()

    def parse_fissure(self, data):
        self.reset_fissure()
        n_fis = len(self.alerts['ActiveMissions'])
        for fissure in data:
            fissure_id = fissure['_id']['$oid']
            init = fissure['Activation']['$date']['$numberLong']  # non usato
            end = fissure['Expiry']['$date']['$numberLong']

            timer = int(end[:10]) - int(timeUtils.get_local_time())
            if (timer > 0):
                found = 0
                for fissures in self.alerts['ActiveMissions']:
                    if (fissures.get_fissure_id() == fissure_id):
                        found = 1

                if (found == 0):
                    node, plan = get_node(fissure['Node'])
                    mis = get_mission_type(fissure['MissionType'])

                    n_tier, tier = get_relic_tier(fissure['Modifier'])
                    seed = fissure['Seed']
                    region = get_region(fissure['Region'] - 1)

                    temp = FissureBox(fissure_id, seed)
                    temp.set_fissure_data(node, plan, mis, init, end, tier, region)
                    self.alerts['ActiveMissions'].append(temp)
                    del temp

        self.add_fissure(n_fis)

    def add_fissure(self, n_fis):
        for i in range(n_fis, len(self.alerts['ActiveMissions'])):
            if (not self.alerts['ActiveMissions'][i].is_expired()):
                self.gridFissure.addLayout(self.alerts['ActiveMissions'][i].FisBox, self.gridFissure.count(), 0)
                NotificationService.send_notification(
                    self.alerts['ActiveMissions'][i].get_title(),
                    self.alerts['ActiveMissions'][i].to_string(),
                    None)

    def reset_fissure(self):
        canc = []
        for i in range(0, len(self.alerts['ActiveMissions'])):
            if (self.alerts['ActiveMissions'][i].is_expired()):
                canc.append(i)
        i = len(canc)
        while i > 0:
            self.alerts['ActiveMissions'][canc[i - 1]].hide()
            remove_widget(self.alerts['ActiveMissions'][canc[i - 1]].FisBox)
            del self.alerts['ActiveMissions'][canc[i - 1]]
            i -= 1

    def open_relics(self):
        self.RelicWidget = RelicWidget()
        self.RelicWidget.show()


def get_relic_tier(tier):
    if (tier[-1] == "1"):
        return 1, "T1 Lith"
    elif (tier[-1] == "2"):
        return 2, "T2 Meso"
    elif (tier[-1] == "3"):
        return 3, "T3 Neo"
    elif (tier[-1] == "4"):
        return 4, "T4 Axi"
    elif (tier[-1] == "5"):
        return 5, "T5 Requiem"
    else:
        print(translate("relicWidget", "unknownRelicTier") + ": " + tier)
        LogHandler.err(translate("relicWidget", "unknownRelicTier") + ": " + tier)
        return tier[-1], tier
