# coding=utf-8
from PyQt5 import QtCore

from warframeAlert.services.optionHandlerService import OptionsHandler
from warframeAlert.utils.fileUtils import get_cur_dir, get_separator


def translate(name, source):
    return QtCore.QCoreApplication.translate(name, source)


class Translator():
    cur_dir = get_cur_dir()
    TRANSLATION_PATH = get_separator() + "translation" + get_separator() + "warframeAlert_"

    def __init__(self):
        self. app = QtCore.QCoreApplication.instance()
        self.translator = QtCore.QTranslator()
        translation_file = self.cur_dir + self.TRANSLATION_PATH + OptionsHandler.get_option("Language", str) + ".qm"
        self.translator.load(translation_file)
        self.app.installTranslator(self.translator)
