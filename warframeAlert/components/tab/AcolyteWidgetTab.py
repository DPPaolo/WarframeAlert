# coding=utf-8
from PyQt5 import QtWidgets, QtCore

from warframeAlert.components.common.Acolyte import Acolyte
from warframeAlert.constants.warframeTypes import PersistentEnemies
from warframeAlert.services.notificationService import NotificationService
from warframeAlert.services.optionHandlerService import OptionsHandler
from warframeAlert.services.translationService import translate
from warframeAlert.utils import timeUtils
from warframeAlert.utils.commonUtils import remove_widget, print_traceback, bool_to_yes_no, create_pixmap
from warframeAlert.utils.gameTranslationUtils import get_accolyte_name, get_node, get_region
from warframeAlert.utils.logUtils import LogHandler


class AcolyteWidgetTab():

    def __init__(self) -> None:
        self.alerts = {'PersistentEnemies': []}
        self.acolyteWidget = QtWidgets.QWidget()

        self.gridAcc = QtWidgets.QGridLayout(self.acolyteWidget)

        self.acolyteWidget.setLayout(self.gridAcc)

        self.gridAcc.setAlignment(QtCore.Qt.AlignTop)

    def get_widget(self) -> QtWidgets.QWidget:
        return self.acolyteWidget

    def get_length(self) -> int:
        return len(self.alerts['PersistentEnemies'])

    def update_acolyte(self, data: PersistentEnemies) -> None:
        if (OptionsHandler.get_option("Tab/Acolyte") == 1):
            try:
                self.parse_acolyte(data)
            except Exception as er:
                LogHandler.err(translate("acolyteWidgetTab", "acolyteParsingError") + ": " + str(er))
                print_traceback(translate("acolyteWidgetTab", "acolyteParsingError") + ": " + str(er))
                self.acolyte_not_available()
        else:
            self.acolyte_not_available()

    def parse_acolyte(self, data: PersistentEnemies) -> None:
        n_acc = len(self.alerts['PersistentEnemies'])
        for acc in data:
            acc_id = acc['_id']['$oid']
            try:
                region = get_region(acc['Region'])
            except KeyError:
                region = translate("acolyteWidgetTab", "noRegion")
            if (acc['LastDiscoveredLocation'] == ""):
                node = translate("acolyteWidgetTab", "noDiscovered")
                planet = ""
            else:
                node, planet = get_node(acc['LastDiscoveredLocation'])
            per = acc['HealthPercent']
            time = timeUtils.get_time(acc['LastDiscoveredTime']['$date']['$numberLong'])  # not used
            discovered = bool_to_yes_no(acc['Discovered'])

            found = 0
            for acolyte in self.alerts['PersistentEnemies']:
                if (acolyte.get_acc_id() == acc_id):
                    found = 1
                    acolyte.set_acc_position(per, time, discovered, node, planet, region)

            if (found == 0):
                ticket = bool_to_yes_no(acc['UseTicketing'])
                loc_tag = acc['LocTag']
                name = get_accolyte_name(acc['AgentType'])
                icon = acc['Icon']
                level = acc['Rank']
                flee = acc['FleeDamage']

                temp = Acolyte(acc_id)
                temp.set_acc_data(name, level, icon, flee, ticket, loc_tag)
                temp.set_acc_position(per, time, discovered, node, planet, region)
                self.alerts['PersistentEnemies'].append(temp)
                del temp

        self.add_acolytes(n_acc)

    def add_acolytes(self, n_acc: int) -> None:
        for i in range(n_acc, len(self.alerts['PersistentEnemies'])):
            if (not self.alerts['PersistentEnemies'][i].is_dead()):
                self.gridAcc.addLayout(self.alerts['PersistentEnemies'][i].AccBox, self.gridAcc.count(), 0)
                NotificationService.send_notification(
                    self.alerts['PersistentEnemies'][i].get_title(),
                    self.alerts['PersistentEnemies'][i].to_string(),
                    create_pixmap(self.alerts['PersistentEnemies'][i].get_image()))

    def acolyte_not_available(self) -> None:
        for i in reversed(range(0, len(self.alerts['PersistentEnemies']))):
            self.alerts['PersistentEnemies'][i].hide()
            remove_widget(self.alerts['PersistentEnemies'][i].AccBox)
            del self.alerts['PersistentEnemies'][i]
