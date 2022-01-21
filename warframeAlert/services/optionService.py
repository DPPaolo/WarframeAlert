# coding=utf-8

from PyQt6 import QtCore
from PyQt6.QtWidgets import QWidget

from warframeAlert.components.widget.OptionsWidget import OptionsWidget
from warframeAlert.services.optionHandlerService import OptionsHandler
from warframeAlert.services.tabService import TabService
from warframeAlert.services.updateProgramService import UpdateProgramService
from warframeAlert.services.updateService import UpdateService


class OptionService(QtCore.QObject):

    def __init__(self, tab_service: TabService, update_service: UpdateService,
                 update_program_service: UpdateProgramService) -> None:
        super().__init__()
        self.tab_service = tab_service
        self.update_service = update_service
        self.update_program_service = update_program_service
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

    def open_update(self) -> None:
        self.update_program_service.open_update()

    def update_cycle_update(self, cycle_text: str) -> None:
        OptionsHandler.set_option("Update/Cycle", int(cycle_text))
        self.update_service.stop()
        self.update_service.start()
