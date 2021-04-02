# coding=utf-8
from PyQt5 import QtCore, QtWidgets, QtGui

from warframeAlert.components.common.CommonImages import CommonImages
from warframeAlert.components.common.EmptySpace import EmptySpace
from warframeAlert.components.common.MissionDropView import MissionDropView
from warframeAlert.components.widget.MissionDropViewWidget import MissionDropViewWidget
from warframeAlert.constants.files import IMAGE_NAME
from warframeAlert.services.translationService import translate
from warframeAlert.utils.commonUtils import get_last_item_with_backslash
from warframeAlert.utils.fileUtils import get_separator
from warframeAlert.utils.stringUtils import divide_for_n
from warframeAlert.utils.warframeUtils import get_relic_item, get_relic_drop


class RelicBox():

    def __init__(self, tier):

        self.ViewDropWidget = None

        self.Font = QtGui.QFont()
        self.Font.setBold(True)

        self.RelicImg = CommonImages()
        self.RelicName = QtWidgets.QLabel("")
        self.RelicReward1 = QtWidgets.QLabel("")
        self.RelicReward2 = QtWidgets.QLabel("")
        self.RelicReward3 = QtWidgets.QLabel("")
        self.RelicReward4 = QtWidgets.QLabel("")
        self.RelicReward5 = QtWidgets.QLabel("")
        self.RelicReward6 = QtWidgets.QLabel("")
        self.name = ""
        self.tier = tier
        self.RelicDrop = QtWidgets.QPushButton(translate("relicBox", "viewRelicDrop"))

        self.RelicDrop.clicked.connect(lambda: self.open_drop_relic())

        self.RelicName.setFont(self.Font)

        self.RelicVBox = QtWidgets.QVBoxLayout()
        self.RelicBox = QtWidgets.QVBoxLayout()

        self.RelicHBox = QtWidgets.QHBoxLayout()

        self.RelicVBox.addWidget(self.RelicName)
        self.RelicVBox.addWidget(self.RelicReward1)
        self.RelicVBox.addWidget(self.RelicReward2)
        self.RelicVBox.addWidget(self.RelicReward3)
        self.RelicVBox.addWidget(self.RelicReward4)
        self.RelicVBox.addWidget(self.RelicReward5)
        self.RelicVBox.addWidget(self.RelicReward6)
        self.RelicVBox.addLayout(EmptySpace().SpaceBox)

        self.RelicHBox.addWidget(self.RelicImg.image)
        self.RelicHBox.addLayout(self.RelicVBox)
        self.RelicHBox.addStretch(1)

        self.RelicBox.addLayout(self.RelicHBox)
        self.RelicBox.addWidget(self.RelicDrop)
        self.RelicBox.addStretch(1)

    def set_relic_data(self, name, reward):
        self.name = name
        self.RelicName.setText(name)
        self.RelicReward1.setText(reward[0][0])
        self.RelicReward2.setText(reward[1][0])
        self.RelicReward3.setText(reward[2][0])
        self.RelicReward4.setText(reward[3][0])
        self.RelicReward5.setText(reward[4][0])
        self.RelicReward6.setText(reward[5][0])

        self.RelicReward1.setStyleSheet(set_relic_rarity_font(reward[0][1]))
        self.RelicReward2.setStyleSheet(set_relic_rarity_font(reward[1][1]))
        self.RelicReward3.setStyleSheet(set_relic_rarity_font(reward[2][1]))
        self.RelicReward4.setStyleSheet(set_relic_rarity_font(reward[3][1]))
        self.RelicReward5.setStyleSheet(set_relic_rarity_font(reward[4][1]))
        self.RelicReward6.setStyleSheet(set_relic_rarity_font(reward[5][1]))

        self.set_relic_image()

    def set_relic_image(self):
        if (self.tier == 1):
            tier = "Lith"
        elif (self.tier == 2):
            tier = "Meso"
        elif (self.tier == 3):
            tier = "Neo"
        elif (self.tier == 4):
            tier = "Axi"
        elif (self.tier == 5):
            tier = "Requiem"
        else:
            tier = "Lith"
        img = IMAGE_NAME[tier]
        image = get_last_item_with_backslash(img)
        image_name = "assets" + get_separator() + "image" + get_separator() + image

        self.RelicImg.set_image(image_name)
        self.RelicImg.set_image_dimension(60, 60, QtCore.Qt.KeepAspectRatio)

    def set_relic_tier(self, tier):
        self.tier = tier
        self.set_relic_image()

    def set_relic_name(self, name):
        reward = get_relic_item(name)
        self.set_relic_data(name, reward)

    def hide_button(self):
        self.RelicDrop.hide()

    def open_drop_relic(self):
        reward = get_relic_drop(self.name)
        reward = divide_for_n(reward, 3)
        name = [translate("relicBox", "missions"), "", ""]
        drop = MissionDropView()
        drop.set_drop(3, name, [reward[0], reward[1], reward[2]])

        self.ViewDropWidget = MissionDropViewWidget(None, drop).get_widget()
        self.ViewDropWidget.setWindowTitle(translate("relicBox", "missionDrop") + ' ' + self.name)
        self.ViewDropWidget.show()


def set_relic_rarity_font(rarity):
    if (translate("warframeUtils", "rare") in rarity):
        return "QLabel { color : gold; }"
    elif (translate("warframeUtils", "notCommon") in rarity):
        return "QLabel { color : gray; }"
    else:
        return "QLabel { color : brown; }"
