# coding=utf-8
from PyQt5 import QtWidgets, QtCore

from warframeAlert.components.common.SpecialAlert import create_alert
from warframeAlert.services.notificationService import NotificationService
from warframeAlert.services.translationService import translate
from warframeAlert.utils import timeUtils
from warframeAlert.utils.commonUtils import remove_widget, bool_to_yes_no
from warframeAlert.utils.gameTranslationUtils import get_item_name


class AlertWidget():
    AllerteWidget = None

    def __init__(self):

        self.alerts = {'Alerts': []}

        self.AllerteWidget = QtWidgets.QWidget()

        self.NoAlert = QtWidgets.QLabel(translate("alertWidget", "noAlert"))
        self.NoAlert.setAlignment(QtCore.Qt.AlignCenter)

        self.gridAllerte = QtWidgets.QGridLayout(self.AllerteWidget)
        self.gridAllerte.setAlignment(QtCore.Qt.AlignTop)
        self.gridAllerte.addWidget(self.NoAlert, 0, 0)
        self.AllerteWidget.setLayout(self.gridAllerte)

    def get_widget(self):
        return self.AllerteWidget

    def get_lenght(self):
        return len(self.alerts['Alerts'])

    def parse_alert_data(self, data):
        self.reset_alerts()
        n_alert = len(self.alerts['Alerts'])
        for alert in data:
            try:
                alert_id = alert['_id']['$oid']
            except KeyError:
                alert_id = str(timeUtils.get_local_time())
            try:
                init = alert['Activation']['$date']['$numberLong']
                end = alert['Expiry']['$date']['$numberLong']
            except KeyError:
                init = str((int(timeUtils.get_local_time())) * 1000)
                end = str((int(timeUtils.get_local_time()) + 3600) * 1000)

            tempo = int(end[:10]) - int(timeUtils.get_local_time())
            if (tempo < 0):
                found = 0

                for old_alert in self.alerts['Alerts']:
                    if (old_alert.get_alert_id() == alert_id):
                        found = 1

                if (found == 0):
                    temp = create_alert(alert['MissionInfo'], alert_id)
                    temp.set_alert_time(end, init)
                    temp.set_alert_time_name(translate("alertWidget", "end") + ": ")

                    if ('ForceUnlock' in alert):
                        temp.set_alert_unlock(bool_to_yes_no(alert['ForceUnlock']))

                    if (alert['MissionInfo']['missionReward']):
                        if ('items' in alert['MissionInfo']['missionReward']):
                            url_item = str(alert['MissionInfo']['missionReward']['items'][0])
                            items = get_item_name(url_item)
                            temp.set_alert_image(url_item, items)
                        elif ('countedItems' in alert['MissionInfo']['missionReward']):
                            url_item = alert['MissionInfo']['missionReward']['countedItems'][0]['ItemType']
                            items = get_item_name(url_item)
                            temp.set_alert_image(url_item, items)
                        else:
                            temp.set_default_alert_image()
                    else:
                        temp.set_default_alert_image()

                    if (not temp.is_hided()):
                        self.alerts['Alerts'].append(temp)
                    del temp

        self.add_alerts(n_alert)

    def add_alerts(self, n_alert):
        for i in range(n_alert, len(self.alerts['Alerts'])):
            if (not self.alerts['Alerts'][i].is_expired()):
                self.gridAllerte.addLayout(self.alerts['Alerts'][i].AlertBox, self.gridAllerte.count(), 0)
                NotificationService.send_notification(
                        self.alerts['Alerts'][i].get_title(),
                        self.alerts['Alerts'][i].to_string(),
                        self.alerts['Alerts'][i].get_image())
        if (len(self.alerts['Alerts']) > 0):
            self.NoAlert.hide()

    def reset_alerts(self):
        self.NoAlert.show()
        canc = []
        for i in range(0, len(self.alerts['Alerts'])):
            if (self.alerts['Alerts'][i].is_expired()):
                canc.append(i)
        i = len(canc)
        while i > 0:
            self.alerts['Alerts'][canc[i-1]].hide()
            remove_widget(self.alerts['Alerts'][canc[i-1]].AlertBox)
            del self.alerts['Alerts'][canc[i-1]]
            i -= 1

