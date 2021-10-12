# coding=utf-8
import os

from PyQt6 import QtWidgets, QtGui

from warframeAlert.components.common.MessageBox import MessageBox, MessageBoxType
from warframeAlert.constants.files import UPDATE_SITE
from warframeAlert.services.networkService import check_connection, retrieve_version, get_actual_version, \
    ProgressBarDownloader, Downloader
from warframeAlert.services.optionHandlerService import OptionsHandler
from warframeAlert.services.translationService import translate
from warframeAlert.utils import commonUtils
from warframeAlert.utils.fileUtils import get_separator, is_window_os, get_cur_dir
from warframeAlert.utils.logUtils import LogHandler


class UpdateProgramWidget():
    UpdateWidget = None

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
        try:
            if (is_window_os()):
                downloader = Downloader(UPDATE_SITE + "changelog.txt", "changelog_temp.txt")
                downloader.start()
                downloader.download_completed.connect(lambda: self.update_changelog_screen())
        except Exception as er:  # UnicodeDecodeError
            LogHandler.err(translate("updateProgramWidget", "errorDownloadChangelog") + ": " + str(er))
            commonUtils.print_traceback(translate("updateProgramWidget", "errorDownloadChangelog") + ": " + str(er))
        self.textEditUpdate.ensureCursorVisible()
        self.gridAupdate = QtWidgets.QGridLayout(self.UpdateWidget)

        self.gridAupdate.addWidget(self.UpdateTitleLabel, 0, 1)
        self.gridAupdate.addWidget(self.textEditUpdate, 1, 0, 1, 3)
        self.gridAupdate.addWidget(self.UpdatePButton, 2, 2)
        self.gridAupdate.addWidget(self.UpdatePer, 3, 0, 1, 3)

        self.UpdatePButton.clicked.connect(lambda: self.check_download_program())

        self.UpdateWidget.resize(380, 350)

    def get_widget(self) -> QtWidgets.QWidget:
        return self.UpdateWidget

    def update_changelog_screen(self) -> None:
        try:
            fp2 = open("changelog_temp.txt", "r")
            out = open("../changelog.txt", "w")
            for line in fp2.readlines():
                out.write(line)
            out.flush()
            out.close()
            fp2.close()
            os.remove("changelog_temp.txt")
            fp = open("../changelog.txt", "r")
            self.textEditUpdate.setText("")
            for line in fp.readlines():
                line = line.replace("\n", "")
                self.textEditUpdate.append(line)
            fp.close()
            self.textEditUpdate.moveCursor(QtGui.QTextCursor.Start)
        except Exception as er:
            self.textEditUpdate.setText(translate("updateProgramWidget", "noChangelog"))
            LogHandler.err(translate("updateProgramWidget", "noChangelog") + ": " + str(er))
            commonUtils.print_traceback(translate("updateProgramWidget", "cantReadChangelog") + ": " + str(er))

    def check_download_program(self) -> None:
        if (retrieve_version() == get_actual_version()):
            MessageBox(translate("updateProgramWidget", "lastVersionTitle"),
                       translate("updateProgramWidget", "lastVersionDesc"), MessageBoxType.INFO)
        else:
            self.download_program()

    def download_program(self) -> None:
        if not check_connection():
            return
        self.UpdatePer.show()
        self.UpdatePButton.hide()
        ver = retrieve_version()
        name = r"Warframe Alert " + str(ver) + ".exe"
        try:
            downloader = ProgressBarDownloader(self.UpdatePer, UPDATE_SITE + "Warframe_Alert.exe", name)
            downloader.start()
            downloader.download_completed.connect(lambda: self.prepare_restart(ver, name))
        except Exception as er:
            MessageBox(translate("updateProgramWidget", "title"),
                       translate("updateProgramWidget", "versionDownloadError") + "\n" + str(er),
                       MessageBoxType.ERROR)
            commonUtils.print_traceback(translate("updateProgramService", "versionDownloadError") + "\n" + str(er))
            LogHandler.err(str(er))

    def prepare_restart(self, ver: str, name: str) -> None:
        d = get_cur_dir()
        ver_at = get_actual_version()
        OptionsHandler.set_option("Version", int(ver.split(".")[0]))
        OptionsHandler.set_option("SubVersion", int(ver.split(".")[1]))
        self.UpdatePer.hide()
        pid = os.getpid()
        fp = open("PostUpdate.txt", "w")
        fp.write(str(pid) + "\n")
        fp.write(ver_at)
        fp.flush()
        fp.close()
        os.startfile(d + get_separator() + name, "open")
