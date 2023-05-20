# coding=utf-8
from PyQt6 import QtWidgets, QtCore, QtGui

from warframeAlert.components.common.Countdown import Countdown
from warframeAlert.constants.warframeTypes import FeaturedGuilds, PrimeAccessAvailability, PrimeVaultAvailabilities
from warframeAlert.services.translationService import translate
from warframeAlert.utils import timeUtils
from warframeAlert.utils.commonUtils import bool_to_yes_no
from warframeAlert.utils.gameTranslationUtils import get_node
from warframeAlert.utils.logUtils import LogHandler
from warframeAlert.utils.stringUtils import divide_message


class GeneralInfoWidget():
    generalInfoWidget = None

    def __init__(self) -> None:
        self.generalInfoWidget = QtWidgets.QWidget()

        font = QtGui.QFont()
        font.setBold(True)

        self.EarthTime = Countdown()
        self.EarthStatus = QtWidgets.QLabel(translate("generalWidget", "earthTime") + ": N/D")
        self.Version = QtWidgets.QLabel(translate("generalWidget", "fileVersion") + ": N/D")
        self.MobVersion = QtWidgets.QLabel(translate("generalWidget", "mobileFileVersion") + ": N/D")
        self.ForceLogoutVersion = QtWidgets.QLabel(translate("generalWidget", "forceLogoutVersion") + ": N/D")
        self.DTLDSActivated = QtWidgets.QLabel(translate("generalWidget", "DTLSActivated") + ": N/D")
        self.SentientAnomalies = QtWidgets.QLabel(translate("generalWidget", "sentientAnomalies") + ": N/D")
        self.WorldSeedLab = QtWidgets.QLabel(translate("generalWidget", "worldSeed") + ": ")
        self.WorldSeed = QtWidgets.QLabel("N/D")
        self.PrimeAccessLab = QtWidgets.QLabel(translate("generalWidget", "primeAccessState") + ": ")
        self.PrimeAccess = QtWidgets.QLabel("N/D")
        self.PrimeVaultLab = QtWidgets.QLabel(translate("generalWidget", "primeVaultState") + ": ")
        self.PrimeVault = QtWidgets.QLabel("N/D")
        self.FeaturedDojoLab = QtWidgets.QLabel(translate("generalWidget", "featuredDojo") + ": ")
        self.FeaturedDojo = QtWidgets.QLabel("N/D")

        self.EarthTime.TimeOut.connect(self.calculate_earth_time)

        self.EarthTime.TimeLab.setFont(font)
        self.gridOther = QtWidgets.QGridLayout(self.generalInfoWidget)

        self.gridOther.addWidget(self.EarthStatus, 0, 0)
        self.gridOther.addWidget(self.EarthTime.TimeLab, 0, 1)
        self.gridOther.addWidget(self.Version, 1, 0)
        self.gridOther.addWidget(self.MobVersion, 1, 1)
        self.gridOther.addWidget(self.ForceLogoutVersion, 2, 0)
        self.gridOther.addWidget(self.DTLDSActivated, 2, 1)
        self.gridOther.addWidget(self.SentientAnomalies, 3, 0)
        self.gridOther.addWidget(self.WorldSeedLab, 4, 0)
        self.gridOther.addWidget(self.WorldSeed, 5, 0, 1, 2)
        self.gridOther.addWidget(self.PrimeAccessLab, 6, 0)
        self.gridOther.addWidget(self.PrimeAccess, 6, 1)
        self.gridOther.addWidget(self.PrimeVaultLab, 7, 0)
        self.gridOther.addWidget(self.PrimeVault, 7, 1)
        self.gridOther.addWidget(self.FeaturedDojoLab, 8, 0)
        self.gridOther.addWidget(self.FeaturedDojo, 8, 1)

        self.generalInfoWidget.setLayout(self.gridOther)
        self.gridOther.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.calculate_earth_time()

    def get_widget(self) -> QtWidgets.QWidget:
        return self.generalInfoWidget

    def calculate_earth_time(self) -> None:
        earth_time, day = timeUtils.get_earth_time()
        if (day):
            self.EarthStatus.setText(translate("generalWidget", "earthTimeDay"))
            self.EarthTime.set_name(translate("generalWidget", "timeToNight") + ": ")
        else:
            self.EarthStatus.setText(translate("generalWidget", "earthTimeNight"))
            self.EarthTime.set_name(translate("generalWidget", "timeToDay") + ": ")

        self.EarthTime.set_countdown(int(timeUtils.get_local_time()) + earth_time)
        self.EarthTime.start()

    def set_other_datas(self, version: int, mob_version: str, world_seed: str,
                        force_logout: int, dtls: bool, sentient_anomalies: str) -> None:
        version_text = translate("generalWidget", "fileVersion") + ": " + str(version)
        mobile_version_text = translate("generalWidget", "mobileFileVersion") + ": " + str(mob_version)
        force_logout_text = translate("generalWidget", "forceLogoutVersion") + ": " + bool_to_yes_no(force_logout)
        dtls_active_text = translate("generalWidget", "DTLSActivated") + ": " + bool_to_yes_no(dtls)
        if (len(sentient_anomalies) > 2):
            sentient_anomalies_node = "CrewBattleNode" + sentient_anomalies.split(":")[1].split("}")[0]
        else:
            sentient_anomalies_node = "/Lotus/Types/Keys/SortieBossKeyPhorid"
        anomalies_text = translate("generalWidget", "sentientAnomalies") + ": " + get_node(sentient_anomalies_node)[0]
        self.Version.setText(version_text)
        self.MobVersion.setText(mobile_version_text)
        self.ForceLogoutVersion.setText(force_logout_text)
        self.DTLDSActivated.setText(dtls_active_text)
        self.WorldSeed.setText(divide_message(world_seed, 100))
        self.SentientAnomalies.setText(anomalies_text)

    def parse_featured_dojo(self, data: FeaturedGuilds) -> None:
        guild = ["", "", "", "", ""]
        if (data):
            for dojo in data:
                dojo_id = dojo['_id']['$oid']
                alliance_id = None
                if ('AllianceId' in dojo):
                    alliance_id = dojo['AllianceId']['$oid']
                tier = int(dojo['Tier'])
                name = dojo['Name']
                emblem_active = dojo['Emblem']
                guild[tier - 1] = (name, dojo_id, alliance_id, emblem_active)
            self.set_featured_dojo(guild)

    def set_featured_dojo(self, dojo:  list[tuple[str, str, str, bool]]) -> None:
        data = tooltip = ""

        if (dojo[0] != ''):
            data += translate("generalWidget", "tier1") + ": " + dojo[0][0] + "\n"
            tooltip += translate("generalWidget", "tier1Id") + ": " + dojo[0][1]
            tooltip += build_dojo_tooltip_line(dojo[0][1], dojo[0][2], dojo[0][3])

        if (dojo[1] != ''):
            data += translate("generalWidget", "tier2") + ": " + dojo[1][0] + "\n"
            tooltip += translate("generalWidget", "tier2Id") + ": " + dojo[1][1]
            tooltip += build_dojo_tooltip_line(dojo[1][1], dojo[1][2], dojo[1][3])

        if (dojo[2] != ''):
            data += translate("generalWidget", "tier3") + ": " + dojo[2][0] + "\n"
            tooltip += translate("generalWidget", "tier3Id") + ": " + dojo[2][1]
            tooltip += build_dojo_tooltip_line(dojo[2][1], dojo[2][2], dojo[2][3])

        if (dojo[3] != ''):
            data += translate("generalWidget", "tier4") + ": " + dojo[3][0] + "\n"
            tooltip += translate("generalWidget", "tier4Id") + ": " + dojo[3][1]
            tooltip += build_dojo_tooltip_line(dojo[3][1], dojo[3][2], dojo[3][3])

        if (dojo[4] != ''):
            data += translate("generalWidget", "tier5") + ": " + dojo[4][0]
            tooltip += translate("generalWidget", "tier5Id") + ": " + dojo[4][1]
            tooltip += build_dojo_tooltip_line(dojo[4][1], dojo[4][2], dojo[4][3])

        self.FeaturedDojo.setText(data)
        self.FeaturedDojo.setToolTip(tooltip)

    def reset_featured_dojo(self) -> None:
        self.FeaturedDojo.setText("N/D")

    def parse_prime_access(self, prime: PrimeAccessAvailability, vault_available: PrimeVaultAvailabilities) -> None:
        self.PrimeVault.setText("")
        if (prime['State'] == "PRIME1"):
            state = translate("generalWidget", "primeState1")  # White Skin?
        elif (prime['State'] == "PRIME2"):
            state = translate("generalWidget", "primeState2")  # Dark Skin?
        elif (prime['State'] == "COMING_SOON"):
            state = translate("generalWidget", "comingSoon")
        else:
            state = prime['State']
            LogHandler.debug(translate("generalWidget", "primeStateUnknown") + " " + state)
        self.PrimeAccess.setText(state)
        if (len(vault_available) > 5):
            LogHandler.debug(translate("generalWidget", "morePrimeVault"))
        data = translate("generalWidget", "vault0") + ": " + str(vault_available[0]) + "\n"
        data += translate("generalWidget", "vault1") + ": " + str(vault_available[1]) + "\n"
        data += translate("generalWidget", "vault2") + ": " + str(vault_available[2]) + "\n"
        data += translate("generalWidget", "vault3") + ": " + str(vault_available[3]) + "\n"
        data += translate("generalWidget", "vault4") + ": " + str(vault_available[4])
        # data += translate("generalWidget", "vault5") + ": " + str(vault_available[5]) # Vault Nova e Mag Prime
        self.PrimeVault.setText(data)

    def reset_prime_access(self) -> None:
        self.PrimeAccess.setText("N/D")
        self.PrimeVault.setText("N/D")


def build_dojo_tooltip_line(dojo_id: str, alliance_id: str, has_emblem: bool) -> str:
    tooltip = " ("
    if (alliance_id is not None):
        tooltip = " (" + translate("generalWidget", "guildAllianceId") + " " + alliance_id + ", "
    else:
        tooltip += dojo_id + " " + translate("generalWidget", "noAlliance") + ", "
    tooltip += translate("generalWidget", "hasEmblem") + ": " + bool_to_yes_no(has_emblem) + ")\n"
    return tooltip
