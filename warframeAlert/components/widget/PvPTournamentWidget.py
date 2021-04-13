# coding=utf-8
from PyQt5 import QtWidgets, QtCore

from warframeAlert.services.translationService import translate
from warframeAlert.utils.commonUtils import remove_widget


class PvPTournamentWidget():
    TournamentPvPWidget = None

    def __init__(self):

        self.alerts = {'PvPTournament': []}

        self.TournamentPvPWidget = QtWidgets.QWidget()

        self.NoPvPTourLab = QtWidgets.QLabel(translate("pvpTournamentWidget", "noTournament"))
        self.NoPvPTourLab.setAlignment(QtCore.Qt.AlignCenter)
        self.gridPvPTour = QtWidgets.QGridLayout(self.TournamentPvPWidget)
        self.gridPvPTour.addWidget(self.NoPvPTourLab, 0, 0)

        self.TournamentPvPWidget.setLayout(self.gridPvPTour)

        self.gridPvPTour.setAlignment(QtCore.Qt.AlignTop)

    def get_widget(self):
        return self.TournamentPvPWidget

    def get_lenght(self):
        return len(self.alerts['PvPTournament'])

    def parse_pvp_tournament(self, data):
        self.reset_pvp_tournament()

        n_pvp_t = len(self.alerts['PvPTournament'])

        if (data):
            self.add_pvp_tournament(n_pvp_t)

    def add_pvp_tournament(self, n_pvp_t):
        for i in range(n_pvp_t, len(self.alerts['PvPTournament'])):
            self.gridPvPTour.addLayout(self.alerts['PvPTournament'][i].PvPAltBox, self.gridPvPTour.count(), 0)

        if (len(self.alerts['PvPTournament']) > 0):
            self.NoPvPTourLab.hide()

    def reset_pvp_tournament(self):
        self.NoPvPTourLab.show()
        canc = []
        for i in range(0, len(self.alerts['PvPTournament'])):
            if (self.alerts['PvPTournament'][i].is_expired()):
                canc.append(i)
        i = len(canc)
        while i > 0:
            self.alerts['PvPTournament'][canc[i - 1]].hide()
            remove_widget(self.alerts['PvPTournament'][canc[i - 1]].PvPBox)
            del self.alerts['PvPTournament'][canc[i - 1]]
            i -= 1

    def pvp_tournament_not_available(self):
        self.NoPvPTourLab.show()
        self.reset_pvp_tournament()
