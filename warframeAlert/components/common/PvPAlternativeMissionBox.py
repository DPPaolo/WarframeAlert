# coding=utf-8
from PyQt6 import QtCore, QtWidgets, QtGui

from warframeAlert.components.common.EmptySpace import EmptySpace
from warframeAlert.services.translationService import translate
from warframeAlert.utils.gameTranslationUtils import get_pvp_alt_desc, get_item_name


class PvPAlternativeMissionBox():

    def __init__(self, name: str) -> None:
        self.Font = QtGui.QFont()
        self.Font.setBold(True)

        self.PvPAltName = QtWidgets.QLabel(name)
        self.PvPAltMode = QtWidgets.QLabel(translate("pvpAlternativeMissionBox", "modality") + ": N/D")
        self.PvPAltName.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.PvPAltMode.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.PvPAltName.setFont(self.Font)
        self.PvPAltMode.setFont(self.Font)
        self.PvPAltDesc = QtWidgets.QLabel("")
        self.PvPAltDesc.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.PvPAltDisAmmo = QtWidgets.QLabel(translate("pvpAlternativeMissionBox", "ammoPickup") + ": N/D")
        self.PvPAltDisEnergy = QtWidgets.QLabel(translate("pvpAlternativeMissionBox", "energyPickup") + ": N/D")
        self.PvPAltDisEnergySurge = QtWidgets.QLabel(translate("pvpAlternativeMissionBox", "energySurge") + ": N/D")
        self.PvPAltDisHUDWeapon = QtWidgets.QLabel(translate("pvpAlternativeMissionBox", "weaponHUD") + ": N/D")
        self.PvPAltDisChangeWeapon = QtWidgets.QLabel(translate("pvpAlternativeMissionBox", "weaponSwap") + ": N/D")
        self.PvPAltTime = QtWidgets.QLabel(translate("pvpAlternativeMissionBox", "matchDuration") + ": N/D")
        self.PvPAltPlayer = QtWidgets.QLabel(translate("pvpAlternativeMissionBox", "maxPlayer") + ": N/D")
        self.PvPAltMaxSquad = QtWidgets.QLabel(translate("pvpAlternativeMissionBox", "maxDiffSquadPlayer") + ": N/D")
        self.PvPAltMinPlayer = QtWidgets.QLabel(translate("pvpAlternativeMissionBox", "minSquadPlayer") + ": N/D")

        self.PvPAltWarframeLab = QtWidgets.QLabel(translate("pvpAlternativeMissionBox", "warframePermitted"))
        self.PvPAltWarframe = QtWidgets.QLabel("N/D")
        self.PvPAltPrimaryLab = QtWidgets.QLabel(translate("pvpAlternativeMissionBox", "primaryWeaponPermitted"))
        self.PvPAltPrimary = QtWidgets.QLabel("N/D")
        self.PvPAltSecondaryLab = QtWidgets.QLabel(translate("pvpAlternativeMissionBox", "secondaryWeaponPermitted"))
        self.PvPAltSecondary = QtWidgets.QLabel("N/D")
        self.PvPAltMeleeLab = QtWidgets.QLabel(translate("pvpAlternativeMissionBox", "meleePermitted"))
        self.PvPAltMelee = QtWidgets.QLabel("N/D")

        self.PvPAltPrimaryLab.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.PvPAltPrimary.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.PvPAltSecondaryLab.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.PvPAltSecondary.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.PvPAltMeleeLab.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.PvPAltMelee.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.PvPAltWarframeLab.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.PvPAltWarframe.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.PvPAltBox0 = QtWidgets.QHBoxLayout()
        self.PvPAltBox1 = QtWidgets.QHBoxLayout()
        self.PvPAltBox2 = QtWidgets.QHBoxLayout()
        self.PvPAltBox3 = QtWidgets.QHBoxLayout()
        self.PvPAltBox4 = QtWidgets.QHBoxLayout()
        self.PvPAltBox5 = QtWidgets.QHBoxLayout()
        self.PvPAltBox6 = QtWidgets.QHBoxLayout()
        self.PvPAltBox7 = QtWidgets.QHBoxLayout()

        self.PvPAltBox = QtWidgets.QVBoxLayout()

        self.PvPAltBox0.addWidget(self.PvPAltName)
        self.PvPAltBox0.addWidget(self.PvPAltMode)

        self.PvPAltBox1.addWidget(self.PvPAltDisAmmo)
        self.PvPAltBox1.addWidget(self.PvPAltDisEnergy)
        self.PvPAltBox1.addWidget(self.PvPAltDisEnergySurge)

        self.PvPAltBox2.addWidget(self.PvPAltDisHUDWeapon)
        self.PvPAltBox2.addWidget(self.PvPAltDisChangeWeapon)
        self.PvPAltBox2.addWidget(self.PvPAltTime)

        self.PvPAltBox3.addWidget(self.PvPAltPlayer)
        self.PvPAltBox3.addWidget(self.PvPAltMaxSquad)
        self.PvPAltBox3.addWidget(self.PvPAltMinPlayer)

        self.PvPAltBox4.addWidget(self.PvPAltWarframeLab)
        self.PvPAltBox4.addWidget(self.PvPAltWarframe)
        self.PvPAltBox5.addWidget(self.PvPAltPrimaryLab)
        self.PvPAltBox5.addWidget(self.PvPAltPrimary)
        self.PvPAltBox6.addWidget(self.PvPAltSecondaryLab)
        self.PvPAltBox6.addWidget(self.PvPAltSecondary)
        self.PvPAltBox7.addWidget(self.PvPAltMeleeLab)
        self.PvPAltBox7.addWidget(self.PvPAltMelee)

        self.PvPAltBox.addLayout(self.PvPAltBox0)
        self.PvPAltBox.addWidget(self.PvPAltDesc)
        self.PvPAltBox.addWidget(EmptySpace().SpaceBox)
        self.PvPAltBox.addLayout(self.PvPAltBox1)
        self.PvPAltBox.addLayout(self.PvPAltBox2)
        self.PvPAltBox.addLayout(self.PvPAltBox3)
        self.PvPAltBox.addWidget(EmptySpace().SpaceBox)
        self.PvPAltBox.addLayout(self.PvPAltBox4)
        self.PvPAltBox.addLayout(self.PvPAltBox5)
        self.PvPAltBox.addLayout(self.PvPAltBox6)
        self.PvPAltBox.addLayout(self.PvPAltBox7)

    def get_name(self) -> str:
        return self.PvPAltName.text()

    def set_disabled_data(self, disable_ammo: bool, disable_energy: bool, disable_energy_surge: bool,
                          disable_hud: bool, disable_weapon_swap: bool) -> None:
        if (not disable_ammo):
            self.PvPAltDisAmmo.setText(translate("pvpAlternativeMissionBox", "ammoPickup") + ": "
                                       + translate("pvpAlternativeMissionBox", "enabledF"))
        else:
            self.PvPAltDisAmmo.setText(translate("pvpAlternativeMissionBox", "ammoPickup") + ": "
                                       + translate("pvpAlternativeMissionBox", "disabledF"))
        if (not disable_energy):
            self.PvPAltDisEnergy.setText(translate("pvpAlternativeMissionBox", "energyPickup") + ": "
                                         + translate("pvpAlternativeMissionBox", "enabledF"))
        else:
            self.PvPAltDisEnergy.setText(translate("pvpAlternativeMissionBox", "energyPickup") + ": "
                                         + translate("pvpAlternativeMissionBox", "disabledF"))
        if (not disable_energy_surge):
            self.PvPAltDisEnergySurge.setText(translate("pvpAlternativeMissionBox", "energySurge") + ": "
                                              + translate("pvpAlternativeMissionBox", "enabledF"))
        else:
            self.PvPAltDisEnergySurge.setText(translate("pvpAlternativeMissionBox", "energySurge") + ": "
                                              + translate("pvpAlternativeMissionBox", "disabledF"))
        if (not disable_hud):
            self.PvPAltDisHUDWeapon.setText(translate("pvpAlternativeMissionBox", "weaponHUD") + ": "
                                            + translate("pvpAlternativeMissionBox", "enabledM"))
        else:
            self.PvPAltDisHUDWeapon.setText(translate("pvpAlternativeMissionBox", "weaponHUD") + ": "
                                            + translate("pvpAlternativeMissionBox", "disabledM"))
        if (not disable_weapon_swap):
            self.PvPAltDisChangeWeapon.setText(translate("pvpAlternativeMissionBox", "weaponSwap") + ": "
                                               + translate("pvpAlternativeMissionBox", "enabledM"))
        else:
            self.PvPAltDisChangeWeapon.setText(translate("pvpAlternativeMissionBox", "weaponSwap") + ": "
                                               + translate("pvpAlternativeMissionBox", "disabledM"))

    def set_pvp_data_match(self, time: int, player: int, max_team: int, min_players: int, mode: str, desc: str) -> None:
        self.PvPAltMode.setText(translate("pvpAlternativeMissionBox", "modality") + ": " + mode)
        self.PvPAltTime.setText(translate("pvpAlternativeMissionBox", "matchDuration") + ": " + str(time))
        self.PvPAltPlayer.setText(translate("pvpAlternativeMissionBox", "maxPlayer") + ": " + str(player))
        self.PvPAltMaxSquad.setText(translate("pvpAlternativeMissionBox", "maxDiffSquadPlayer") + ": " + str(max_team))
        self.PvPAltMinPlayer.setText(translate("pvpAlternativeMissionBox", "minSquadPlayer") + ": " + str(min_players))
        self.PvPAltDesc.setText(get_pvp_alt_desc(desc))

    def set_pvp_weapon_restriction(self, warframe: str, primary: str, secondary: str, melee: str) -> None:
        self.PvPAltWarframe.setText(get_item_name(warframe, 0))
        self.PvPAltPrimary.setText(get_item_name(primary, 0))
        self.PvPAltSecondary.setText(get_item_name(secondary, 0))
        self.PvPAltMelee.setText(get_item_name(melee, 0))

    def hide(self) -> None:
        self.PvPAltDisAmmo.hide()
        self.PvPAltDisEnergy.hide()
        self.PvPAltDisEnergySurge.hide()
        self.PvPAltDisHUDWeapon.hide()
        self.PvPAltDisChangeWeapon.hide()
        self.PvPAltName.hide()
        self.PvPAltDesc.hide()
        self.PvPAltMode.hide()
        self.PvPAltTime.hide()
        self.PvPAltPlayer.hide()
        self.PvPAltMaxSquad.hide()
        self.PvPAltMinPlayer.hide()
        self.PvPAltPrimaryLab.hide()
        self.PvPAltPrimary.hide()
        self.PvPAltSecondaryLab.hide()
        self.PvPAltSecondary.hide()
        self.PvPAltMeleeLab.hide()
        self.PvPAltMelee.hide()
        self.PvPAltWarframeLab.hide()
        self.PvPAltWarframe.hide()
