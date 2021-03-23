# coding=utf-8
from itertools import groupby

from PyQt5 import QtWidgets, QtCore, QtGui

from warframeAlert.components.common.RelicBox import RelicBox
from warframeAlert.components.widget.SearchRelicWidget import SearchRelicWidget
from warframeAlert.services.translationService import translate
from warframeAlert.utils.fileUtils import get_separator
from warframeAlert.utils.warframeUtils import get_relic_tier_from_name, get_all_relic_from_file, \
    get_relic_rarity_from_percent


class RelicWidget():
    AllerteWidget = None

    def __init__(self):
        self.RelicWidget = QtWidgets.QWidget()

        self.RelicWidget.setWindowTitle(translate("relicWidget", "relicWidgetTitle"))
        self.RelicWidget.setWindowIcon(QtGui.QIcon("images" + get_separator() + "Warframe.ico"))

        self.LithWidget = QtWidgets.QWidget()
        self.MesoWidget = QtWidgets.QWidget()
        self.NeoWidget = QtWidgets.QWidget()
        self.AxiWidget = QtWidgets.QWidget()
        self.RequiemWidget = QtWidgets.QWidget()

        self.RelicTabber = QtWidgets.QTabWidget(self.RelicWidget)

        self.gridLith = QtWidgets.QGridLayout(self.LithWidget)
        self.gridMeso = QtWidgets.QGridLayout(self.MesoWidget)
        self.gridNeo = QtWidgets.QGridLayout(self.NeoWidget)
        self.gridAxi = QtWidgets.QGridLayout(self.AxiWidget)
        self.gridRequiem = QtWidgets.QGridLayout(self.RequiemWidget)

        self.RelScrollBar1 = QtWidgets.QScrollArea()
        self.RelScrollBar2 = QtWidgets.QScrollArea()
        self.RelScrollBar3 = QtWidgets.QScrollArea()
        self.RelScrollBar4 = QtWidgets.QScrollArea()
        self.RelScrollBar5 = QtWidgets.QScrollArea()

        self.RelScrollBar1.setWidgetResizable(True)
        self.RelScrollBar2.setWidgetResizable(True)
        self.RelScrollBar3.setWidgetResizable(True)
        self.RelScrollBar4.setWidgetResizable(True)
        self.RelScrollBar5.setWidgetResizable(True)

        self.RelScrollBar1.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.RelScrollBar2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.RelScrollBar3.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.RelScrollBar4.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.RelScrollBar5.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.LithWidget.setLayout(self.gridLith)
        self.MesoWidget.setLayout(self.gridMeso)
        self.NeoWidget.setLayout(self.gridNeo)
        self.AxiWidget.setLayout(self.gridAxi)
        self.RequiemWidget.setLayout(self.gridRequiem)

        self.RelScrollBar1.setWidget(self.LithWidget)
        self.RelScrollBar2.setWidget(self.MesoWidget)
        self.RelScrollBar3.setWidget(self.NeoWidget)
        self.RelScrollBar4.setWidget(self.AxiWidget)
        self.RelScrollBar5.setWidget(self.RequiemWidget)

        self.RelicTabber.insertTab(1, self.RelScrollBar1, translate("relicWidget", "relicLith"))
        self.RelicTabber.insertTab(2, self.RelScrollBar2, translate("relicWidget", "relicMeso"))
        self.RelicTabber.insertTab(3, self.RelScrollBar3, translate("relicWidget", "relicNeo"))
        self.RelicTabber.insertTab(4, self.RelScrollBar4, translate("relicWidget", "relicAxi"))
        self.RelicTabber.insertTab(5, self.RelScrollBar5, translate("relicWidget", "relicRequiem"))

        self.SearchRelic = SearchRelicWidget()
        self.RelicTabber.insertTab(6, self.SearchRelic.get_widget(), translate("relicWidget", "searchRelics"))

        self.RelicWidget.resize(650, 450)

        self.gridRelic = QtWidgets.QGridLayout(self.RelicWidget)
        self.gridRelic.addWidget(self.RelicTabber, 0, 0)

        self.update_relic_widgets()

    def get_widget(self):
        return self.RelicWidget

    def show(self):
        self.RelicWidget.show()

    def hide(self):
        self.RelicWidget.hide()

    def update_relic_widgets(self):
        all_relics = get_all_relic_from_file()
        for relic_tier_name, relics in groupby(all_relics, key=lambda x: x['tier']):
            for relic in relics:
                if (relic["state"] == "Intact"):
                    tier = get_relic_tier_from_name(relic['tier'])
                    rewards = []
                    for reward in relic["rewards"]:
                        reward_name = reward["itemName"]
                        rarity = get_relic_rarity_from_percent(reward['chance'], "Intact")
                        data = (reward_name, rarity)
                        rewards.append(data)

                    temp = RelicBox(tier)
                    temp.set_relic_data(relic["tier"] + " " + relic["relicName"], rewards)
                    if (tier == 1):
                        grid_count = self.gridLith.count()
                        self.gridLith.addLayout(temp.RelicBox, int(grid_count / 2), grid_count % 2)
                    elif (tier == 2):
                        grid_count = self.gridMeso.count()
                        self.gridMeso.addLayout(temp.RelicBox, int(grid_count / 2), grid_count % 2)
                    elif (tier == 3):
                        grid_count = self.gridNeo.count()
                        self.gridNeo.addLayout(temp.RelicBox, int(grid_count / 2), grid_count % 2)
                    elif (tier == 4):
                        grid_count = self.gridAxi.count()
                        self.gridAxi.addLayout(temp.RelicBox, int(grid_count / 2), grid_count % 2)
                    elif (tier == 5):
                        grid_count = self.gridRequiem.count()
                        self.gridRequiem.addLayout(temp.RelicBox, int(grid_count / 2), grid_count % 2)
                    del temp
