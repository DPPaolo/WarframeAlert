# coding=utf-8
from typing import List

from PyQt5 import QtGui, QtWidgets, QtCore

from warframeAlert.services.translationService import translate
from warframeAlert.utils.gameTranslationUtils import get_node, get_syndicate_rank


class SyndicateBox():

    def __init__(self, syndicate_widget: QtWidgets.QWidget) -> None:
        self.Font = QtGui.QFont()
        self.Font.setBold(True)

        self.syn_id = ""
        self.tag = ""
        self.seed = ""

        self.SynMis1 = QtWidgets.QLabel(translate("syndicateBox", "rank1") + ": ")
        self.SynMis2 = QtWidgets.QLabel(translate("syndicateBox", "rank2") + ": ")
        self.SynMis3 = QtWidgets.QLabel(translate("syndicateBox", "rank3") + ": ")
        self.SynMis4 = QtWidgets.QLabel(translate("syndicateBox", "rank4") + ": ")
        self.SynMis5 = QtWidgets.QLabel(translate("syndicateBox", "rank5") + ": ")

        self.SynMis1.setFont(self.Font)
        self.SynMis2.setFont(self.Font)
        self.SynMis3.setFont(self.Font)
        self.SynMis4.setFont(self.Font)
        self.SynMis5.setFont(self.Font)

        self.Mis1 = QtWidgets.QLabel("N/D")
        self.Mis21 = QtWidgets.QLabel("N/D")
        self.Mis22 = QtWidgets.QLabel("N/D")
        self.Mis31 = QtWidgets.QLabel("N/D")
        self.Mis32 = QtWidgets.QLabel("N/D")
        self.Mis33 = QtWidgets.QLabel("N/D")
        self.Mis41 = QtWidgets.QLabel("N/D")
        self.Mis42 = QtWidgets.QLabel("N/D")
        self.Mis43 = QtWidgets.QLabel("N/D")
        self.Mis51 = QtWidgets.QLabel("N/D")
        self.Mis52 = QtWidgets.QLabel("N/D")
        self.Mis53 = QtWidgets.QLabel("N/D")
        self.Mis61 = QtWidgets.QLabel("N/D")
        self.Mis62 = QtWidgets.QLabel("N/D")
        self.Mis7 = QtWidgets.QLabel("N/D")

        self.SynGrid = QtWidgets.QGridLayout(syndicate_widget)

        self.SynGrid.addWidget(self.SynMis1, 0, 0)
        self.SynGrid.addWidget(self.Mis1, 1, 0)
        self.SynGrid.addWidget(self.Mis21, 1, 1)
        self.SynGrid.addWidget(self.Mis31, 1, 2)
        self.SynGrid.addWidget(self.SynMis2, 2, 0)
        self.SynGrid.addWidget(self.Mis22, 3, 0)
        self.SynGrid.addWidget(self.Mis32, 3, 1)
        self.SynGrid.addWidget(self.Mis41, 3, 2)
        self.SynGrid.addWidget(self.SynMis3, 4, 0)
        self.SynGrid.addWidget(self.Mis33, 5, 0)
        self.SynGrid.addWidget(self.Mis42, 5, 1)
        self.SynGrid.addWidget(self.Mis51, 5, 2)
        self.SynGrid.addWidget(self.SynMis4, 6, 0)
        self.SynGrid.addWidget(self.Mis43, 7, 0)
        self.SynGrid.addWidget(self.Mis52, 7, 1)
        self.SynGrid.addWidget(self.Mis61, 7, 2)
        self.SynGrid.addWidget(self.SynMis5, 8, 0)
        self.SynGrid.addWidget(self.Mis53, 9, 0)
        self.SynGrid.addWidget(self.Mis62, 9, 1)
        self.SynGrid.addWidget(self.Mis7, 9, 2)

        self.SynGrid.setAlignment(QtCore.Qt.AlignTop)

    def get_syn_id(self) -> str:
        return self.syn_id

    def set_syndicate(self, tag: str, syn_id: str, seed: int) -> None:
        self.syn_id = syn_id
        self.tag = tag
        self.seed = seed
        self.SynMis1.setText(translate("syndicateBox", "rank1") + ": " + get_syndicate_rank(tag, 0))
        self.SynMis2.setText(translate("syndicateBox", "rank2") + ": " + get_syndicate_rank(tag, 1))
        self.SynMis3.setText(translate("syndicateBox", "rank3") + ": " + get_syndicate_rank(tag, 2))
        self.SynMis4.setText(translate("syndicateBox", "rank4") + ": " + get_syndicate_rank(tag, 3))
        self.SynMis5.setText(translate("syndicateBox", "rank5") + ": " + get_syndicate_rank(tag, 4))

    def set_syndicate_mission(self, mis: List[str]) -> None:
        mis1 = get_node(mis[0])
        mis2 = get_node(mis[1])
        mis3 = get_node(mis[2])
        mis4 = get_node(mis[3])
        mis5 = get_node(mis[4])
        mis6 = get_node(mis[5])
        mis7 = get_node(mis[6])
        self.Mis1.setText(mis1[0] + " " + mis1[1])
        self.Mis21.setText(mis2[0] + " " + mis2[1])
        self.Mis22.setText(mis2[0] + " " + mis2[1])
        self.Mis31.setText(mis3[0] + " " + mis3[1])
        self.Mis32.setText(mis3[0] + " " + mis3[1])
        self.Mis33.setText(mis3[0] + " " + mis3[1])
        self.Mis41.setText(mis4[0] + " " + mis4[1])
        self.Mis42.setText(mis4[0] + " " + mis4[1])
        self.Mis43.setText(mis4[0] + " " + mis4[1])
        self.Mis51.setText(mis5[0] + " " + mis5[1])
        self.Mis52.setText(mis5[0] + " " + mis5[1])
        self.Mis53.setText(mis5[0] + " " + mis5[1])
        self.Mis61.setText(mis6[0] + " " + mis6[1])
        self.Mis62.setText(mis6[0] + " " + mis6[1])
        self.Mis7.setText(mis7[0] + " " + mis7[1])

    def set_syndicate_not_available(self) -> None:
        self.Mis1.setText("N/D")
        self.Mis21.setText("N/D")
        self.Mis22.setText("N/D")
        self.Mis31.setText("N/D")
        self.Mis32.setText("N/D")
        self.Mis33.setText("N/D")
        self.Mis41.setText("N/D")
        self.Mis42.setText("N/D")
        self.Mis43.setText("N/D")
        self.Mis51.setText("N/D")
        self.Mis52.setText("N/D")
        self.Mis53.setText("N/D")
        self.Mis61.setText("N/D")
        self.Mis62.setText("N/D")
        self.Mis7.setText("N/D")
