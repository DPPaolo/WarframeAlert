# coding=utf-8
import json
from typing import Tuple

from warframeAlert.constants import warframeData
from warframeAlert.constants.alerts import ALERT_ENEMY, ALERT_INFO, ALERT_WEAPON_RESTRICTION, MAP_TYPE, \
    ALERT_LEVEL_AURA, ALERT_FX, ALERT_BOSS, ALERT_VIP_AGENT
from warframeAlert.constants.events import ACCOLYTE_NAME, TASK_TYPE, UPGRADE_TYPE
from warframeAlert.constants.maps import NODE_NAME_IT, FACTION, REGION_MAP, MISSION_TYPE
from warframeAlert.constants.other_missions import SIMARIS_TARGET, SEASON_CHALLENGE, SORTIE_BOSS, SORTIE_MODIFIER, \
    INVASION_LOCTAG
from warframeAlert.constants.pvp import PVP_MISSION_TYPE, PVP_CHALLENGE_TYPE, PVP_CHALLENGE_DESC, PVP_ALT_DESC
from warframeAlert.constants.syndicates import SYNDICATE_NAME, BOUNTY_JOB_NAME, BOUNTY_JOB_DESC, BOUNTY_STAGE, \
    SYNDICATE_RANK_NAME
from warframeAlert.constants.warframeData import RARITY
from warframeAlert.services.optionHandlerService import OptionsHandler
from warframeAlert.services.translationService import translate
from warframeAlert.utils.commonUtils import get_last_item_with_backslash
from warframeAlert.utils.fileUtils import get_separator
from warframeAlert.utils.logUtils import LogHandler


def get_node(name: str) -> Tuple[str, str]:
    if (OptionsHandler.get_option("Language", str) == "it"):
        return get_node_it(name)
    else:
        return get_node_en(name)


def get_node_it(name: str) -> Tuple[str, str]:
    if (name in NODE_NAME_IT):
        return NODE_NAME_IT[name][0], "(" + NODE_NAME_IT[name][1] + ")"
    elif (name == ""):
        return "", "(????)"
    else:
        print(translate("gameTranslation", "unknownNode") + ": " + name)
        LogHandler.err(translate("gameTranslation", "unknownNode") + ": " + name)
        return name, "(????)"


def get_node_en(name: str) -> Tuple[str, str]:
    translation_path = "data" + get_separator() + "SolNodes.json"
    try:
        fp = open(translation_path)
        data = fp.read()
    except KeyError:
        print(translate("gameTranslation", "errorFileSolNodes"))
        LogHandler.err(translate("gameTranslation", "errorFileSolNodes"))
        return name, "(????)"
    fp.close()
    json_data = json.loads(data)
    found = 0
    if (name in json_data):
        value = json_data[name]['value'].replace("\n", "")
        if (" " not in value):
            return value, "(????)"
        data = value.split(" ")
        if (len(data) >= 2 and "(" not in value):
            return value, "(????)"
        return data[0], data[1]
    if (found == 0):
        return name, "(????)"


def get_faction(name: str) -> str:
    faction = name.replace("\n", "")
    if (faction in FACTION):
        return FACTION[faction]
    else:
        print(translate("gameTranslation", "unknownFaction") + ": " + faction)
        LogHandler.err(translate("gameTranslation", "unknownFaction") + ": " + faction)
        return faction


def get_item_name(name: str, warning=True) -> str:
    if (OptionsHandler.get_option("Language", str) == "it"):
        return get_item_name_it(name, warning)
    else:
        return get_item_name_en(name)


def get_item_name_it(name: str, warning: bool) -> str:
    if (name in warframeData.ITEM_NAME_IT):
        return warframeData.ITEM_NAME_IT[name]
    else:
        if (warning):
            print(translate("gameTranslation", "unknownItemName") + ": " + name)
            LogHandler.err(translate("gameTranslation", "unknownItemName") + ": " + name)
        return get_last_item_with_backslash(name)


def get_item_name_en(name: str) -> str:
    translation_path = "data" + get_separator() + "Language.json"
    try:
        fp = open(translation_path)
        data = fp.read()
    except KeyError:
        print(translate("gameTranslation", "errorFileLanguage"))
        LogHandler.err(translate("gameTranslation", "errorFileLanguage"))
        return get_last_item_with_backslash(name)
    fp.close()
    json_data = json.loads(data)
    name_lower = name.lower()
    found = 0
    if (name_lower in json_data):
        return json_data[name_lower]['value'].replace("\n", "")
    if (found == 0):
        return get_last_item_with_backslash(name)


