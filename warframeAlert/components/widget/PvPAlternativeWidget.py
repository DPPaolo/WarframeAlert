# coding=utf-8
from PyQt5 import QtWidgets, QtCore

from warframeAlert.components.common.PvPAlternativeMissionBox import PvPAlternativeMissionBox
from warframeAlert.services.translationService import translate
from warframeAlert.utils.commonUtils import remove_widget, get_last_item_with_backslash
from warframeAlert.utils.gameTranslationUtils import get_pvp_mission_type


class PvPAlternativeWidget():
    PvPAlternativeWidget = None

    def __init__(self):

        self.alerts = {'PvPAlternative': []}

        self.PvPAlternativeWidget = QtWidgets.QWidget()

        self.gridPvPAlt = QtWidgets.QGridLayout(self.PvPAlternativeWidget)
        self.NoPvPAltLab = QtWidgets.QLabel(translate("pvpAlternativeWidget", "noOtherMission"))
        self.NoPvPAltLab.setAlignment(QtCore.Qt.AlignCenter)
        self.gridPvPAlt.addWidget(self.NoPvPAltLab, 0, 0)

        self.PvPAlternativeWidget.setLayout(self.gridPvPAlt)

        self.gridPvPAlt.setAlignment(QtCore.Qt.AlignTop)

    def get_widget(self):
        return self.PvPAlternativeWidget

    def get_lenght(self):
        return len(self.alerts['PvPAlternative'])

    def parse_pvp_alternative_mission(self, data):
        self.reset_pvp_alternative()
        n_pvp_alt = len(self.alerts['PvPAlternative'])
        if (data):
            for pvp in data:
                name = get_last_item_with_backslash(pvp['TitleLoc'])
                found = 0
                for mission in self.alerts['PvPAlternative']:
                    if (mission.get_name() == name):
                        found = 1

                if (found == 0):
                    desc = pvp['DescriptionLoc']
                    disable_ammo = pvp['DisableAmmoPickups']
                    disable_energy = pvp['DisableEnergyPickups']
                    disable_energy_surge = pvp['DisableEnergySurge']
                    if ('DisableWeaponHud' in pvp):
                        disable_hud_weapon = pvp['DisableWeaponHud']
                    else:
                        disable_hud_weapon = False
                    if ('DisableWeaponSwitching' in pvp):
                        disable_change_weapon = pvp['DisableWeaponSwitching']
                    else:
                        disable_change_weapon = False
                    if ('MatchTimeOverride' in pvp):
                        time = pvp['MatchTimeOverride']
                    else:
                        time = "Standard"
                    if ('MaxPlayersOverride' in pvp):
                        player = pvp['MaxPlayersOverride']
                    else:
                        player = "Standard"
                    if ('MaxTeamCountDifferenceOverride' in pvp):
                        maxteam = pvp['MaxTeamCountDifferenceOverride']
                    else:
                        maxteam = "Standard"
                    if ('MinPlayersPerTeamOverride' in pvp):
                        minplayer = pvp['MinPlayersPerTeamOverride']
                    else:
                        minplayer = "Standard"
                    mode = get_pvp_mission_type(pvp['TargetMode'])
                    weapon = []
                    for loadout in pvp['ForcedLoadouts'][0]['WeaponOverrides']:
                        if (bool(loadout['Override'])):
                            if (loadout['Resource'] == ''):
                                weapon.append(translate("pvpAlternativeWidget", "none").upper() + "NESSUNA")
                            else:
                                weapon.append(loadout['Resource'])
                        else:
                            weapon.append(translate("pvpAlternativeWidget", "any").upper() + "QUALUNQUE")

                    temp = PvPAlternativeMissionBox(name)
                    temp.set_pvp_data_match(time, player, maxteam, minplayer, mode, desc)
                    temp.set_disabled_data(disable_ammo, disable_energy, disable_energy_surge,
                                           disable_hud_weapon, disable_change_weapon)
                    temp.set_pvp_weapon_restriction(weapon[0], weapon[2], weapon[1], weapon[3])

                    self.alerts['PvPAlternative'].append(temp)
                    del temp

        self.add_pvp_alternative(n_pvp_alt)

    def add_pvp_alternative(self, n_pvp_alt):
        for i in range(n_pvp_alt, len(self.alerts['PvPAlternative'])):
            self.gridPvPAlt.addLayout(self.alerts['PvPAlternative'][i].PvPAltBox, self.gridPvPAlt.count(), 0)

        if (len(self.alerts['PvPAlternative']) > 0):
            self.NoPvPAltLab.hide()

    def reset_pvp_alternative(self):
        self.NoPvPAltLab.show()
        canc = []
        for i in range(0, len(self.alerts['PvPAlternative'])):
            canc.append(i)
        i = len(canc)
        while i > 0:
            self.alerts['PvPAlternative'][canc[i - 1]].hide()
            remove_widget(self.alerts['PvPAlternative'][canc[i - 1]].PvPAltBox)
            del self.alerts['PvPAlternative'][canc[i - 1]]
            i -= 1

    def pvp_alternative_mission_not_available(self):
        self.NoPvPAltLab.show()
        self.reset_pvp_alternative()
