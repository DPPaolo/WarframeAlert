# coding=utf-8
import sys

from PyQt6 import QtWidgets, QtCore

from warframeAlert.components.common.MessageBox import MessageBox, MessageBoxType
from warframeAlert.services.networkService import check_connection
from warframeAlert.services.translationService import translate
from warframeAlert.services.updateFileService import UpdateFileService
from warframeAlert.utils import commonUtils
from warframeAlert.utils.logUtils import LogHandler


class UpdateRequiredFilesWidget(QtCore.QObject):
    all_file_downloaded = QtCore.pyqtSignal()
    UpdateFileWidget = None

    def __init__(self, service: UpdateFileService) -> None:
        super().__init__()
        self.update_file_service = service
        self.UpdateFileWidget = QtWidgets.QWidget()
        self.UpdateFileTitleLabel = QtWidgets.QLabel(translate("updateProgramService", "updateFileTitle") + "....")

        self.gridFileUpdate = QtWidgets.QGridLayout(self.UpdateFileWidget)

        self.gridFileUpdate.addWidget(self.UpdateFileTitleLabel, 0, 0)

        self.UpdateFileWidget.setLayout(self.gridFileUpdate)

        self.UpdateFileWidget.resize(350, 50)

        QtCore.QTimer.singleShot(1500, lambda: self.download_program_file())

    def get_widget(self) -> QtWidgets.QWidget:
        return self.UpdateFileWidget

    def close(self) -> None:
        self.all_file_downloaded.emit()
        self.UpdateFileWidget.close()

    def download_program_file(self) -> None:
        if not check_connection():
            commonUtils.print_traceback(translate("updateService", "noConnection"))
            return
        try:
            self.update_file_service.download_all_file()
            self.update_file_service.file_downloaded.connect(lambda: self.close())
        except Exception as er:
            MessageBox(translate("updateService", "saveError"), str(er), MessageBoxType.ERROR)
            LogHandler.err(translate("updateService", "saveError"))
            LogHandler.err(str(er))
            commonUtils.print_traceback(translate("updateService", "saveError") + " " + str(er))
            sys.exit()