def get_enemy_name(name: str) -> str:
    if (name in ALERT_ENEMY):
        return ALERT_ENEMY[name]
    else:
        print(translate("gameTranslation", "unknownEnemy") + ": " + name)
        LogHandler.err(translate("gameTranslation", "unknownEnemy") + ": " + name)
        return get_last_item_with_backslash(name)


def get_simaris_target(simaris_target: str) -> str:
    if (simaris_target in SIMARIS_TARGET):
        return SIMARIS_TARGET[simaris_target]
    else:
        print(translate("gameTranslation", "unknownSimarisTarget") + ": " + simaris_target)
        LogHandler.err(translate("gameTranslation", "unknownSimarisTarget") + ": " + simaris_target)
        return get_last_item_with_backslash(simaris_target)


def get_invasion_loc_tag(loc_tag: str) -> str:
    if (loc_tag in INVASION_LOCTAG):
        return INVASION_LOCTAG[loc_tag][OptionsHandler.get_option("Language", str)]
    else:
        print(translate("gameTranslation", "unknownInvasionLocTag") + ": " + loc_tag)
        LogHandler.err(translate("gameTranslation", "unknownInvasionLocTag") + ": " + loc_tag)
        return get_last_item_with_backslash(loc_tag)


def get_acolyte_name(name: str) -> str:
    if (name in ACCOLYTE_NAME):
        return ACCOLYTE_NAME[name]
    else:
        print(translate("gameTranslation", "unknownAcolyte") + ": " + name)
        LogHandler.err(translate("gameTranslation", "unknownAcolyte") + ": " + name)
        return get_last_item_with_backslash(name)


def get_upgrade_type(upgrade: str) -> str:
    if (upgrade in UPGRADE_TYPE):
        return UPGRADE_TYPE[upgrade][OptionsHandler.get_option("Language", str)]
    else:
        print(translate("gameTranslation", "unknownUpgradeType") + ": " + str(upgrade))
        LogHandler.err(translate("gameTranslation", "unknownUpgradeType") + ": " + str(upgrade))
        return upgrade


def get_region(region: int | str) -> str:
    if (region in REGION_MAP):
        return REGION_MAP[int(region)][OptionsHandler.get_option("Language", str)]
    else:
        print(translate("gameTranslation", "unknownRegion") + ": " + str(region))
        LogHandler.err(translate("gameTranslation", "unknownRegion") + ": " + str(region))
        return str(region)


def get_mission_type(mission: str) -> str:
    mission = mission.replace("\n", "")
    if (mission in MISSION_TYPE):
        return MISSION_TYPE[mission][OptionsHandler.get_option("Language", str)]
    elif (mission == ""):
        return ""
    else:
        print(translate("gameTranslation", "unknownMissionType") + ": " + mission)
        LogHandler.err(translate("gameTranslation", "unknownMissionType") + ": " + mission)
        return mission


def get_alert_info(alert_info: str) -> str:
    if (alert_info in ALERT_INFO):
        return ALERT_INFO[alert_info][OptionsHandler.get_option("Language", str)]
    else:
        print(translate("gameTranslation", "unknownAlertInfo") + ": " + alert_info)
        LogHandler.err(translate("gameTranslation", "unknownAlertInfo") + ": " + alert_info)
        return get_last_item_with_backslash(alert_info)


def get_alert_weapon_restriction(weapon: str) -> str:
    if (weapon in ALERT_WEAPON_RESTRICTION):
        return ALERT_WEAPON_RESTRICTION[weapon][OptionsHandler.get_option("Language", str)]
    else:
        print(translate("gameTranslation", "unknownWeaponRestriction") + ": " + weapon)
        LogHandler.err(translate("gameTranslation", "unknownWeaponRestriction") + ": " + weapon)
        return get_last_item_with_backslash(weapon)


def get_mission_from_starchart(node: str) -> str:
    translation_path = "data" + get_separator() + "SolNodes.json"
    try:
        fp = open(translation_path)
        data = fp.read()
    except KeyError:
        print(translate("gameTranslation", "errorFileSolNodes"))
        LogHandler.err(translate("gameTranslation", "errorFileSolNodes"))
        return ""
    fp.close()
    json_data = json.loads(data)
    for elem in json_data:
        name = json_data[elem]['value']
        if (node in name):
            return json_data[elem]['type']
    return ""


