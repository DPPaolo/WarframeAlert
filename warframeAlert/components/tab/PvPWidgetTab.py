# coding=utf-8
from PyQt6 import QtWidgets, QtCore

from warframeAlert.components.common.Countdown import Countdown
from warframeAlert.components.common.PvPMissionBox import PvPMissionBox
from warframeAlert.components.widget.PvPAlternativeWidget import PvPAlternativeWidget
from warframeAlert.components.widget.PvPTournamentWidget import PvPTournamentWidget
from warframeAlert.constants.warframeTypes import PVPChallengeInstances, PVPActiveTournaments, PVPAlternativeModes
from warframeAlert.services.optionHandlerService import OptionsHandler
from warframeAlert.services.translationService import translate
from warframeAlert.utils import commonUtils, timeUtils
from warframeAlert.utils.commonUtils import remove_widget, get_last_item_with_backslash
from warframeAlert.utils.gameTranslationUtils import get_pvp_mission_type, get_pvp_mission_name, get_pvp_desc
from warframeAlert.utils.logUtils import LogHandler


class PvPWidgetTab():

    def __init__(self) -> None:
        self.PvPWidget = QtWidgets.QWidget()

        self.alerts = {'PvPMission': {}}
        self.alerts['PvPMission']['Daily'] = []
        self.alerts['PvPMission']['Weekly'] = []

        self.DayPvPWidget = QtWidgets.QWidget()
        self.WeekPvPWidget = QtWidgets.QWidget()
        self.OtherPvPWidget = PvPAlternativeWidget()
        self.TournamentWidget = PvPTournamentWidget()

        self.PvPWeekInit = QtWidgets.QLabel(translate("pvpWidgetTab", "start") + " N/D")
        self.PvPWeekFin = Countdown(translate("pvpWidgetTab", "end"))
        self.PvPDayInit = QtWidgets.QLabel(translate("pvpWidgetTab", "start") + " N/D")
        self.PvPDayFin = Countdown(translate("pvpWidgetTab", "end"))

        self.PvPTabber = QtWidgets.QTabWidget(self.PvPWidget)

        self.gridDayPvP = QtWidgets.QGridLayout(self.DayPvPWidget)
        self.gridWeekPvP = QtWidgets.QGridLayout(self.WeekPvPWidget)

        self.gridWeekPvP.addWidget(self.PvPWeekInit, 0, 0)
        self.gridWeekPvP.addWidget(self.PvPWeekFin.TimeLab, 0, 1)
        self.gridDayPvP.addWidget(self.PvPDayInit, 0, 0)
        self.gridDayPvP.addWidget(self.PvPDayFin.TimeLab, 0, 1)

        self.gridWeekPvP.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.gridDayPvP.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

        self.PvPTabber.insertTab(0, self.DayPvPWidget, translate("pvpWidgetTab", "dailyMission"))
        self.PvPTabber.insertTab(1, self.WeekPvPWidget, translate("pvpWidgetTab", "weeklyMission"))
        self.PvPTabber.insertTab(2, self.OtherPvPWidget.get_widget(), translate("pvpWidgetTab", "alternativeMission"))
        self.PvPTabber.insertTab(3, self.TournamentWidget.get_widget(), translate("pvpWidgetTab", "tournamentMission"))

        grid_pvp = QtWidgets.QGridLayout(self.PvPWidget)
        grid_pvp.addWidget(self.PvPTabber, 0, 0)
        grid_pvp.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.PvPWidget.setLayout(grid_pvp)

    def get_widget(self) -> QtWidgets.QWidget:
        return self.PvPWidget

    def update_tab(self) -> None:
        self.PvPTabber.insertTab(2, self.OtherPvPWidget.get_widget(), translate("pvpWidgetTab", "alternativeMission"))
        self.PvPTabber.insertTab(3, self.TournamentWidget.get_widget(), translate("pvpWidgetTab", "tournamentMission"))

        if (not (self.OtherPvPWidget.get_length() > 0)):
            self.PvPTabber.removeTab(self.PvPTabber.indexOf(self.OtherPvPWidget.get_widget()))
        if (not (self.TournamentWidget.get_length() > 0)):
            self.PvPTabber.removeTab(self.PvPTabber.indexOf(self.TournamentWidget.get_widget()))

    def update_pvp_mission(self, data: PVPChallengeInstances) -> None:
        if (OptionsHandler.get_option("Tab/PVP") == 1):
            try:
                self.parse_pvp_mission(data)
            except Exception as er:
                LogHandler.err(translate("pvpWidgetTab", "pvpMissionUpdateError") + ": " + str(er))
                commonUtils.print_traceback(translate("pvpWidgetTab", "pvpMissionUpdateError") + ": " + str(er))
                self.pvp_mission_not_available()
                return
        else:
            self.reset_pvp_mission()

    def update_pvp_alternative_mission(self, data: PVPAlternativeModes) -> None:
        if (OptionsHandler.get_option("Tab/PVP") == 1):
            try:
                self.OtherPvPWidget.parse_pvp_alternative_mission(data)
            except Exception as er:
                LogHandler.err(translate("pvpWidgetTab", "pvpAlternativeUpdateError") + ": " + str(er))
                commonUtils.print_traceback(translate("pvpWidgetTab", "pvpAlternativeUpdateError") + ": " + str(er))
                self.OtherPvPWidget.pvp_alternative_mission_not_available()
                return
        else:
            self.OtherPvPWidget.pvp_alternative_mission_not_available()

    def update_pvp_tournament(self, data: PVPActiveTournaments) -> None:
        if (OptionsHandler.get_option("Tab/PVP") == 1):
            try:
                self.TournamentWidget.parse_pvp_tournament(data)
            except Exception as er:
                LogHandler.err(translate("pvpWidgetTab", "pvpTournamentUpdateError") + ": " + str(er))
                commonUtils.print_traceback(translate("pvpWidgetTab", "pvpTournamentUpdateError") + ": " + str(er))
                self.TournamentWidget.pvp_tournament_not_available()
                return
        else:
            self.TournamentWidget.pvp_tournament_not_available()

    def pvp_mission_not_available(self) -> None:
        self.reset_pvp_mission()
        self.PvPWeekInit.setText(translate("pvpWidgetTab", "start") + " N/D")
        self.PvPWeekFin.set_countdown(-1)
        self.PvPWeekFin.start()
        self.PvPDayInit.setText(translate("pvpWidgetTab", "start") + " N/D")
        self.PvPDayFin.set_countdown(-1)
        self.PvPDayFin.start()

    def set_pvp_day_time(self, init: int, end: int) -> None:
        self.PvPDayInit.setText(translate("pvpWidgetTab", "start") + " " + timeUtils.get_time(init))
        self.PvPDayFin.set_countdown(end)
        self.PvPDayFin.start()

    def set_pvp_week_time(self, init: int, end: int) -> None:
        self.PvPWeekInit.setText(translate("pvpWidgetTab", "start") + " " + timeUtils.get_time(init))
        self.PvPWeekFin.set_countdown(end)
        self.PvPWeekFin.start()

    def parse_pvp_mission(self, data: PVPChallengeInstances) -> None:
        self.reset_pvp_mission()
        n_pvp_d = len(self.alerts['PvPMission']['Daily'])
        n_pvp_w = len(self.alerts['PvPMission']['Weekly'])
        week_timer_set = daily_timer_set = False
        for pvp in data:
            difficulty = -1
            pvp_id = pvp['_id']['$oid']
            init = pvp['startDate']['$date']['$numberLong']
            end = pvp['endDate']['$date']['$numberLong']

            category = get_pvp_mission_type(pvp['Category'])

            is_none_challenge = get_pvp_mission_type("PVPChallengeTypeCategory_WEEKLY_ROOT") == category
            is_daily_challenge = get_pvp_mission_type("PVPChallengeTypeCategory_DAILY") == category
            is_weekly_challenge = get_pvp_mission_type("PVPChallengeTypeCategory_WEEKLY") == category

            if (not is_none_challenge):

                time = int(end[:10]) - int(timeUtils.get_local_time())
                if (time > 0):

                    if (not week_timer_set and is_weekly_challenge):
                        self.set_pvp_week_time(init, end[:10])
                        week_timer_set = True
                    elif (not daily_timer_set and is_daily_challenge):
                        self.set_pvp_day_time(init, end[:10])
                        daily_timer_set = True

                    found = 0

                    if (is_daily_challenge):
                        for mission in self.alerts['PvPMission']['Daily']:
                            if (mission.get_pvp_id() == pvp_id):
                                found = 1
                    elif (is_weekly_challenge):
                        for mission in self.alerts['PvPMission']['Weekly']:
                            if (mission.get_pvp_id() == pvp_id):
                                found = 1

                    if (found == 0):
                        generated = pvp['isGenerated']
                        challenge = get_last_item_with_backslash(pvp['challengeTypeRefID'])
                        if ("EASY" in challenge):
                            difficulty = 0
                            challenge = challenge[:-4]
                        elif ("MEDIUM" in challenge):
                            difficulty = 1
                            challenge = challenge[:-6]
                        elif ("HARD" in challenge):
                            difficulty = 2
                            challenge = challenge[:-4]
                        name = get_pvp_mission_name(challenge, pvp['challengeTypeRefID'])
                        mission = get_pvp_mission_type(pvp['PVPMode'])
                        param = pvp['params'][0]
                        desc = get_pvp_desc(challenge, str(param['v']))
                        sub_challenge = pvp['subChallenges']

                        temp = PvPMissionBox(pvp_id, generated)
                        temp.set_pvp_data(name, desc, mission, difficulty, end, sub_challenge)

                        if (is_daily_challenge):
                            self.alerts['PvPMission']['Daily'].append(temp)
                        elif (is_weekly_challenge):
                            self.alerts['PvPMission']['Weekly'].append(temp)
                        del temp

        self.add_pvp_mission(n_pvp_d, n_pvp_w)

    def add_pvp_mission(self, n_pvp_d: int, n_pvp_w: int) -> None:
        for i in range(n_pvp_d, len(self.alerts['PvPMission']['Daily'])):
            if (not self.alerts['PvPMission']['Daily'][i].is_expired()):
                self.gridDayPvP.addLayout(self.alerts['PvPMission']['Daily'][i].PvPMissionBox, self.gridDayPvP.count(),
                                          0)
        for i in range(n_pvp_w, len(self.alerts['PvPMission']['Weekly'])):
            if (not self.alerts['PvPMission']['Weekly'][i].is_expired()):
                self.gridWeekPvP.addLayout(self.alerts['PvPMission']['Weekly'][i].PvPMissionBox,
                                           self.gridWeekPvP.count(), 0)

        if (len(self.alerts['PvPMission']['Daily']) == 0):
            self.pvp_mission_not_available()

    def reset_pvp_mission(self) -> None:
        cancelled = []
        for i in range(0, len(self.alerts['PvPMission']['Daily'])):
            if (self.alerts['PvPMission']['Daily'][i].is_expired()):
                cancelled.append(i)
        i = len(cancelled)
        while i > 0:
            self.alerts['PvPMission']['Daily'][cancelled[i - 1]].hide()
            remove_widget(self.alerts['PvPMission']['Daily'][cancelled[i - 1]].PvPMissionBox)
            del self.alerts['PvPMission']['Daily'][cancelled[i - 1]]
            i -= 1
        cancelled = []
        for i in range(0, len(self.alerts['PvPMission']['Weekly'])):
            if (self.alerts['PvPMission']['Weekly'][i].is_expired()):
                cancelled.append(i)
        i = len(cancelled)
        while i > 0:
            self.alerts['PvPMission']['Weekly'][cancelled[i - 1]].hide()
            remove_widget(self.alerts['PvPMission']['Weekly'][cancelled[i - 1]].PvPMissionBox)
            del self.alerts['PvPMission']['Weekly'][cancelled[i - 1]]
            i -= 1
