# coding=utf-8
from PyQt6 import QtWidgets, QtCore

from warframeAlert.services.optionHandlerService import OptionsHandler
from warframeAlert.services.translationService import translate
from warframeAlert.utils.commonUtils import int_to_bool


class ConfigTabWidget():
    ConfigTabWidget = None

    def __init__(self) -> None:
        self.ConfigTabWidget = QtWidgets.QWidget()
        self.gridConfTab = QtWidgets.QGridLayout(self.ConfigTabWidget)

        self.TabConfigLabel = QtWidgets.QLabel(translate("configTabWidget", "activeTabs"), self.ConfigTabWidget)

        self.NewsConfig = QtWidgets.QCheckBox(translate("tabService", "news"))
        self.SeasonConfig = QtWidgets.QCheckBox(translate("tabService", "nightwave"))
        self.TAConfig = QtWidgets.QCheckBox(translate("tabService", "events"))
        self.AcolyteConfig = QtWidgets.QCheckBox(translate("tabService", "acolyte"))
        self.BountyConfig = QtWidgets.QCheckBox(translate("tabService", "bounty"))
        self.InvasionConfig = QtWidgets.QCheckBox(translate("tabService", "invasion"))
        self.SortieConfig = QtWidgets.QCheckBox(translate("tabService", "sortie"))
        self.SyndicateConfig = QtWidgets.QCheckBox(translate("tabService", "syndicate"))
        self.FissureConfig = QtWidgets.QCheckBox(translate("tabService", "fissure"))
        self.BaroConfif = QtWidgets.QCheckBox(translate("tabService", "baro"))
        self.SalesConfif = QtWidgets.QCheckBox(translate("tabService", "sales"))
        self.PVPConfig = QtWidgets.QCheckBox(translate("tabService", "pvp"))
        self.OtherConfig = QtWidgets.QCheckBox(translate("tabService", "other"))

        self.gridConfTab.addWidget(self.TabConfigLabel, 0, 0)
        self.gridConfTab.addWidget(self.NewsConfig, 1, 0)
        self.gridConfTab.addWidget(self.SeasonConfig, 1, 1)
        self.gridConfTab.addWidget(self.TAConfig, 2, 0)
        self.gridConfTab.addWidget(self.AcolyteConfig, 2, 1)
        self.gridConfTab.addWidget(self.BountyConfig, 3, 0)
        self.gridConfTab.addWidget(self.InvasionConfig, 3, 1)
        self.gridConfTab.addWidget(self.SortieConfig, 4, 0)
        self.gridConfTab.addWidget(self.SyndicateConfig, 4, 1)
        self.gridConfTab.addWidget(self.FissureConfig, 5, 0)
        self.gridConfTab.addWidget(self.BaroConfif, 5, 1)
        self.gridConfTab.addWidget(self.SalesConfif, 6, 0)
        self.gridConfTab.addWidget(self.PVPConfig, 6, 1)
        self.gridConfTab.addWidget(self.OtherConfig, 7, 0)

        self.ConfigTabWidget.setLayout(self.gridConfTab)
        self.gridConfTab.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

        self.NewsConfig.setChecked(int_to_bool(OptionsHandler.get_option("Tab/News")))
        self.SeasonConfig.setChecked(int_to_bool(OptionsHandler.get_option("Tab/Nightwave")))
        self.TAConfig.setChecked(int_to_bool(OptionsHandler.get_option("Tab/TactAll")))
        self.AcolyteConfig.setChecked(int_to_bool(OptionsHandler.get_option("Tab/Acolyte")))
        self.BountyConfig.setChecked(int_to_bool(OptionsHandler.get_option("Tab/Cetus")))
        self.InvasionConfig.setChecked(int_to_bool(OptionsHandler.get_option("Tab/Invasion")))
        self.SortieConfig.setChecked(int_to_bool(OptionsHandler.get_option("Tab/Sortie")))
        self.SyndicateConfig.setChecked(int_to_bool(OptionsHandler.get_option("Tab/Syndicate")))
        self.FissureConfig.setChecked(int_to_bool(OptionsHandler.get_option("Tab/Fissure")))
        self.BaroConfif.setChecked(int_to_bool(OptionsHandler.get_option("Tab/Baro")))
        self.SalesConfif.setChecked(int_to_bool(OptionsHandler.get_option("Tab/Market")))
        self.PVPConfig.setChecked(int_to_bool(OptionsHandler.get_option("Tab/PVP")))
        self.OtherConfig.setChecked(int_to_bool(OptionsHandler.get_option("Tab/Other")))

        self.NewsConfig.clicked.connect(
            lambda: OptionsHandler.update_config_tab("Tab/News", self.NewsConfig.isChecked()))
        self.SeasonConfig.clicked.connect(
            lambda: OptionsHandler.update_config_tab("Tab/Nightwave", self.SeasonConfig.isChecked()))
        self.TAConfig.clicked.connect(
            lambda: OptionsHandler.update_config_tab("Tab/TactAll", self.TAConfig.isChecked()))
        self.AcolyteConfig.clicked.connect(
            lambda: OptionsHandler.update_config_tab("Tab/Acolyte", self.AcolyteConfig.isChecked()))
        self.BountyConfig.clicked.connect(
            lambda: OptionsHandler.update_config_tab("Tab/Cetus", self.BountyConfig.isChecked()))
        self.InvasionConfig.clicked.connect(
            lambda: OptionsHandler.update_config_tab("Tab/Invasion", self.InvasionConfig.isChecked()))
        self.SortieConfig.clicked.connect(
            lambda: OptionsHandler.update_config_tab("Tab/Sortie", self.SortieConfig.isChecked()))
        self.SyndicateConfig.clicked.connect(
            lambda: OptionsHandler.update_config_tab("Tab/Syndicate", self.SyndicateConfig.isChecked()))
        self.FissureConfig.clicked.connect(
            lambda: OptionsHandler.update_config_tab("Tab/Fissure", self.FissureConfig.isChecked()))
        self.BaroConfif.clicked.connect(
            lambda: OptionsHandler.update_config_tab("Tab/Baro", self.BaroConfif.isChecked()))
        self.SalesConfif.clicked.connect(
            lambda: OptionsHandler.update_config_tab("Tab/Market", self.SalesConfif.isChecked()))
        self.PVPConfig.clicked.connect(
            lambda: OptionsHandler.update_config_tab("Tab/PVP", self.PVPConfig.isChecked()))
        self.OtherConfig.clicked.connect(
            lambda: OptionsHandler.update_config_tab("Tab/Other", self.OtherConfig.isChecked()))

    def get_widget(self) -> QtWidgets.QWidget:
        return self.ConfigTabWidget
