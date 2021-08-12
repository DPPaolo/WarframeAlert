# coding=utf-8
from PyQt5 import QtCore

from warframeAlert.components.common.MessageBox import MessageBox, MessageBoxType
from warframeAlert.constants.files import DATA_SITE
from warframeAlert.services import networkService
from warframeAlert.services.optionHandlerService import OptionsHandler
from warframeAlert.services.translationService import translate
from warframeAlert.utils.commonUtils import print_traceback
from warframeAlert.utils.fileUtils import get_separator
from warframeAlert.utils.logUtils import LogHandler


class UpdateService(QtCore.QObject):
    file_downloaded = QtCore.pyqtSignal()
    fist_init_completed = QtCore.pyqtSignal()

    def __init__(self) -> None:
        super().__init__()
        self.update_timer: QtCore.QTimer = QtCore.QTimer()
        self.downloader_thread = None
        update_cycle: int = OptionsHandler.get_option("Update/Cycle")
        if (str(update_cycle).isdigit() and int(update_cycle) >= 30):
            self.download_alert_file(True)

    def start(self) -> None:
        update_cycle: int = OptionsHandler.get_option("Update/Cycle")
        if (not str(update_cycle).isdigit()):
            return
        if (int(update_cycle) < 30):
            self.stop()
            return

        self.update_timer.singleShot(int(update_cycle)*1000, self.download_alert_file)

    def stop(self) -> None:
        self.update_timer.stop()
        self.update_timer.deleteLater()

    def download_alert_file(self, download_only: bool = False) -> None:
        opt: int = OptionsHandler.get_option("Update/Console")
        if (opt == 0):
            url: str = DATA_SITE["PC"]
        elif (opt == 1):
            url: str = DATA_SITE["PS4"]
        elif (opt == 2):
            url: str = DATA_SITE["XBOX"]
        elif (opt == 3):
            url: str = DATA_SITE["SWITCH"]
        else:
            url: str = DATA_SITE["PC"]
        #  TODO: implement then python 3.10 release
        # match opt:
        #     case 0:
        #         url: str = DATA_SITE["PC"]
        #     case 1:
        #         url: str = DATA_SITE["PS4"]
        #     case 2:
        #         url: str = DATA_SITE["XBOX"]
        #     case 3:
        #         url: str = DATA_SITE["SWITCH"]
        #     case _:
        #         url: str = DATA_SITE["PC"]

        try:
            path = "data" + get_separator() + "allerte.json"
            self.downloader_thread: networkService.Downloader = networkService.Downloader(url, path, 0)
            self.downloader_thread.start()
            self.downloader_thread.download_completed.connect(lambda: self.download_finished(download_only))
        except Exception as er:
            MessageBox(translate("updateService", "saveError"), str(er), MessageBoxType.ERROR)
            LogHandler.err(translate("updateService", "saveError"))
            LogHandler.err(str(er))
            print_traceback(translate("updateService", "saveError") + " " + str(er))

    def download_finished(self, download_only: bool) -> None:
        if (OptionsHandler.get_option("Debug") == 1):
            LogHandler.debug("allerte.json" + " " + translate("updateService", "downloaded"))
        self.file_downloaded.emit()
        if (not download_only):
            self.start()
        else:
            self.fist_init_completed.emit()
            OptionsHandler.set_first_init(False)
