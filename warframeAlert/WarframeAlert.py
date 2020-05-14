#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5 import QtGui, QtCore, QtWidgets

from utils import timeUtils, commonUtils

import os
import shutil
import subprocess
import sys
import time
import Qtwarframe
import warframe
import warframeData
import warframeClass

from warframeAlert.services.networkService import check_connection
from warframeAlert.services.notificationService import NotificationService
from warframeAlert.services.optionHandlerService import OptionsHandler
from warframeAlert.services.tabService import TabService
from warframeAlert.services.translationService import Translator, translate
from warframeAlert.services.trayService import TrayService
from warframeAlert.utils import fileUtils
from warframeAlert.utils.fileUtils import create_default_folder, get_cur_dir, get_separator
from warframeAlert.utils.logUtils import LogHandler


warframeData.TRAY_ICON = None

#Creazione file di configurazione
#gestore_opzioni = warframeClass.gestore_opzioni()

#Avvia i vari gestori del programma
#warframeData.gestore_update = warframeClass.gestore_update()
#warframeData.gestore_update_file = warframeClass.gestore_update_file()


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
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

        self.setWindowTitle(translate("main", "title"))

        self.app = QtCore.QCoreApplication.instance()
        self.app.setApplicationName(translate("main", "title"))
        self.app.setOrganizationName("Onniscente")
        self.setWindowIcon(QtGui.QIcon("assets" + get_separator() + "icon" + get_separator() + "Warframe.ico"))

        self.mainWidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.mainWidget)

        # Start the tab Service
        self.mainTabber = QtWidgets.QTabWidget(self.mainWidget)
        self.tabService = TabService(self.mainTabber)



        #Crea il menu e le sue schede
        #self.tab_menu = warframeClass.tab_menu()

        #Crea la finestra delle opzioni
        #gestore_opzioni.create_config_widget()

        #Crea la finestra per gli aggiornamenti
        #warframeData.gestore_update.create_update_widget()
                
        #self.create_menu()      #crea il Menu

        #self.statusBar() # crea una veloce barra di stato

        #gestore_opzioni.UpdateTabber.connect(self.update_tab)

        self.mainGrid = QtWidgets.QGridLayout(self.mainWidget)
        self.mainGrid.addWidget(self.mainTabber, 0, 0, 1, 1)

        #self.init_app()

        self.tabService.update_tabber()

        self.resize(680, 450)
        
    # def start_update(self):
    #     #Aggiorna il contenuto delle varie Tab e avvia il timer di aggiornamento
    #     self.tabService.update(False)
    #     self.resize(680, 450)
    #
    #     OptionsHandler.set_first_init(False)
    #     warframeData.gestore_update.start_update_timer(self)
    #
    # def closeEvent(self, event):
    #     if (warframeClass.gestore_opzioni.get_option("TrayIcon") == 1):
    #         event.ignore()
    #         self.hide()
    #         NotificationService.send_notification(
    #             "Warframe Alert",
    #             "L'applicazione verrà ridotta ad icona.",
    #             QtWidgets.QSystemTrayIcon.Information)
    #     #else:
    #         #salva dati sula size() e pos() della finestra principale
    #         #resize(settings.value("size", QSize(400, 400)).toSize());
    #         #move(settings.value("pos", QPoint(200, 200)).toPoint());

    # def init_app(self):
    #
    #     #Controlla se c'è stato un aggiornamento della versione del programma
    #     if (fileUtils.check_file("PostUpdate.txt")):
    #         fp = open("PostUpdate.txt", "r")
    #         line = fp.readlines()
    #         pid = str(line[0]).replace("\n", "")
    #         ver = str(line[1]).replace("\n", "")
    #         fp.close()
    #         name = r'Warframe Alert ' + ver + ".exe"
    #         try:
    #             subprocess.call("taskkill /PID " + pid)
    #             time.sleep(1)
    #             os.remove(name)
    #         except Exception as er:
    #             warframe.stampa_errore("Impossibile cancellare/chiudere la vecchia versione del programma\n" + str(er))
    #         os.remove("PostUpdate.txt")
    #
    #     #Scarica i file se e' il primo avvio e crea il file di opzioni
    #     if (warframeClass.gestore_opzioni.get_option("FirstInit") == 0):
    #         if not check_connection() and not (warframeClass.gestore_opzioni.get_option("Debug") == 1):
    #             Qtwarframe.errore("Il primo avvio dell'applicazione necessita di una connessione ad internet.\nAssicurati di essere connesso alla rete")
    #             self.emit(QtCore.SLOT('close()'))
    #             return
    #
    #         create_default_folder()
    #
    #         gestore_opzioni.create_config()
    #         warframeData.gestore_update.open_update_file()
    #         if (not fileUtils.is_linux_os() and not fileUtils.is_linux_os()):
    #             if getattr(sys, 'frozen', False):
    #                 path = getattr(sys, '_MEIPASS', os.getcwd())
    #                 shutil.copytree(path + "/assets/icon", "assets/icon")
    #                 shutil.copytree(path + "/assets/image", "assets/image")
    #                 shutil.copytree(path + "/translation", "translation")
    #         warframeClass.gestore_opzioni.set_option("FirstInit", 1)
    #
    #     # #controlla se è presente l'icona del programma
    #     ##sistemare e farlo fare solo manca un file in quelle cartelle
    #     if not fileUtils.check_file("assets/icon/Warframe.ico") and getattr(sys, 'frozen', False):
    #         path = getattr(sys, '_MEIPASS', os.getcwd())
    #         shutil.copytree(path + "/assets/icon", "assets/icon")
    #         shutil.copytree(path + "/assets/image", "assets/image")
    #         shutil.copytree(path + "/translation", "translation")
    #
    #     #aggiorna i file necessari al funzionamento
    #     if (warframeClass.gestore_opzioni.get_option("Update/Cycle") != 0):
    #         warframeData.gestore_update_file.update_alert_file_only(True)
    #
    #
    #     date = warframeClass.gestore_opzioni.get_option("Update/AutoUpdateAll")
    #     att_date = int(timeUtils.get_local_time())
    #     if ((att_date - date) > 604800):
    #         warframeClass.gestore_opzioni.set_option("Update/AutoUpdateAll", att_date)
    #         warframeData.gestore_update.open_update_file()

    # def create_menu(self):
    #     self.menu = self.menuBar()
    #
    #     file = self.menu.addMenu('&File')
    #     if (warframeClass.gestore_opzioni.get_option("Debug") == 1):
    #         debug = self.menu.addMenu('&Debug')
    #     tool = self.menu.addMenu('&Strumenti')
    #     aiuto = self.menu.addMenu('&Aiuto')
    #
    #     #Menu File
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
    #
    #     esci = QtWidgets.QAction("Esci", file)
    #     esci.setShortcut("Ctrl+Q")
    #     esci.setStatusTip("Esci dall'Applicazione")
    #     esci.triggered.connect(QtCore.QCoreApplication.quit)
    #     file.addAction(esci)
    #
    #     #Menu Debug
    #     if (warframeClass.gestore_opzioni.get_option("Debug") == 1):
    #         update_file = QtWidgets.QAction("Aggiorna Tutti i File", debug)
    #         update_file.setShortcut("Ctrl+U")
    #         update_file.setStatusTip("Aggiorna Tutti i File utilizzati dal programma")
    #         update_file.triggered.connect(lambda: warframeData.gestore_update_file.update_alert_file(False))
    #         debug.addAction(update_file)
    #
    #         update_only_file = QtWidgets.QAction("Aggiorna File Allerte", debug)
    #         update_only_file.setShortcut("Ctrl+T")
    #         update_only_file.setStatusTip("Aggiorna solo il File delle Allerte")
    #         update_only_file.triggered.connect(lambda: warframeData.gestore_update_file.update_alert_file_only(False))
    #         debug.addAction(update_only_file)
    #
    #         parse_file = QtWidgets.QAction("Parserizza il File", debug)
    #         parse_file.setShortcut("Ctrl+P")
    #         parse_file.setStatusTip("Traduce le Allerte a Schermo")
    #         parse_file.triggered.connect(lambda: self.update(False))
    #         debug.addAction(parse_file)
    #
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
    #     if (warframeClass.gestore_opzioni.get_option("ViewStarChart") == 0):
    #         self.MSTool.setVisible(False)
    #     if (warframeClass.gestore_opzioni.get_option("ViewMissionDeck") == 0):
    #         self.MDTool.setVisible(False)
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

    # def update_fissure(self, data):
    #     if (warframeClass.gestore_opzioni.get_option("Tab/Fissure")== 1):
    #         try:
    #             Qtwarframe.parse_fissure(self.tab_fissure, data)
    #         except Exception as er:
    #             warframe.err("Errore nelle Fissure: " + str(er))
    #             warframe.stampa_errore("Errore nelle Fissure: " + str(er))
    #             self.tab_fissure.reset_fissure()
    #             return
    #     else:
    #         self.tab_fissure.reset_fissure()
    #
    # def update_dark_sector(self, data):
    #     if (warframeClass.gestore_opzioni.get_option("Tab/PvP")== 1):
    #         try:
    #             Qtwarframe.parse_dark_sector(self.tab_pvp, data)
    #         except Exception as er:
    #             warframe.err("Errore nei Settori Oscuri: " + str(er))
    #             warframe.stampa_errore("Errore nei Settori Oscuri: " + str(er))
    #             self.tab_pvp.reset_dark_sector()
    #             return
    #
    # def update_sales(self, data):
    #     if (warframeClass.gestore_opzioni.get_option("Tab/Market")== 1):
    #         try:
    #             Qtwarframe.parse_sales(self.tab_sconti, data)
    #         except Exception as er:
    #             warframe.err("Errore negli Sconti: " + str(er))
    #             warframe.stampa_errore("Errore negli Sconti: " + str(er))
    #             self.tab_sconti.reset_sales()
    #             return
    #     else:
    #         self.tab_sconti.reset_sales()
    #
    # def update_PVP_tournament(self, data):
    #     if (warframeClass.gestore_opzioni.get_option("Tab/PVP")== 1):
    #         try:
    #             Qtwarframe.parse_pvp_tournament(self.tab_pvp, data)
    #         except Exception as er:
    #             warframe.err("Errore nei Tornei PvP: " + str(er))
    #             warframe.stampa_errore("Errore nei Tornei PvP: " + str(er))
    #             self.tab_pvp.PVP_tournament_not_available()
    #             return
    #     else:
    #         self.tab_pvp.PVP_tournament_not_available()
    #
    # def update_PVP_alternative_mission(self, data):
    #     if (warframeClass.gestore_opzioni.get_option("Tab/PVP")== 1):
    #         try:
    #             Qtwarframe.parse_pvp_alternative_mission(self.tab_pvp, data)
    #         except Exception as er:
    #             warframe.err("Errore nelle Missioni PvP Alternative: " + str(er))
    #             warframe.stampa_errore("Errore nelle Missioni PvP Alternative: " + str(er))
    #             self.tab_pvp.PVP_alternative_mission_not_available()
    #             return
    #     else:
    #         self.tab_pvp.PVP_alternative_mission_not_available()
    #
    # def update_PVP_mission(self, data):
    #     if (warframeClass.gestore_opzioni.get_option("Tab/PVP")== 1):
    #         try:
    #             Qtwarframe.parse_pvp_mission(self.tab_pvp, data)
    #         except Exception as er:
    #             warframe.err("Errore nelle Missioni PvP: " + str(er))
    #             warframe.stampa_errore("Errore nelle Missioni PvP: " + str(er))
    #             self.tab_pvp.PVP_mission_not_available()
    #             return
    #     else:
    #         self.tab_pvp.PVP_alternative_mission_not_available()
    #
    # def update_sortie(self, data):
    #     if (warframeClass.gestore_opzioni.get_option("Tab/Sortie")== 1):
    #         try:
    #             Qtwarframe.parse_sortie(self.tab_sortie, data)
    #         except Exception as er:
    #             warframe.err("Errore nelle Sortie: " + str(er))
    #             warframe.stampa_errore("Errore nelle Sortie: " + str(er))
    #             self.tab_sortie.sortie_not_available()
    #             return
    #     else:
    #         self.tab_sortie.sortie_not_available()
    #
    # def update_baro(self, data):
    #     if (warframeClass.gestore_opzioni.get_option("Tab/Baro")== 1):
    #         try:
    #             Qtwarframe.parse_baro(self.tab_baro, data)
    #         except Exception as er:
    #             warframe.err("Errore in Baro Ki'Teer: " + str(er))
    #             warframe.stampa_errore("Errore in Baro Ki'Teer: " + str(er))
    #             self.tab_baro.delete_baro()
    #             return
    #     else:
    #         self.tab_baro.delete_baro()
    #
    # def open_old_allert(self):
    #     path = get_cur_dir()
    #     path = QtWidgets.QFileDialog.getOpenFileName(self, "Seleziona allerta precedente", path, "JSON (*.json)")
    #     if (path[0]):
    #         self.update(path[0])


    # def open_update(self):
    #     warframeData.gestore_update.open_update()
    #
    # def get_actual_version(self):
    #     return warframeData.gestore_update.get_actual_version()
    #
    # def retrieve_version(self):
    #     return warframeData.gestore_update.retrieve_version()

app = QtWidgets.QApplication(sys.argv)
app.setStyle('Fusion')

main = MainWindow()
# ver = main.get_actual_version()
# ver2 = main.retrieve_version()
# if (float(ver) < float(ver2)):
#     main.open_update()
# else:
#     try:
#         main.start_update()
#         main.show()
#     except Exception as er:
#         print(er)
#
main.show()
sys.exit(app.exec_())