# coding=utf-8
import os
import subprocess

from PyQt6 import QtWidgets, QtGui

from warframeAlert.components.common.MessageBox import MessageBox, MessageBoxType
from warframeAlert.constants.files import UPDATE_SITE
from warframeAlert.services.networkService import check_connection, retrieve_text_file, get_actual_version, \
    ProgressBarDownloader, Downloader
from warframeAlert.services.optionHandlerService import OptionsHandler
from warframeAlert.services.translationService import translate
from warframeAlert.utils import commonUtils
from warframeAlert.utils.fileUtils import get_separator, is_windows_os, get_cur_dir, is_linux_os, is_mac_os
from warframeAlert.utils.logUtils import LogHandler


class UpdateProgramWidget():
    UpdateWidget = None
    changelog_downloader = None
    downloader = None

    def __init__(self) -> None:
        self.UpdateWidget = QtWidgets.QWidget()
        warframe_icon = "assets" + get_separator() + "icon" + get_separator() + "Warframe.ico"
        self.UpdateWidget.setWindowIcon(QtGui.QIcon(warframe_icon))

        self.UpdateTitleLabel = QtWidgets.QLabel(translate("updateProgramWidget", "changelog") + ":")
        self.textEditUpdate = QtWidgets.QTextEdit(self.UpdateWidget)
        self.textEditUpdate.setReadOnly(True)
        self.textEditUpdate.setText(translate("updateProgramWidget", "loading") + "...")
        self.UpdatePButton = QtWidgets.QPushButton(translate("updateProgramWidget", "updateProgram"))
        self.UpdatePer = QtWidgets.QProgressBar()
        self.UpdatePer.hide()
        self.gridUpdate = QtWidgets.QGridLayout(self.UpdateWidget)

        self.gridUpdate.addWidget(self.UpdateTitleLabel, 0, 1)
        self.gridUpdate.addWidget(self.textEditUpdate, 1, 0, 1, 3)
        self.gridUpdate.addWidget(self.UpdatePButton, 2, 2)
        self.gridUpdate.addWidget(self.UpdatePer, 3, 0, 1, 3)

        self.UpdatePButton.clicked.connect(lambda: self.check_download_program())

        self.changelog_downloader = Downloader(UPDATE_SITE + "changelog.txt", "changelog.txt", 0)

        ver = retrieve_text_file("version.txt", get_actual_version())
        name = r"Warframe Alert " + str(ver) + ".exe"
        self.downloader = ProgressBarDownloader(UPDATE_SITE + "Warframe_Alert.exe", name)
        self.downloader.updated_value.connect(self.update_progress_bar)
        self.downloader.download_completed.connect(lambda: self.prepare_restart(str(ver), name))

        self.UpdateWidget.resize(380, 350)

    def get_widget(self) -> QtWidgets.QWidget:
        return self.UpdateWidget

    def show_widget(self) -> None:
        try:
            changelog = retrieve_text_file("changelog.txt")
            self.textEditUpdate.setText(changelog)
            self.textEditUpdate.moveCursor(QtGui.QTextCursor.MoveOperation.Start)
            self.textEditUpdate.ensureCursorVisible()
        except Exception as er:  # UnicodeDecodeError
            self.textEditUpdate.setText(translate("updateProgramWidget", "noChangelog"))
            LogHandler.err(translate("updateProgramWidget", "errorDownloadChangelog") + ": " + str(er))
            commonUtils.print_traceback(translate("updateProgramWidget", "errorDownloadChangelog") + ": " + str(er))

        self.changelog_downloader.start()
        self.UpdateWidget.show()

    def check_download_program(self) -> None:
        actual_version = get_actual_version()
        if (float(retrieve_text_file("version.txt", actual_version)) == float(actual_version)):
            MessageBox(translate("updateProgramWidget", "lastVersionTitle"),
                       translate("updateProgramWidget", "lastVersionDesc"), MessageBoxType.INFO)
        else:
            self.download_program()

    def download_program(self) -> None:
        if not check_connection():
            return
        self.UpdatePer.show()
        self.UpdatePButton.hide()
        try:
            self.UpdatePer.setProperty("value", 0.0)
            self.downloader.start()
        except Exception as er:
            MessageBox(translate("updateProgramWidget", "title"),
                       translate("updateProgramWidget", "versionDownloadError") + "\n" + str(er),
                       MessageBoxType.ERROR)
            commonUtils.print_traceback(translate("updateProgramService", "versionDownloadError") + "\n" + str(er))
            LogHandler.err(str(er))

    def update_progress_bar(self, value: float) -> None:
        self.UpdatePer.setProperty("value", value)

    def prepare_restart(self, ver: str, name: str) -> None:
        d = get_cur_dir()
        actual_version = get_actual_version()
        OptionsHandler.set_option("Version", int(ver.split(".")[0]))
        OptionsHandler.set_option("SubVersion", int(ver.split(".")[1]))
        self.UpdatePer.hide()
        pid = os.getpid()
        fp = open("PostUpdate.txt", "w")
        fp.write(str(pid) + "\n")
        fp.write(actual_version)
        fp.flush()
        fp.close()
        if (is_windows_os()):
            os.startfile(d + get_separator() + name, "open")
        elif (is_linux_os()):
            subprocess.call(["xdg-open", d + get_separator() + name])
        elif (is_mac_os()):
            subprocess.call(["open", d + get_separator() + name])
