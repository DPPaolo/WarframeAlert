# coding=utf-8
from PyQt5 import QtWidgets, QtCore

from warframeAlert.components.common.TwitchBox import TwitchBox
from warframeAlert.services.translationService import translate
from warframeAlert.utils import timeUtils
from warframeAlert.utils.commonUtils import remove_widget


class TwitchPromoWidget():
    twitchPromoWidget = None
    n_twitch_promo = 0

    def __init__(self):
        self.data = {'TwitchPromos': []}

        self.twitchPromoWidget = QtWidgets.QWidget()

        self.gridTwitch = QtWidgets.QGridLayout(self.twitchPromoWidget)

        self.NoTwitchLab = QtWidgets.QLabel(translate("twitchPromoWidget", "no_Twich_Promo"))

        self.gridTwitch.addWidget(self.NoTwitchLab, 0, 0)

        self.NoTwitchLab.setAlignment(QtCore.Qt.AlignCenter)
        self.gridTwitch.setAlignment(QtCore.Qt.AlignTop)

        self.twitchPromoWidget.setLayout(self.gridTwitch)

    def get_widget(self):
        return self.twitchPromoWidget

    def parse_twitch_promo(self, twitch_data):
        self.reset_twitch_promo()
        if (twitch_data):
            n_promo = len(self.data['TwitchPromos'])
            for promo in twitch_data:
                streams = []
                init = timeUtils.get_time(promo['startDate']['$date']['$numberLong'])
                end = promo['endDate']['$date']['$numberLong']

                achievement = promo['achievement']
                agent_types = promo['agentTypes']
                spawn = promo['spawnChance']
                cooldown = promo['cooldown']

                remaining_time = int(end[:10]) - int(timeUtils.get_local_time())
                if (remaining_time > 0):
                    found = 0

                    for twitch in self.data['TwitchPromos']:
                        if (twitch.get_iniz() == init):
                            found = 1

                    if (found == 0):
                        twitch_type = promo['type']
                        if ('streamers' in promo):
                            for stream in promo['streamers']:
                                streams.append(stream)
                        temp = TwitchBox()
                        temp.set_twitch_data(init, end, twitch_type, agent_types, spawn, cooldown, achievement, streams)
                        self.data['TwitchPromos'].append(temp)
                        del temp

            self.add_twich_promo(n_promo)

    def add_twich_promo(self, n_twitch_promo):
        for i in range(n_twitch_promo, len(self.data['TwitchPromos'])):
            self.gridTwitch.addLayout(self.data['TwitchPromos'][i].TwitchBox, self.gridTwitch.count(), 0)
            self.n_twitch_promo += 1

        if (len(self.data['TwitchPromos']) > 0):
            self.NoTwitchLab.hide()
            LogHandler.debug(translate("twitchPromoWidget", "active_twich_promo"))

    def reset_twitch_promo(self):
        self.NoTwitchLab.show()
        canc = []
        for i in range(0, len(self.data['TwitchPromos'])):
            if (self.data['TwitchPromos'][i].is_expired()):
                canc.append(i)
        i = len(canc)
        while i > 0:
            self.data['TwitchPromos'][canc[i-1]].hide()
            remove_widget(self.data['TwitchPromos'][canc[i-1]].TwitchBox)
            del self.data['TwitchPromos'][canc[i-1]]
            i -= 1
