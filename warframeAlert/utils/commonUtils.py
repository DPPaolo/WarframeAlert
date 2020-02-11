# coding=utf-8
import sys
import traceback

from warframeAlert.services.translationService import translate


def print_traceback(mess):
    print(mess)
    exc_type, exc_value, exc_traceback = sys.exc_info()
    traceback.print_exception(exc_type, exc_value, exc_traceback)


def get_last_item_with_backslash(text):
    text = text.split("/")
    return text[len(text) - 1]


def bool_to_yes_no(boolean):
    if (boolean):
        return translate("commonUtils", "yes")
    else:
        return translate("commonUtils", "no")


def remove_widget(layout):
    for i in reversed(range(layout.count())):
        if (layout.itemAt(i) is not None):
            widget_to_remove = layout.itemAt(i).widget()
            # remove the layout from the layout's list
            layout.removeWidget(widget_to_remove)
            # without parent, the layout will be deleted automatically
            if (widget_to_remove is not None):
                widget_to_remove.setParent(None)
