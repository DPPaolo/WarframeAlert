# coding=utf-8
from typing import List

from PyQt6 import QtGui, QtWidgets

from warframeAlert.components.common.MissionDropView import MissionDropView
from warframeAlert.components.widget.MissionDropViewWidget import MissionDropViewWidget
from warframeAlert.constants.warframeTypes import SyndicateJobs
from warframeAlert.services.translationService import translate
from warframeAlert.utils.commonUtils import get_last_item_with_backslash
from warframeAlert.utils.gameTranslationUtils import get_bounty_job, get_bounty_job_desc
from warframeAlert.utils.stringUtils import divide_message
from warframeAlert.utils.warframeUtils import get_bounty_reward


class BountyBox():

    def __init__(self) -> None:
        self.Font = QtGui.QFont()
        self.Font.setBold(True)

        self.missionDropWidget = None
        self.viewDropWidget = None
        self.reward = ""
        self.bounty_id = ""

        self.BountyNumber = QtWidgets.QLabel(translate("bountyBox", "bountyName") + " ")

        self.BountyJob = QtWidgets.QLabel("N/D")
        self.BountyDesc = QtWidgets.QLabel("N/D")
        self.BountyLevel = QtWidgets.QLabel("N/D")
        self.BountyXPLab = QtWidgets.QLabel(translate("bountyBox", "affinity") + ": ")
        self.BountyXP = QtWidgets.QLabel("N/D")
        self.BountyReward = QtWidgets.QPushButton(translate("bountyBox", "drop"))
        self.BountyRewardType = QtWidgets.QLabel("N/D")
        self.BountySyn = QtWidgets.QLabel(translate("bountyBox", "syndicate") + " : N/D")

        self.BountyNumber.setFont(self.Font)
        self.BountyRewardType.setFont(self.Font)
        self.BountySyn.setFont(self.Font)

        self.bountyHBox1 = QtWidgets.QHBoxLayout()
        self.bountyHBox2 = QtWidgets.QHBoxLayout()

        self.bountyVBox1 = QtWidgets.QVBoxLayout()
        self.bountyVBox2 = QtWidgets.QVBoxLayout()

        self.BountyBox = QtWidgets.QHBoxLayout()

        self.bountyHBox1.addWidget(self.BountyJob)
        self.bountyHBox1.addWidget(self.BountyLevel)

        self.bountyHBox2.addWidget(self.BountyXPLab)
        self.bountyHBox2.addWidget(self.BountyXP)
        self.bountyHBox2.addWidget(self.BountyRewardType)

        self.bountyVBox1.addWidget(self.BountyNumber)
        self.bountyVBox1.addLayout(self.bountyHBox1)
        self.bountyVBox1.addWidget(self.BountyDesc)

        self.bountyVBox2.addLayout(self.bountyHBox2)
        self.bountyVBox2.addWidget(self.BountyReward)
        self.bountyVBox2.addWidget(self.BountySyn)

        self.BountyBox.addLayout(self.bountyVBox1)
        self.BountyBox.addLayout(self.bountyVBox2)

        self.BountyReward.clicked.connect(lambda: self.open_drop_bounty())

    def set_bounty_mission(self, job: str, rew: str, min_lv: int, max_lv: int, xp: List[int]) -> None:
        self.reward = rew
        self.BountyJob.setText(get_last_item_with_backslash(get_bounty_job(job)))
        self.BountyDesc.setText(divide_message(get_bounty_job_desc(job)))
        self.BountyLevel.setText(translate("bountyBox", "level") + ": " + str(min_lv) + " - " + str(max_lv))
        affinity = 0
        for i in range(0, len(xp)):
            affinity += int(xp[i])
        self.BountyXP.setText(str(affinity))
        if (rew == ""):
            self.BountyRewardType.setText(translate("bountyBox", "rewardType") + " N/D")
        else:
            reward_type = rew[-8] if (rew[-8] in ["A", "B", "C"]) else "A"
            self.BountyRewardType.setText(translate("bountyBox", "rewardType") + " " + reward_type)

    def set_syndicate(self, syn: str, num: int | str, use_token: bool) -> None:
        self.BountySyn.setText(translate("bountyBox", "syndicate") + ": " + syn)
        self.BountyNumber.setText(translate("bountyBox", "bountyName") + " " + str(num))
        if (use_token):
            self.BountyXPLab.setText(translate("bountyBox", "token") + ": ")

    def set_bounty_id(self, bounty_id: str) -> None:
        self.bounty_id = bounty_id

    def get_bounty_id(self) -> str:
        return self.bounty_id

    def open_drop_bounty(self) -> None:
        name = [translate("bountyBox", "rewardType") + " A",
                translate("bountyBox", "rewardType") + " B",
                translate("bountyBox", "rewardType") + " C"]
        drop = MissionDropView()
        self.missionDropWidget = MissionDropViewWidget(drop)
        self.viewDropWidget = self.missionDropWidget.get_widget()
        if ('Venus' in self.reward):
            reward = get_bounty_reward(self.reward, "fortuna")
            drop.set_drop(3, name, reward)
            self.viewDropWidget.setWindowTitle(translate("bountyBox", "dropFortuna"))
        elif ('Ghoul' in self.reward):
            reward = get_bounty_reward(self.reward, "cetus")
            drop.set_drop(1, name, reward)
            self.viewDropWidget.setWindowTitle(translate("bountyBox", "dropGhoul"))
        elif ('Eidolon' in self.reward):
            reward = get_bounty_reward(self.reward, "cetus")
            drop_num = 1 if ("Plague" in self.reward) else 3
            drop.set_drop(drop_num, name, reward)
            self.viewDropWidget.setWindowTitle(translate("bountyBox", "dropCetus"))
        elif ('Deimos' in self.reward):
            reward = get_bounty_reward(self.reward, "deimos")
            drop.set_drop(3, name, reward)
            self.viewDropWidget.setWindowTitle(translate("bountyBox", "dropDeimos"))
        else:
            print(translate("bountyBox", "noBountyRewardFound") + " " + self.reward)
        self.viewDropWidget.show()

    def hide(self) -> None:
        self.BountyNumber.hide()
        self.BountyJob.hide()
        self.BountyDesc.hide()
        self.BountyLevel.hide()
        self.BountyXPLab.hide()
        self.BountyXP.hide()
        self.BountyReward.hide()
        self.BountyRewardType.hide()
        self.BountySyn.hide()


def create_bounty_box(job: SyndicateJobs) -> BountyBox:
    xp: List[int] = []
    job_type = rew = ""
    min_lv = max_lv = 0
    if ('maxEnemyLevel' in job):
        max_lv = job['maxEnemyLevel']
    if ('minEnemyLevel' in job):
        min_lv = job['minEnemyLevel']
    if ('rewards' in job):
        rew = job['rewards']
    if ('xpAmounts' in job):
        for i in job['xpAmounts']:
            xp.append(i)
    if ('jobType' in job):
        job_type = job['jobType']
    bounty = BountyBox()
    bounty.set_bounty_mission(job_type, rew, min_lv, max_lv, xp)
    return bounty
