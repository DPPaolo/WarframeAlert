# coding=utf-8
from enum import Enum
from PyQt5 import QtWidgets

from warframeAlert.services.translationService import translate


class MessageBoxType(Enum):
    INFO = 0
    ERROR = 1


class MessageBox():

    def __init__(self, title: str, message: str, message_type: MessageBoxType) -> None:
        self.messageBox = QtWidgets.QMessageBox()
        if (title != ""):
            self.messageBox.setText(title)
            self.messageBox.setInformativeText(message)
        else:
            self.messageBox.setText(message)

        match message_type:
            case MessageBoxType.INFO:
                self.messageBox.setIcon(QtWidgets.QMessageBox.Information)
                self.messageBox.setWindowTitle(translate("messageBox", "info"))
            case MessageBoxType.ERROR:
                self.messageBox.setIcon(QtWidgets.QMessageBox.Critical)
                self.messageBox.setWindowTitle(translate("messageBox", "error"))

        self.messageBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        self.messageBox.exec_()
