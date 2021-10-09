# coding=utf-8
from PyQt5 import QtGui, QtWidgets

from warframeAlert.components.common.Alert import Alert
from warframeAlert.constants.warframeTypes import AlertMissionInfo
from warframeAlert.services.translationService import translate
from warframeAlert.utils.commonUtils import bool_to_yes_no, get_last_item_with_backslash
from warframeAlert.utils.gameTranslationUtils import get_faction, get_node, get_mission_type, \
    get_map_type, get_alert_info, get_item_name, get_alert_weapon_restriction, get_vip_agent, get_alert_fx, \
    get_alert_aura
from warframeAlert.utils.logUtils import LogHandler
from warframeAlert.utils.stringUtils import divide_message
from warframeAlert.utils.warframeUtils import parse_reward


class SpecialAlert(Alert):

    def __init__(self, alert_id: str) -> None:
        super().__init__(alert_id)

        self.Font = QtGui.QFont()
        self.Font.setBold(True)

        self.extra_text = ""

        self.AlertExtraInfo = QtWidgets.QLabel("")
        self.AlertExtraInfo.setFont(self.Font)

        self.AlerthExtraBox0 = QtWidgets.QHBoxLayout()

        self.AlerthExtraBox0.addStretch(1)
        self.AlerthExtraBox0.addWidget(self.AlertExtraInfo)
        self.AlerthExtraBox0.addStretch(1)

        self.AlertHBox0.addLayout(self.AlerthExtraBox0)

    def set_alert_title_info(self, desc: str) -> None:
        if (desc != ""):
            self.extra_text += desc.upper() + ""

    def set_alert_info(self, reqitem: str, consume_item: str, weapon: str) -> None:
        add_bracket_end = False
        info = reqitem or consume_item or weapon
        if (info and self.extra_text != ""):
            self.extra_text += " ("
            add_bracket_end = True
        if (weapon != ""):
            self.extra_text += translate("specialAlert", "restriction") + ": " + str(weapon)
        if (reqitem != ""):
            if (weapon != ""):
                self.extra_text += "\t"
            self.extra_text += translate("specialAlert", "requiredItem") + ": " + str(reqitem)
            if (consume_item != ""):
                if (consume_item == translate("commonUtils", "yes")):
                    self.extra_text += " " + translate("specialAlert", "itemConsumed")
                else:
                    self.extra_text += " " + translate("specialAlert", "itemNotConsumed")
        if (add_bracket_end):
            self.extra_text += ")"

    def set_alert_other_info(self, leader: str, advanced_spawn: str, aura: str, vip: str, fx: str) -> None:
        if (self.extra_text != ""):
            self.extra_text += "\n"
        if (leader != ""):
            self.extra_text += translate("specialAlert", "leaderAllowed") + "? " + str(leader)
        if (advanced_spawn != ""):
            self.extra_text += "\t" + translate("specialAlert", "advancedSpawn") + ": " + str(advanced_spawn)
        if (vip != ""):
            self.extra_text += "\t" + translate("specialAlert", "vipAgent") + ": " + str(vip)
        if (aura != ""):
            self.extra_text += "\t" + translate("specialAlert", "missionAura") + ": " + str(aura)
        if (fx != ""):
            self.extra_text += "\t" + translate("specialAlert", "fx") + ": " + str(fx)

    def set_extra_info(self) -> None:
        text = divide_message(self.extra_text, 110)
        self.AlertExtraInfo.setText(text)

    def hide(self) -> None:
        super().hide()
        self.AlertExtraInfo.hide()


