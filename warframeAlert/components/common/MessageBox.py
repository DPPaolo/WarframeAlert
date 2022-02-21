# coding=utf-8
from enum import Enum
from typing import Callable, Any

from PyQt6 import QtWidgets

from warframeAlert.services.translationService import translate


class MessageBoxType(Enum):
    INFO = 0
    ERROR = 1
    INFO_WITH_LINK = 2


class MessageBox():

    def __init__(self, title: str, message: str, message_type: MessageBoxType,
                 link_function: Callable[..., Any] = None) -> None:
        self.messageBox = QtWidgets.QMessageBox()
        if (title != ""):
            self.messageBox.setText(title)
            self.messageBox.setInformativeText(message)
        else:
            self.messageBox.setText(message)

        match message_type:
            case MessageBoxType.INFO:
                self.messageBox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                self.messageBox.setWindowTitle(translate("messageBox", "info"))
            case MessageBoxType.ERROR:
                self.messageBox.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                self.messageBox.setWindowTitle(translate("messageBox", "error"))
            case MessageBoxType.INFO_WITH_LINK:
                self.messageBox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                self.messageBox.setWindowTitle(translate("messageBox", "info"))
                update_button = self.messageBox.addButton(translate("messageBox", "update"),
                                                          QtWidgets.QMessageBox.ButtonRole.ActionRole)
                update_button.clicked.connect(lambda: link_function())

        self.messageBox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        self.messageBox.exec()
