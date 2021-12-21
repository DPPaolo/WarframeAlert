# coding=utf-8
from typing import List

from PyQt6 import QtWidgets

from warframeAlert.components.common.Countdown import Countdown
from warframeAlert.components.common.Spoiler import Spoiler
from warframeAlert.components.common.VaultItemBox import VaultItemBox
from warframeAlert.components.common.VaultScheduleBox import VaultScheduleBox
from warframeAlert.constants.warframeTypes import PrimeVaultManifestInfo, PrimeVaultScheduleInfo
from warframeAlert.services.translationService import translate
from warframeAlert.utils import timeUtils
from warframeAlert.utils.commonUtils import get_last_item_with_backslash


class EventVaultTrader():

    def __init__(self, event_id: str) -> None:
        self.event_id = event_id

        self.EventNameLab = QtWidgets.QLabel(translate("event", "event") + ":")
        self.EventName = QtWidgets.QLabel("N/D")
        self.EventInitialInitLab = QtWidgets.QLabel(translate("eventVault", "initialInit"))
        self.EventInitialInit = QtWidgets.QLabel("N/D")

        self.EventInitLab = QtWidgets.QLabel(translate("event", "init"))
        self.EventInit = QtWidgets.QLabel("N/D")
        self.EventEndLab = QtWidgets.QLabel(translate("event", "end"))
        self.EventEnd = Countdown()

        self.EventSuccessLab = QtWidgets.QLabel(translate("event", "eventCompleted") + ":")
        self.EventSuccess = QtWidgets.QLabel("N/D")
        self.EventRegionLab = QtWidgets.QLabel(translate("eventVault", "node") + ":")
        self.EventRegion = QtWidgets.QLabel("N/D")

        self.EventPhaseLab = QtWidgets.QLabel(translate("eventVault", "phase") + ":")
        self.EventPhase = QtWidgets.QLabel("N/D")
        self.EventParamsLab = QtWidgets.QLabel(translate("eventVault", "params") + ":")
        self.EventParams = QtWidgets.QLabel("N/D")

        self.manifestSpoiler = Spoiler(translate("eventVault", "manifest"))
        self.manifestSpoilerBox = QtWidgets.QVBoxLayout()
        self.manifestSpoiler.set_content_layout(self.manifestSpoilerBox)

        self.scheduleSpoiler = Spoiler(translate("eventVault", "schedule"))
        self.scheduleSpoilerBox = QtWidgets.QVBoxLayout()
        self.scheduleSpoiler.set_content_layout(self.scheduleSpoilerBox)

        self.TAInfoBox = QtWidgets.QVBoxLayout()

        self.TAEventBox = QtWidgets.QHBoxLayout()

        self.TADescBox1 = QtWidgets.QHBoxLayout()
        self.TADescBox2 = QtWidgets.QHBoxLayout()
        self.TADescBox3 = QtWidgets.QHBoxLayout()
        self.TADescBox4 = QtWidgets.QHBoxLayout()
        self.TADescBox5 = QtWidgets.QHBoxLayout()

        self.TADescBox1.addWidget(self.EventNameLab)
        self.TADescBox1.addWidget(self.EventName)
        self.TADescBox1.addWidget(self.EventInitialInitLab)
        self.TADescBox1.addWidget(self.EventInitialInit)

        self.TADescBox2.addWidget(self.EventInitLab)
        self.TADescBox2.addWidget(self.EventInit)
        self.TADescBox2.addWidget(self.EventEndLab)
        self.TADescBox2.addWidget(self.EventEnd.TimeLab)

        self.TADescBox3.addWidget(self.EventPhaseLab)
        self.TADescBox3.addWidget(self.EventPhase)
        self.TADescBox3.addWidget(self.EventParamsLab)
        self.TADescBox3.addWidget(self.EventParams)

        self.TADescBox4.addWidget(self.EventRegionLab)
        self.TADescBox4.addWidget(self.EventRegion)
        self.TADescBox4.addWidget(self.EventSuccessLab)
        self.TADescBox4.addWidget(self.EventSuccess)

        self.TAInfoBox.addLayout(self.TADescBox1)
        self.TAInfoBox.addLayout(self.TADescBox2)
        self.TAInfoBox.addLayout(self.TADescBox3)
        self.TAInfoBox.addLayout(self.TADescBox4)
        self.TAInfoBox.addWidget(self.scheduleSpoiler)
        self.TAInfoBox.addWidget(self.manifestSpoiler)

        self.TAEventBox.addLayout(self.TAInfoBox)

    def set_event_info(self, init: str, end: int, initial_init: str, completed: str, node: str,
                       params: str, phase: int) -> None:
        self.EventName.setText(translate("eventVault", "eventVaultName"))
        self.EventInit.setText(init)
        self.EventInitialInit.setText(initial_init)
        self.EventEnd.set_countdown(end[:10])
        self.EventSuccess.setText(completed)
        self.EventRegion.setText(node)
        self.EventEnd.start()
        self.EventPhase.setText(str(phase))
        self.EventParams.setText(params)

    def set_manifest_data(self, manifest: List[PrimeVaultManifestInfo]) -> None:
        for elem in manifest:
            item = get_last_item_with_backslash(elem['ItemType'])
            aya = elem['RegularPrice'] if ('RegularPrice' in elem) else 0
            regal_aya = elem['PrimePrice'] if ('PrimePrice' in elem) else 0

            vault_item = VaultItemBox(item, aya, regal_aya)
            self.manifestSpoilerBox.addLayout(vault_item.VaultItemLayoutBox)

        self.manifestSpoiler.set_content_layout(self.manifestSpoilerBox)

    def set_schedule_data(self, schedule: List[PrimeVaultScheduleInfo]) -> None:
        for elem in schedule:
            item = get_last_item_with_backslash(elem['FeaturedItem'])
            end = elem['Expiry']['$date']['$numberLong']

            vault_schedule = VaultScheduleBox(item, end)
            self.scheduleSpoilerBox.addLayout(vault_schedule.ScheduleBox)

        self.scheduleSpoiler.set_content_layout(self.scheduleSpoilerBox)

    def get_event_id(self) -> str:
        return self.event_id

    def is_expired(self) -> bool:
        return (int(self.EventEnd.get_time()) - int(timeUtils.get_local_time())) < 0

    def get_title(self) -> str:
        return self.EventName.text()

    def hide(self) -> None:
        self.EventNameLab.hide()
        self.EventName.hide()
        self.EventInitLab.hide()
        self.EventInit.hide()
        self.EventInitialInitLab.hide()
        self.EventInitialInit.hide()
        self.EventEndLab.hide()
        self.EventEnd.hide()
        self.EventParamsLab.hide()
        self.EventParams.hide()
        self.EventPhaseLab.hide()
        self.EventPhase.hide()
        self.EventRegionLab.hide()
        self.EventRegion.hide()
        self.EventSuccessLab.hide()
        self.EventSuccess.hide()
        self.scheduleSpoiler.hide()
        self.manifestSpoiler.hide()
