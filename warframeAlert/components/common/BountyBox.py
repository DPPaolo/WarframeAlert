# coding=utf-8
from PyQt5 import QtGui, QtWidgets

from warframeAlert.components.common.MissionDropView import MissionDropView
from warframeAlert.components.widget.MissionDropViewWidget import MissionDropViewWidget
from warframeAlert.services.translationService import translate
from warframeAlert.utils.gameTranslationUtils import get_cetus_job, get_cetus_job_desc
from warframeAlert.utils.warframeUtils import get_bounty_reward


class BountyBox():

    def __init__(self):
        self.Font = QtGui.QFont()
        self.Font.setBold(True)

        self.missionDropWidget = None
        self.viewDropWidget = None
        self.reward = ""
        self.cetus_id = ""

        self.CetusNum = QtWidgets.QLabel(translate("bountyBox", "bountyName") + " ")

        self.CetusJob = QtWidgets.QLabel("N/D")
        self.CetusDesc = QtWidgets.QLabel("N/D")
        self.CetusLevel = QtWidgets.QLabel("N/D")
        self.CetusXPLab = QtWidgets.QLabel(translate("bountyBox", "affinity") + ": ")
        self.CetusXP = QtWidgets.QLabel("N/D")
        self.CetusReward = QtWidgets.QPushButton(translate("bountyBox", "drop"))
        self.CetusRewardType = QtWidgets.QLabel("N/D")
        self.CetusSyn = QtWidgets.QLabel(translate("bountyBox", "syndicate") + " : N/D")

        self.CetusNum.setFont(self.Font)
        self.CetusRewardType.setFont(self.Font)
        self.CetusSyn.setFont(self.Font)

        cetushbox1 = QtWidgets.QHBoxLayout()
        cetushbox2 = QtWidgets.QHBoxLayout()

        cetusvbox1 = QtWidgets.QVBoxLayout()
        cetusvbox2 = QtWidgets.QVBoxLayout()

        self.CetusBox = QtWidgets.QHBoxLayout()

        cetushbox1.addWidget(self.CetusJob)
        cetushbox1.addWidget(self.CetusLevel)

        cetushbox2.addWidget(self.CetusXPLab)
        cetushbox2.addWidget(self.CetusXP)
        cetushbox2.addWidget(self.CetusRewardType)

        cetusvbox1.addWidget(self.CetusNum)
        cetusvbox1.addLayout(cetushbox1)
        cetusvbox1.addWidget(self.CetusDesc)

        cetusvbox2.addLayout(cetushbox2)
        cetusvbox2.addWidget(self.CetusReward)
        cetusvbox2.addWidget(self.CetusSyn)

        self.CetusBox.addLayout(cetusvbox1)
        self.CetusBox.addLayout(cetusvbox2)

        self.CetusReward.clicked.connect(lambda: self.open_drop_cetus())

    def set_cetus_mission(self, job, rew, minlv, maxlv, xp):
        self.reward = rew
        self.CetusJob.setText(get_cetus_job(job))
        self.CetusDesc.setText(get_cetus_job_desc(job))
        self.CetusLevel.setText(translate("bountyBox", "level") + ": " + str(minlv) + " - " + str(maxlv))
        affinity = 0
        for i in range(0, len(xp)):
            affinity += int(xp[i])
        self.CetusXP.setText(str(affinity))
        if (rew == ""):
            self.CetusRewardType.setText(translate("bountyBox", "rewardType") + " N/D")
        else:
            self.CetusRewardType.setText(translate("bountyBox", "rewardType") + " " + rew[-8])

    def set_syndicate(self, syn, num):
        self.CetusSyn.setText(translate("bountyBox", "syndicate") + ": " + syn)
        self.CetusNum.setText(translate("bountyBox", "bountyName") + " " + str(num))

    def set_cetus_id(self, cetus_id):
        self.cetus_id = cetus_id

    def get_cetus_id(self):
        return self.cetus_id

    def open_drop_cetus(self):

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
        self.CetusNum.hide()
        self.CetusJob.hide()
        self.CetusDesc.hide()
        self.CetusLevel.hide()
        self.CetusXPLab.hide()
        self.CetusXP.hide()
        self.CetusReward.hide()
        self.CetusRewardType.hide()
        self.CetusSyn.hide()

    def __del__(self):
        self.hide()


def create_cetus_box(job):
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
    cetus.set_cetus_mission(job_type, rew, minlv, maxlv, xp)
    return cetus
