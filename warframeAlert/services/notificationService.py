# coding=utf-8
import time
from typing import Optional, Tuple, List

from PyQt6 import QtCore, QtWidgets, QtGui

from warframeAlert.services.optionHandlerService import OptionsHandler
from warframeAlert.services.translationService import translate
from warframeAlert.utils import commonUtils

NotificationData = Tuple[str, str, Optional[QtWidgets.QSystemTrayIcon]]


class NotificationService(QtCore.QThread):
    notification_queue: List[NotificationData] = []

    def __init__(self, tray_icon: QtWidgets.QSystemTrayIcon) -> None:
        super().__init__()
        self.tray_icon = tray_icon

    @classmethod
    def send_notification(cls,
                          title: str,
                          message: str,
                          icon: QtWidgets.QSystemTrayIcon | QtGui.QPixmap | None) -> None:
        if (not OptionsHandler.is_during_init() and OptionsHandler.get_option("Update/Notify")):
            cls.notification_queue.append((title, message, icon))

    def show_notification(self, title: str,
                          message: str,
                          icon: QtWidgets.QSystemTrayIcon.MessageIcon | QtGui.QIcon | None) -> None:
        if (icon is None):
            icon = QtWidgets.QSystemTrayIcon.MessageIcon.Information
        self.tray_icon.showMessage(title, message, icon, 3000)

    def run(self) -> None:
        while (True):
            if (not len(self.notification_queue) == 0):
                notify = self.notification_queue.pop(0)
                try:
                    if (notify[2]):
                        self.show_notification(notify[0], notify[1], QtGui.QIcon(notify[2]))
                    else:
                        self.show_notification(notify[0], notify[1], None)
                except Exception as er:
                    commonUtils.print_traceback(translate("notificationService", "sendNotifError") + ": "
                                                + str(notify)
                                                + "\n" + str(er))
            time.sleep(4)
