# coding=utf-8
from PyQt6 import QtWidgets, QtCore

from warframeAlert.services.optionHandlerService import OptionsHandler
from warframeAlert.services.translationService import translate
from warframeAlert.utils.commonUtils import int_to_bool, bool_to_int

LANGUAGE_TYPE = {
    0: "it",
    1: "en"
}


class ConfigOtherWidget():
    ConfigOtherWidget = None

    def __init__(self) -> None:
        self.ConfigOtherWidget = QtWidgets.QWidget()

        self.gridOtherConfig = QtWidgets.QGridLayout(self.ConfigOtherWidget)

        self.ConfifOtherLabel = QtWidgets.QLabel(translate("configOtherWidget", "extraOptions"))
        self.DebugConfigLabel = QtWidgets.QLabel(translate("configOtherWidget", "debugOptions"))
        self.WarningConfigLabel = QtWidgets.QLabel(translate("configOtherWidget", "alertPt1") + "\n" +
                                                   translate("configOtherWidget", "alertPt2"))

        self.DebugConfig = QtWidgets.QCheckBox("Debug")
        self.InitConfig = QtWidgets.QCheckBox(translate("configOtherWidget", "firstInstallation"))
        self.TrayConfig = QtWidgets.QCheckBox(translate("configOtherWidget", "minimizeOnClose"))

        self.ComboBoxLangageLabel = QtWidgets.QLabel(translate("configOtherWidget", "language"))
        self.ComboBoxLangageLabel.setToolTip(translate("configOtherWidget", "languageTooltip"))

        self.ComboBoxLangage = QtWidgets.QComboBox(self.ConfigOtherWidget)

        self.ComboBoxLangage.addItem(translate("configOtherWidget", "it"))
        self.ComboBoxLangage.addItem(translate("configOtherWidget", "en"))

        self.ComboBoxLangage.setCurrentIndex(find_language_index())
        self.ComboBoxLangage.currentIndexChanged.connect(update_language_app)

        self.gridOtherConfig.addWidget(self.ConfifOtherLabel, 0, 0)
        self.gridOtherConfig.addWidget(self.WarningConfigLabel, 1, 0, 1, 2)
        self.gridOtherConfig.addWidget(self.DebugConfigLabel, 2, 0)
        self.gridOtherConfig.addWidget(self.DebugConfig, 3, 0)
        self.gridOtherConfig.addWidget(self.InitConfig, 3, 1)
        self.gridOtherConfig.addWidget(self.TrayConfig, 4, 0, 1, 2)
        self.gridOtherConfig.addWidget(self.ComboBoxLangageLabel, 5, 0)
        self.gridOtherConfig.addWidget(self.ComboBoxLangage, 6, 0)

        self.ConfigOtherWidget.setLayout(self.gridOtherConfig)
        self.gridOtherConfig.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

        self.DebugConfig.setChecked(int_to_bool(OptionsHandler.get_option("Debug")))
        self.InitConfig.setChecked(int_to_bool(OptionsHandler.get_option("FirstInit")))
        self.TrayConfig.setChecked(int_to_bool(OptionsHandler.get_option("TrayIcon")))

        self.DebugConfig.clicked.connect(
            lambda: OptionsHandler.set_option("Debug", bool_to_int(self.DebugConfig.isChecked())))
        self.InitConfig.clicked.connect(
            lambda: OptionsHandler.set_option("FirstInit", bool_to_int(self.InitConfig.isChecked())))
        self.TrayConfig.clicked.connect(
            lambda: OptionsHandler.set_option("TrayIcon", bool_to_int(self.TrayConfig.isChecked())))

    def get_widget(self) -> QtWidgets.QWidget:
        return self.ConfigOtherWidget


def find_language_index() -> int:
    language = OptionsHandler.get_option("Language", str)
    for language_type in LANGUAGE_TYPE:
        if (LANGUAGE_TYPE[language_type] == language):
            return language_type


def update_language_app(language_index: int) -> None:
    OptionsHandler.set_option("Language", LANGUAGE_TYPE[language_index])
