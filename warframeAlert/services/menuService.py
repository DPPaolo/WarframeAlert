# coding=utf-8

from warframeAlert.components.common.MessageBox import MessageBox, MessageBoxType
from warframeAlert.components.widget.EELogWidget import EELogWidget
from warframeAlert.services.translationService import translate


class MenuService():
    COPYRIGHT = translate("menuService", "createdBy") + " Onniscente\n\n" + \
                "Warframe's Content and Materials are Trademarks and Copyrights of Digital Extremes."

    def __init__(self) -> None:
        self.EELogViewWidget = EELogWidget()

    def show_info(self) -> None:
        MessageBox(translate("menuService", "infoTitle"), self.COPYRIGHT, MessageBoxType.INFO)

    def open_window_read_warframe_log(self) -> None:
        self.EELogViewWidget.get_widget().show()
