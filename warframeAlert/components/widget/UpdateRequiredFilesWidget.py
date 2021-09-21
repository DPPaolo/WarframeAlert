# coding=utf-8

from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer

from warframeAlert.components.common.MessageBox import MessageBox, MessageBoxType
from warframeAlert.constants.files import OTHER_FILE_SITE, OTHER_FILE_NAME
from warframeAlert.services.networkService import check_connection, ProgressBarDownloader
from warframeAlert.services.optionHandlerService import OptionsHandler
from warframeAlert.services.translationService import translate
from warframeAlert.utils import commonUtils, warframeFileUtils
from warframeAlert.utils.fileUtils import get_separator
from warframeAlert.utils.logUtils import LogHandler


class UpdateRequiredFilesWidget():
    UpdateFileWidget = None

    def __init__(self) -> None:
        self.UpdateFileWidget = QtWidgets.QWidget()

        self.UpdateFileTitleLabel = QtWidgets.QLabel(translate("updateProgramService", "updateFileTitle") + ":")
        self.UpdateFilePer = QtWidgets.QProgressBar()

        self.gridFileUpdate = QtWidgets.QGridLayout(self.UpdateFileWidget)

        self.gridFileUpdate.addWidget(self.UpdateFileTitleLabel, 0, 0)
        self.gridFileUpdate.addWidget(self.UpdateFilePer, 1, 0)

        self.UpdateFileWidget.setLayout(self.gridFileUpdate)

        self.UpdateFileWidget.resize(350, 50)

        QTimer.singleShot(1500, lambda: self.download_other_file(self.UpdateFilePer, self.UpdateFileTitleLabel, 0))

    def get_widget(self) -> QtWidgets.QWidget:
        return self.UpdateFileWidget

    def download_program_file(self) -> None:
        if not check_connection():
            commonUtils.print_traceback(translate("updateService", "noConnection"))
            return
        try:
            self.download_other_file(self.UpdateFilePer, self.UpdateFileTitleLabel, 0)
        except Exception as er:
            MessageBox(translate("updateService", "saveError"), str(er), MessageBoxType.ERROR)
            LogHandler.err(translate("updateService", "saveError"))
            LogHandler.err(str(er))
            commonUtils.print_traceback(translate("updateService", "saveError") + " " + str(er))

    def download_other_file(self, progress_bar: QtWidgets.QProgressBar, label: QtWidgets.QLabel, index: int) -> None:
        i = index
        if (i >= len(OTHER_FILE_NAME)):
            warframeFileUtils.write_json_drop()
            OptionsHandler.set_option("FirstInit", 1)
            self.UpdateFileWidget.close()
            return
        label.setText(translate("updateProgramService", "updateFileTitle") + ": " + OTHER_FILE_NAME[i])
        path = "data" + get_separator() + OTHER_FILE_NAME[i]
        downloader = ProgressBarDownloader(progress_bar, OTHER_FILE_SITE[i], path)
        downloader.download_completed.connect(lambda: self.download_other_file(progress_bar, label, i + 1))
        downloader.start()
