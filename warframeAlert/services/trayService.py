# coding=utf-8
from PyQt5 import QtCore, QtWidgets, QtGui

from warframeAlert.services.translationService import translate
from warframeAlert.utils.commonUtils import get_separator
from warframeAlert.utils.fileUtils import get_asset_path


class TrayService():
    tray_icon = None

    def __init__(self, application):
        self.app = application

        self.tray_icon = QtWidgets.QSystemTrayIcon(self.app)
        self.tray_icon.setIcon(QtGui.QIcon(get_asset_path() + "icon" + get_separator() + "Warframe.ico"))

        show_app = QtWidgets.QAction(translate("trayService", "open"), self.app)
        show_app.triggered.connect(self.app.show)

        hide_app = QtWidgets.QAction(translate("trayService", "hide"), self.app)
        hide_app.triggered.connect(self.app.hide)

        quit_app = QtWidgets.QAction(translate("trayService", "exit"), self.app)
        quit_app.triggered.connect(QtCore.QCoreApplication.quit)

        tray_menu = QtWidgets.QMenu()
        tray_menu.addAction(show_app)
        tray_menu.addAction(hide_app)
        tray_menu.addAction(quit_app)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()
        # noinspection PyUnresolvedReferences
        self.tray_icon.activated[QtWidgets.QSystemTrayIcon.ActivationReason].connect(self.show_tray)

    def show_tray(self, event):
        if (event == QtWidgets.QSystemTrayIcon.DoubleClick):
            self.app.show()

    def get_tray_icon(self):
        return self.tray_icon