def get_map_type(map_type: str) -> str:
    for maps in MAP_TYPE:
        if (maps in map_type):
            return MAP_TYPE[maps][OptionsHandler.get_option("Language", str)]
    else:
        print(translate("gameTranslation", "unknownMapType") + ": " + map_type)
        LogHandler.err(translate("gameTranslation", "unknownMapType") + ": " + map_type)
        return get_last_item_with_backslash(map_type)


def get_alert_aura(aura: str) -> str:
    if (aura in ALERT_LEVEL_AURA):
        return ALERT_LEVEL_AURA[aura][OptionsHandler.get_option("Language", str)]
    else:
        print(translate("gameTranslation", "unknownAuraType") + ": " + aura)
        LogHandler.err(translate("gameTranslation", "unknownAuraType") + ": " + aura)
        return get_last_item_with_backslash(aura)


def get_alert_fx(fx: str) -> str:
    if (fx in ALERT_FX):
        return ALERT_FX[fx][OptionsHandler.get_option("Language", str)]
    else:
        print(translate("gameTranslation", "unknownFXType") + ": " + fx)
        LogHandler.err(translate("gameTranslation", "unknownFXType") + ": " + fx)
        return get_last_item_with_backslash(fx)


def get_vip_agent(vip_agent: str) -> str:
    if (vip_agent == ""):
        return ""
    if (vip_agent in ALERT_BOSS):
        return ALERT_BOSS[vip_agent][OptionsHandler.get_option("Language", str)]
    elif (vip_agent in ALERT_VIP_AGENT):
        return ALERT_VIP_AGENT[vip_agent][OptionsHandler.get_option("Language", str)]
    else:
        print(translate("gameTranslation", "unknownVipType") + ": " + vip_agent)
        LogHandler.err(translate("gameTranslation", "unknownVipType") + ": " + vip_agent)
        return get_last_item_with_backslash(vip_agent)


def get_task_type(task: str) -> Tuple[str, int]:
    if (task in TASK_TYPE):
        return TASK_TYPE[task][OptionsHandler.get_option("Language", str)]
    else:
        print(translate("gameTranslation", "unknownReconstructionTaskType") + ": " + task)
        LogHandler.err(translate("gameTranslation", "unknownReconstructionTaskType") + ": " + task)
        return (get_last_item_with_backslash(task), 0)


def get_syndicate(syn: str) -> str:
    if (syn in SYNDICATE_NAME):
        return SYNDICATE_NAME[syn][OptionsHandler.get_option("Language", str)]
    else:
        print(translate("gameTranslation", "unknownSyndicate") + ": " + syn)
        LogHandler.err(translate("gameTranslation", "unknownSyndicate") + ": " + syn)
        return syn


def get_syndicate_rank(syn: str, rank: int) -> str:
    if (syn in SYNDICATE_RANK_NAME):
        return SYNDICATE_RANK_NAME[syn][OptionsHandler.get_option("Language", str)][rank]
    else:
        print(translate("gameTranslation", "unknownSyndicateRank") + ": " + str(rank) + " " + syn)
        LogHandler.err(translate("gameTranslation", "unknownSyndicateRank") + str(rank) + " " + ": " + syn)
        return syn


def get_bounty_job(job: str) -> str:
    if (OptionsHandler.get_option("Language", str) == "it"):
        return get_bounty_job_it(job)
    else:
        return get_bounty_job_en(job)


def get_bounty_job_it(job: str) -> str:
    if (job in BOUNTY_JOB_NAME):
        return BOUNTY_JOB_NAME[job]
    else:
        print(translate("gameTranslation", "unknownJob") + ": " + ": " + job)
        LogHandler.err(translate("gameTranslation", "unknownJob") + ": " + job)
        return job


def get_bounty_job_en(job: str) -> str:
    return get_item_name_en(job)


def get_bounty_job_desc(job: str) -> str:
    if (job in BOUNTY_JOB_DESC):
        return BOUNTY_JOB_DESC[job][OptionsHandler.get_option("Language", str)]
    else:
        print(translate("gameTranslation", "unknownJobDesc") + ": " + job)
        LogHandler.err(translate("gameTranslation", "unknownMapType") + ": " + job)
        return BOUNTY_JOB_DESC[""][OptionsHandler.get_option("Language", str)]


