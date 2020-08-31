# coding=utf-8
from PyQt5 import QtWidgets, QtCore

from warframeAlert.components.common.Countdown import Countdown
from warframeAlert.components.widget.BountyWidget import BountyWidget
from warframeAlert.services.optionHandlerService import OptionsHandler
from warframeAlert.services.translationService import translate
from warframeAlert.utils import timeUtils
from warframeAlert.utils.commonUtils import print_traceback
from warframeAlert.utils.logUtils import LogHandler


class BountyWidgetTab():
    def __init__(self):
        self.BountiesWidget = QtWidgets.QWidget()
        self.BountiesGrid = QtWidgets.QGridLayout(self.BountiesWidget)

        self.OstronWidget = BountyWidget()
        self.FortunaWidget = BountyWidget()
        self.DeimosWidget = BountyWidget()

        self.BountiesTabber = QtWidgets.QTabWidget(self.BountiesWidget)

        self.CetusInit = QtWidgets.QLabel("N/D")
        self.CetusEnd = Countdown(translate("bountyWidgetTab", "bountyEnd") + " ")
        self.CetusTime = Countdown()
        self.FortunaTime = Countdown()
        self.DeimosTime = Countdown()

        self.BountiesGrid.addWidget(self.CetusInit, 0, 0)
        self.BountiesGrid.addWidget(self.CetusEnd.TimeLab, 0, 1)
        self.BountiesGrid.addWidget(self.CetusTime.TimeLab, 1, 0)
        self.BountiesGrid.addWidget(self.FortunaTime.TimeLab, 1, 1)
        self.BountiesGrid.addWidget(self.DeimosTime.TimeLab, 1, 2)
        self.BountiesGrid.addWidget(self.BountiesTabber, 2, 0, 1, 3)

        self.BountiesTabber.insertTab(0, self.OstronWidget.get_widget(), translate("bountyWidgetTab", "ostron"))
        self.BountiesTabber.insertTab(1, self.FortunaWidget.get_widget(), translate("bountyWidgetTab", "fortuna"))
        self.BountiesTabber.insertTab(2, self.DeimosWidget.get_widget(), translate("bountyWidgetTab", "hiveMind"))

        self.BountiesGrid.setAlignment(QtCore.Qt.AlignTop)

        self.BountiesWidget.setLayout(self.BountiesGrid)

        self.CetusTimeFin = int(timeUtils.get_local_time()) + 3600

        self.CetusTime.TimeOut.connect(self.set_cetus_time)
        self.FortunaTime.TimeOut.connect(self.set_fortuna_time)
        self.DeimosTime.TimeOut.connect(self.set_deimos_time)

    def get_widget(self):
        return self.BountiesWidget

    def update_bounties(self, data):
        if (OptionsHandler.get_option("Tab/Cetus") == 1):
            try:
                for syndicate in data:
                    tag = syndicate['Tag']
                    if (tag == 'CetusSyndicate'):
                        self.OstronWidget.parse_bounty(syndicate)
                        bounty_init, bounty_end = self.OstronWidget.get_timer()
                        self.set_time(bounty_init, bounty_end)
                    elif (tag == 'SolarisSyndicate'):
                        self.FortunaWidget.parse_bounty(syndicate)
                    elif (tag == 'EntratiSyndicate'):
                        self.DeimosWidget.parse_bounty(syndicate, True)
                    else:
                        if ('Jobs' in syndicate):
                            LogHandler.debug(translate("bountyWidgetTab", "newSynJobs") + " " + tag)
                            print(syndicate['Jobs'])
            except Exception as er:
                LogHandler.err(translate("bountyWidgetTab", "bountiesError") + ": " + str(er))
                print_traceback(translate("bountyWidgetTab", "bountiesError") + ": " + str(er))
                self.bounty_not_available()
        else:
            LogHandler.debug(
                translate("bountyWidgetTab", "newSynJobs"))
            self.bounty_not_available()

    def set_time(self, init, end):
        self.CetusInit.setText(
            translate("bountyWidgetTab", "bountyInit") + ": " + timeUtils.get_time(init))
        self.CetusEnd.set_countdown(end)
        self.CetusEnd.start()
        self.CetusTimeFin = end
        self.set_cetus_time()
        self.set_fortuna_time()
        self.set_deimos_time()

    def set_cetus_time(self):
        cetus_time, day = timeUtils.get_cetus_time(int(self.CetusTimeFin))
        if (day):
            self.CetusTime.set_name(translate("bountyWidgetTab", "cetusDay") + " ")
        else:
            self.CetusTime.set_name(translate("bountyWidgetTab", "cetusNight") + " ")

        self.CetusTime.set_countdown(int(timeUtils.get_local_time()) + cetus_time)
        self.CetusTime.start()

    def set_fortuna_time(self):
        fortuna_time, warm = timeUtils.get_fortuna_time()
        if (warm):
            self.FortunaTime.set_name(translate("bountyWidgetTab", "fortunaHot") + " ")
        else:
            self.FortunaTime.set_name(translate("bountyWidgetTab", "fortunaCold") + " ")

        self.FortunaTime.set_countdown(int(timeUtils.get_local_time()) + fortuna_time)
        self.FortunaTime.start()

    # same time of cetus
    def set_deimos_time(self):
        deimos_time, fass = timeUtils.get_cetus_time(int(self.CetusTimeFin))
        if (fass):
            self.DeimosTime.set_name(translate("bountyWidgetTab", "deimosFass") + " ")
        else:
            self.DeimosTime.set_name(translate("bountyWidgetTab", "deimosVome") + " ")

        self.DeimosTime.set_countdown(int(timeUtils.get_local_time()) + deimos_time)
        self.DeimosTime.start()

    def bounty_not_available(self):
        self.OstronWidget.reset_bounty()
        self.FortunaWidget.reset_bounty()
        self.CetusInit.setText(translate("bountyWidgetTab", "bountyInit") + " : N/D")
