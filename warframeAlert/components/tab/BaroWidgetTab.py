# coding=utf-8
from enum import Enum

from PyQt6 import QtWidgets, QtCore

from warframeAlert.components.common.BaroItemBox import BaroItemBox
from warframeAlert.components.common.Countdown import Countdown
from warframeAlert.constants.warframeTypes import VoidTraders
from warframeAlert.services.notificationService import NotificationService
from warframeAlert.services.optionHandlerService import OptionsHandler
from warframeAlert.services.translationService import translate
from warframeAlert.utils import timeUtils
from warframeAlert.utils.commonUtils import print_traceback, remove_widget
from warframeAlert.utils.gameTranslationUtils import get_node, get_item_name
from warframeAlert.utils.logUtils import LogHandler
from warframeAlert.utils.stringUtils import divide_message


class BaroState(Enum):
    BARO_NOT_ARRIVED = 0,
    BARO_ARRIVED = 1,
    BARO_ITEM_COMPLETED = 2


class BaroWidgetTab():
    def __init__(self) -> None:
        self.alerts = {'VoidTraders': []}

        self.baro_arrived = BaroState.BARO_NOT_ARRIVED
        self.baro_con_arrived = BaroState.BARO_NOT_ARRIVED

        self.BaroWidget = QtWidgets.QWidget()

        self.ItemBaroWidget = QtWidgets.QWidget()

        self.BaroTabber = QtWidgets.QTabWidget()

        self.BaroDesc = QtWidgets.QLabel("")
        self.BaroDesc.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        self.BaroEnd = Countdown()
        self.BaroEnd.TimeLab.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.BaroConDesc = QtWidgets.QLabel("")
        self.BaroConDesc.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        self.BaroConEnd = Countdown()
        self.BaroConEnd.TimeLab.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.NoBaro = QtWidgets.QLabel(translate("baroWidget", "noBaro"))
        self.NoBaro.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.gridBaroItems = QtWidgets.QGridLayout(self.ItemBaroWidget)
        self.gridBaroItems.addWidget(self.NoBaro, 0, 0, 1, 6)

        self.BaroScrollBar = QtWidgets.QScrollArea()
        self.BaroScrollBar.setWidgetResizable(True)
        self.BaroScrollBar.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.ItemBaroWidget.setLayout(self.gridBaroItems)

        self.BaroScrollBar.setWidget(self.ItemBaroWidget)

        self.BaroTabber.insertTab(0, self.BaroScrollBar, translate("baroWidget", "baroItem"))

        self.gridBaro = QtWidgets.QGridLayout(self.BaroWidget)
        self.gridBaro.addWidget(self.BaroDesc, 0, 0)
        self.gridBaro.addWidget(self.BaroEnd.TimeLab, 0, 1)
        self.gridBaro.addWidget(self.BaroConDesc, 1, 0)
        self.gridBaro.addWidget(self.BaroConEnd.TimeLab, 1, 1)
        self.gridBaro.addWidget(self.BaroTabber, 2, 0, 1, 2)
        self.gridBaro.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

        self.BaroWidget.setLayout(self.gridBaro)

    def get_widget(self) -> QtWidgets.QWidget:
        return self.BaroWidget

    def update_baro(self, data: VoidTraders) -> None:
        if (OptionsHandler.get_option("Tab/Baro") == 1):
            try:
                self.parse_baro(data)
            except Exception as er:
                LogHandler.debug(translate("baroWidget", "baroError") + ": " + str(er))
                print_traceback(translate("baroWidget", "baroError") + ": " + str(er))
                self.delete_baro()
                return
        else:
            self.delete_baro()

    def parse_baro(self, data: VoidTraders) -> None:
        self.reset_baro()
        n_baro = len(self.alerts['VoidTraders'])
        manifest_empty = 0
        for baro in data:
            baro_id = baro['_id']['$oid']
            init = timeUtils.get_time(baro['Activation']['$date']['$numberLong'])
            start = baro['Activation']['$date']['$numberLong']
            end = baro['Expiry']['$date']['$numberLong']
            node, planet = get_node(baro['Node'])

            desc = translate("baroWidget", "arrived") + ": " + init
            desc += "\t" + translate("baroWidget", "on") + " " + node + " " + planet

            if ('TennoCon' in node):
                self.BaroConDesc.setToolTip("ID " + baro['Character'] + ": " + str(baro_id))
                self.set_tennocon_time(desc, start[:10], end[:10])
            else:
                self.BaroDesc.setToolTip("ID " + baro['Character'] + ": " + str(baro_id))
                self.set_time(desc, start[:10], end[:10])

            if ('Manifest' in baro):
                manifest_empty += 1
                for baro_item in baro['Manifest']:
                    item = get_item_name(baro_item['ItemType'])
                    item = divide_message(item, 18)

                    found = 0
                    for old_baro_item in self.alerts['VoidTraders']:
                        if (old_baro_item.get_item_name() == item):
                            found = 1

                    if (found == 0):
                        platinum_price = baro_item['PrimePrice']
                        credit_price = baro_item['RegularPrice']
                        temp = BaroItemBox()
                        temp.set_baro_item(item, platinum_price, credit_price)
                        temp.set_baro_image(baro_item['ItemType'])
                        self.alerts['VoidTraders'].append(temp)
                        del temp

                self.add_baro_item(n_baro, node, planet)

        if (manifest_empty == 0):
            self.delete_baro()

    def add_baro_item(self, n_baro: int, node: str, plan: str) -> None:
        n = n_baro
        for i in range(n_baro, len(self.alerts['VoidTraders'])):
            self.gridBaroItems.addLayout(self.alerts['VoidTraders'][i].BaroBox, int(n / 4), (n % 4))
            n += 1

        if (len(self.alerts['VoidTraders']) > 0):
            self.NoBaro.hide()
            if (self.baro_arrived == BaroState.BARO_NOT_ARRIVED):
                self.baro_arrived = BaroState.BARO_ARRIVED

            if (self.baro_con_arrived == BaroState.BARO_NOT_ARRIVED):
                self.baro_con_arrived = BaroState.BARO_ARRIVED

        if (self.baro_arrived == BaroState.BARO_ARRIVED):
            NotificationService.send_notification(
                translate("baroWidget", "baroArrived") + "!",
                node + " " + plan,
                None)
            self.baro_arrived = BaroState.BARO_ITEM_COMPLETED

        if (self.baro_con_arrived == BaroState.BARO_ARRIVED):
            NotificationService.send_notification(
                translate("baroWidget", "baroArrived") + "!",
                node + " " + plan,
                None)
            self.baro_con_arrived = BaroState.BARO_ITEM_COMPLETED

    def set_time(self, desc: str, start: int, end: int) -> None:
        local_time = int(timeUtils.get_local_time())
        time = (int(start) - local_time) if (int(start) >= local_time) else (int(end) - local_time)
        if (time > 0):
            self.BaroEnd.set_name(translate("baroWidget", "end") + " ")
            self.BaroEnd.set_countdown(start if (int(start) >= local_time) else end)
            self.BaroEnd.start()
        else:
            self.BaroEnd.hide()
        self.BaroDesc.setText(desc)

    def set_tennocon_time(self, desc: str, start: int, end: int) -> None:
        local_time = int(timeUtils.get_local_time())
        time = (int(start) - local_time) if (int(start) >= local_time) else (int(end) - local_time)
        if (time > 0):
            self.BaroConEnd.set_name(translate("baroWidget", "end") + " ")
            self.BaroConEnd.set_countdown(start if (int(start) >= local_time) else end)
            self.BaroConEnd.start()
        else:
            self.BaroConEnd.hide()
        self.BaroConDesc.setText(desc)

    def delete_baro(self) -> None:
        self.baro_arrived = BaroState.BARO_NOT_ARRIVED
        self.baro_con_arrived = BaroState.BARO_NOT_ARRIVED
        self.BaroEnd.set_name(translate("baroWidget", "init") + " ")
        for i in reversed(range(0, len(self.alerts['VoidTraders']))):
            self.alerts['VoidTraders'][i].hide()
            remove_widget(self.alerts['VoidTraders'][i].BaroBox)
            del self.alerts['VoidTraders'][i]
            i -= 1

    def reset_baro(self) -> None:
        self.NoBaro.show()
        self.BaroEnd.TimeLab.show()
        self.BaroConEnd.TimeLab.show()
