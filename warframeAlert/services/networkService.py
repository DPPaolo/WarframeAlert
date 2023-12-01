# coding=utf-8
import os
import ssl
import subprocess
import time
import urllib.request
from urllib.error import URLError

import requests
from PyQt6 import QtCore

from warframeAlert.constants.files import UPDATE_SITE
from warframeAlert.services.optionHandlerService import OptionsHandler
from warframeAlert.services.translationService import translate
from warframeAlert.utils import commonUtils
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


def get_actual_version() -> str:
    major_version = OptionsHandler.get_option("Version")
    minor_version = OptionsHandler.get_option("SubVersion")
    return str(major_version) + "." + str(minor_version)


def retrieve_text_file(file_name: str, default_value: str = "") -> str:
    text = default_value
    if not check_connection():
        return text
    else:
        response = requests.get(UPDATE_SITE + file_name)
        if (response.status_code == 200):
            response.encoding = "windows-1252"
            text = response.text
    return text


def clean_update_program() -> None:
    fp = open("PostUpdate.txt")
    line = fp.readlines()
    pid = str(line[0]).replace("\n", "")
    ver = str(line[1]).replace("\n", "")
    fp.close()
    os.remove("PostUpdate.txt")
    name = r'Warframe Alert ' + ver + ".exe"
    try:
        subprocess.call("taskkill /f /PID " + pid)
        time.sleep(2)
        os.remove(name)
    except Exception as er:
        LogHandler.err(translate("updateProgramService", "newVersionError") + ":\n" + str(er))


class Downloader(QtCore.QThread):
    download_completed = QtCore.pyqtSignal()

    def __init__(self, url: str, path: str, time_to_sleep: int = 10) -> None:
        QtCore.QThread.__init__(self)
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


class ProgressBarDownloader(QtCore.QThread):
    download_completed = QtCore.pyqtSignal()
    updated_value = QtCore.pyqtSignal(float)

    def __init__(self, url: str, path: str) -> None:
        QtCore.QThread.__init__(self)
        self.url: str = url
        self.path: str = path

    def run(self) -> None:
        fp = open(self.path, "wb")
        response = urllib.request.urlopen(self.url)
        downloaded = 0
        try:
            size = int(response.info()['Content-Length'])
            while True:
                chunk = response.read(2048)
                if (not chunk):
                    break
                downloaded += len(chunk)
                fp.write(chunk)
                per = (float(downloaded) / size) * 100
                self.updated_value.emit(per)
        except Exception as er:
            print(str(er))
            commonUtils.print_traceback(str(er))
        self.download_completed.emit()
