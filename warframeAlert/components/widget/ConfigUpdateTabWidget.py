# coding=utf-8
from PyQt6 import QtWidgets, QtCore

from warframeAlert.services.optionHandlerService import OptionsHandler
from warframeAlert.services.translationService import translate
from warframeAlert.utils.commonUtils import int_to_bool, bool_to_int


class ConfigUpdateTabWidget():
    ConfigUpdateTabWidget = None

    def __init__(self, option_service) -> None:
        self.ConfigUpdateTabWidget = QtWidgets.QWidget()

        self.gridUpdateConfig = QtWidgets.QGridLayout(self.ConfigUpdateTabWidget)

        self.UpdateButton = QtWidgets.QPushButton(translate("configUpdateTabWidget", "updateApp"))

        self.ConfigUpdateLabel = QtWidgets.QLabel(translate("configUpdateTabWidget", "updateDataLabel"))
        self.CycleConfigLabel = QtWidgets.QLabel(translate("configUpdateTabWidget", "updateDataSec") + ":")
        self.ConsoleConfigLabel = QtWidgets.QLabel(translate("configUpdateTabWidget", "platform") + ":")

        self.CycleComboBox = QtWidgets.QComboBox(self.ConfigUpdateTabWidget)
        self.PlatformComboBox = QtWidgets.QComboBox(self.ConfigUpdateTabWidget)
        self.AutoUpConfig = QtWidgets.QCheckBox(translate("configUpdateTabWidget", "activeAutoUpdate"))
        self.NotificationConfig = QtWidgets.QCheckBox(translate("configUpdateTabWidget", "activeNotification"))

        self.CycleComboBox.addItem("0")
        self.CycleComboBox.addItem("30")
        self.CycleComboBox.addItem("60")
        self.CycleComboBox.addItem("150")
        self.CycleComboBox.addItem("300")
        self.CycleComboBox.addItem("600")
        self.CycleComboBox.addItem("900")

        self.PlatformComboBox.addItem("PC")
        self.PlatformComboBox.addItem("PS4")
        self.PlatformComboBox.addItem("Xbox One")
        self.PlatformComboBox.addItem("Nintendo Switch")

        self.gridUpdateConfig.addWidget(self.ConfigUpdateLabel, 0, 0)
        self.gridUpdateConfig.addWidget(self.CycleConfigLabel, 1, 0)
        self.gridUpdateConfig.addWidget(self.CycleComboBox, 1, 1)
        self.gridUpdateConfig.addWidget(self.ConsoleConfigLabel, 2, 0)
        self.gridUpdateConfig.addWidget(self.PlatformComboBox, 2, 1)
        self.gridUpdateConfig.addWidget(self.AutoUpConfig, 3, 0)
        self.gridUpdateConfig.addWidget(self.UpdateButton, 3, 1)
        self.gridUpdateConfig.addWidget(self.NotificationConfig, 4, 0)

        self.ConfigUpdateTabWidget.setLayout(self.gridUpdateConfig)
        self.gridUpdateConfig.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

        cycle_index = self.CycleComboBox.findText(str(OptionsHandler.get_option("Update/Cycle")))
        if (cycle_index == -1):
            cycle_index = 0
        self.CycleComboBox.setCurrentIndex(cycle_index)

        self.PlatformComboBox.setCurrentIndex(OptionsHandler.get_option("Update/Console"))

        self.AutoUpConfig.setChecked(int_to_bool(OptionsHandler.get_option("Update/AutoUpdate")))
        self.NotificationConfig.setChecked(int_to_bool(OptionsHandler.get_option("Update/Notify")))

        self.CycleComboBox.currentTextChanged[str].connect(option_service.update_cycle_update)
        self.PlatformComboBox.currentIndexChanged[int].connect(update_platform_type)
        self.AutoUpConfig.clicked.connect(
            lambda: OptionsHandler.set_option("Update/AutoUpdate", bool_to_int(self.AutoUpConfig.isChecked())))
        self.NotificationConfig.clicked.connect(
            lambda: OptionsHandler.set_option("Update/Notify", bool_to_int(self.NotificationConfig.isChecked())))

        self.UpdateButton.clicked.connect(lambda: option_service.open_update())

    def get_widget(self) -> QtWidgets.QWidget:
        return self.ConfigUpdateTabWidget


def update_platform_type(console_index: int) -> None:
    OptionsHandler.set_option("Update/Console", console_index)
