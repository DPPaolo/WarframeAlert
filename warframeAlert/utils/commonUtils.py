# coding=utf-8
import platform
import sys
import traceback


def print_traceback(mess):
    print(mess)
    exc_type, exc_value, exc_traceback = sys.exc_info()
    traceback.print_exception(exc_type, exc_value, exc_traceback)


def get_os_type():
    return platform.system()


def is_mac_os():
    return get_os_type() == "Darwin"


def get_separator():
    sep = "\\"  # Windows default separator
    if (is_mac_os()):  # the OS is a MacOs
        sep = "/"
    return sep


def get_last_item_with_backslash(text):
    text = text.split("/")
    return text[len(text) - 1]


def remove_widget(layout):
    for i in reversed(range(layout.count())):
        if (layout.itemAt(i) is not None):
            widget_to_remove = layout.itemAt(i).widget()
            # remove the layout from the layout's list
            layout.removeWidget(widget_to_remove)
            # without parent, the layout will be deleted automatically
            if (widget_to_remove is not None):
                widget_to_remove.setParent(None)
