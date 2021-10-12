# coding=utf-8
from __future__ import annotations

from typing import List, Tuple

from PyQt6 import QtCore, QtWidgets, QtGui

from warframeAlert.components.common.Event import Event
from warframeAlert.services.translationService import translate


class ClanEvent(Event):

    def __init__(self, event_id: str, req_node: Tuple[str, str] | None) -> None:
        super().__init__(event_id)

        self.Font = QtGui.QFont()
        self.Font.setBold(True)

        self.TASDesc = QtWidgets.QLabel(translate("clanEvent", "clanScore"))
        self.TARank0 = QtWidgets.QLabel(translate("clanEvent", "solo"))
        self.TARank1 = QtWidgets.QLabel(translate("clanEvent", "ghost"))
        self.TARank2 = QtWidgets.QLabel(translate("clanEvent", "shadow"))
        self.TARank3 = QtWidgets.QLabel(translate("clanEvent", "storm"))
        self.TARank4 = QtWidgets.QLabel(translate("clanEvent", "mountain"))
        self.TARank5 = QtWidgets.QLabel(translate("clanEvent", "moon"))
        self.TAVRank0 = QtWidgets.QLabel("N/D")
        self.TAVRank1 = QtWidgets.QLabel("N/D")
        self.TAVRank2 = QtWidgets.QLabel("N/D")
        self.TAVRank3 = QtWidgets.QLabel("N/D")
        self.TAVRank4 = QtWidgets.QLabel("N/D")
        self.TAVRank5 = QtWidgets.QLabel("N/D")

        self.TASDesc.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.TASDesc.setFont(self.Font)

        self.TAClanBox1 = QtWidgets.QHBoxLayout()
        self.TAClanBox2 = QtWidgets.QHBoxLayout()
        self.TAClanBox = QtWidgets.QVBoxLayout()

        self.TAClanBox1.addWidget(self.TARank0)
        self.TAClanBox1.addWidget(self.TARank1)
        self.TAClanBox1.addWidget(self.TARank2)
        self.TAClanBox1.addWidget(self.TARank3)
        self.TAClanBox1.addWidget(self.TARank4)
        self.TAClanBox1.addWidget(self.TARank5)

        self.TAClanBox2.addWidget(self.TAVRank0)
        self.TAClanBox2.addWidget(self.TAVRank1)
        self.TAClanBox2.addWidget(self.TAVRank2)
        self.TAClanBox2.addWidget(self.TAVRank3)
        self.TAClanBox2.addWidget(self.TAVRank4)
        self.TAClanBox2.addWidget(self.TAVRank5)

        self.TAClanBox.addWidget(self.TASDesc)
        self.TAClanBox.addLayout(self.TAClanBox1)
        self.TAClanBox.addLayout(self.TAClanBox2)

        self.TADescVBox.addLayout(self.TAClanBox)

        self.set_req_node(req_node)

    def set_clan_score(self, rank: List[str]):
        self.TAVRank0.setText(str(rank[0]))
        self.TAVRank1.setText(str(rank[1]))
        self.TAVRank2.setText(str(rank[2]))
        self.TAVRank3.setText(str(rank[3]))
        self.TAVRank4.setText(str(rank[4]))
        self.TAVRank5.setText(str(rank[5]))

    def set_req_node(self, req_node: Tuple[str, str] | None) -> None:
        if (not req_node):
            return
        self.TASDesc.setText(translate("clanEvent", "unlockScore") + " " + req_node[0] + " " + req_node[1])

    def hide(self) -> None:
        super().hide()
        self.TASDesc.hide()
        self.TARank0.hide()
        self.TARank1.hide()
        self.TARank2.hide()
        self.TARank3.hide()
        self.TARank4.hide()
        self.TARank5.hide()
        self.TAVRank0.hide()
        self.TAVRank1.hide()
        self.TAVRank2.hide()
        self.TAVRank3.hide()
        self.TAVRank4.hide()
        self.TAVRank5.hide()
