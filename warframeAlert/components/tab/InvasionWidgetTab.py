# coding=utf-8
from PyQt5 import QtWidgets, QtCore, QtGui

from warframeAlert.components.common.Invasion import Invasion
from warframeAlert.components.common.InvasionNode import InvasionNode
from warframeAlert.services.notificationService import NotificationService
from warframeAlert.services.optionHandlerService import OptionsHandler
from warframeAlert.services.translationService import translate
from warframeAlert.utils import commonUtils, timeUtils
from warframeAlert.utils.commonUtils import remove_widget
from warframeAlert.utils.gameTranslationUtils import get_node, get_faction, get_invasion_loctag
from warframeAlert.utils.logUtils import LogHandler
from warframeAlert.utils.warframeUtils import parse_reward


class InvasionWidgetTab():

    def __init__(self):
        self.InvasionWidget = QtWidgets.QWidget()

        self.alerts = {'Invasions': {'Grineer': [], 'Corpus': [], 'Infested': []}, 'NodeOverrides': []}

        self.InvGrineerWidget = QtWidgets.QWidget()
        self.InvCorpusWidget = QtWidgets.QWidget()
        self.InvInfestedWidget = QtWidgets.QWidget()
        self.InvOccWidget = QtWidgets.QWidget()

        self.gridGInv = QtWidgets.QGridLayout()
        self.gridCInv = QtWidgets.QGridLayout()
        self.gridIInv = QtWidgets.QGridLayout()
        self.gridOccInv = QtWidgets.QGridLayout()

        self.Invtabber = QtWidgets.QTabWidget()

        self.NoInvG = QtWidgets.QLabel(translate("invasionWidget", "NoGrineerInvasion"))
        self.NoInvC = QtWidgets.QLabel(translate("invasionWidget", "NoCorpusInvasion"))
        self.NoInvI = QtWidgets.QLabel(translate("invasionWidget", "NoInfestedInvasion"))
        self.NoInvOcc = QtWidgets.QLabel(translate("invasionWidget", "NoNodeOccuped"))

        self.gridGInv.addWidget(self.NoInvG, 0, 0)
        self.gridCInv.addWidget(self.NoInvC, 0, 0)
        self.gridIInv.addWidget(self.NoInvI, 0, 0)
        self.gridOccInv.addWidget(self.NoInvOcc, 0, 0)

        self.FomorLabel = QtWidgets.QLabel(translate("invasionWidget", "fomorian") + " :")
        self.RazorLabel = QtWidgets.QLabel(translate("invasionWidget", "razorback") + " :")
        self.FomorPer = QtWidgets.QProgressBar(self.InvasionWidget)
        self.RazorPer = QtWidgets.QProgressBar(self.InvasionWidget)
        self.FomorPer.setMaximum(100)
        self.FomorPer.setMaximum(100)

        self.InvScrollBarG = QtWidgets.QScrollArea()
        self.InvScrollBarC = QtWidgets.QScrollArea()
        self.InvScrollBarI = QtWidgets.QScrollArea()
        self.InvScrollBarO = QtWidgets.QScrollArea()

        self.InvScrollBarG.setWidgetResizable(True)
        self.InvScrollBarC.setWidgetResizable(True)
        self.InvScrollBarI.setWidgetResizable(True)
        self.InvScrollBarO.setWidgetResizable(True)
        self.InvScrollBarG.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.InvScrollBarC.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.InvScrollBarI.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.InvScrollBarO.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.InvScrollBarG.setBackgroundRole(QtGui.QPalette.NoRole)
        self.InvScrollBarC.setBackgroundRole(QtGui.QPalette.NoRole)
        self.InvScrollBarI.setBackgroundRole(QtGui.QPalette.NoRole)
        self.InvScrollBarO.setBackgroundRole(QtGui.QPalette.NoRole)

        self.InvGrineerWidget.setLayout(self.gridGInv)
        self.InvCorpusWidget.setLayout(self.gridCInv)
        self.InvInfestedWidget.setLayout(self.gridIInv)
        self.InvOccWidget.setLayout(self.gridOccInv)

        self.InvScrollBarG.setWidget(self.InvGrineerWidget)
        self.InvScrollBarC.setWidget(self.InvCorpusWidget)
        self.InvScrollBarI.setWidget(self.InvInfestedWidget)
        self.InvScrollBarO.setWidget(self.InvOccWidget)

        self.Invtabber.insertTab(0, self.InvScrollBarG, translate("invasionWidget", "GrineerInvasion"))
        self.Invtabber.insertTab(1, self.InvScrollBarC, translate("invasionWidget", "CorpusInvasion"))
        self.Invtabber.insertTab(2, self.InvScrollBarI, translate("invasionWidget", "InfestedInvasion"))
        self.Invtabber.insertTab(3, self.InvScrollBarO, translate("invasionWidget", "OccupiedNode"))

        self.gridInv2 = QtWidgets.QGridLayout(self.InvasionWidget)
        self.gridInv2.addWidget(self.FomorLabel, 0, 0)
        self.gridInv2.addWidget(self.FomorPer, 0, 1)
        self.gridInv2.addWidget(self.RazorLabel, 0, 2)
        self.gridInv2.addWidget(self.RazorPer, 0, 3)
        self.gridInv2.addWidget(self.Invtabber, 1, 0, 1, 4)
        self.gridInv2.setAlignment(QtCore.Qt.AlignTop)

        self.gridGInv.setAlignment(QtCore.Qt.AlignTop)
        self.gridCInv.setAlignment(QtCore.Qt.AlignTop)
        self.gridIInv.setAlignment(QtCore.Qt.AlignTop)
        self.gridOccInv.setAlignment(QtCore.Qt.AlignTop)

        self.InvasionWidget.setLayout(self.gridInv2)

    def get_widget(self):
        return self.InvasionWidget

    def update_tab(self):
        self.Invtabber.insertTab(3, self.InvScrollBarO, translate("invasionWidget", "OccupiedNode"))

        if (not len(self.alerts['NodeOverrides']) > 0):
            self.Invtabber.removeTab(self.Invtabber.indexOf(self.InvScrollBarO))

    def update_invasion(self, data):
        if (OptionsHandler.get_option("Tab/Invasion") == 1):
            try:
                self.parse_invasion(data)
            except Exception as er:
                LogHandler.err(translate("invasionWidget", "invasionUpdateError") + ": " + str(er))
                commonUtils.print_traceback(translate("invasionWidget", "invasionUpdateError") + ": " + str(er))
                self.reset_invasion()

    def parse_invasion(self, data):
        self.reset_invasion()
        n_inv_g = len(self.alerts['Invasions']['Grineer'])
        n_inv_c = len(self.alerts['Invasions']['Corpus'])
        n_inv_i = len(self.alerts['Invasions']['Infested'])
        for invasion in data:
            try:
                invasion_id = invasion['_id']['$oid']
            except KeyError:
                invasion_id = invasion['_id']['$id']
            completed = invasion['Completed']
            count = invasion['Count']
            goal = invasion['Goal']
            attacker_faction = get_faction(invasion['AttackerMissionInfo']['faction'])
            defender_faction = get_faction(invasion['DefenderMissionInfo']['faction'])
            percentage = [count, goal, 0]
            if (defender_faction == "Infested"):
                percentage[2] = 1

            found = 0
            for inv in self.alerts['Invasions'][defender_faction]:
                if (inv.get_invasion_id() == invasion_id):
                    found = 1
                    inv.set_invasion_perc(percentage)
                    inv.set_completed(completed)

            if (found == 0):
                try:
                    init = invasion['Activation']['$date']['$numberLong']
                except KeyError:
                    init = str((int(timeUtils.get_local_time())) * 1000)
                chain_id = ""
                if ('ChainID' in invasion):
                    chain_id = invasion["ChainID"]

                temp = Invasion(invasion_id, chain_id)
                temp.set_completed(completed)
                if (temp.is_completed()):
                    del temp
                    continue

                node, planet = get_node(invasion['Node'])
                loc_tag = get_invasion_loctag(invasion['LocTag'])
                if (len(invasion['AttackerReward']) > 0):
                    attacker_reward_item = invasion['AttackerReward']['countedItems'][0]['ItemType']
                    attacker_reward = parse_reward(invasion['AttackerReward'])
                else:
                    attacker_reward_item = ""
                    attacker_reward = ""
                if (len(invasion['DefenderReward']) > 0):
                    defender_reward_item = invasion['DefenderReward']['countedItems'][0]['ItemType']
                    defender_reward = parse_reward(invasion['DefenderReward'])
                else:
                    defender_reward_item = ""
                    defender_reward = ""

                temp.set_invasion_data(node, planet, attacker_faction, defender_faction)
                temp.set_invasion_info(init, loc_tag, percentage)
                temp.set_invasion_reward(attacker_reward, defender_reward, attacker_reward_item, defender_reward_item)
                self.alerts['Invasions'][defender_faction].append(temp)

                del temp

        self.add_invasions(n_inv_g, n_inv_c, n_inv_i)

    def add_invasions(self, n_inv_g, n_inv_c, n_inv_i):
        for i in range(n_inv_g, len(self.alerts['Invasions']['Grineer'])):
            if (not self.alerts['Invasions']['Grineer'][i].is_completed()):
                self.gridGInv.addLayout(self.alerts['Invasions']['Grineer'][i].InvasionBox, self.gridGInv.count(), 0)
                NotificationService.send_notification(
                    self.alerts['Invasions']['Grineer'][i].get_title(),
                    self.alerts['Invasions']['Grineer'][i].to_string(),
                    None)
        for i in range(n_inv_c, len(self.alerts['Invasions']['Corpus'])):
            if (not self.alerts['Invasions']['Corpus'][i].is_completed()):
                self.gridCInv.addLayout(self.alerts['Invasions']['Corpus'][i].InvasionBox, self.gridCInv.count(), 0)
                NotificationService.send_notification(
                    self.alerts['Invasions']['Corpus'][i].get_title(),
                    self.alerts['Invasions']['Corpus'][i].to_string(),
                    None)
        for i in range(n_inv_i, len(self.alerts['Invasions']['Infested'])):
            if (not self.alerts['Invasions']['Infested'][i].is_completed()):
                self.gridIInv.addLayout(self.alerts['Invasions']['Infested'][i].InvasionBox, self.gridIInv.count(), 0)
                NotificationService.send_notification(
                    self.alerts['Invasions']['Infested'][i].get_title(),
                    self.alerts['Invasions']['Infested'][i].to_string(),
                    None)
        if (len(self.alerts['Invasions']['Grineer']) > 0):
            self.NoInvG.hide()
        if (len(self.alerts['Invasions']['Corpus']) > 0):
            self.NoInvC.hide()
        if (len(self.alerts['Invasions']['Infested']) > 0):
            self.NoInvI.hide()

    def reset_invasion(self):
        self.NoInvG.show()
        self.NoInvC.show()
        self.NoInvI.show()
        inv = self.alerts['Invasions']
        for temp in [inv['Grineer'], inv['Corpus'], inv['Infested']]:
            canc = []
            for i in range(0, len(temp)):
                if (temp[i].is_completed()):
                    canc.append(i)
            i = len(canc)
            while i > 0:
                temp[canc[i-1]].hide()
                remove_widget(temp[canc[i-1]].InvasionBox)
                del temp[canc[i-1]]
                i -= 1

    def update_node_ovveride(self, data):
        if (OptionsHandler.get_option("Tab/Invasion") == 1):
            try:
                self.parse_node_override(data)
            except Exception as er:
                LogHandler.err(translate("invasionWidget", "nodeOverrideUpdateError") + ": " + str(er))
                commonUtils.print_traceback(translate("invasionWidget", "nodeOverrideUpdateError") + ": " + str(er))
                self.reset_invasion_node()

    def parse_node_override(self, data):
        self.reset_invasion_node()
        n_nod = len(self.alerts['NodeOverrides'])
        for nod in data:
            try:
                node_id = nod['_id']['$oid']
            except KeyError:
                node_id = nod['_id']['$id']
            node = get_node(nod['Node'])
            if ('Faction' in nod):
                for override in self.alerts['NodeOverrides']:
                    found = 0
                    if (override.get_node_id() == node_id):
                        found = 1

                    if (found == 0):
                        try:
                            expiry = nod['Expiry']['$date']['$numberLong']
                        except KeyError:
                            expiry = str((int(timeUtils.get_local_time()) + 3600) * 1000)
                        faction = get_faction(nod['Faction'])

                        timer = int(expiry[:10]) - int(timeUtils.get_local_time())
                        if (timer > 0):
                            temp = InvasionNode(node_id)
                            temp.set_invasion_node_data(faction, node, expiry)

                            self.alerts['NodeOverrides'].append(temp)
                            del temp

        self.add_invasion_node(n_nod)

    def add_invasion_node(self, n_nod):
        for i in range(n_nod, len(self.alerts['NodeOverrides'])):
            if (not self.alerts['NodeOverrides'][i].is_expired()):
                self.gridOccInv.addLayout(self.alerts['NodeOverrides'][i].InvasionNodeBox, self.gridOccInv.count(), 0)

        if (len(self.alerts['NodeOverrides']) > 0):
            self.NoInvOcc.hide()

    def reset_invasion_node(self):
        self.NoInvOcc.show()
        canc = []
        for i in range(0, len(self.alerts['NodeOverrides'])):
            if (self.alerts['NodeOverrides'][i].is_expired()):
                canc.append(i)
        i = len(canc)
        while i > 0:
            self.alerts['NodeOverrides'][canc[i-1]].hide()
            remove_widget(self.alerts['NodeOverrides'][canc[i-1]].InvasionNodeBox)
            del self.alerts['NodeOverrides'][canc[i-1]]
            i -= 1

    def update_invasion_project(self, data):
        try:
            self.parse_invasion_project(data)
        except Exception as er:
            LogHandler.err(translate("invasionWidget", "invasionProjectUpdateError") + ": " + str(er))
            commonUtils.print_traceback(translate("invasionWidget", "invasionProjectUpdateError") + ": " + str(er))
            self.reset_invasion_project()

    def parse_invasion_project(self, data):
        self.reset_invasion_project()
        fomor = data[0]
        razor = data[1]
        unk = data[2]
        if (unk != 0):
            print(translate("invasionWidget", "unknownInvasionProject") + str(unk))
        self.set_invasion_project(fomor, razor)

    def set_invasion_project(self, fomor, razor):
        self.FomorPer.setToolTip(str(fomor) + "%")
        self.RazorPer.setToolTip(str(razor) + "%")
        if (float(fomor) >= 100):
            fomor = 100
        if (float(razor) >= 100):
            razor = 100
        self.FomorPer.setValue(float(fomor))
        self.RazorPer.setValue(float(razor))

    def reset_invasion_project(self):
        self.FomorPer.reset()
        self.RazorPer.reset()
