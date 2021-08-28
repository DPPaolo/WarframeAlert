# coding=utf-8
from typing import List

from PyQt5 import QtWidgets

from warframeAlert.utils.commonUtils import remove_widget


def get_sortie_reward_color(rarity: float) -> str:
    if (rarity >= 12.0):
        return "QLabel { color : brown; }"
    elif (rarity >= 3.0):
        return "QLabel { color : gray; }"
    elif (rarity >= 1.0):
        return "QLabel { color:gold; }"
    else:
        return "QLabel { color:purple; }"


class SortieMissionDropView():

    def __init__(self) -> None:

        self.DropBox = QtWidgets.QVBoxLayout()

    def set_drop(self, drop: List[str]) -> None:
        for i in range(0, len(drop), 3):
            drop_to_visualize = [drop[i],
                                 drop[i + 1] if i + 1 < len(drop) else "",
                                 drop[i + 2] if i + 2 < len(drop) else ""]
            self.DropBox.addLayout(SortieMissionDropRow(drop_to_visualize).DropListBox)

    def set_drop_message(self, text: str) -> None:
        remove_widget(self.DropBox)
        self.DropBox.addLayout(SortieMissionDropRow([text, "", ""]).DropListBox)


class SortieMissionDropRow():

    def __init__(self, drop: List[str, str, str]) -> None:

        self.ViewDrop1 = QtWidgets.QLabel(drop[0])
        self.ViewDrop2 = QtWidgets.QLabel(drop[1])
        self.ViewDrop3 = QtWidgets.QLabel(drop[2])

        if ("%)" in drop[0]):
            self.ViewDrop1.setStyleSheet(get_sortie_reward_color(float(drop[0].split("%)")[0].split(" ")[-1])))
        if ("%)" in drop[1]):
            self.ViewDrop2.setStyleSheet(get_sortie_reward_color(float(drop[1].split("%)")[0].split(" ")[-1])))
        if ("%)" in drop[2]):
            self.ViewDrop3.setStyleSheet(get_sortie_reward_color(float(drop[2].split("%)")[0].split(" ")[-1])))

        self.DropListBox = QtWidgets.QHBoxLayout()

        self.DropListBox.addWidget(self.ViewDrop1)
        self.DropListBox.addWidget(self.ViewDrop2)
        self.DropListBox.addWidget(self.ViewDrop3)
