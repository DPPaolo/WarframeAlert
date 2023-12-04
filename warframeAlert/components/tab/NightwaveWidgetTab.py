# coding=utf-8
from PyQt6 import QtWidgets, QtCore

from warframeAlert.components.common.Countdown import Countdown
from warframeAlert.components.common.SeasonBox import SeasonBox
from warframeAlert.constants.warframeTypes import SeasonInfo
from warframeAlert.services.notificationService import NotificationService
from warframeAlert.services.optionHandlerService import OptionsHandler
from warframeAlert.services.translationService import translate
from warframeAlert.utils import commonUtils, timeUtils
from warframeAlert.utils.commonUtils import remove_widget
from warframeAlert.utils.gameTranslationUtils import get_syndicate, get_nightwave_challenge
from warframeAlert.utils.logUtils import LogHandler


class NightwaveWidgetTab():

    def __init__(self) -> None:
        self.alerts = {'SeasonInfo': []}

        self.nightwaveWidget = QtWidgets.QWidget()
        self.ChallengeWidget = QtWidgets.QWidget()

        self.SeasonEnd = Countdown(" " + translate("nightwaveWidgetTab", "end") + " ")
        self.SeasonEnd.set_alignment(QtCore.Qt.AlignmentFlag.AlignRight)

        self.SeasonData = QtWidgets.QLabel("??? " +
                                           translate("nightwaveWidgetTab", "season") +
                                           " N/D " +
                                           translate("nightwaveWidgetTab", "phase") +
                                           " N/D")
        self.SeasonParam = QtWidgets.QLabel("")
        self.SeasonSpace = QtWidgets.QLabel(" ")
        self.SeasonData.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        self.SeasonParam.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)

        self.NoSeason = QtWidgets.QLabel(translate("nightwaveWidgetTab", "noNightwave"))
        self.NoSeason.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.NightwaveGrid = QtWidgets.QGridLayout(self.ChallengeWidget)
        self.NightwaveGrid.addWidget(self.NoSeason, 0, 0)
        self.NightwaveGrid.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

        self.SeasonScrollBar = QtWidgets.QScrollArea()
        self.SeasonScrollBar.setWidgetResizable(True)
        self.SeasonScrollBar.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.SeasonScrollBar.setWidget(self.ChallengeWidget)

        self.SeasonTabber = QtWidgets.QTabWidget()
        self.SeasonTabber.insertTab(1, self.SeasonScrollBar, translate("nightwaveWidgetTab", "missionAvailable"))

        self.SeasonGrid = QtWidgets.QGridLayout(self.nightwaveWidget)

        self.SeasonGrid.addWidget(self.SeasonData, 0, 0)
        self.SeasonGrid.addWidget(self.SeasonParam, 0, 1)
        self.SeasonGrid.addWidget(self.SeasonSpace, 0, 2)
        self.SeasonGrid.addWidget(self.SeasonEnd.TimeLab, 0, 3)
        self.SeasonGrid.addWidget(self.SeasonTabber, 1, 0, 1, 4)
        self.SeasonGrid.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

        self.nightwaveWidget.setLayout(self.SeasonGrid)

    def get_widget(self) -> QtWidgets.QWidget:
        return self.nightwaveWidget

    def update_nightwave_season(self, data: SeasonInfo) -> None:
        if (OptionsHandler.get_option("Tab/Nightwave") == 1):
            try:
                self.parse_nightwave(data)
            except Exception as er:
                LogHandler.err(translate("nightwaveWidgetTab", "nightwaveParsingError") + ": " + str(er))
                commonUtils.print_traceback(translate("nightwaveWidgetTab", "nightwaveParsingError") + ": " + str(er))
                self.reset_season()
                return
        else:
            self.reset_season()

    def parse_nightwave(self, data: SeasonInfo) -> None:
        self.reset_season()

        if (data):
            n_nightwave = len(self.alerts['SeasonInfo'])

            init = timeUtils.get_time(data['Activation']['$date']['$numberLong'])
            end = data['Expiry']['$date']['$numberLong']

            syn = get_syndicate(data['AffiliationTag'])
            season = data['Season']
            phase = data['Phase']
            param = data['Params']

            self.update_nightwave_data(init, end, syn, season, phase, param)

            for challenge in data['ActiveChallenges']:
                challenge_id = challenge['_id']['$oid']
                trovato = 0
                for mission in self.alerts['SeasonInfo']:
                    if (mission.get_challenge_id() == challenge_id):
                        trovato = 1

                if (trovato == 0):
                    init = challenge['Activation']['$date']['$numberLong']
                    end = challenge['Expiry']['$date']['$numberLong']
                    permanent = challenge['Permanent'] if ('Permanent' in challenge) else False

                    nightwave_challenge = get_nightwave_challenge(challenge['Challenge'])
                    if ('Daily' in challenge):
                        daily = challenge['Daily']
                    else:
                        daily = False

                    temp = SeasonBox(challenge_id)
                    temp.set_data(init, end, nightwave_challenge, daily, permanent)
                    self.alerts['SeasonInfo'].append(temp)

                    del temp

            self.add_nightwave(n_nightwave)
        else:
            self.season_not_available()

    def update_nightwave_data(self, init: str, end: int, syn: str, season: int, phase: int, param: str) -> None:
        self.SeasonEnd.set_countdown(end[:10])
        self.SeasonEnd.start()
        self.SeasonData.setToolTip(translate("nightwaveWidgetTab", "init") + " " + init)
        self.SeasonData.setText(syn + "\t\t" + translate("nightwaveWidgetTab", "season") + " " + str(int(season) + 1)
                                + " " + translate("nightwaveWidgetTab", "phase") + " " + str(int(phase) + 1))
        if (param != ""):
            self.SeasonParam.setText(translate("nightwaveWidgetTab", "parameters") + " " + str(param))

    def add_nightwave(self, n_nightwave: int) -> None:
        if (len(self.alerts['SeasonInfo']) > 0):
            self.NoSeason.hide()
        n = n_nightwave
        for i in range(n_nightwave, len(self.alerts['SeasonInfo'])):
            if (not self.alerts['SeasonInfo'][i].is_expired()):
                self.NightwaveGrid.addLayout(self.alerts['SeasonInfo'][i].SeasonBox, int(n / 2), n % 2)
                n += 1
                NotificationService.send_notification(
                    self.alerts['SeasonInfo'][i].get_title(),
                    self.alerts['SeasonInfo'][i].to_string(),
                    None)

    def reset_season(self) -> None:
        self.NoSeason.show()
        cancelled = []
        for i in range(0, len(self.alerts['SeasonInfo'])):
            if (self.alerts['SeasonInfo'][i].is_expired()):
                cancelled.append(i)
        i = len(cancelled)
        while i > 0:
            self.alerts['SeasonInfo'][cancelled[i - 1]].hide()
            remove_widget(self.alerts['SeasonInfo'][cancelled[i - 1]].SeasonBox)
            del self.alerts['SeasonInfo'][cancelled[i - 1]]
            i -= 1

    def season_not_available(self) -> None:
        self.SeasonEnd.set_countdown(-1)
        self.SeasonEnd.hide()
        self.SeasonData.setText(translate("nightwaveWidgetTab", "noSeasonActive"))
        self.SeasonParam.setText("")
