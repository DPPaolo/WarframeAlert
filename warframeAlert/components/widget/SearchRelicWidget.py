# coding=utf-8
from PyQt6 import QtWidgets, QtCore

from warframeAlert.components.common.RelicBox import RelicBox
from warframeAlert.services.translationService import translate
from warframeAlert.utils.warframeUtils import get_relic_tier_from_name, add_all_relic_from_file, \
    add_all_relic_item_from_file, get_relic_drop, get_relic_drop_from_name


class SearchRelicWidget():

    def __init__(self) -> None:
        self.SearchRelicWidget = QtWidgets.QWidget()

        self.SearchRelicLab = QtWidgets.QLabel(translate("searchRelicWidget", "searchRelic"))
        self.SearchRelicLab.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        self.RelicDrops = QtWidgets.QTextEdit(self.SearchRelicWidget)
        self.RelicDrops.setReadOnly(True)
        self.SearchRelicByItemLab = QtWidgets.QLabel(translate("searchRelicWidget", "searchByItem"))
        self.SearchRelicByItemLab.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        self.ItemsRelicText = QtWidgets.QTextEdit(self.SearchRelicWidget)
        self.ItemsRelicText.setReadOnly(True)
        self.RelicBox = RelicBox(1)
        self.RelicBox.hide_button()

        self.RelicComboBox = QtWidgets.QComboBox(self.SearchRelicWidget)
        self.ItemComboBox = QtWidgets.QComboBox(self.SearchRelicWidget)

        add_all_relic_from_file(self.RelicComboBox)
        add_all_relic_item_from_file(self.ItemComboBox)

        self.gridSearchRelic = QtWidgets.QGridLayout(self.SearchRelicWidget)

        self.gridSearchRelic.addWidget(self.SearchRelicLab, 0, 0)
        self.gridSearchRelic.addWidget(self.RelicComboBox, 0, 1)
        self.gridSearchRelic.addLayout(self.RelicBox.RelicBox, 0, 2, 2, 1)
        self.gridSearchRelic.addWidget(self.RelicDrops, 1, 0, 1, 2)
        self.gridSearchRelic.addWidget(self.SearchRelicByItemLab, 2, 0)
        self.gridSearchRelic.addWidget(self.ItemComboBox, 2, 1)
        self.gridSearchRelic.addWidget(self.ItemsRelicText, 3, 0, 1, 3)

        self.RelicComboBox.currentIndexChanged[int].connect(self.search_by_relic)
        self.ItemComboBox.currentIndexChanged[int].connect(self.search_by_item)

        self.SearchRelicWidget.setLayout(self.gridSearchRelic)

    def get_widget(self) -> QtWidgets.QWidget:
        return self.SearchRelicWidget

    def show(self) -> None:
        self.SearchRelicWidget.show()

    def hide(self) -> None:
        self.SearchRelicWidget.hide()

    def search_by_relic(self) -> None:
        name = self.RelicComboBox.currentText()
        drop = get_relic_drop(name)
        self.RelicDrops.setText(drop)
        tier = get_relic_tier_from_name(name)
        self.RelicBox.set_relic_tier(tier)
        self.RelicBox.set_relic_name(name)

    def search_by_item(self) -> None:
        name = self.ItemComboBox.currentText()
        drop = get_relic_drop_from_name(name)
        self.ItemsRelicText.setText(drop)
