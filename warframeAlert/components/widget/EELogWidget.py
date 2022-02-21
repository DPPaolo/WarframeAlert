# coding=utf-8
import os
import subprocess

from PyQt6 import QtWidgets, QtGui

from warframeAlert.components.common.MessageBox import MessageBox, MessageBoxType
from warframeAlert.services.translationService import translate
from warframeAlert.utils import commonUtils
from warframeAlert.utils.fileUtils import get_separator, is_windows_os, is_linux_os, is_mac_os
from warframeAlert.utils.logUtils import LogHandler


class EELogWidget():
    EELogViewWidget = None

    def __init__(self) -> None:
        self.EELogViewWidget = QtWidgets.QWidget()
        warframe_icon = "assets" + get_separator() + "icon" + get_separator() + "Warframe.ico"
        self.EELogViewWidget.setWindowIcon(QtGui.QIcon(warframe_icon))
        self.EELogViewWidget.setWindowTitle(translate("eelogWidget", "title"))

        self.gridEE = QtWidgets.QGridLayout(self.EELogViewWidget)

        self.selPath = QtWidgets.QPushButton(translate("eelogWidget", "browse"))
        self.openEE = QtWidgets.QPushButton(translate("eelogWidget", "openFile"))

        self.PathLabel = QtWidgets.QLabel(translate("eelogWidget", "pathDesc") + ': ', self.EELogViewWidget)

        self.textEditEE = QtWidgets.QTextEdit(self.EELogViewWidget)
        self.textEditEE.setReadOnly(True)
        self.textEditEE2 = QtWidgets.QTextEdit(self.EELogViewWidget)
        self.textEditEE2.setMaximumHeight(self.PathLabel.sizeHint().height() * 2)
        self.textEditEE2.setMaximumWidth(self.PathLabel.sizeHint().width() * 6)
        self.textEditEE2.setReadOnly(True)
        default_path = get_separator() + "Warframe" + get_separator() + "EE.log"
        if (is_windows_os):
            self.textEditEE2.setText(os.getenv('LOCALAPPDATA') + default_path)

        self.radio1 = QtWidgets.QRadioButton(translate("eelogWidget", "all"), self.EELogViewWidget)
        self.radio2 = QtWidgets.QRadioButton("Error/Warning", self.EELogViewWidget)
        self.radio3 = QtWidgets.QRadioButton("Info", self.EELogViewWidget)
        self.radio4 = QtWidgets.QRadioButton("Diag", self.EELogViewWidget)

        self.radio1.clicked.connect(self.update_view_eelog)
        self.radio2.clicked.connect(self.update_view_eelog)
        self.radio3.clicked.connect(self.update_view_eelog)
        self.radio4.clicked.connect(self.update_view_eelog)
        self.selPath.clicked.connect(self.select_eelog)
        self.openEE.clicked.connect(self.open_eelog)

        self.gridEE.addWidget(self.radio1, 0, 0)
        self.gridEE.addWidget(self.radio2, 0, 1)
        self.gridEE.addWidget(self.radio3, 0, 2)
        self.gridEE.addWidget(self.radio4, 0, 3)
        self.gridEE.addWidget(self.openEE, 0, 4)
        self.gridEE.addWidget(self.textEditEE, 1, 0, 1, 5)
        self.gridEE.addWidget(self.PathLabel, 2, 0)
        self.gridEE.addWidget(self.textEditEE2, 2, 1, 1, 3)
        self.gridEE.addWidget(self.selPath, 2, 4)

        self.EELogViewWidget.setLayout(self.gridEE)

        self.EELogViewWidget.resize(550, 300)

    def get_widget(self) -> QtWidgets.QWidget:
        return self.EELogViewWidget

    def update_view_eelog(self) -> None:
        if (self.radio1.isChecked()):
            choice = 0
        elif (self.radio2.isChecked()):
            choice = 1
        elif (self.radio3.isChecked()):
            choice = 2
        elif (self.radio4.isChecked()):
            choice = 3
        else:
            choice = 0
        path = self.textEditEE2.toPlainText()
        self.view_eelog(path, choice)

    def select_eelog(self) -> None:
        path = self.textEditEE2.toPlainText()
        if (path == ""):
            path = "C:\\"
        file_selected = QtWidgets.QFileDialog.getOpenFileName(caption=translate("eelogWidget", "selectFile"),
                                                              directory=path, filter="Log (*.log)")
        if (file_selected[0]):
            self.textEditEE2.setText(file_selected[0])
            self.update_view_eelog()

    def open_eelog(self) -> None:
        path = self.textEditEE2.toPlainText()
        path = path[0:-6]
        if (path == ""):
            path = "C:\\"
        os.startfile(path, "open")
        if (is_windows_os()):
            os.startfile(path, "open")
        elif (is_linux_os()):
            subprocess.call(["xdg-open", path])
        elif (is_mac_os()):
            subprocess.call(["open", path])

    def view_eelog(self, path: str, choice: int) -> None:
        self.textEditEE.clear()
        try:
            fp = open(path, "r", encoding='utf-8')
        except Exception as er:
            MessageBox(translate("eelogWidget", "errorTitle"),
                       translate("eelogWidget", "errorFileNotFound") + ".\n" +
                       translate("eelogWidget", "errorCheckPath"), MessageBoxType.ERROR)
            LogHandler.err(translate("eelogWidget", "errorFileNotFound") + ": " + str(er))
            return
        for line in fp.readlines():
            try:
                line = line.replace("\n", "")
                match choice:
                    case 1:
                        if ("[Error]" in line or "[Warning]" in line):
                            self.textEditEE.append(line)
                    case 2:
                        if ("[Info]" in line):
                            self.textEditEE.append(line)
                    case 3:
                        if ("[Diag]" in line):
                            self.textEditEE.append(line)
                    case _:
                        self.textEditEE.append(line)

            except Exception as err:
                MessageBox(translate("eelogWidget", "errorTitleReadError"),
                           translate("eelogWidget", "errorReadErrorLine") + "\n" + line + " "
                           + translate("eelogWidget", "errorLineDesc") + ":\n" + str(err),
                           MessageBoxType.ERROR)
                commonUtils.print_traceback(translate("eelogWidget", "errorReadErrorLine") + " " + line
                                            + " " + translate("eelogWidget", "errorLineDesc") + "\n" + str(err))
                return
        self.textEditEE.moveCursor(QtGui.QTextCursor.MoveOperation.Start)
        self.textEditEE.ensureCursorVisible()
        fp.close()
