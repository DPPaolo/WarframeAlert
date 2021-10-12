# coding=utf-8
from PyQt6 import QtCore

from warframeAlert.services.optionHandlerService import OptionsHandler
from warframeAlert.utils.fileUtils import get_cur_dir, get_separator


def translate(name: str, source: str) -> str:
    return QtCore.QCoreApplication.translate(name, source)


class Translator():
    cur_dir: str = get_cur_dir()
    TRANSLATION_PATH: str = get_separator() + "translation" + get_separator() + "warframeAlert_"

    def __init__(self) -> None:
        self.app: QtCore.QCoreApplication = QtCore.QCoreApplication.instance()
        self.translator: QtCore.QTranslator() = QtCore.QTranslator()
        translation_file = self.cur_dir + self.TRANSLATION_PATH + OptionsHandler.get_option("Language", str) + ".qm"
        self.translator.load(translation_file)
        self.app.installTranslator(self.translator)
