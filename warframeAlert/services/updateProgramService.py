# coding=utf-8

from warframeAlert.components.widget.UpdateProgramWidget import UpdateProgramWidget
from warframeAlert.components.widget.UpdateRequiredFilesWidget import UpdateRequiredFilesWidget
from warframeAlert.services.translationService import translate
from warframeAlert.services.updateFileService import UpdateFileService


class UpdateProgramService():
    AutoUpdate = None
    UpdateFile = None

    def __init__(self, service: UpdateFileService) -> None:
        self.AutoUpdate = UpdateProgramWidget()
        self.UpdateFile = UpdateRequiredFilesWidget(service)

    def open_update(self) -> None:
        self.AutoUpdate.get_widget().setWindowTitle(translate("updateProgramService", "title"))
        self.AutoUpdate.show_widget()

    def open_and_update_file(self) -> None:
        self.UpdateFile.get_widget().setWindowTitle(translate("updateProgramService", "updateFileTitle"))
        self.UpdateFile.show_widget()
