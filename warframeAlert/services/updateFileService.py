# coding=utf-8
from typing import List

from PyQt6 import QtCore

from warframeAlert.components.common.MessageBox import MessageBox, MessageBoxType
from warframeAlert.constants.files import OTHER_FILE_SITE, OTHER_FILE_NAME, DEFAULT_MANIFEST_SITE
from warframeAlert.services import networkService
from warframeAlert.services.optionHandlerService import OptionsHandler
from warframeAlert.services.translationService import translate
from warframeAlert.utils import warframeFileUtils
from warframeAlert.utils.commonUtils import print_traceback
from warframeAlert.utils.fileUtils import get_separator
from warframeAlert.utils.logUtils import LogHandler


class UpdateFileService(QtCore.QObject):
    file_downloaded = QtCore.pyqtSignal()
    num_files_downloaded: int = 0

    def __init__(self) -> None:
        super().__init__()
        self.downloader_thread: List[networkService.Downloader] = []

    def download_all_file(self) -> None:
        self.downloader_thread: List[networkService.Downloader] = []
        self.num_files_downloaded = 0
        for i in range(0, len(OTHER_FILE_SITE)):
            try:
                download_path: str = "data" + get_separator() + OTHER_FILE_NAME[i]
                url: str = OTHER_FILE_SITE[i]
                self.downloader_thread.append(networkService.Downloader(url, download_path, 0))
                self.downloader_thread[i].start()
            except Exception as er:
                MessageBox(translate("updateService", "saveError"), str(er), MessageBoxType.ERROR)
                LogHandler.err(translate("updateService", "saveError"))
                LogHandler.err(str(er))
                print_traceback(translate("updateService", "saveError") + " " + str(er))

        self.downloader_thread[0].download_completed.connect(lambda: self.download_finished(0))
        self.downloader_thread[1].download_completed.connect(lambda: self.download_finished(1))
        self.downloader_thread[2].download_completed.connect(lambda: self.download_finished(2))
        self.downloader_thread[3].download_completed.connect(lambda: self.download_finished(3))
        self.downloader_thread[4].download_completed.connect(lambda: self.download_finished(4))
        self.downloader_thread[5].download_completed.connect(lambda: self.download_finished(5))
        self.downloader_thread[6].download_completed.connect(lambda: self.download_finished(6))
        self.downloader_thread[7].download_completed.connect(lambda: self.download_finished(7))
        self.downloader_thread[8].download_completed.connect(lambda: self.download_finished(8))
        self.downloader_thread[9].download_completed.connect(lambda: self.download_finished(9))
        self.downloader_thread[10].download_completed.connect(lambda: self.download_finished(10))
        self.downloader_thread[11].download_completed.connect(lambda: self.download_finished(11))
        self.downloader_thread[12].download_completed.connect(lambda: self.download_finished(12))
        self.downloader_thread[13].download_completed.connect(lambda: self.download_finished(13))

    def download_finished(self, index: int) -> None:
        self.num_files_downloaded += 1
        if (OptionsHandler.get_option("Debug") == 1):
            LogHandler.debug(OTHER_FILE_NAME[index] + " " + translate("updateService", "downloaded"))
        if (self.num_files_downloaded == len(OTHER_FILE_NAME)):
            self.downloader_thread: List[networkService.Downloader] = []
            manifest_id: str = warframeFileUtils.decompress_export_manifest_index()
            if (manifest_id != ""):
                self.download_export_manifest(manifest_id)
            warframeFileUtils.write_json_drop()
            print(translate("updateService", "downloadFinished"))
            self.file_downloaded.emit()

    def download_export_manifest(self, manifest_id: str) -> None:
        file_name: str = "ExportManifest.json"
        download_path: str = "data" + get_separator() + file_name
        url: str = DEFAULT_MANIFEST_SITE + manifest_id
        self.downloader_thread.append(networkService.Downloader(url, download_path, 0))
        self.downloader_thread[0].start()
        self.downloader_thread[0].download_completed.connect(
            lambda: print(file_name + " " + translate("updateService", "downloaded")))
