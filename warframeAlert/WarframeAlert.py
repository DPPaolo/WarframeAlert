#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtWidgets import QMenuBar

from warframeAlert.components.common.MessageBox import MessageBox, MessageBoxType
from warframeAlert.services.menuService import MenuService, open_old_alert
from warframeAlert.services.networkService import check_connection, get_actual_version, retrieve_text_file, \
    clean_update_program
from warframeAlert.services.notificationService import NotificationService
from warframeAlert.services.optionHandlerService import OptionsHandler
from warframeAlert.services.optionService import OptionService
from warframeAlert.services.tabService import TabService
from warframeAlert.services.translationService import Translator, translate
from warframeAlert.services.trayService import TrayService
from warframeAlert.services.updateFileService import UpdateFileService
from warframeAlert.services.updateProgramService import UpdateProgramService
from warframeAlert.services.updateService import UpdateService
from warframeAlert.utils import fileUtils, timeUtils
from warframeAlert.utils.fileUtils import get_separator
from warframeAlert.utils.logUtils import LogHandler


class MainWindow(QtWidgets.QMainWindow):
    logHandler: LogHandler = None
    optionHandler: OptionsHandler = None
    translator: Translator = None
    tray: TrayService = None
    notification_service: NotificationService = None
    update_service: UpdateService = None
    update_file_service: UpdateFileService = None
    tabService: TabService = None
    updateProgramService: UpdateProgramService = None
    menuService = MenuService = None
    navBarMenu: QMenuBar = None
    options: OptionService = None

    def __init__(self) -> None:
        super().__init__()

        # Copy mandatory files if missing
        fileUtils.check_mandatory_files()

        # Start the log handler
        self.logHandler = LogHandler()

        # Start the options service
        self.optionHandler = OptionsHandler()

        # Start the translation Service
        self.translator = Translator()

        self.setWindowTitle(translate("main", "title"))

        self.app = QtCore.QCoreApplication.instance()
        self.app.setApplicationName(translate("main", "title"))
        self.app.setOrganizationName("Onnisciente")
        self.setWindowIcon(QtGui.QIcon("assets" + get_separator() + "icon" + get_separator() + "Warframe.ico"))

        self.mainWidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.mainWidget)

        self.resize(680, 450)

        # Check if there is a new version downloaded
        if (fileUtils.check_file("PostUpdate.txt")):
            clean_update_program()

    def start_main_services(self) -> None:
        # Start the tab Service
        main_tabber = QtWidgets.QTabWidget(self.mainWidget)
        self.tabService = TabService(main_tabber)

        main_grid = QtWidgets.QGridLayout(self.mainWidget)
        main_grid.addWidget(main_tabber, 0, 0, 1, 1)

        self.tabService.update_tabber()

        # Start the update service
        self.update_service = UpdateService()

        self.update_service.file_downloaded.connect(lambda: self.tabService.update(""))

        # Start the file update service
        self.update_file_service = UpdateFileService()

        # Start the program service updater
        self.updateProgramService = UpdateProgramService(self.update_file_service)

        if (OptionsHandler.get_option("FirstInit") == 0):
            # Download files if it's the first init
            self.init_app()
        else:
            update_cycle = OptionsHandler.get_option("Update/Cycle")
            if ((not str(update_cycle).isdigit() or int(update_cycle) < 30) and not check_connection()):
                self.tabService.update("")

        self.show()

    def start_other_services(self) -> None:

        # Create service used on the menu on top of the tabs
        self.menuService = MenuService()

        # Create the nav bar menu on top of the tabs
        self.navBarMenu = self.menuBar()
        self.create_menu()

        # Create a status bar under the tabs
        self.statusBar()

        # Create the options screen
        self.options = OptionService(self.tabService, self.update_service, self.updateProgramService)

        # Start the tray Service
        self.tray = TrayService(self)

        # Start the notification Service
        self.notification_service = NotificationService(self.tray.get_tray_icon())
        self.notification_service.start()

    def start_update(self) -> None:
        self.update_service.start()
        QtCore.QTimer.singleShot(1000*60, lambda: check_for_update())

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
        if (not check_connection()):
            MessageBox(translate("main", "noConnection"),
                       translate("main", "noConnectionFirstInit"),
                       MessageBoxType.ERROR)
            sys.exit()

        self.optionHandler.create_config()

        self.updateProgramService.open_and_update_file()
        self.updateProgramService.UpdateFile.all_file_downloaded.connect(lambda: self.tabService.update(""))
        OptionsHandler.set_option("FirstInit", 1)

    def schedule_update_secondary_files(self) -> None:
        old_update_date = OptionsHandler.get_option("Update/AutoUpdateAll")
        actual_date = int(timeUtils.get_local_time())
        if ((actual_date - old_update_date) > 604800 and check_connection()):
            OptionsHandler.set_option("Update/AutoUpdateAll", actual_date)
            QtCore.QTimer.singleShot(45 * 1000, lambda: self.update_file_service.download_all_file())

    def create_menu(self) -> None:
        file = self.navBarMenu.addMenu('&' + translate("main", "fileMenu"))
        debug = self.navBarMenu.addMenu('&' + translate("main", "dataMenu"))
        tool = self.navBarMenu.addMenu('&' + translate("main", "toolsMenu"))
        info = self.navBarMenu.addMenu('&' + translate("main", "helpMenu"))

        # Files Menu
        open_alert = QtGui.QAction(translate("main", "openOldFile") + "...", file)
        open_alert.setShortcut("Ctrl+O")
        open_alert.setStatusTip(translate("main", "openOldFileTip"))
        open_alert.triggered.connect(lambda: open_old_alert(self.tabService))
        file.addAction(open_alert)

        option = QtGui.QAction(translate("main", "options"), file)
        option.setShortcut("Ctrl+O")
        option.setStatusTip(translate("main", "openOptionsTip"))
        option.triggered.connect(lambda: self.options.open_option())
        file.addAction(option)

        exit_menu = QtGui.QAction(translate("main", "exitMenu"), file)
        exit_menu.setShortcut("Ctrl+Q")
        exit_menu.setStatusTip(translate("main", "exitMenuDesc"))
        exit_menu.triggered.connect(QtCore.QCoreApplication.quit)
        file.addAction(exit_menu)

        # Debug Menu
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

        parse_file = QtGui.QAction(translate("main", "parseUpdateFilesMenu"), debug)
        parse_file.setShortcut("Ctrl+P")
        parse_file.setStatusTip(translate("main", "parseUpdateFilesMenuTip"))
        parse_file.triggered.connect(lambda: self.tabService.update(""))
        debug.addAction(parse_file)

        # Tools Menu
        read_log = QtGui.QAction(translate("main", "readEELog"), tool)
        read_log.setShortcut("Ctrl+E")
        read_log.setStatusTip(translate("main", "toolHelpMenuEELog"))
        read_log.triggered.connect(self.menuService.open_window_read_warframe_log)
        tool.addAction(read_log)

        # Info Menu
        copyright_info = QtGui.QAction(translate("main", "infoHelpMenu"), info)
        copyright_info.setShortcut("Ctrl+I")
        copyright_info.setStatusTip(translate("main", "infoHelpMenuTooltip"))
        copyright_info.triggered.connect(self.menuService.show_info)
        info.addAction(copyright_info)


def check_for_update() -> None:
    actual_version = get_actual_version()
    online_version = retrieve_text_file("version.txt", actual_version)
    if (float(actual_version) < float(online_version)):
        MessageBox(translate("main", "updateProgramTitleBox"), translate("main", "updateProgramDescBox"),
                   MessageBoxType.INFO_WITH_LINK, main.options.open_update)


app = QtWidgets.QApplication(sys.argv)
app.setStyle('Fusion')

try:
    main = MainWindow()
    main.start_main_services()
    main.start_other_services()
    main.start_update()
except Exception as er:
    print(er)

sys.exit(app.exec())
