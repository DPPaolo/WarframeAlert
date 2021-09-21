# coding=utf-8
import os
import ssl
import subprocess
import time
import urllib.request
from urllib.error import URLError

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QThread

from warframeAlert.constants.files import UPDATE_SITE
from warframeAlert.services.optionHandlerService import OptionsHandler
from warframeAlert.services.translationService import translate
from warframeAlert.utils import commonUtils
from warframeAlert.utils.fileUtils import create_default_folder, get_separator
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


def get_actual_version() -> str:
    major_version = OptionsHandler.get_option("Version")
    minor_version = OptionsHandler.get_option("SubVersion")
    return str(major_version) + "." + str(minor_version)


def retrieve_version() -> str:
    ver = "0.0"
    if not check_connection():
        return ver
    try:
        download(UPDATE_SITE + "version.txt", "data" + get_separator() + "version.txt")
    except Exception as er:
        LogHandler.err(translate("networkService", "versionCheckError") + " " + str(er))
        print(translate("networkService", "versionCheckError") + " " + str(er))
        commonUtils.print_traceback(translate("networkService", "versionCheckError"))
        return ver
    fp = open("data" + get_separator() + "version.txt", "r")
    for line in fp.readlines():
        ver = line.replace("\n", "")
    fp.close()
    os.remove('data' + get_separator() + 'version.txt')
    return ver


def update_program() -> None:
    fp = open("PostUpdate.txt", "r")
    line = fp.readlines()
    pid = str(line[0]).replace("\n", "")
    ver = str(line[1]).replace("\n", "")
    fp.close()
    name = r'Warframe Alert ' + ver + ".exe"
    try:
        subprocess.call("taskkill /PID " + pid)
        time.sleep(2)
        os.remove(name)
    except Exception as er:
        LogHandler.err(translate("updateProgramService", "newVersionError") + ":\n" + str(er))
    os.remove("PostUpdate.txt")


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


class ProgressBarDownloader(QThread):
    download_completed = QtCore.pyqtSignal()

    def __init__(self, progress_bar: QtWidgets.QProgressBar, url: str, path: str) -> None:
        QThread.__init__(self)
        self.progressBar = progress_bar
        self.url: str = url
        self.path: str = path

    def run(self) -> None:
        fp = open(self.path, "wb")
        response = urllib.request.urlopen(self.url)
        downloaded = 0
        self.progressBar.setProperty("value", 0.0)
        try:
            size = int(response.info()['Content-Length'])
            while True:
                chunk = response.read(2048)
                if (not chunk):
                    break
                downloaded += len(chunk)
                fp.write(chunk)
                per = (float(downloaded) / size) * 100
                self.progressBar.setProperty("value", per)
        except Exception as er:
            print(str(er))
            commonUtils.print_traceback(str(er))
        self.download_completed.emit()
