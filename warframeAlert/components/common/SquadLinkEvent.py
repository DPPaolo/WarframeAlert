# coding=utf-8
import json

from PyQt5 import QtWidgets

from warframeAlert.components.common.Countdown import Countdown
from warframeAlert.components.common.Event import Event
from warframeAlert.services.translationService import translate
from warframeAlert.utils import timeUtils


class SquadLinkEvent(Event):

    def __init__(self, event_id):
        super().__init__(event_id)

        self.TAWaveEndLab = QtWidgets.QLabel(translate("squadLinkEvent", "waveEnd") + ": ")
        self.TAWaveEnd = Countdown()
        self.TANextWaveInitLab = QtWidgets.QLabel(translate("squadLinkEvent", "nextWaveInit") + ": ")
        self.TANextWaveInit = Countdown()
        self.TASquadExtra = QtWidgets.QLabel("")

        self.TASquadLinkbox1 = QtWidgets.QHBoxLayout()
        self.TASquadLinkbox2 = QtWidgets.QHBoxLayout()

        self.TASquadLinkbox1.addWidget(self.TAWaveEndLab)
        self.TASquadLinkbox1.addWidget(self.TAWaveEnd.TimeLab)
        self.TASquadLinkbox1.addWidget(self.TANextWaveInitLab)
        self.TASquadLinkbox1.addWidget(self.TANextWaveInit.TimeLab)

        self.TASquadLinkbox2.addWidget(self.TASquadExtra)

        self.TADescvbox.addLayout(self.TASquadLinkbox1)
        self.TADescvbox.addLayout(self.TASquadLinkbox2)

    def set_squad_link_data(self, init, end, next_init, next_end):
        wave_init = translate("squadLinkEvent", "waveInit") + ": " + timeUtils.get_time(init[:10])
        if (next_end != 0):
            next_wave_end = translate("squadLinkEvent", "nextWaveEnd") + ": " + timeUtils.get_time(next_end[:10])
        self.TAWaveEndLab.setToolTip(wave_init)
        self.TAWaveEnd.set_tooltip(wave_init)
        self.TAWaveEnd.set_countdown(end[:10])
        self.TAWaveEnd.start()
        self.TANextWaveInitLab.setToolTip(next_wave_end)
        self.TANextWaveInit.set_tooltip(next_wave_end)
        self.TANextWaveInit.set_countdown(next_init[:10])
        self.TANextWaveInit.start()

    def set_squad_link_extra_data(self, completition_bonus, epoch_number, pause_scheduling, metadata):
        metadata = json.loads(metadata)
        extra_text = ""
        if ('progressReq' in metadata):
            extra_text += translate("squadLinkEvent", "murexNumber") + ": " + str(metadata['progressReq']) + "\t"
        if ('duration' in metadata):
            duration = timeUtils.get_alert_time(int(metadata['duration']) * 60)
            extra_text += translate("squadLinkEvent", "duration") + ": " + str(duration) + "\t"
        if ('cooldown' in metadata):
            extra_text += translate("squadLinkEvent", "cooldown") + ": " + str(metadata['cooldown']) + "m\n"
        if ('groundTiers' in metadata):
            ground_tier = metadata['groundTiers']
            extra_text += translate("squadLinkEvent", "groundTier") + ": "
            for num in range(len(ground_tier) - 1):
                extra_text += str(ground_tier[num]) + ", "
            extra_text += str(ground_tier[len(ground_tier)-1]) + "\t"
        if ('spaceTiers' in metadata):
            ground_tier = metadata['spaceTiers']
            extra_text += translate("squadLinkEvent", "spaceTier") + ": "
            for num in range(len(ground_tier) - 1):
                extra_text += str(ground_tier[num]) + ", "
            extra_text += str(ground_tier[len(ground_tier) - 1]) + "\n"

        extra_text += translate("squadLinkEvent", "epoch_number") + ": " + str(epoch_number) + "\t"
        extra_text += translate("squadLinkEvent", "completitionBonus") + ": "
        for num in range(len(completition_bonus) - 1):
            extra_text += str(completition_bonus[num]) + ", "
        extra_text += str(completition_bonus[len(completition_bonus)-1]) + "\t"
        extra_text += translate("squadLinkEvent", "pauseAutoScheduling") + ": " + pause_scheduling
        self.TASquadExtra.setText(extra_text)

    def hide(self):
        self.TAWaveEndLab.hide()
        self.TAWaveEnd.hide()
        self.TANextWaveInitLab.hide()
        self.TANextWaveInit.hide()
        self.TASquadExtra.hide()
