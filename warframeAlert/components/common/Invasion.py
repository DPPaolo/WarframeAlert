# coding=utf-8
from typing import List

from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt

from warframeAlert.components.common.CommonImages import CommonImages
from warframeAlert.components.common.EmptySpace import EmptySpace
from warframeAlert.services.translationService import translate
from warframeAlert.utils.commonUtils import get_last_item_with_backslash
from warframeAlert.utils.fileUtils import get_separator
from warframeAlert.utils.timeUtils import get_date_time
from warframeAlert.utils.warframeUtils import get_weapon_part, get_weapon_type, get_image_path_from_name


class Invasion():

    def __init__(self, invasion_id: str, chain_id: str) -> None:
        self.completed: bool = False
        self.image = None
        self.invasion_id = invasion_id
        self.invasion_chain_id = chain_id
        self.InvDesc = QtWidgets.QLabel("N/D")
        self.InvStart = QtWidgets.QLabel("N/D")
        self.InvNode = QtWidgets.QLabel("N/D")
        self.InvAttacker = QtWidgets.QLabel("N/D")
        self.InvDefender = QtWidgets.QLabel("N/D")
        self.InvRewardAtt = QtWidgets.QLabel("")
        self.InvRewardDef = QtWidgets.QLabel("")
        self.InvSpace = QtWidgets.QLabel("")
        self.InvVS = QtWidgets.QLabel("VS")
        self.InvAttackerImg = CommonImages()
        self.InvDefenderImg = CommonImages()
        self.InvPer = QtWidgets.QProgressBar()

        self.InvasionBox1 = QtWidgets.QHBoxLayout()
        self.InvasionBox2 = QtWidgets.QHBoxLayout()
        self.InvasionBox3 = QtWidgets.QHBoxLayout()
        self.InvasionBox4 = QtWidgets.QVBoxLayout()
        self.InvasionBox5 = QtWidgets.QHBoxLayout()
        self.InvasionBox6 = QtWidgets.QHBoxLayout()

        self.InvasionBox = QtWidgets.QVBoxLayout()

        self.InvasionBox1.addWidget(self.InvDesc)
        self.InvasionBox1.addStretch(1)
        self.InvasionBox1.addWidget(self.InvStart)
        self.InvasionBox1.addStretch(1)
        self.InvasionBox1.addWidget(self.InvNode)

        self.InvasionBox2.addWidget(self.InvAttacker)
        self.InvasionBox2.addStretch(1)
        self.InvasionBox2.addWidget(self.InvVS)
        self.InvasionBox2.addStretch(1)
        self.InvasionBox2.addWidget(self.InvDefender)

        self.InvasionBox3.addWidget(self.InvRewardAtt)
        self.InvasionBox3.addStretch(1)
        self.InvasionBox3.addWidget(self.InvSpace)
        self.InvasionBox3.addStretch(1)
        self.InvasionBox3.addWidget(self.InvRewardDef)

        self.InvasionBox4.addLayout(self.InvasionBox1)
        self.InvasionBox4.addLayout(self.InvasionBox2)
        self.InvasionBox4.addLayout(self.InvasionBox3)

        self.InvasionBox5.addWidget(self.InvAttackerImg.image)
        self.InvasionBox5.addLayout(self.InvasionBox4)
        self.InvasionBox5.addWidget(self.InvDefenderImg.image)

        self.InvasionBox6.addWidget(self.InvPer)

        self.InvasionBox.addLayout(self.InvasionBox5)
        self.InvasionBox.addLayout(self.InvasionBox6)
        self.InvasionBox.addLayout(EmptySpace().SpaceBox)

    def set_completed(self, completed: bool) -> None:
        self.completed = completed

    def is_completed(self) -> bool:
        return self.completed

    def get_invasion_id(self) -> str:
        return self.invasion_id

    def get_title(self) -> str:
        return self.InvDesc.text() + " " + self.InvNode.text()

    def to_string(self) -> str:
        name = self.InvAttacker.text() + " vs " + self.InvDefender.text() + "\n"
        if (self.InvAttacker.text() == "Infested"):
            reward = self.InvRewardDef.text()
        else:
            reward = self.InvRewardAtt.text() + " vs " + self.InvRewardDef.text()

        return name + reward

    def get_image(self) -> str:
        return self.image

    def set_invasion_data(self, mission: str, node: str, attacker_faction: str, defender_faction: str) -> None:
        self.InvNode.setText(mission + " " + node)
        self.InvAttacker.setText(defender_faction)
        self.InvDefender.setText(attacker_faction)
        self.InvAttacker.setStyleSheet(get_invasion_color(defender_faction))
        self.InvDefender.setStyleSheet(get_invasion_color(attacker_faction))

    def set_invasion_info(self, init: int, loctag: str, perc: List[int]):
        self.InvStart.setText(translate("invasion", "invasionInit") + " " + get_date_time(init))
        self.InvDesc.setText(loctag)
        self.set_invasion_perc(perc)

    def set_invasion_reward(self, attacker_reward: str, defender_reward: str,
                            attacker_reward_item: str, defender_reward_item: str) -> None:
        self.InvRewardAtt.setText(attacker_reward)
        self.InvRewardDef.setText(defender_reward)
        self.set_invasion_image(attacker_reward, defender_reward, attacker_reward_item, defender_reward_item)

    def set_invasion_perc(self, perc: List[int]) -> None:
        self.InvPer.reset()
        self.InvPer.setMaximum(perc[1])
        if (perc[2] == 1):
            value = perc[1] + perc[0]
        else:
            value = perc[1] / 2 + perc[0] / 2
        if (value > perc[1] * 2 or value < 0):
            value = 0
        if (perc[2] == 1):
            if ((value * 100 / perc[1]) >= 100):
                self.InvPer.setValue(100)
            else:
                self.InvPer.setValue(int(value))
            self.InvPer.setToolTip(str(value * 100 / perc[1]) + "%")
        else:
            if ((value * 100 / perc[1]) >= 100):
                self.InvPer.setValue(100)
            else:
                self.InvPer.setValue(int(value))
            self.InvPer.setToolTip(str(value * 100 / perc[1]) + "%")

    def set_invasion_image(self, attacker_reward: str, defender_reward: str,
                           attacker_reward_item: str, defender_reward_item: str) -> None:
        if (" x " in attacker_reward):
            attacker_reward = attacker_reward.split(" x ")[1]
        if (" x " in defender_reward):
            defender_reward = defender_reward.split(" x ")[1]
        # Attacker Image (Left)
        if (attacker_reward_item != ""):
            part = get_weapon_part(attacker_reward_item)
            if (part):
                if (part == "Unknown"):
                    self.InvAttackerImg.hide()
                elif (part == "Blueprint"):
                    part = get_weapon_type(attacker_reward_item)
                img = get_image_path_from_name(part)
            elif (get_image_path_from_name(attacker_reward) != attacker_reward):
                img = get_image_path_from_name(attacker_reward)
            else:
                img = attacker_reward_item + ".png"
            image_name = "assets" + get_separator() + "image" + get_separator() + get_last_item_with_backslash(img)
            self.InvAttackerImg.set_image(image_name)
            self.image = image_name
            self.InvAttackerImg.set_image_dimension(50, 50, Qt.AspectRatioMode.KeepAspectRatio)
        else:
            self.InvAttackerImg.hide()

        # Defender Image (Right)
        part = get_weapon_part(defender_reward_item)
        if (part):
            if (part == "Unknown"):
                self.InvDefenderImg.hide()
            elif (part == "Blueprint"):
                part = get_weapon_type(defender_reward_item)
            img = get_image_path_from_name(part)
        elif (get_image_path_from_name(defender_reward) != defender_reward):
            img = get_image_path_from_name(defender_reward)
        else:
            img = defender_reward_item + ".png"
        image_name = "assets" + get_separator() + "image" + get_separator() + get_last_item_with_backslash(img)
        self.InvDefenderImg.set_image(image_name)
        if (not self.image):
            self.image = image_name
        self.InvDefenderImg.set_image_dimension(50, 50, Qt.AspectRatioMode.KeepAspectRatio)

    def hide(self) -> None:
        self.InvDesc.hide()
        self.InvStart.hide()
        self.InvNode.hide()
        self.InvAttacker.hide()
        self.InvDefender.hide()
        self.InvRewardAtt.hide()
        self.InvRewardDef.hide()
        self.InvSpace.hide()
        self.InvVS.hide()
        self.InvAttackerImg.hide()
        self.InvDefenderImg.hide()
        self.InvPer.hide()


def get_invasion_color(faction: str) -> str:
    if (faction == "Grineer"):
        return "QLabel { color : red; }"
    elif (faction == "Corpus"):
        return "QLabel { color : blue; }"
    elif (faction == "Infested"):
        return "QLabel { color : green; }"
