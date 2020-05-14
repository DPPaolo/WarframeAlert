# coding=utf-8
import time

from PyQt5 import QtCore


class OptionsHandler(QtCore.QObject):
    UpdateTabber = QtCore.pyqtSignal()
    setting = QtCore.QSettings("config.ini", QtCore.QSettings.IniFormat)
    first_init = True

    def __init__(self):
        super().__init__()
        self.setting.setFallbacksEnabled(False)
        self.ConfWidget = None

    def create_config(self):
        self.set_option("ViewStarChart", 1)  # Star Chart
        self.set_option("ViewMissionDeck", 1)  # Missions List with Drops
        self.set_option("Debug", 0)  # Debug Message
        self.set_option("Version", "13")  # Program Main Version
        self.set_option("SubVersion", "2")  # Program Sub Version
        self.set_option("FirstInit", 0)  # First Installation
        self.set_option("TrayIcon", 0)  # Tray Icon Disable
        self.set_option("Language", "it")  # App Language

        # Tabber Activated by Default
        self.set_option("Tab/News", 1)
        self.set_option("Tab/TactAll", 1)
        self.set_option("Tab/Accolyt", 1)
        self.set_option("Tab/Cetus", 1)
        self.set_option("Tab/Invasion", 1)
        self.set_option("Tab/Sortie", 1)
        self.set_option("Tab/Syndicate", 1)
        self.set_option("Tab/Fissure", 1)
        self.set_option("Tab/Baro", 1)
        self.set_option("Tab/Market", 1)
        self.set_option("Tab/PVP", 1)
        self.set_option("Tab/Nightwave", 1)
        self.set_option("Tab/Other", 1)

        self.set_option("Update/Cycle", 300)  # Update Cycle
        self.set_option("Update/Console", 0)  # 0 PC, 1 PS4, 2 Xbox One
        self.set_option("Update/AutoUpdate", 1)  # Automatic Update
        self.set_option("Update/AutoUpdateAll", str(time.mktime(time.localtime()))[0:-2])  # Update All Files Timer
        self.set_option("Update/Notify", 1)  # Notification

    @classmethod
    def set_first_init(cls, value):
        cls.first_init = value

    @classmethod
    def get_first_init(cls):
        return cls.first_init

    @classmethod
    def get_option(cls, option, tipo=int):
        val = cls.setting.value(option, tipo)
        if (tipo == int):
            if (str(val).isdigit()):
                return int(val)
            else:
                return 0
        else:
            return val

    @classmethod
    def set_option(cls, option, value):
        cls.setting.setValue(option, value)

    def get_widget(self):
        return self.ConfWidget

    # def create_config_widget(self):
    #     self.ConfWidget = warframeUI.widget_config(self)
    #     self.ConfWidget.setWindowTitle('Opzioni')

    # def update_conf_checkbox(self, tipo, obj):
    #     self.set_option(tipo, warframe.booltoint(obj.isChecked()))

    # def update_conf_tab(self, tipo, obj):
    #     self.update_conf_checkbox(tipo, obj)
    #     self.UpdateTabber.emit()
    #
    # #@pyqtSlot()
    # def update_console_agg(self, ConsoleIndex):
    #     self.set_option("Update/Console", ConsoleIndex)

    # #@pyqtSlot()
    # def update_cycle_agg(self, ComboBoxText):
    #     self.set_option("Update/Cycle", int(ComboBoxText))
    #     warframeData.gestore_update.set_timer()

    # def update_conf(self):
    #     self.AutoUpConf.setChecked(warframe.inttobool(self.get_option("Update/AutoUpdate")))

    # def open_option(self):
    #     self.ConfWidget.show()
