# coding=utf-8
import time

from PyQt5 import QtCore, QtWidgets, QtGui

from warframeAlert.services.optionHandlerService import OptionsHandler
from warframeAlert.services.translationService import translate
from warframeAlert.utils import commonUtils


class NotificationService(QtCore.QThread):
    notif_queue = []

    def __init__(self, tray_icon):
        super().__init__()
        self.tray_icon = tray_icon

    @classmethod
    def send_notification(cls, title, message, icon):
        if (not OptionsHandler.get_first_init() and OptionsHandler.get_option("Update/Notify")):
            cls.notif_queue.append((title, message, icon))

    def show_notif(self, title, message, icon):
        if (icon is None):
            icon = QtWidgets.QSystemTrayIcon.Information
        self.tray_icon.showMessage(title, message, icon, 3000)

    def run(self):
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
