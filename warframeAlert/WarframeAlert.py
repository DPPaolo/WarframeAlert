#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtCore import QTimer

from warframeAlert.components.common.MessageBox import MessageBox, MessageBoxType
from warframeAlert.services.networkService import check_connection, get_actual_version, retrieve_version, update_program
from warframeAlert.services.notificationService import NotificationService
from warframeAlert.services.optionHandlerService import OptionsHandler
from warframeAlert.services.tabService import TabService
from warframeAlert.services.translationService import Translator, translate
from warframeAlert.services.trayService import TrayService
from warframeAlert.services.updateFileService import UpdateFileService
from warframeAlert.services.updateProgramService import UpdateProgramService
from warframeAlert.services.updateService import UpdateService
from warframeAlert.utils import fileUtils, timeUtils
from warframeAlert.utils.fileUtils import create_default_folder, get_separator, copy_bundled_files_to_current_dir
from warframeAlert.utils.logUtils import LogHandler


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self) -> None:
        super().__init__()

        # Start the log handler
        self.logHandler = LogHandler()

        # Start the options service
        self.optionHandler = OptionsHandler()

        # Start the translation Service
        self.translator = Translator()

        # Start the tray Service
        self.tray = TrayService(self)

        # Start the notification Service
        self.notification_service = NotificationService(self.tray.get_tray_icon())
        self.notification_service.start()

        # Start the update service
        self.update_service = UpdateService()

        # Start the file update service
        self.update_file_service = UpdateFileService()

        self.setWindowTitle(translate("main", "title"))

        self.app = QtCore.QCoreApplication.instance()
        self.app.setApplicationName(translate("main", "title"))
        self.app.setOrganizationName("Onnisciente")
        self.setWindowIcon(QtGui.QIcon("assets" + get_separator() + "icon" + get_separator() + "Warframe.ico"))

        self.mainWidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.mainWidget)

        # Start the tab Service
        self.mainTabber = QtWidgets.QTabWidget(self.mainWidget)
        self.tabService = TabService(self.mainTabber)

        # Create the nav bar menu on top of the tabs
        self.navBarMenu = self.menuBar()
        self.create_menu()

        # Create a status bar under the tabs
        self.statusBar()


        #Crea il menu e le sue schede
        #self.tab_menu = warframeClass.tab_menu()

        #Crea la finestra delle opzioni
        #gestore_opzioni.create_config_widget()

        # Start the program service updater
        self.updateProgramService = UpdateProgramService()

        #gestore_opzioni.UpdateTabber.connect(self.update_tab)
        self.update_service.file_downloaded.connect(lambda: self.tabService.update(""))
        if (OptionsHandler.get_option("FirstInit") != 0):
            self.update_service.fist_init_completed.connect(self.show)

        self.mainGrid = QtWidgets.QGridLayout(self.mainWidget)
        self.mainGrid.addWidget(self.mainTabber, 0, 0, 1, 1)

        self.tabService.update_tabber()

        self.resize(680, 450)

        self.init_app()

        update_cycle = OptionsHandler.get_option("Update/Cycle")
        if (not str(update_cycle).isdigit() or int(update_cycle) < 30):
            self.tabService.update("")

    def start_update(self) -> None:
        self.resize(680, 450)
        self.update_service.start()

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        if (OptionsHandler.get_option("TrayIcon") == 1):
            event.ignore()
            self.hide()
            NotificationService.send_notification(
                translate("main", "title"),
                translate("main", "closeToTray"),
                None
            )

    def init_app(self) -> None:
        # Check if there is a new version downloaded
        if (fileUtils.check_file("PostUpdate.txt")):
            update_program()

        # Download files if it's the first init
        if (OptionsHandler.get_option("FirstInit") == 0):
            if (not check_connection()):
                MessageBox(translate("main", "noConnection"),
                           translate("main", "noConnectionFirstInit"),
                           MessageBoxType.ERROR)
                sys.exit()

            create_default_folder()
            self.optionHandler.create_config()

            if (not fileUtils.is_linux_os() and not fileUtils.is_mac_os()):
                if getattr(sys, 'frozen', False):
                    copy_bundled_files_to_current_dir()

            self.updateProgramService.open_and_update_file(self.update_file_service)
            self.updateProgramService.UpdateFile.all_file_downloaded.connect(self.show_after_first_init)
            OptionsHandler.set_option("FirstInit", 1)
        else:
            # Copy bundled files if missing
            #TODO: sistemare e farlo fare solo se manca un file in quelle cartelle
            if (not fileUtils.check_file("assets/icon/Warframe.ico") and getattr(sys, 'frozen', False)):
                copy_bundled_files_to_current_dir()

            old_update_date = OptionsHandler.get_option("Update/AutoUpdateAll")
            actual_date = int(timeUtils.get_local_time())
            if ((actual_date - old_update_date) > 604800 and check_connection()):
                OptionsHandler.set_option("Update/AutoUpdateAll", actual_date)
                QTimer.singleShot(60 * 1000, lambda: self.update_file_service.download_all_file())

    def show_after_first_init(self) -> None:
        self.tabService.update("")
        self.show()

    def create_menu(self) -> None:
        file = self.navBarMenu.addMenu('&' + translate("main", "fileMenu"))
        debug = self.navBarMenu.addMenu('&' + translate("main", "dataMenu"))
        tool = self.navBarMenu.addMenu('&' + translate("main", "toolsMenu"))
        info = self.navBarMenu.addMenu('&' + translate("main", "helpMenu"))

        # Files Menu
    #     open_alert = QtWidgets.QAction("Apri...", file)
    #     open_alert.setShortcut("Ctrl+A")
    #     open_alert.setStatusTip("Apri un file json contenente dati di allerte precedenti")
    #     open_alert.triggered.connect(self.open_old_allert)
    #     file.addAction(open_alert)
    #
    #     opzioni = QtWidgets.QAction("Opzioni", file)
    #     opzioni.setShortcut("Ctrl+O")
    #     opzioni.setStatusTip("Opzioni dell'Applicazione")
    #     opzioni.triggered.connect(lambda: gestore_opzioni.open_option())
    #     file.addAction(opzioni)

        exit_menu = QtGui.QAction(translate("main", "exitMenu"), file)
        exit_menu.setShortcut("Ctrl+Q")
        exit_menu.setStatusTip(translate("main", "exitMenuDesc"))
        exit_menu.triggered.connect(QtCore.QCoreApplication.quit)
        file.addAction(exit_menu)

        # Data Menu

        update_file = QtGui.QAction(translate("main", "updateFileMenu"), debug)
        update_file.setShortcut("Ctrl+U")
        update_file.setStatusTip(translate("main", "updateFileMenuDesc"))
        update_file.triggered.connect(lambda: self.update_service.download_alert_file(True))
        debug.addAction(update_file)

        update_only_file = QtGui.QAction(translate("main", "updateFilesMenu"), debug)
        update_only_file.setShortcut("Ctrl+T")
        update_only_file.setStatusTip(translate("main", "updateFilesMenuDesc"))
        update_only_file.triggered.connect(lambda: self.update_file_service.download_all_file())
        debug.addAction(update_only_file)
    #
    #         parse_file = QtWidgets.QAction("Parserizza il File", debug)
    #         parse_file.setShortcut("Ctrl+P")
    #         parse_file.setStatusTip("Traduce le Allerte a Schermo")
    #         parse_file.triggered.connect(lambda: self.update(False))
    #         debug.addAction(parse_file)
    #       togliere non serve mappa stellare

    #     #Menu Strumenti
    #     self.MSTool = QtWidgets.QAction("Mappa Stellare", tool)
    #     self.MSTool.setShortcut("Ctrl+M")
    #     self.MSTool.setStatusTip("Consente di Vedere Tutti i Nodi della Mappa Stellare")
    #     self.MSTool.triggered.connect(self.tab_menu.open_window_mappa_stellare)
    #     tool.addAction(self.MSTool)
    #
    #     self.MDTool = QtWidgets.QAction("Drop Missioni", tool)
    #     self.MDTool.setShortcut("Ctrl+S")
    #     self.MDTool.setStatusTip("Consente di Vedere i Drop di ogni Missione")
    #     self.MDTool.triggered.connect(self.tab_menu.open_window_mission_deck)
    #     tool.addAction(self.MDTool)
    #
    #     EELog = QtWidgets.QAction("Leggi EE.log", tool)
    #     EELog.setShortcut("Ctrl+E")
    #     EELog.setStatusTip("Apre la finestra per la lettura dell'EE.log")
    #     EELog.triggered.connect(self.tab_menu.open_window_EELog)
    #     tool.addAction(EELog)
    #
    #     warframeData.MSTool = self.MSTool
    #     warframeData.MDTool = self.MDTool
    #
    #     #Menu Aiuto
    #     info = QtWidgets.QAction("Informazioni", aiuto)
    #     info.setShortcut("Ctrl+I")
    #     info.setStatusTip("Informazioni sul Programma")
    #     info.triggered.connect(self.tab_menu.info)
    #     aiuto.addAction(info)

    # def open_old_allert(self):
    #     path = get_cur_dir()
    #     path = QtWidgets.QFileDialog.getOpenFileName(self, "Seleziona allerta precedente", path, "JSON (*.json)")
    #     if (path[0]):
    #         self.update(path[0])


app = QtWidgets.QApplication(sys.argv)
app.setStyle('Fusion')

main = MainWindow()
ver = get_actual_version()
ver2 = retrieve_version()
if (float(ver) < float(ver2)):
    main.updateProgramService.open_update()
else:
    try:
        main.start_update()
    except Exception as er:
        print(er)

sys.exit(app.exec())
