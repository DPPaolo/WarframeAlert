# coding=utf-8
from PyQt5 import QtWidgets, QtCore, QtGui

from warframeAlert.components.common.Countdown import Countdown
from warframeAlert.services.translationService import translate
from warframeAlert.utils import timeUtils
from warframeAlert.utils.commonUtils import bool_to_yes_no
from warframeAlert.utils.logUtils import LogHandler


class GeneralInfoWidget():
    generalInfoWidget = None

    def __init__(self):
        self.generalInfoWidget = QtWidgets.QWidget()

        font = QtGui.QFont()
        font.setBold(True)

        self.EarthTime = Countdown()
        self.EarthStatus = QtWidgets.QLabel(translate("generalWidget", "earthTime") + ": N/D")
        self.Version = QtWidgets.QLabel(translate("generalWidget", "fileVersion") + ": N/D")
        self.MobVersion = QtWidgets.QLabel(translate("generalWidget", "mobileFileVersion") + ": N/D")
        self.ForceLogoutVersion = QtWidgets.QLabel(translate("generalWidget", "forceLogoutVersion") + ": N/D")
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
        self.gridOther.addWidget(self.WorldSeedLab, 3, 0)
        self.gridOther.addWidget(self.WorldSeed, 4, 0, 1, 2)
        self.gridOther.addWidget(self.PrimeAccessLab, 5, 0)
        self.gridOther.addWidget(self.PrimeAccess, 5, 1)
        self.gridOther.addWidget(self.PrimeVaultLab, 6, 0)
        self.gridOther.addWidget(self.PrimeVault, 6, 1)
        self.gridOther.addWidget(self.FeaturedDojoLab, 7, 0)
        self.gridOther.addWidget(self.FeaturedDojo, 7, 1)

        self.generalInfoWidget.setLayout(self.gridOther)
        self.gridOther.setAlignment(QtCore.Qt.AlignTop)
        self.calculate_earth_time()

    def get_widget(self):
        return self.generalInfoWidget

    def calculate_earth_time(self):
        earth_time, day = timeUtils.get_earth_time()
        if (day):
            self.EarthStatus.setText(translate("generalWidget", "earthTimeDay"))
            self.EarthTime.set_name(translate("generalWidget", "timeToNight") + ": ")
        else:
            self.EarthStatus.setText(translate("generalWidget", "earthTimeNight"))
            self.EarthTime.set_name(translate("generalWidget", "timeToDay") + ": ")

        self.EarthTime.set_countdown(int(timeUtils.get_local_time()) + earth_time)
        self.EarthTime.start()

    def set_other_datas(self, version, mob_version, world_seed, force_logout):
        version_text = translate("generalWidget", "fileVersion") + ": " + str(version)
        mobile_version_text = translate("generalWidget", "mobileFileVersion") + ": " + str(mob_version)
        force_logout_text = translate("generalWidget", "forceLogoutVersion") + ": " + bool_to_yes_no(force_logout)
        self.Version.setText(version_text)
        self.MobVersion.setText(mobile_version_text)
        self.ForceLogoutVersion.setText(force_logout_text)
        w_seed = ""
        len_world_seed = len(world_seed)
        j = 0
        while (j < len_world_seed):
            w_seed = w_seed + world_seed[j:j+100] + "\n"
            j += 100
        w_seed = w_seed + world_seed[j:]
        self.WorldSeed.setText(w_seed)

    def parse_featured_dojo(self, data):
        guild = ["", "", "", "", ""]
        if (data):
            for dojo in data:
                dojo_id = dojo['_id']['$oid']
                try:
                    alliance_id = dojo['AllianceId']['$oid']
                except KeyError:
                    alliance_id = dojo_id + " (" + translate("generalWidget", "noAlliance") + ")"
                tier = int(dojo['Tier'])
                name = dojo['Name']
                guild[tier - 1] = (name, dojo_id, alliance_id)
            self.set_featured_dojo(guild)

    def set_featured_dojo(self, dojo):
        data = translate("generalWidget", "tier1") + ": " + dojo[0][0] + "\n"
        data += translate("generalWidget", "tier2") + ": " + dojo[1][0] + "\n"
        data += translate("generalWidget", "tier3") + ": " + dojo[2][0] + "\n"
        data += translate("generalWidget", "tier4") + ": " + dojo[3][0] + "\n"
        data += translate("generalWidget", "tier5") + ": " + dojo[4][0]
        tooltip = translate("generalWidget", "tier1Id") + ": " + dojo[0][1]
        tooltip += " (" + translate("generalWidget", "guildAllianceId") + " " + dojo[0][2] + ")\n"
        tooltip += translate("generalWidget", "tier2Id") + ": " + dojo[1][1]
        tooltip += " (" + translate("generalWidget", "guildAllianceId") + " " + dojo[1][2] + ")\n"
        tooltip += translate("generalWidget", "tier3Id") + ": " + dojo[2][1]
        tooltip += " (" + translate("generalWidget", "guildAllianceId") + " " + dojo[2][2] + ")\n"
        tooltip += translate("generalWidget", "tier4Id") + ": " + dojo[3][1]
        tooltip += " (" + translate("generalWidget", "guildAllianceId") + " " + dojo[3][2] + ")\n"
        tooltip += translate("generalWidget", "tier5Id") + ": " + dojo[4][1]
        tooltip += " (" + translate("generalWidget", "guildAllianceId") + " " + dojo[4][2] + ")"
        self.FeaturedDojo.setText(data)
        self.FeaturedDojo.setToolTip(tooltip)

    def reset_featured_dojo(self):
        self.FeaturedDojo.setText("N/D")

    def parse_prime_access(self, prime, vault_available):
        self.PrimeVault.setText("")
        if (prime['State'] == "PRIME1"):
            state = translate("generalWidget", "primeState1")  # White Skin?
        elif (prime['State'] == "PRIME2"):
            state = translate("generalWidget", "primeState2")  # Dark Skin?
        else:
            state = prime['State']
            LogHandler.debug(translate("generalWidget", "primeStateUnknown") + state)
            print(translate("generalWidget", "primeStateUnknown") + state)
        self.PrimeAccess.setText(state)
        if (len(vault_available) > 5):
            print(translate("generalWidget", "morePrimeVault"))
        data = translate("generalWidget", "vault0") + ": " + str(vault_available[0]) + "\n"
        data += translate("generalWidget", "vault1") + ": " + str(vault_available[1]) + "\n"
        data += translate("generalWidget", "vault2") + ": " + str(vault_available[2]) + "\n"
        data += translate("generalWidget", "vault3") + ": " + str(vault_available[3]) + "\n"
        data += translate("generalWidget", "vault4") + ": " + str(vault_available[4])
        # data += translate("generalWidget", "vault5") + ": " + str(vault_available[5]) # Vault Nova e Mag Prime
        self.PrimeVault.setText(data)

    def reset_prime_access(self):
        self.PrimeAccess.setText("N/D")
        self.PrimeVault.setText("N/D")
