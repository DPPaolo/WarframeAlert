# coding=utf-8

from PyQt6 import QtWidgets, QtGui

from warframeAlert.utils.commonUtils import get_last_item_with_backslash
from warframeAlert.utils.gameTranslationUtils import get_1999_day_event_type, get_1999_day_todo, get_1999_day_upgrade, \
    get_1999_day_birthday


class CalendarDayBox():

    def __init__(self, day: int) -> None:
        self.day = day

        self.DayLabel = QtWidgets.QLabel("N/D")
        self.EventName = QtWidgets.QLabel("N/D")

        self.Font = QtGui.QFont()
        self.Font.setBold(True)
        self.EventName.setFont(self.Font)

        self.EventReward1 = QtWidgets.QLabel("N/D")
        self.EventChallenge1 = QtWidgets.QLabel("N/D")
        self.EventUpgrade1 = QtWidgets.QLabel("N/D")
        self.EventConversation1 = QtWidgets.QLabel("N/D")
        self.EventDialog1 = QtWidgets.QLabel("N/D")

        self.EventReward2 = QtWidgets.QLabel("N/D")
        self.EventChallenge2 = QtWidgets.QLabel("N/D")
        self.EventUpgrade2 = QtWidgets.QLabel("N/D")
        self.EventConversation2 = QtWidgets.QLabel("N/D")
        self.EventDialog2 = QtWidgets.QLabel("N/D")

        self.EventReward3 = QtWidgets.QLabel("N/D")
        self.EventChallenge3 = QtWidgets.QLabel("N/D")
        self.EventUpgrade3 = QtWidgets.QLabel("N/D")
        self.EventConversation3 = QtWidgets.QLabel("N/D")
        self.EventDialog3 = QtWidgets.QLabel("N/D")

        self.DayBox = QtWidgets.QHBoxLayout()

        self.DayEventBox = QtWidgets.QVBoxLayout()

        self.EventBox1 = QtWidgets.QHBoxLayout()
        self.EventBox2 = QtWidgets.QHBoxLayout()
        self.EventBox3 = QtWidgets.QHBoxLayout()

        self.EventBox1.addWidget(self.EventReward1)
        self.EventBox1.addWidget(self.EventChallenge1)
        self.EventBox1.addWidget(self.EventUpgrade1)
        self.EventBox1.addWidget(self.EventConversation1)
        self.EventBox1.addWidget(self.EventDialog1)

        self.EventBox2.addWidget(self.EventReward2)
        self.EventBox2.addWidget(self.EventChallenge2)
        self.EventBox2.addWidget(self.EventUpgrade2)
        self.EventBox2.addWidget(self.EventConversation2)
        self.EventBox2.addWidget(self.EventDialog2)

        self.EventBox3.addWidget(self.EventReward3)
        self.EventBox3.addWidget(self.EventChallenge3)
        self.EventBox3.addWidget(self.EventUpgrade3)
        self.EventBox3.addWidget(self.EventConversation3)
        self.EventBox3.addWidget(self.EventDialog3)

        self.DayEventBox.addLayout(self.EventBox1)
        self.DayEventBox.addLayout(self.EventBox2)
        self.DayEventBox.addLayout(self.EventBox3)

        self.DayBox.addWidget(self.DayLabel)
        self.DayBox.addWidget(self.EventName)
        self.DayBox.addLayout(self.DayEventBox)

    def create_base_event(self, event_type: str) -> None:

        self.DayLabel.setText(str(self.day))
        self.EventName.setText(get_1999_day_event_type(event_type))
        self.hide_events()

    def add_first_event(self, challenge: str, upgrade: str,
                        reward: str, dialogue_name: str, dialogue: str) -> None:
        self.EventChallenge1.setText(get_1999_day_todo(challenge) if challenge != "" else challenge)
        self.EventReward1.setText(get_last_item_with_backslash(reward))
        self.EventUpgrade1.setText(get_1999_day_upgrade(upgrade) if upgrade != "" else upgrade)
        self.EventDialog1.setText(get_last_item_with_backslash(dialogue_name))
        self.EventConversation1.setText(get_1999_day_birthday(dialogue) if dialogue != "" else dialogue)
        self.show_first_event()

    def add_second_event(self, challenge: str, upgrade: str,
                         reward: str, dialogue_name: str, dialogue: str) -> None:
        self.EventChallenge2.setText(get_1999_day_todo(challenge) if challenge != "" else challenge)
        self.EventReward2.setText(get_last_item_with_backslash(reward))
        self.EventUpgrade2.setText(get_1999_day_upgrade(upgrade) if upgrade != "" else upgrade)
        self.EventDialog2.setText(get_last_item_with_backslash(dialogue_name))
        self.EventConversation2.setText(get_1999_day_birthday(dialogue) if dialogue != "" else dialogue)
        self.show_second_event()

    def add_third_event(self, challenge: str, upgrade: str,
                        reward: str, dialogue_name: str, dialogue: str) -> None:
        self.EventChallenge3.setText(get_1999_day_todo(challenge) if challenge != "" else challenge)
        self.EventReward3.setText(get_last_item_with_backslash(reward))
        self.EventUpgrade3.setText(get_1999_day_upgrade(upgrade) if upgrade != "" else upgrade)
        self.EventDialog3.setText(get_last_item_with_backslash(dialogue_name))
        self.EventConversation3.setText(get_1999_day_birthday(dialogue) if dialogue != "" else dialogue)
        self.show_third_event()

    def show_first_event(self):
        self.EventReward1.show()
        self.EventChallenge1.show()
        self.EventUpgrade1.show()
        self.EventConversation1.show()
        self.EventDialog1.show()

    def show_second_event(self):
        self.EventReward2.show()
        self.EventChallenge2.show()
        self.EventUpgrade2.show()
        self.EventConversation2.show()
        self.EventDialog2.show()

    def show_third_event(self):
        self.EventReward3.show()
        self.EventChallenge3.show()
        self.EventUpgrade3.show()
        self.EventConversation3.show()
        self.EventDialog3.show()

    def hide_events(self):
        self.EventReward1.hide()
        self.EventChallenge1.hide()
        self.EventUpgrade1.hide()
        self.EventConversation1.hide()
        self.EventDialog1.hide()
        self.EventReward2.hide()
        self.EventChallenge2.hide()
        self.EventUpgrade2.hide()
        self.EventConversation2.hide()
        self.EventDialog2.hide()
        self.EventReward3.hide()
        self.EventChallenge3.hide()
        self.EventUpgrade3.hide()
        self.EventConversation3.hide()
        self.EventDialog3.hide()

