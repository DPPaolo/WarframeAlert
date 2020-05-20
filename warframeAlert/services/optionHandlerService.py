# coding=utf-8
import time

from PyQt5 import QtCore


class OptionsHandler(QtCore.QObject):
    #UpdateTabber = QtCore.pyqtSignal()
    setting = QtCore.QSettings("config.ini", QtCore.QSettings.IniFormat)
    first_init = True
    default_value = {
        "Language": "it",       # App Language
        "Version": "13",        # Program Main Version
        "SubVersion": "2",      # Program Sub Version
        "FirstInit": 0,         # First Installation
        "TrayIcon": 0,          # Tray Icon Disable
        "Debug": 0,             # Debug Messages Disabled
        # All Tabs are active by default
        "Tab/News": 1,
        "Tab/TactAll": 1,
        "Tab/Accolyt": 1,
        "Tab/Cetus": 1,
        "Tab/Invasion": 1,
        "Tab/Sortie": 1,
        "Tab/Syndicate": 1,
        "Tab/Fissure": 1,
        "Tab/Baro": 1,
        "Tab/Market": 1,
        "Tab/PVP": 1,
        "Tab/Nightwave": 1,
        "Tab/Other": 1,
        "Update/Cycle": 300,        # Update Cycle
        "Update/Console": 0,        # 0 PC, 1 PS4, 2 Xbox One, 3 Nintendo Switch
        "Update/AutoUpdate": 1,     # Automatic Update
        "Update/AutoUpdateAll": str(time.mktime(time.localtime()))[0:-2],   # Update All Files Timer
        "Update/Notify": 1          # Notification
    }

    def __init__(self):
        super().__init__()
        self.setting.setFallbacksEnabled(False)
        self.ConfWidget = None

    def create_config(self):
        for key in self.default_value:
            self.set_option(key, self.default_value[key])

    @classmethod
    def set_first_init(cls, value):
        cls.first_init = value

    @classmethod
    def get_first_init(cls):
        return cls.first_init

    @classmethod
    def get_option(cls, option, option_type=int):
        val = cls.setting.value(option, cls.default_value[option], type=option_type)
        if (option_type == int):
            if (str(val).isdigit()):
                return int(val)
            else:
                return 0
        else:
            return str(val)

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

    # @pyqtSlot()
    #def update_lang_agg(self, ConsoleIndex):
    #    self.set_option("Language", ConsoleIndex)

    # #@pyqtSlot()
    # def update_cycle_agg(self, ComboBoxText):
    #     self.set_option("Update/Cycle", int(ComboBoxText))
    #     warframeData.gestore_update.set_timer()

    # def update_conf(self):
    #     self.AutoUpConf.setChecked(warframe.inttobool(self.get_option("Update/AutoUpdate")))

    # def open_option(self):
    #     self.ConfWidget.show()
