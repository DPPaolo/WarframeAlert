# coding=utf-8
import ssl
import time
import urllib.request
from urllib.error import URLError

from PyQt5 import QtCore
from PyQt5.QtCore import QThread

from warframeAlert import warframeData
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


def download(url, path):
    create_default_folder()
    urllib.request.urlretrieve(url, path)


def check_connection():
    try:
        urllib.request.urlopen("https://www.google.com")
        return True
    except URLError:
        return False


class Downloader(QThread):
    download_completed = QtCore.pyqtSignal()

    def __init__(self, url, path):
        QThread.__init__(self)
        self.url = url
        self.path = path

    def run(self):
        downloaded = False
        while(not downloaded):
            if (not check_connection()):
                time.sleep(300)
                continue
            try:
                download(self.url, self.path)
                time.sleep(10)
                self.download_completed.emit()
                downloaded = True
            except URLError as url_error:
                if (warframeData.UPDATE_SITE in self.url):
                    print(translate("networkService", "connectionError") + ": " + self.url)
                LogHandler.err(translate("networkService", "connectionError") + ": " + self.url + "\n" + str(url_error))
                time.sleep(600)
            except ValueError:
                pass
