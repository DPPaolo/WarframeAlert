# coding=utf-8
from PyQt5 import QtWidgets, QtCore

from warframeAlert.components.common.Accolyte import Accolyte
from warframeAlert.services.notificationService import NotificationService
from warframeAlert.services.optionHandlerService import OptionsHandler
from warframeAlert.services.translationService import translate
from warframeAlert.utils import timeUtils
from warframeAlert.utils.commonUtils import remove_widget, print_traceback, bool_to_yes_no
from warframeAlert.utils.gameTranslationUtils import get_accolyte_name, get_node, get_region
from warframeAlert.utils.logUtils import LogHandler


class AccolyteWidgetTab():

    def __init__(self):
        self.alerts = {'PersistentEnemies': []}
        self.accolyteWidget = QtWidgets.QWidget()

        self.gridAcc = QtWidgets.QGridLayout(self.accolyteWidget)

        self.accolyteWidget.setLayout(self.gridAcc)

        self.gridAcc.setAlignment(QtCore.Qt.AlignTop)

    def get_widget(self):
        return self.accolyteWidget

    def get_lenght(self):
        return len(self.alerts['PersistentEnemies'])

    def update_accolyte(self, data):
        if (OptionsHandler.get_option("Tab/Accolyt") == 1):
            try:
                self.parse_accolyte(data)
            except Exception as er:
                LogHandler.err(translate("accolyteWidgetTab", "accolyteParsingError") + ": " + str(er))
                print_traceback(translate("accolyteWidgetTab", "accolyteParsingError") + ": " + str(er))
                self.accolyte_not_available()
        else:
            self.accolyte_not_available()

    def parse_accolyte(self, data):
        n_acc = len(self.alerts['PersistentEnemies'])
        for acc in data:
            try:
                acc_id = acc['_id']['$oid']
            except KeyError:
                acc_id = acc['_id']['$id']
            try:
                region = get_region(acc['Region'])
            except KeyError:
                region = translate("accolyteWidgetTab", "noRegion")
            if (acc['LastDiscoveredLocation'] == ""):
                node = translate("accolyteWidgetTab", "noDiscovered")
                planet = ""
            else:
                node, planet = get_node(acc['LastDiscoveredLocation'])
            per = acc['HealthPercent']
            time = timeUtils.get_time(acc['LastDiscoveredTime']['$date']['$numberLong'])  # non usato
            discovered = bool_to_yes_no(acc['Discovered'])

            found = 0
            for accolyte in self.alerts['PersistentEnemies']:
                if (accolyte.get_acc_id() == acc_id):
                    found = 1
                    accolyte.set_acc_position(per, time, discovered, node, planet, region)

            if (found == 0):
                ticket = bool_to_yes_no(acc['UseTicketing'])
                loctag = acc['LocTag']
                name = get_accolyte_name(acc['AgentType'])
                icon = acc['Icon']
                level = acc['Rank']
                flee = acc['FleeDamage']

                temp = Accolyte(acc_id)
                temp.set_acc_data(name, level, icon, flee, ticket, loctag)
                temp.set_acc_position(per, time, discovered, node, planet, region)
                self.alerts['PersistentEnemies'].append(temp)
                del temp

        self.add_accolytes(n_acc)

    def add_accolytes(self, n_acc):
        for i in range(n_acc, len(self.alerts['PersistentEnemies'])):
            if (not self.alerts['PersistentEnemies'][i].is_dead()):
                self.gridAcc.addLayout(self.alerts['PersistentEnemies'][i].AccBox, self.gridAcc.count(), 0)
                NotificationService.send_notification(
                    self.alerts['PersistentEnemies'][i].get_title(),
                    self.alerts['PersistentEnemies'][i].to_string(),
                    None)

    def accolyte_not_available(self):
        for i in reversed(range(0, len(self.alerts['PersistentEnemies']))):
            self.alerts['PersistentEnemies'][i].hide()
            remove_widget(self.alerts['PersistentEnemies'][i].AccBox)
            del self.alerts['PersistentEnemies'][i]
