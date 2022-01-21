# coding=utf-8
from PyQt6 import QtWidgets, QtGui

from warframeAlert.components.widget.ConfigOtherWidget import ConfigOtherWidget
from warframeAlert.components.widget.ConfigTabWidget import ConfigTabWidget
from warframeAlert.components.widget.ConfigUpdateTabWidget import ConfigUpdateTabWidget
from warframeAlert.services.translationService import translate
from warframeAlert.utils.fileUtils import get_separator


class OptionsWidget():

    def __init__(self, option_service) -> None:
        self.ConfigWidget = QtWidgets.QWidget()

        warframe_icon = "assets" + get_separator() + "icon" + get_separator() + "Warframe.ico"
        self.ConfigWidget.setWindowIcon(QtGui.QIcon(warframe_icon))

        self.ConfigTabber = QtWidgets.QTabWidget(self.ConfigWidget)

        self.ConfigUpdateTab = ConfigUpdateTabWidget(option_service)
        self.ConfigTab = ConfigTabWidget(option_service)
        self.ConfigOtherTab = ConfigOtherWidget()

        self.ConfigTabber.insertTab(0, self.ConfigUpdateTab.get_widget(), translate("optionsWidget", "update"))
        self.ConfigTabber.insertTab(1, self.ConfigTab.get_widget(), translate("optionsWidget", "tab"))
        self.ConfigTabber.insertTab(2, self.ConfigOtherTab.get_widget(), translate("optionsWidget", "other"))

        self.gridConfig = QtWidgets.QGridLayout(self.ConfigWidget)
        self.gridConfig.addWidget(self.ConfigTabber, 0, 0)

        self.ConfigWidget.setLayout(self.gridConfig)

    def get_widget(self) -> QtWidgets.QWidget:
        return self.ConfigWidget

    def show(self) -> None:
        self.ConfigWidget.show()

    def hide(self) -> None:
        self.ConfigWidget.hide()
