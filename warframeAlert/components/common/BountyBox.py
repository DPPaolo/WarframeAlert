# coding=utf-8
from PyQt5 import QtGui, QtWidgets

from warframeAlert.components.common.MissionDropView import MissionDropView
from warframeAlert.components.widget.MissionDropViewWidget import MissionDropViewWidget
from warframeAlert.services.translationService import translate
from warframeAlert.utils.gameTranslationUtils import get_bounty_job, get_bounty_job_desc
from warframeAlert.utils.warframeUtils import get_bounty_reward


class BountyBox():

    def __init__(self):
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

        bountyhbox1 = QtWidgets.QHBoxLayout()
        bountyhbox2 = QtWidgets.QHBoxLayout()

        bountyvbox1 = QtWidgets.QVBoxLayout()
        bountyvbox2 = QtWidgets.QVBoxLayout()

        self.BountyBox = QtWidgets.QHBoxLayout()

        bountyhbox1.addWidget(self.BountyJob)
        bountyhbox1.addWidget(self.BountyLevel)

        bountyhbox2.addWidget(self.BountyXPLab)
        bountyhbox2.addWidget(self.BountyXP)
        bountyhbox2.addWidget(self.BountyRewardType)

        bountyvbox1.addWidget(self.BountyNumber)
        bountyvbox1.addLayout(bountyhbox1)
        bountyvbox1.addWidget(self.BountyDesc)

        bountyvbox2.addLayout(bountyhbox2)
        bountyvbox2.addWidget(self.BountyReward)
        bountyvbox2.addWidget(self.BountySyn)

        self.BountyBox.addLayout(bountyvbox1)
        self.BountyBox.addLayout(bountyvbox2)

        self.BountyReward.clicked.connect(lambda: self.open_drop_bounty())

    def set_bounty_mission(self, job, rew, minlv, maxlv, xp):
        self.reward = rew
        self.BountyJob.setText(get_bounty_job(job))
        self.BountyDesc.setText(get_bounty_job_desc(job))
        self.BountyLevel.setText(translate("bountyBox", "level") + ": " + str(minlv) + " - " + str(maxlv))
        affinity = 0
        for i in range(0, len(xp)):
            affinity += int(xp[i])
        self.BountyXP.setText(str(affinity))
        if (rew == ""):
            self.BountyRewardType.setText(translate("bountyBox", "rewardType") + " N/D")
        else:
            self.BountyRewardType.setText(translate("bountyBox", "rewardType") + " " + rew[-8])

    def set_syndicate(self, syn, num):
        self.BountySyn.setText(translate("bountyBox", "syndicate") + ": " + syn)
        self.BountyNumber.setText(translate("bountyBox", "bountyName") + " " + str(num))

    def set_bounty_id(self, bounty_id):
        self.bounty_id = bounty_id

    def get_bounty_id(self):
        return self.bounty_id

    def open_drop_bounty(self):
        name = [translate("bountyBox", "rewardType") + " A",
                translate("bountyBox", "rewardType") + " B",
                translate("bountyBox", "rewardType") + " C"]
        drop = MissionDropView()
        if ('Venus' in self.reward):
            reward = get_bounty_reward(self.reward, "fortuna")
            drop.set_drop(3, name, reward)
            self.missionDropWidget = MissionDropViewWidget(None, drop)
            self.viewDropWidget = self.missionDropWidget.get_widget()
            self.viewDropWidget.setWindowTitle(translate("bountyBox", "dropFortuna"))
        elif ('Ghoul' in self.reward):
            reward = get_bounty_reward(self.reward, "cetus")
            drop.set_drop(1, name, reward)
            self.missionDropWidget = MissionDropViewWidget(None, drop)
            self.viewDropWidget = self.missionDropWidget.get_widget()
            self.viewDropWidget.setWindowTitle(translate("bountyBox", "dropGhoul"))
        else:
            reward = get_bounty_reward(self.reward, "cetus")
            drop.set_drop(3, name, reward)
            self.missionDropWidget = MissionDropViewWidget(None, drop)
            self.viewDropWidget = self.missionDropWidget.get_widget()
            self.viewDropWidget.setWindowTitle(translate("bountyBox", "dropCetus"))
        self.viewDropWidget.show()

    def hide(self):
        self.BountyNumber.hide()
        self.BountyJob.hide()
        self.BountyDesc.hide()
        self.BountyLevel.hide()
        self.BountyXPLab.hide()
        self.BountyXP.hide()
        self.BountyReward.hide()
        self.BountyRewardType.hide()
        self.BountySyn.hide()


def create_bounty_box(job):
    xp = []
    job_type = minlv = maxlv = rew = ""
    if ('maxEnemyLevel' in job):
        maxlv = job['maxEnemyLevel']
    if ('minEnemyLevel' in job):
        minlv = job['minEnemyLevel']
    if ('rewards' in job):
        rew = job['rewards']
    if ('xpAmounts' in job):
        for i in job['xpAmounts']:
            xp.append(i)
    if ('jobType' in job):
        job_type = job['jobType']
    cetus = BountyBox()
    cetus.set_bounty_mission(job_type, rew, minlv, maxlv, xp)
    return cetus
