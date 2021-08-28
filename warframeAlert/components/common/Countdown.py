# coding=utf-8
import time

from PyQt5 import QtCore, QtWidgets, sip
from PyQt5.QtCore import QThread

from warframeAlert.services.translationService import translate
from warframeAlert.utils import timeUtils, commonUtils
from warframeAlert.utils.logUtils import LogHandler


class Countdown(QThread):
    TimeOut = QtCore.pyqtSignal()
    time = 0

    def __init__(self, *name) -> None:
        QThread.__init__(self)
        self.deleted = 0
        self.stop = 0
        if name:
            self.name = name[0]
        else:
            self.name = ""
        self.TimeLab = QtWidgets.QLabel(self.name)

    def __del__(self) -> None:
        self.deleted = 1
        try:
            self.wait()
        except RuntimeError:
            pass

    def run(self) -> None:
        while(not self.deleted):
            if not self.stop:
                end_time = int(self.time) - int(timeUtils.get_local_time())
                self.stop = 0
                try:
                    if (not sip.isdeleted(self.TimeLab)):
                        self.calculate_time(end_time)
                except Exception as er:
                    commonUtils.print_traceback(translate("countdown", "countdown_error") + ":\n" + str(end_time))
                    LogHandler.err(translate("countdown", "countdown_error") + " " + str(end_time))
                    LogHandler.err(str(er))
                    end_time = translate("countdown", "Error")
                    self.TimeLab.setText(self.name + str(end_time))
            time.sleep(1)

    def get_time(self) -> int:
        return self.time

    def calculate_time(self, end_time: int) -> None:
        if (end_time < 0):
            calculated_end_timer = translate("timeUtils", "Timed Out")
            self.TimeLab.setText(self.name + " " + str(calculated_end_timer))
            self.stop = 1
            self.TimeOut.emit()
        else:
            calculated_end_timer = timeUtils.get_alert_time(end_time)
            self.TimeLab.setText(self.name + " " + calculated_end_timer)

    def set_name(self, name: str) -> None:
        self.name = name

    def set_countdown(self, timer: int) -> None:
        self.time = int(timer)

    def set_alignment(self, alignment: QtCore.Qt.AlignmentFlag) -> None:
        self.TimeLab.setAlignment(alignment)

    def set_tooltip(self, text: str) -> None:
        self.TimeLab.setToolTip(text)

    def start_timer(self) -> None:
        self.stop = 0

    def stop_timer(self) -> None:
        self.stop = 1

    def hide(self) -> None:
        self.TimeLab.hide()
