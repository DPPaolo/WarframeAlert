# coding=utf-8
from PyQt6 import QtCore, QtWidgets, QtGui
from PyQt6.QtWidgets import QSystemTrayIcon, QMenu

from warframeAlert.services.translationService import translate
from warframeAlert.utils.fileUtils import get_asset_path, get_separator


class TrayService():
    tray_icon: QSystemTrayIcon = None

    def __init__(self, application) -> None:
        self.app = application

        self.tray_icon: QSystemTrayIcon = QtWidgets.QSystemTrayIcon(self.app)
        self.tray_icon.setIcon(QtGui.QIcon(get_asset_path() + "icon" + get_separator() + "Warframe.ico"))

        show_app: QtGui.QAction = QtGui.QAction(translate("trayService", "open"), self.app)
        show_app.triggered.connect(self.app.show)

        hide_app: QtGui.QAction = QtGui.QAction(translate("trayService", "hide"), self.app)
        hide_app.triggered.connect(self.app.hide)

        quit_app: QtGui.QAction = QtGui.QAction(translate("trayService", "exit"), self.app)
        quit_app.triggered.connect(QtCore.QCoreApplication.quit)

        tray_menu: QMenu = QtWidgets.QMenu()
        tray_menu.addAction(show_app)
        tray_menu.addAction(hide_app)
        tray_menu.addAction(quit_app)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()
        self.tray_icon.activated[QtWidgets.QSystemTrayIcon.ActivationReason].connect(self.show_tray)

    def show_tray(self, event: QtWidgets.QSystemTrayIcon.ActivationReason) -> None:
        if (event == QtWidgets.QSystemTrayIcon.DoubleClick):
            self.app.show()

    def get_tray_icon(self) -> QSystemTrayIcon:
        return self.tray_icon
