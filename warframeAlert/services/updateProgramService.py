# coding=utf-8

from PyQt5 import QtCore

from warframeAlert.components.widget.UpdateProgramWidget import UpdateProgramWidget
from warframeAlert.services.translationService import translate


class UpdateProgramService(QtCore.QObject):
    AutoUpdate = None
    UpdateFileWidget = None

    def __init__(self) -> None:
        super().__init__()

    def open_update(self) -> None:
        self.AutoUpdate = UpdateProgramWidget().get_widget()
        self.AutoUpdate.setWindowTitle(translate("updateProgramService", "title"))
        self.AutoUpdate.show()

    def open_update_file(self) -> None:
        self.UpdateFileWidget, obj = warframeUI.widget_update_file(self)
        self.UpdateFileWidget.setWindowTitle(translate("updateProgramService", "updateFileTitle"))
        self.UpdateFileWidget.show()
        warframeData.gestore_update_file.download_program_file(obj)

