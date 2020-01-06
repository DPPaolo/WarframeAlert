from PyQt5 import QtCore

from warframeAlert.services.optionHandlerService import OptionsHandler
from warframeAlert.utils.commonUtils import get_cur_dir


def translate(name, source):
    return QtCore.QCoreApplication.translate(name, source, None, -1)


class Translator():
    cur_dir = get_cur_dir()
    TRANSLATION_PATH = "/translation/warframeAlert_"

    def __init__(self, app):
        self.translator = QtCore.QTranslator()
        self.translator.load(self.cur_dir + self.TRANSLATION_PATH + OptionsHandler.get_option("Language", str) + ".qm")
        app.installTranslator(self.translator)


