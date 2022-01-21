# coding=utf-8

from PyQt6 import QtCore
from PyQt6.QtWidgets import QWidget

from warframeAlert.components.widget.OptionsWidget import OptionsWidget
from warframeAlert.services.optionHandlerService import OptionsHandler
from warframeAlert.services.tabService import TabService


class OptionService(QtCore.QObject):
    UpdateTabber = QtCore.pyqtSignal()

    def __init__(self, tab_service: TabService) -> None:
        super().__init__()
        self.tab_service = tab_service
        self.ConfigWidget = OptionsWidget(self).get_widget()

    def get_widget(self) -> QWidget:
        return self.ConfigWidget

    def open_option(self) -> None:
        self.ConfigWidget.show()

    def set_config_widget(self, widget: QWidget) -> None:
        self.ConfigWidget = widget

    def update_config_tab(self, option: str, value: int):
        OptionsHandler.set_option(option, value)
        self.tab_service.update_tabber()

    # #@pyqtSlot()
    # def update_console_agg(self, ConsoleIndex):
    #     OptionHandler.set_option("Update/Console", ConsoleIndex)

    # #@pyqtSlot()
    # def update_cycle_agg(self, ComboBoxText):
    #     OptionsHandler.set_option("Update/Cycle", int(ComboBoxText))
    #     warframeData.gestore_update.set_timer()

    # def update_conf(self):
    #     self.AutoUpConf.setChecked(int_to_bool(OptionsHandler.get_option("Update/AutoUpdate")))
