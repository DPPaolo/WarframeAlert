# coding=utf-8
import ssl
import time
import urllib.request
from urllib.error import URLError

from PyQt5 import QtCore
from PyQt5.QtCore import QThread

from warframeAlert.constants.files import UPDATE_SITE
from warframeAlert.services.optionHandlerService import OptionsHandler
from warframeAlert.services.translationService import translate
from warframeAlert.utils.fileUtils import create_default_folder
from warframeAlert.utils.logUtils import LogHandler

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context


def download(url: str, path: str) -> None:
    create_default_folder()
    urllib.request.urlretrieve(url, path)


def check_connection() -> bool:
    try:
        urllib.request.urlopen("https://www.google.com")
        return True
    except URLError:
        return False


class Downloader(QThread):
    download_completed = QtCore.pyqtSignal()

    def __init__(self, url: str, path: str, time_to_sleep: int = 10) -> None:
        QThread.__init__(self)
        self.url: str = url
        self.path: str = path
        self.time_to_sleep: int = time_to_sleep

    def run(self) -> None:
        downloaded = False
        while (not downloaded):
            if (not check_connection()):
                time.sleep(300)
                continue
            try:
                download(self.url, self.path)
                if (self.time_to_sleep > 0):
                    time.sleep(int(self.time_to_sleep))
                self.download_completed.emit()
                downloaded = True
            except URLError as url_error:
                if (UPDATE_SITE in self.url or OptionsHandler.get_option("Debug") == 1):
                    print(translate("networkService", "connectionError") + ": " + self.url + "\n")
                LogHandler.err(translate("networkService", "connectionError") + ": " + self.url + "\n" + str(url_error))
                time.sleep(600)
            except ValueError:
                pass
            except Exception as ex:
                LogHandler.err(translate("networkService", "connectionError") + ": " + self.url + "\n" + str(ex))