def create_alert(alert: AlertMissionInfo, alert_id: str) -> Alert | SpecialAlert | None:
    wave = ""
    if (alert):
        # Base Data
        node, plan = get_node(alert['location'])
        mis_type = get_mission_type(alert['missionType'])
        if ('nightmare' in alert):
            mis_type += " (Nightmare)"
        if ('archwingRequired' in alert or 'isSharkwingMission' in alert):
            mis_type += " (Archwing)"
        faction = "(" + get_faction(alert['faction']) + ")"
        max_lv = alert['maxEnemyLevel']
        min_lv = alert['minEnemyLevel']
        level = str(min_lv) + "-" + str(max_lv)
        mis_level = get_map_type(alert['levelOverride'])
        item = parse_reward(alert['missionReward'])
        if ('maxWaveNum' in alert):
            wave = str(alert['maxWaveNum'])
            if (alert['missionType'] == "MT_SURVIVAL"):
                wave += " " + translate("specialAlert", "minutes")
            elif (alert['missionType'] == "MT_DEFENSE"):
                wave += " " + translate("specialAlert", "waves")
            elif (alert['missionType'] == "MT_INTEL"):
                if (wave == "1"):
                    wave += " " + translate("specialAlert", "terminal")
                else:
                    wave += " " + translate("specialAlert", "terminals")
            elif (alert['missionType'] == "MT_TERRITORY"):
                wave += " " + translate("specialAlert", "rounds")
            elif (alert['missionType'] == "MT_EXCAVATE"):
                wave = str(int(wave) * 100) + " Cryotic"
            elif (alert['missionType'] == "MT_ARTIFACT"):
                wave += " " + translate("specialAlert", "pipe")
            else:
                LogHandler.debug(translate("specialAlert", "unkownWaveType") + " " + alert['missionType'])
        difficulty = alert['difficulty']*100
        enemy_spec = alert['enemySpec']

        # Extra Data
        extra = 0
        desc = reqitem = consume_item = weapon = extra_enemy_spec = ""
        leaderallowed = advanced_spawners = vip = aura = fx = icon = ""

        if ('descText' in alert):
            desc = get_alert_info(alert['descText'])
            extra = 1
        if ('goalTag' in alert):
            desc = desc or alert['goalTag']
            extra = 1
        if ('extraEnemySpec' in alert):
            extra_enemy_spec = alert['extraEnemySpec']
        if ('advancedSpawners' in alert):
            advanced_spawners = ""
            for spawn in alert['advancedSpawners']:
                advanced_spawners += get_last_item_with_backslash(spawn) + " "
        if ('requiredItems' in alert):
            for req_i in alert['requiredItems']:
                reqitem += get_item_name(req_i) + " "
            extra = 1
        if ('requiredItemsCounts' in alert):
            reqitem = str(alert['requiredItemsCounts']) + "x " + reqitem
            extra = 1
        if ('consumeRequiredItems' in alert):
            consume_item = bool_to_yes_no(alert['consumeRequiredItems'])
            extra = 1
        if ('exclusiveWeapon' in alert):
            weapon = get_alert_weapon_restriction(alert['exclusiveWeapon'])
            extra = 1
        if ('leadersAlwaysAllowed' in alert):
            leaderallowed = bool_to_yes_no(alert['leadersAlwaysAllowed'])
            extra = 1
        if ('levelAuras' in alert):
            if (alert['levelAuras']):
                for l_aura in alert['levelAuras']:
                    aura += get_alert_aura(l_aura)
                extra = 1
        if ('vipAgent' in alert):
            vip = get_vip_agent(alert['vipAgent'])
            extra = 1
        if ('fxLayer' in alert):
            fx = get_alert_fx(alert['fxLayer'])
            extra = 1
        if ('icon' in alert):
            icon = alert['icon']

    else:
        return None

    if (not faction or not mis_type or not mis_level):
        return None
    if (extra == 0):
        temp = Alert(alert_id)
    else:
        temp = SpecialAlert(alert_id)
        temp.set_alert_title_info(desc)
        temp.set_alert_info(reqitem, consume_item, weapon)
        temp.set_alert_other_info(leaderallowed, advanced_spawners, aura, vip, fx)
        temp.set_extra_info()

    temp.set_alert_data(node, plan, level, mis_type, faction, item, wave, mis_level)
    temp.set_alert_extra_data(difficulty, enemy_spec, extra_enemy_spec)
    if (icon != ""):
        temp.set_alert_image("", icon)
    return temp
