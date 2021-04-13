# coding=utf-8
from PyQt5 import QtCore, QtWidgets, QtGui

from warframeAlert.components.common.EmptySpace import EmptySpace
from warframeAlert.services.translationService import translate
from warframeAlert.utils.gameTranslationUtils import get_pvp_alt_desc, get_item_name


class PvPAlternativeMissionBox():

    def __init__(self, name):
        self.Font = QtGui.QFont()
        self.Font.setBold(True)

        self.PvPAltName = QtWidgets.QLabel(name)
        self.PvPAltMode = QtWidgets.QLabel(translate("pvpAlternativeMissionBox", "modality") + ": N/D")
        self.PvPAltName.setAlignment(QtCore.Qt.AlignCenter)
        self.PvPAltMode.setAlignment(QtCore.Qt.AlignCenter)
        self.PvPAltName.setFont(self.Font)
        self.PvPAltMode.setFont(self.Font)
        self.PvPAltDesc = QtWidgets.QLabel("")
        self.PvPAltDesc.setAlignment(QtCore.Qt.AlignCenter)

        self.PvPAltdisAmmo = QtWidgets.QLabel(translate("pvpAlternativeMissionBox", "ammoPickup") + ": N/D")
        self.PvPAltdisEnergy = QtWidgets.QLabel(translate("pvpAlternativeMissionBox", "energyPickup") + ": N/D")
        self.PvPAltdisEnergySurge = QtWidgets.QLabel(translate("pvpAlternativeMissionBox", "energySurge") + ": N/D")
        self.PvPAltdisHUDWeapon = QtWidgets.QLabel(translate("pvpAlternativeMissionBox", "weaponHUD") + ": N/D")
        self.PvPAltdisChangeWeapon = QtWidgets.QLabel(translate("pvpAlternativeMissionBox", "weaponSwap") + ": N/D")
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

        self.PvPAltPrimaryLab.setAlignment(QtCore.Qt.AlignCenter)
        self.PvPAltPrimary.setAlignment(QtCore.Qt.AlignCenter)
        self.PvPAltSecondaryLab.setAlignment(QtCore.Qt.AlignCenter)
        self.PvPAltSecondary.setAlignment(QtCore.Qt.AlignCenter)
        self.PvPAltMeleeLab.setAlignment(QtCore.Qt.AlignCenter)
        self.PvPAltMelee.setAlignment(QtCore.Qt.AlignCenter)
        self.PvPAltWarframeLab.setAlignment(QtCore.Qt.AlignCenter)
        self.PvPAltWarframe.setAlignment(QtCore.Qt.AlignCenter)

        self.PvPAltbox0 = QtWidgets.QHBoxLayout()
        self.PvPAltbox1 = QtWidgets.QHBoxLayout()
        self.PvPAltbox2 = QtWidgets.QHBoxLayout()
        self.PvPAltbox3 = QtWidgets.QHBoxLayout()
        self.PvPAltbox4 = QtWidgets.QHBoxLayout()
        self.PvPAltbox5 = QtWidgets.QHBoxLayout()
        self.PvPAltbox6 = QtWidgets.QHBoxLayout()
        self.PvPAltbox7 = QtWidgets.QHBoxLayout()

        self.PvPAltBox = QtWidgets.QVBoxLayout()

        self.PvPAltbox0.addWidget(self.PvPAltName)
        self.PvPAltbox0.addWidget(self.PvPAltMode)

        self.PvPAltbox1.addWidget(self.PvPAltdisAmmo)
        self.PvPAltbox1.addWidget(self.PvPAltdisEnergy)
        self.PvPAltbox1.addWidget(self.PvPAltdisEnergySurge)

        self.PvPAltbox2.addWidget(self.PvPAltdisHUDWeapon)
        self.PvPAltbox2.addWidget(self.PvPAltdisChangeWeapon)
        self.PvPAltbox2.addWidget(self.PvPAltTime)

        self.PvPAltbox3.addWidget(self.PvPAltPlayer)
        self.PvPAltbox3.addWidget(self.PvPAltMaxSquad)
        self.PvPAltbox3.addWidget(self.PvPAltMinPlayer)

        self.PvPAltbox4.addWidget(self.PvPAltWarframeLab)
        self.PvPAltbox4.addWidget(self.PvPAltWarframe)
        self.PvPAltbox5.addWidget(self.PvPAltPrimaryLab)
        self.PvPAltbox5.addWidget(self.PvPAltPrimary)
        self.PvPAltbox6.addWidget(self.PvPAltSecondaryLab)
        self.PvPAltbox6.addWidget(self.PvPAltSecondary)
        self.PvPAltbox7.addWidget(self.PvPAltMeleeLab)
        self.PvPAltbox7.addWidget(self.PvPAltMelee)

        self.PvPAltBox.addLayout(self.PvPAltbox0)
        self.PvPAltBox.addWidget(self.PvPAltDesc)
        self.PvPAltBox.addWidget(EmptySpace().SpaceBox)
        self.PvPAltBox.addLayout(self.PvPAltbox1)
        self.PvPAltBox.addLayout(self.PvPAltbox2)
        self.PvPAltBox.addLayout(self.PvPAltbox3)
        self.PvPAltBox.addWidget(EmptySpace().SpaceBox)
        self.PvPAltBox.addLayout(self.PvPAltbox4)
        self.PvPAltBox.addLayout(self.PvPAltbox5)
        self.PvPAltBox.addLayout(self.PvPAltbox6)
        self.PvPAltBox.addLayout(self.PvPAltbox7)

    def get_name(self):
        return self.PvPAltName.text()

    def set_disabled_data(self, disable_ammo, disable_energy, disable_energy_surge, disable_hud, disable_weapon_swap):
        if (not disable_ammo):
            self.PvPAltdisAmmo.setText(translate("pvpAlternativeMissionBox", "ammoPickup") + ": "
                                       + translate("pvpAlternativeMissionBox", "enabledF"))
        else:
            self.PvPAltdisAmmo.setText(translate("pvpAlternativeMissionBox", "ammoPickup") + ": "
                                       + translate("pvpAlternativeMissionBox", "disabledF"))
        if (not disable_energy):
            self.PvPAltdisEnergy.setText(translate("pvpAlternativeMissionBox", "energyPickup") + ": "
                                         + translate("pvpAlternativeMissionBox", "enabledF"))
        else:
            self.PvPAltdisEnergy.setText(translate("pvpAlternativeMissionBox", "energyPickup") + ": "
                                         + translate("pvpAlternativeMissionBox", "disabledF"))
        if (not disable_energy_surge):
            self.PvPAltdisEnergySurge.setText(translate("pvpAlternativeMissionBox", "energySurge") + ": "
                                              + translate("pvpAlternativeMissionBox", "enabledF"))
        else:
            self.PvPAltdisEnergySurge.setText(translate("pvpAlternativeMissionBox", "energySurge") + ": "
                                              + translate("pvpAlternativeMissionBox", "disabledF"))
        if (not disable_hud):
            self.PvPAltdisHUDWeapon.setText(translate("pvpAlternativeMissionBox", "weaponHUD") + ": "
                                            + translate("pvpAlternativeMissionBox", "enabledM"))
        else:
            self.PvPAltdisHUDWeapon.setText(translate("pvpAlternativeMissionBox", "weaponHUD") + ": "
                                            + translate("pvpAlternativeMissionBox", "disabledM"))
        if (not disable_weapon_swap):
            self.PvPAltdisChangeWeapon.setText(translate("pvpAlternativeMissionBox", "weaponSwap") + ": "
                                               + translate("pvpAlternativeMissionBox", "enabledM"))
        else:
            self.PvPAltdisChangeWeapon.setText(translate("pvpAlternativeMissionBox", "weaponSwap") + ": "
                                               + translate("pvpAlternativeMissionBox", "disabledM"))

    def set_pvp_data_match(self, time, player, maxteam, minplayer, mode, desc):
        self.PvPAltMode.setText(translate("pvpAlternativeMissionBox", "modality") + ": " + mode)
        self.PvPAltTime.setText(translate("pvpAlternativeMissionBox", "matchDuration") + ": " + str(time))
        self.PvPAltPlayer.setText(translate("pvpAlternativeMissionBox", "maxPlayer") + ": " + str(player))
        self.PvPAltMaxSquad.setText(translate("pvpAlternativeMissionBox", "maxDiffSquadPlayer") + ": " + str(maxteam))
        self.PvPAltMinPlayer.setText(translate("pvpAlternativeMissionBox", "minSquadPlayer") + ": " + str(minplayer))
        self.PvPAltDesc.setText(get_pvp_alt_desc(desc))

    def set_pvp_weapon_restriction(self, warframes, primary, secondary, melee):
        self.PvPAltWarframe.setText(get_item_name(warframes, 0))
        self.PvPAltPrimary.setText(get_item_name(primary, 0))
        self.PvPAltSecondary.setText(get_item_name(secondary, 0))
        self.PvPAltMelee.setText(get_item_name(melee, 0))

    def hide(self):
        self.PvPAltdisAmmo.hide()
        self.PvPAltdisEnergy.hide()
        self.PvPAltdisEnergySurge.hide()
        self.PvPAltdisHUDWeapon.hide()
        self.PvPAltdisChangeWeapon.hide()
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
