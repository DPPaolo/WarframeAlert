# coding=utf-8
from PyQt6 import QtWidgets

from warframeAlert.components.common.MessageBox import MessageBox, MessageBoxType
from warframeAlert.components.widget.EELogWidget import EELogWidget
from warframeAlert.services.tabService import TabService
from warframeAlert.services.translationService import translate
from warframeAlert.utils.fileUtils import get_cur_dir


class MenuService():
    COPYRIGHT = " Onniscente\n\nWarframe's Content and Materials are Trademarks and Copyrights of Digital Extremes."

    def __init__(self) -> None:
        self.EELogViewWidget = EELogWidget()

    def show_info(self) -> None:
        copyright_text = translate("menuService", "createdBy") + self.COPYRIGHT
        MessageBox(translate("menuService", "infoTitle"), copyright_text, MessageBoxType.INFO)

    def open_window_read_warframe_log(self) -> None:
        self.EELogViewWidget.get_widget().show()


def open_old_alert(tab_service: TabService) -> None:
    path = get_cur_dir()
    path = QtWidgets.QFileDialog.getOpenFileName(QtWidgets.QWidget(),
                                                 translate("menuService", "selectAlertFile"),
                                                 path, "JSON (*.json)")
    if (path[0]):
        tab_service.update(path[0])
