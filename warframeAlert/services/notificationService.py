# coding=utf-8
import time
from typing import Optional, Tuple, List, Union

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QSystemTrayIcon

from warframeAlert.services.optionHandlerService import OptionsHandler
from warframeAlert.services.translationService import translate
from warframeAlert.utils import commonUtils

NotificationData = Tuple[str, str, Optional[QSystemTrayIcon]]


class NotificationService(QtCore.QThread):
    notif_queue: List[NotificationData] = []

    def __init__(self, tray_icon: QSystemTrayIcon) -> None:
        super().__init__()
        self.tray_icon = tray_icon

    @classmethod
    def send_notification(cls,
                          title: str,
                          message: str,
                          icon: Optional[QSystemTrayIcon]) -> None:
        if (not OptionsHandler.get_first_init() and OptionsHandler.get_option("Update/Notify")):
            cls.notif_queue.append((title, message, icon))

    # TODO: use | instead of Union
    def show_notif(self, title: str,
                   message: str,
                   icon: Union[None, QSystemTrayIcon.MessageIcon, QtGui.QIcon]) -> None:
        if (icon is None):
            icon = QSystemTrayIcon.Information
        self.tray_icon.showMessage(title, message, icon, 3000)

    def run(self) -> None:
        while (True):
            if (not len(self.notif_queue) == 0):
                notify = self.notif_queue.pop(0)
                try:
                    if (notify[2]):
                        self.show_notif(notify[0], notify[1], QtGui.QIcon(notify[2]))
                    else:
                        self.show_notif(notify[0], notify[1], None)
                except Exception as er:
                    commonUtils.print_traceback(translate("notificationService", "sendNotifError") + ": "
                                                + str(notify)
                                                + "\n" + str(er))
            time.sleep(4)
