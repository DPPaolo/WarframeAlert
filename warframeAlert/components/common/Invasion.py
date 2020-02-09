# coding=utf-8
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

from warframeAlert.components.common.CommonImages import CommonImages
from warframeAlert.services.translationService import translate
from warframeAlert.utils.commonUtils import get_last_item_with_backslash, get_separator
from warframeAlert.utils.timeUtils import get_date_time
from warframeAlert.utils.warframeUtils import get_weapon_part, get_weapon_type, get_image_path_from_name, \
    get_image_path_from_export_manifest


def get_invasion_color(faz):
    if (faz == "Grineer"):
        return "QLabel { color : red; }"
    elif (faz == "Corpus"):
        return "QLabel { color : blue; }"
    elif (faz == "Infested"):
        return "QLabel { color : green; }"


class Invasion():

    def __init__(self, invasion_id, chain_id):
        self.completed = False
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
        self.InvasionBox.addStretch(1)

    def set_completed(self, completed):
        self.completed = completed

    def is_completed(self):
        return self.completed

    def get_invasion_id(self):
        return self.invasion_id

    def get_title(self):
        return self.InvDesc.text() + " " + self.InvStart.text() + " " + self.InvNode.text()

    def to_string(self):
        name = self.InvAttacker.text() + " vs " + self.InvDefender.text() + "\n"
        if (self.InvAttacker.text() == "Infested"):
            reward = self.InvRewardDef.text()
        else:
            reward = self.InvRewardAtt.text() + " vs " + self.InvRewardDef.text()

        return name + reward

    def set_invasion_data(self, mission, node, attacker_faction, defender_faction):
        self.InvNode.setText(mission + " " + node)
        self.InvAttacker.setText(defender_faction)
        self.InvDefender.setText(attacker_faction)
        self.InvAttacker.setStyleSheet(get_invasion_color(defender_faction))
        self.InvDefender.setStyleSheet(get_invasion_color(attacker_faction))

    def set_invasion_info(self, init, loctag, perc):
        self.InvStart.setText(translate("invasion", "invasionInit") + " " + get_date_time(init))
        self.InvDesc.setText(loctag)
        self.set_invasion_perc(perc)

    def set_invasion_reward(self, attacker_reward, defender_reward, attacker_reward_item, defender_reward_item):
        self.InvRewardAtt.setText(attacker_reward)
        self.InvRewardDef.setText(defender_reward)
        self.set_invasion_image(attacker_reward, defender_reward, attacker_reward_item, defender_reward_item)

    def set_invasion_perc(self, perc):
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
                self.InvPer.setValue(value)
            self.InvPer.setToolTip(str(value * 100 / perc[1]) + "%")
        else:
            if ((value * 100 / perc[1]) >= 100):
                self.InvPer.setValue(100)
            else:
                self.InvPer.setValue(value)
            self.InvPer.setToolTip(str(value * 100 / perc[1]) + "%")

    def set_invasion_image(self, attacker_reward, defender_reward, attacker_reward_item, defender_reward_item):
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
                img = get_image_path_from_export_manifest(attacker_reward_item)
            image_name = "images" + get_separator() + get_last_item_with_backslash(img)
            self.InvAttackerImg.set_image(image_name)
            self.InvAttackerImg.set_image_dimension(50, 50, Qt.KeepAspectRatio)
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
            img = get_image_path_from_export_manifest(defender_reward_item)
        image_name = "images" + get_separator() + get_last_item_with_backslash(img)
        self.InvDefenderImg.set_image(image_name)
        self.InvDefenderImg.set_image_dimension(50, 50, Qt.KeepAspectRatio)

    def hide(self):
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
