# coding=utf-8
import sys
import traceback

from PyQt5 import QtGui
from PyQt5.QtCore import QObject
from PyQt5.QtGui import QPixmap

from warframeAlert.services.translationService import translate
from warframeAlert.utils.fileUtils import get_cur_dir, get_separator
from warframeAlert.utils.logUtils import LogHandler


def print_traceback(mess: str) -> None:
    LogHandler.debug(mess)
    exc_type, exc_value, exc_traceback = sys.exc_info()
    traceback.print_exception(exc_type, exc_value, exc_traceback)


def get_last_item_with_backslash(text: str) -> str:
    text = text.split("/")
    return text[len(text) - 1]


def create_pixmap(image_name: str) -> QPixmap:
    image = QtGui.QPixmap()
    image.load(get_cur_dir() + get_separator() + image_name)
    return image


def bool_to_yes_no(boolean: bool | int) -> str:
    if (boolean):
        return translate("commonUtils", "yes")
    else:
        return translate("commonUtils", "no")


def bool_to_int(boolean: bool) -> int:
    if (boolean):
        return 1
    else:
        return 0


def remove_widget(layout: QObject) -> None:
    for i in reversed(range(layout.count())):
        if (layout.itemAt(i) is not None):
            widget_to_remove = layout.itemAt(i).widget()
            # remove the layout from the layout's list
            layout.removeWidget(widget_to_remove)
            # without parent, the layout will be deleted automatically
            if (widget_to_remove is not None):
                widget_to_remove.setParent(None)