def get_nightwave_challenge(challenge: str) -> Tuple[str, str, int]:
    if (challenge in SEASON_CHALLENGE):
        challenge_type = SEASON_CHALLENGE[challenge]
        if (OptionsHandler.get_option("Language", str) == "it"):
            return challenge_type
        else:
            translation_path = "data" + get_separator() + "Language.json"
            try:
                fp = open(translation_path)
                data = fp.read()
            except KeyError:
                print(translate("gameTranslation", "errorFileLanguage"))
                LogHandler.err(translate("gameTranslation", "errorFileLanguage"))
                return ("???", get_last_item_with_backslash(challenge), 0)
            fp.close()
            json_data = json.loads(data)
            name_lower = challenge.lower()
            found = 0
            if (name_lower in json_data):
                return (json_data[name_lower]['value'], json_data[name_lower]['desc'], challenge_type[2])
            if (found == 0):
                return ("???", get_last_item_with_backslash(challenge), 0)
    else:
        print(translate("gameTranslation", "unknownChallengeType") + ": " + challenge)
        LogHandler.err(translate("gameTranslation", "unknownChallengeType") + ": " + challenge)
        return ("???", get_last_item_with_backslash(challenge), 0)


def get_sortie_boss(boss: str) -> str:
    if (boss in SORTIE_BOSS):
        return SORTIE_BOSS[boss][OptionsHandler.get_option("Language", str)]
    else:
        print(translate("gameTranslation", "unknownSortieBoss") + ": " + boss)
        LogHandler.err(translate("gameTranslation", "unknownSortieBoss") + ": " + boss)
        return boss


def get_sortie_modifier(modifier: str) -> str:
    if (modifier in SORTIE_MODIFIER):
        return SORTIE_MODIFIER[modifier][OptionsHandler.get_option("Language", str)]
    else:
        print(translate("gameTranslation", "unknownSortieModifier") + ": " + modifier)
        LogHandler.err(translate("gameTranslation", "unknownSortieModifier") + ": " + modifier)
        return modifier


def get_stage_name(stage: str) -> str:
    if (stage in BOUNTY_STAGE):
        return BOUNTY_STAGE[stage][OptionsHandler.get_option("Language", str)]
    else:
        print(translate("gameTranslation", "unknownBountyStage") + ": " + stage)
        LogHandler.err(translate("gameTranslation", "unknownBountyStage") + ": " + stage)
        return stage


def get_rarity(rarity: str) -> str:
    if (rarity in RARITY):
        return RARITY[rarity][OptionsHandler.get_option("Language", str)]
    else:
        print(translate("gameTranslation", "unknownRarity") + ": " + rarity)
        LogHandler.err(translate("gameTranslation", "unknownRarity") + ": " + rarity)
        return rarity


def get_pvp_mission_type(mission: str) -> str:
    if (mission in PVP_MISSION_TYPE):
        return PVP_MISSION_TYPE[mission][OptionsHandler.get_option("Language", str)].upper()
    else:
        print(translate("gameTranslation", "unknownPvPCategory") + ": " + mission)
        LogHandler.err(translate("gameTranslation", "unknownPvPCategory") + ": " + mission)
        return mission.upper()


def get_pvp_mission_name(name: str, complete_name: str) -> str:
    language = OptionsHandler.get_option("Language", str)
    if (language == "it"):
        if (name in PVP_CHALLENGE_TYPE):
            return PVP_CHALLENGE_TYPE[name]
        else:
            print(translate("gameTranslation", "unknownPvPMissionName") + ": " + name)
            LogHandler.err(translate("gameTranslation", "unknownPvPMissionName") + ": " + name)
            return name
    else:
        return get_item_name_en(complete_name)


def get_pvp_desc(challenge: str, num: str) -> str:
    if (challenge in PVP_CHALLENGE_DESC):
        desc = PVP_CHALLENGE_DESC[challenge][OptionsHandler.get_option("Language", str)]
        return desc.replace("{{X}}", num)
    else:
        print(translate("gameTranslation", "unknownPvPDesc") + ": " + challenge)
        LogHandler.err(translate("gameTranslation", "unknownPvPDesc") + ": " + challenge)
        return challenge + " " + num


def get_pvp_alt_desc(name: str) -> str:
    if (name in PVP_ALT_DESC):
        return PVP_ALT_DESC[name][OptionsHandler.get_option("Language", str)]
    else:
        print(translate("gameTranslation", "unknownPvPAlternativeDesc") + ": " + name)
        LogHandler.err(translate("gameTranslation", "unknownPvPAlternativeDesc") + ": " + name)
        return get_last_item_with_backslash(name)
