# coding=utf-8
from typing import List

from PyQt6 import QtGui, QtWidgets, QtCore

from warframeAlert.components.common.CalendarDayBox import CalendarDayBox
from warframeAlert.components.common.Countdown import Countdown
from warframeAlert.constants.warframeTypes import CalendarSeasonDayEvent
from warframeAlert.services.translationService import translate
from warframeAlert.utils import timeUtils
from warframeAlert.utils.commonUtils import remove_widget
from warframeAlert.utils.gameTranslationUtils import get_1999_season


class CalendarSeasonBox():

    def __init__(self) -> None:
        self.Font = QtGui.QFont()
        self.Font.setBold(True)

        self.SeasonEndTime = Countdown(translate("calendarSeasonBox", "end"))
        self.SeasonLabel = QtWidgets.QLabel("N/D")

        self.SeasonYear = QtWidgets.QLabel("N/D")
        self.SeasonVersion = QtWidgets.QLabel("N/D")
        self.SeasonRequirements = QtWidgets.QLabel("N/D")

        self.CalendarGrid = QtWidgets.QGridLayout()

        self.CalendarGrid.addWidget(self.SeasonEndTime.TimeLab, 0, 0)
        self.CalendarGrid.addWidget(self.SeasonLabel, 0, 1)
        self.CalendarGrid.addWidget(self.SeasonYear, 0, 2)
        self.CalendarGrid.addWidget(self.SeasonVersion, 0, 3)
        self.CalendarGrid.addWidget(self.SeasonRequirements, 1, 0, 1, 4)

        self.CalendarGrid.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

        self.CalendarDaysWidget = QtWidgets.QWidget()
        self.gridCalendarDays = QtWidgets.QGridLayout(self.CalendarDaysWidget)

        self.CalendarDaysScrollBar = QtWidgets.QScrollArea()
        self.CalendarDaysScrollBar.setWidgetResizable(True)

        self.CalendarDaysWidget.setLayout(self.gridCalendarDays)

        self.CalendarDaysScrollBar.setWidget(self.CalendarDaysWidget)

        self.daysTabber = QtWidgets.QTabWidget()

        self.daysTabber.insertTab(0, self.CalendarDaysScrollBar, translate("calendarSeasonBox", "days"))

        self.CalendarGrid.addWidget(self.daysTabber, 2, 0, 1, 4)

    def set_data(self, init: int, end: int, season: str,
                 year_iteration: int, version: int, requirements: List[str]) -> None:
        start = timeUtils.get_time(init)
        self.SeasonEndTime.set_tooltip(translate("calendarSeasonBox", "start") + ": " + start)
        self.SeasonEndTime.set_countdown(end)
        self.SeasonEndTime.start()
        season = get_1999_season(season)
        self.SeasonLabel.setText(translate("calendarSeasonBox", "season") + ": " + season)
        self.SeasonYear.setText(translate("calendarSeasonBox", "loop_number") + ": " + str(year_iteration))
        self.SeasonVersion.setText(translate("calendarSeasonBox", "version") + ": " + str(version))
        req = ""
        for requirement in requirements:
            req += requirement + ","
        self.SeasonRequirements.setText(translate("calendarSeasonBox", "requirements") + ": " + req[:-1])


    def calendar_not_available(self) -> None:
        self.SeasonLabel.setText(translate("calendarSeasonBox", "season") + ": N/D")
        self.SeasonYear.setText(translate("calendarSeasonBox", "loop_number") + ": N/D")
        self.SeasonVersion.setText(translate("calendarSeasonBox", "version") + ": N/D")
        self.SeasonRequirements.setText(translate("calendarSeasonBox", "requirements") + ": N/D")
        self.reset_calendar_days()

    def add_calendar_day(self, day_number: int, events: List[CalendarSeasonDayEvent]) -> None:
        day_box = CalendarDayBox(day_number)
        self.gridCalendarDays.addLayout(day_box.DayBox,
                                        self.gridCalendarDays.count(), 0)

        first_event = events[0]
        event_type = first_event["type"]
        day_box.create_base_event(event_type)

        # challenge or conversation to do, only 1 event
        challenge = first_event['challenge'] if ('challenge') in first_event else ""
        upgrade = first_event['upgrade'] if ('upgrade') in first_event else ""
        reward = first_event['reward'] if ('reward') in first_event else ""
        dialogue_name = first_event['dialogueName'] if ('dialogueName') in first_event else ""
        dialogue_convo = first_event['dialogueConvo'] if ('dialogueConvo') in first_event else ""
        day_box.add_first_event(challenge, upgrade, reward, dialogue_name, dialogue_convo)

        if (event_type == "CET_REWARD" or event_type == "CET_UPGRADE"):
            second_event = events[1]
            challenge = second_event['challenge'] if ('challenge') in second_event else ""
            upgrade = second_event['upgrade'] if ('upgrade') in second_event else ""
            reward = second_event['reward'] if ('reward') in second_event else ""
            dialogue_name = second_event['dialogueName'] if ('dialogueName') in second_event else ""
            dialogue_convo = second_event['dialogueConvo'] if ('dialogueConvo') in second_event else ""
            day_box.add_second_event(challenge, upgrade, reward, dialogue_name, dialogue_convo)

        if (event_type == "CET_UPGRADE"):
            third_event = events[2]
            challenge = third_event['challenge'] if ('challenge') in third_event else ""
            upgrade = third_event['upgrade'] if ('upgrade') in third_event else ""
            reward = third_event['reward'] if ('reward') in third_event else ""
            dialogue_name = third_event['dialogueName'] if ('dialogueName') in third_event else ""
            dialogue_convo = third_event['dialogueConvo'] if ('dialogueConvo') in third_event else ""
            day_box.add_third_event(challenge, upgrade, reward, dialogue_name, dialogue_convo)

        self.gridCalendarDays.addLayout(day_box.DayBox,
                                         self.gridCalendarDays.count(), 0)


    def reset_calendar_days(self) -> None:
        for i in range(0, self.gridCalendarDays.count()):
            remove_widget((self.gridCalendarDays.itemAt(i)).DayBox)
