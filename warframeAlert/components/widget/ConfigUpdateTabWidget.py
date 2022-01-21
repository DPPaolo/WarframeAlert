# coding=utf-8
from PyQt6 import QtWidgets, QtCore

from warframeAlert.services.optionHandlerService import OptionsHandler
from warframeAlert.services.translationService import translate
from warframeAlert.utils.commonUtils import int_to_bool


class ConfigUpdateTabWidget():
    ConfigUpdateTabWidget = None

    def __init__(self, option_service) -> None:
        self.ConfigUpdateTabWidget = QtWidgets.QWidget()

        gridAggConf = QtWidgets.QGridLayout(self.ConfigUpdateTabWidget)

        UpdateButton = QtWidgets.QPushButton(translate("configUpdateTabWidget", "updateApp"))

        ConfLabel2 = QtWidgets.QLabel(translate("configUpdateTabWidget", "updateDataLabel"))
        CycleConfLab = QtWidgets.QLabel(translate("configUpdateTabWidget", "updateDataSec") + ":")
        ConsoleConfLab = QtWidgets.QLabel(translate("configUpdateTabWidget", "platform") + ":")

        ComboBoxCycle = QtWidgets.QComboBox(self.ConfigUpdateTabWidget)
        ComboBoxConsole = QtWidgets.QComboBox(self.ConfigUpdateTabWidget)
        AutoUpConf = QtWidgets.QCheckBox(translate("configUpdateTabWidget", "activeAutoUpdate"))
        UpdateNotify = QtWidgets.QCheckBox(translate("configUpdateTabWidget", "activeNotification"))

        ComboBoxCycle.addItem("0")
        ComboBoxCycle.addItem("30")
        ComboBoxCycle.addItem("60")
        ComboBoxCycle.addItem("150")
        ComboBoxCycle.addItem("300")
        ComboBoxCycle.addItem("600")
        ComboBoxCycle.addItem("900")

        ComboBoxConsole.addItem("PC")
        ComboBoxConsole.addItem("PS4")
        ComboBoxConsole.addItem("Xbox One")
        ComboBoxConsole.addItem("Nintendo Switch")

        gridAggConf.addWidget(ConfLabel2, 0, 0)
        gridAggConf.addWidget(CycleConfLab, 1, 0)
        gridAggConf.addWidget(ComboBoxCycle, 1, 1)
        gridAggConf.addWidget(ConsoleConfLab, 2, 0)
        gridAggConf.addWidget(ComboBoxConsole, 2, 1)
        gridAggConf.addWidget(AutoUpConf, 3, 0)
        gridAggConf.addWidget(UpdateButton, 3, 1)
        gridAggConf.addWidget(UpdateNotify, 4, 0)

        self.ConfigUpdateTabWidget.setLayout(gridAggConf)
        gridAggConf.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

        CycleIndex = ComboBoxCycle.findText(str(OptionsHandler.get_option("Update/Cycle")))
        if (CycleIndex == -1):
            CycleIndex = 0
        ComboBoxCycle.setCurrentIndex(CycleIndex)

        ConsoleIndex = OptionsHandler.get_option("Update/Console")
        ComboBoxConsole.setCurrentIndex(ConsoleIndex)

        AutoUpConf.setChecked(int_to_bool(OptionsHandler.get_option("Update/AutoUpdate")))
        UpdateNotify.setChecked(int_to_bool(OptionsHandler.get_option("Update/Notify")))

        #ComboBoxCycle.currentIndexChanged[str].connect(option_service.update_cycle_agg)
        #ComboBoxConsole.currentIndexChanged[int].connect(option_service.update_console_agg)
        AutoUpConf.clicked.connect(lambda: OptionsHandler.set_option("Update/AutoUpdate", AutoUpConf.isChecked()))
        UpdateNotify.clicked.connect(lambda: OptionsHandler.set_option("Update/Notify", UpdateNotify.isChecked()))

        #UpdateButton.clicked.connect(lambda: gestore_update.open_update())

    def get_widget(self) -> QtWidgets.QWidget:
        return self.ConfigUpdateTabWidget
