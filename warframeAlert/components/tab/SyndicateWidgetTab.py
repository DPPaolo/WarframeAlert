# coding=utf-8
from PyQt5 import QtWidgets

from warframeAlert.components.common.Countdown import Countdown
from warframeAlert.components.common.SyndicateBox import SyndicateBox
from warframeAlert.constants.warframeTypes import SyndicateMissions
from warframeAlert.services.optionHandlerService import OptionsHandler
from warframeAlert.services.translationService import translate
from warframeAlert.utils import timeUtils
from warframeAlert.utils.commonUtils import print_traceback
from warframeAlert.utils.logUtils import LogHandler


class SyndicateWidgetTab():

    def __init__(self) -> None:
        self.alerts: dict[str, dict[str, SyndicateBox]] = {'SyndicateMissions': {}}
        self.alerts['SyndicateMissions']['ArbitersSyndicate']: SyndicateBox         # Arbiter of Hexis
        self.alerts['SyndicateMissions']['CephalonSudaSyndicate']: SyndicateBox     # Cephalon Suda
        self.alerts['SyndicateMissions']['NewLokaSyndicate']: SyndicateBox          # New Loka
        self.alerts['SyndicateMissions']['SteelMeridianSyndicate']: SyndicateBox    # Steel Meridian
        self.alerts['SyndicateMissions']['PerrinSyndicate']: SyndicateBox           # Perrin Sequence
        self.alerts['SyndicateMissions']['RedVeilSyndicate']: SyndicateBox          # Red Veil

        self.SyndicateWidget = QtWidgets.QWidget()

        self.SyndicateInitDesc = QtWidgets.QLabel(translate("syndicateWidget", "syndicateInit") + ": ")
        self.SyndicateEndDesc = QtWidgets.QLabel(translate("syndicateWidget", "syndicateEnd") + ": ")
        self.SyndicateInit = QtWidgets.QLabel("N/D")
        self.SyndicateEnd = Countdown()

        self.ArbiterWidget = QtWidgets.QWidget()
        self.CephalonWidget = QtWidgets.QWidget()
        self.NewLokaWidget = QtWidgets.QWidget()
        self.SteelMeridianWidget = QtWidgets.QWidget()
        self.PerrinWidget = QtWidgets.QWidget()
        self.RedVeilWidget = QtWidgets.QWidget()

        self.SyndicateTabber = QtWidgets.QTabWidget(self.SyndicateWidget)

        self.SyndicateTabber.insertTab(0, self.ArbiterWidget, translate("syndicateWidget", "arbiterSyndicate"))
        self.SyndicateTabber.insertTab(1, self.CephalonWidget, translate("syndicateWidget", "cephalonSyndicate"))
        self.SyndicateTabber.insertTab(2, self.NewLokaWidget, translate("syndicateWidget", "newLokaSyndicate"))
        self.SyndicateTabber.insertTab(3, self.SteelMeridianWidget, translate("syndicateWidget", "meridianSyndicate"))
        self.SyndicateTabber.insertTab(4, self.PerrinWidget, translate("syndicateWidget", "perrinSyndicate"))
        self.SyndicateTabber.insertTab(5, self.RedVeilWidget, translate("syndicateWidget", "redVeilSyndicate"))

        self.alerts['SyndicateMissions']['ArbitersSyndicate'] = SyndicateBox(self.ArbiterWidget)
        self.alerts['SyndicateMissions']['CephalonSudaSyndicate'] = SyndicateBox(self.CephalonWidget)
        self.alerts['SyndicateMissions']['NewLokaSyndicate'] = SyndicateBox(self.NewLokaWidget)
        self.alerts['SyndicateMissions']['SteelMeridianSyndicate'] = SyndicateBox(self.SteelMeridianWidget)
        self.alerts['SyndicateMissions']['PerrinSyndicate'] = SyndicateBox(self.PerrinWidget)
        self.alerts['SyndicateMissions']['RedVeilSyndicate'] = SyndicateBox(self.RedVeilWidget)

        self.gridSyndicate = QtWidgets.QGridLayout(self.SyndicateWidget)

        self.gridSyndicate.addWidget(self.SyndicateInitDesc, 0, 0)
        self.gridSyndicate.addWidget(self.SyndicateInit, 0, 1)
        self.gridSyndicate.addWidget(self.SyndicateEndDesc, 0, 2)
        self.gridSyndicate.addWidget(self.SyndicateEnd.TimeLab, 0, 3)
        self.gridSyndicate.addWidget(self.SyndicateTabber, 1, 0, 1, 4)

    def get_widget(self) -> QtWidgets.QWidget:
        return self.SyndicateWidget

    def set_time(self, init: int, end: int) -> None:
        self.SyndicateInit.setText(timeUtils.get_time(str(init)))
        self.SyndicateEnd.set_countdown(end)
        self.SyndicateEnd.start()

    def update_syndicate(self, data: SyndicateMissions) -> None:
        if (OptionsHandler.get_option("Tab/Syndicate") == 1):
            try:
                self.parse_syndicate(data)
            except Exception as er:
                LogHandler.err(translate("syndicateWidget", "syndicateError") + ": " + str(er))
                print_traceback(translate("syndicateWidget", "syndicateError") + ": " + str(er))
                self.syndicate_not_available()
        else:
            LogHandler.debug(translate("syndicateWidget", "noSyndicate"))
            self.syndicate_not_available()

    def parse_syndicate(self, data: SyndicateMissions) -> None:
        sydicates = ['ArbitersSyndicate', 'CephalonSudaSyndicate', 'NewLokaSyndicate',
                     'SteelMeridianSyndicate', 'PerrinSyndicate', 'RedVeilSyndicate']
        syndicate_updated = False

        for syn in data:
            syndicate_id = syn['_id']['$oid']
            init = syn['Activation']['$date']['$numberLong']
            end = syn['Expiry']['$date']['$numberLong']
            seed = syn['Seed']
            tag = syn['Tag']
            node = syn['Nodes']
            if (tag in sydicates):
                if (self.alerts['SyndicateMissions'][tag].get_syn_id() != syndicate_id):
                    self.alerts['SyndicateMissions'][tag].set_syndicate(tag, syndicate_id, seed)
                    self.alerts['SyndicateMissions'][tag].set_syndicate_mission(node)
                    if (not syndicate_updated):
                        self.set_time(init, end[:10])
                        syndicate_updated = True

    def syndicate_not_available(self) -> None:
        self.SyndicateInit.setText("N/D")
        for syn in self.alerts['SyndicateMissions']:
            self.alerts['SyndicateMissions'][syn].set_syndicate_not_available()
