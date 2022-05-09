# coding=utf-8
import time
from typing import Any, Type

from PyQt6 import QtCore


class OptionsHandler(QtCore.QObject):
    UpdateTabber = QtCore.pyqtSignal()
    setting: QtCore.QSettings = QtCore.QSettings("config.ini", QtCore.QSettings.Format.IniFormat)
    during_init: bool = True
    default_value = {
        "Language": "it",       # App Language
        "Version": "13",        # Program Main Version
        "SubVersion": "5",      # Program Sub Version
        "Theme": 0,             # Theme
        "FirstInit": 0,         # First Installation
        "TrayIcon": 0,          # Tray Icon Disable
        "Debug": 0,             # Debug Messages Disabled
        # All Tabs are active by default
        "Tab/News": 1,
        "Tab/TactAll": 1,
        "Tab/Acolyte": 1,
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

    def __init__(self) -> None:
        super().__init__()
        self.setting.setFallbacksEnabled(False)

    def create_config(self) -> None:
        for key in self.default_value:
            self.set_option(key, self.default_value[key])

    @classmethod
    def set_during_init(cls, value: Any) -> None:
        cls.during_init = value

    @classmethod
    def is_during_init(cls) -> bool:
        return cls.during_init

    @classmethod
    def get_option(cls, option: str, option_type: Type[int] | Type[str] = int) -> str | int:
        val = cls.setting.value(option, cls.default_value[option], type=option_type)
        if (option_type == int):
            if (str(val).isdigit()):
                return int(val)
            else:
                return 0
        else:
            return str(val)

    @classmethod
    def set_option(cls, option: str, value: Any) -> None:
        cls.setting.setValue(option, value)
