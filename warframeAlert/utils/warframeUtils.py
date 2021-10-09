# coding=utf-8
import json
from itertools import groupby
from json import JSONDecodeError
from typing import List, Tuple

from PyQt5 import QtWidgets

from warframeAlert import warframeData
from warframeAlert.constants.events import OPERATION_TYPE
from warframeAlert.constants.files import IMAGE_NAME
from warframeAlert.constants.maps import MISSION_TYPE, REGION_MAP
from warframeAlert.constants.syndicates import BOUNTY_RANK_LEVEL
from warframeAlert.constants.warframeFileTypes import SortieFileRewards, BountyFileData, RelicFileData,  \
    MissionFileData, TransientFileData, KeyFileData, MiscFileData
from warframeAlert.constants.warframeTypes import MissionReward
from warframeAlert.services.optionHandlerService import OptionsHandler
from warframeAlert.services.translationService import translate
from warframeAlert.utils.commonUtils import print_traceback
from warframeAlert.utils.fileUtils import get_separator
from warframeAlert.utils.gameTranslationUtils import get_item_name, get_stage_name, get_rarity
from warframeAlert.utils.logUtils import LogHandler


def parse_reward(data: MissionReward) -> str:
    temp_rew = ""
    if ('randomizedItems' in data):
        temp_rew += translate("warframeUtils", "randomItem") + " " + data['randomizedItems']

    if ('items' in data):
        len_data = len(data['items'])
        for i in range(0, len_data):
            temp_rew += get_item_name(data['items'][i])
            if (i+1 < len_data):
                temp_rew += " + "

    if ('countedItems' in data):
        len_data = len(data['countedItems'])
        if (len_data > 0):
            if ("items" in data and len(data['items']) > 0):
                temp_rew += " + "
            for i in range(0, len_data):
                temp_rew += str(data['countedItems'][i]['ItemCount']) + " x "
                temp_rew += get_item_name(data['countedItems'][i]['ItemType'])

    if ('countedStoreItems' in data):
        len_data = len(data['countedStoreItems'])
        if (len_data > 0):
            for i in range(0, len_data):
                temp_rew += str(data['countedStoreItems'][i]['ItemCount']) + " x "
                temp_rew += get_item_name(data['countedStoreItems'][i]['StoreItem'])

    if ('xp' in data):
        if (data['xp'] != 0):
            temp_rew += " + " + str(data['xp']) + " " + translate("warframeUtils", "affinity")

    if ('credits' in data):
        if (data['credits'] != 0):
            if (temp_rew == ""):
                temp_rew += str(data['credits']) + " " + translate("warframeUtils", "credits")
            else:
                temp_rew += " + " + str(data['credits']) + " " + translate("warframeUtils", "credits")

    return temp_rew


def get_weapon_part(part: str) -> str:
    part = part.lower()
    if ("weapon" in part):
        if ("blueprint" in part):
            return "Blueprint"
        elif ("stock" in part):
            return "Stock"
        elif ("receiver" in part):
            return "Receiver"
        elif ("barrel" in part):
            return "Barrel"
        elif ("handle" in part):
            return "Handle"
        elif ("blade" in part):
            return "Blade"
        elif ("link" in part):
            return "Link"
        elif ("heatsink" in part):
            return "Heatsink"
        elif ("disc" in part):
            return "Disc"
        elif ("limb" in part):
            return "Limb"
        elif ("grip" in part):
            return "Grip"
        elif ("string" in part):
            return "String"
        elif ("head" in part):
            return "Head"
        elif ("hilt" in part):
            return "Hilt"
        elif ("pouch" in part):
            return "Pouch"
        elif ("stars" in part):
            return "Stars"
        elif ("gauntlet" in part):
            return "Gauntlet"
        else:
            print(translate("warframeUtils", "weaponPartsNotFound") + " " + part)
            LogHandler.err(translate("warframeUtils", "weaponPartsNotFound") + " " + part)
            return "Unknown"
    else:
        return ""


def get_weapon_type(part: str) -> str:
    part = part.lower()
    if ("karak" in part):
        return "Karak Wraith"
    elif ("latron" in part):
        return "Latron Wraith"
    elif ("strun" in part):
        return "Strun Wraith"
    elif ("vipers" in part):
        return "Twin Vipers Wraith"
    elif ("dera" in part):
        return "Dera Vandal"
    elif ("snipetron" in part):
        return "Snipetron Vandal"
    elif ("combatknife" in part):
        return "Sheev"
    else:
        print(translate("warframeUtils", "weaponTypeNotFound") + " " + part)
        LogHandler.err(translate("warframeUtils", "weaponTypeNotFound") + " " + part)
        return "Unknown"


def get_operation_type(operation: str) -> str:
    if (operation in OPERATION_TYPE):
        return OPERATION_TYPE[operation]
    else:
        print(translate("warframeUtils", "operationTypeNotFound") + " " + operation)
        LogHandler.err(translate("warframeUtils", "operationTypeNotFound") + " " + operation)
        return operation


def get_image_path_from_name(name: str) -> str:
    if (name in IMAGE_NAME):
        return IMAGE_NAME[name]
    else:
        return name


def read_drop_file(name: str) -> dict:
    try:
        fp = open("data" + get_separator() + name + ".json")
    except FileNotFoundError as err:
        LogHandler.err("File " + name + translate("warframeUtils", "jsonFileNotFound") + ":\n " + str(err))
        print_traceback("File " + name + translate("warframeUtils", "jsonFileNotFound") + ":\n  " + str(err))
        return {}
    data = fp.readlines()
    fp.close()
    try:
        return json.loads(data[0])
    except IndexError or JSONDecodeError:
        return {}


def get_bounty_reward(reward: str, file_name: str) -> List[str]:
    language = OptionsHandler.get_option("Language", str)
    no_reward = translate("warframeUtils", "noBountyReward").replace(" ", "\n")
    prefix = ""
    match file_name:
        case "cetus":
            prefix = "cetusBountyRewards"
        case "fortuna":
            prefix = "solarisBountyRewards"
        case "deimos":
            prefix = "deimosRewards"
    try:
        json_data: List[BountyFileData] = read_drop_file(file_name + "_" + language)[prefix]
    except KeyError or Exception:
        return [no_reward, no_reward, no_reward]
    reward_type = reward.split("/Lotus/Types/Game/MissionDecks/")[1][:-7]
    if (reward_type in BOUNTY_RANK_LEVEL):
        reward_type = BOUNTY_RANK_LEVEL[reward_type]
    else:
        print(translate("warframeUtils", "bountyRewardNotFound") + " " + reward_type)
        return [no_reward, no_reward, no_reward]

    rew_a = rew_b = rew_c = no_reward
    for bounty_level in json_data:
        if (bounty_level['bountyLevel'] == reward_type):
            if ('A' in bounty_level['rewards']):
                rot_a = bounty_level['rewards']['A']
                rot_a.sort(key=lambda x: x['stage'])
                rew_a = ""
                for stage, stage_rewards in groupby(rot_a, key=lambda x: x['stage']):
                    stage_translated = stage if (language == "en") else get_stage_name(stage)
                    rew_a += stage_translated + "\n\n"
                    for drop in stage_rewards:
                        item = drop['itemName']
                        rar = get_rarity(drop['rarity'].upper()) + " " + str(drop['chance']) + "%"
                        rew_a += item + " (" + rar + ")\n"
                    rew_a += "\n"

            if ('B' in bounty_level['rewards']):
                rot_b = bounty_level['rewards']['B']
                rot_b.sort(key=lambda x: x['stage'])
                rew_b = ""
                for stage, stage_rewards in groupby(rot_b, key=lambda x: x['stage']):
                    stage_translated = stage if (language == "en") else get_stage_name(stage)
                    rew_b += stage_translated + "\n\n"
                    for drop in stage_rewards:
                        item = drop['itemName']
                        rar = get_rarity(drop['rarity'].upper()) + " " + str(drop['chance']) + "%"
                        rew_b += item + " (" + rar + ")\n"
                    rew_b += "\n"

            if ('C' in bounty_level['rewards']):
                rot_c = bounty_level['rewards']['C']
                rot_c.sort(key=lambda x: x['stage'])
                rew_c = ""
                for stage, stage_rewards in groupby(rot_c, key=lambda x: x['stage']):
                    stage_translated = stage if (language == "en") else get_stage_name(stage)
                    rew_c += stage_translated + "\n\n"
                    for drop in stage_rewards:
                        item = drop['itemName']
                        rar = get_rarity(drop['rarity'].upper()) + " " + str(drop['chance']) + "%"
                        rew_c += item + " (" + rar + ")\n"
                    rew_c += "\n"

    if (rew_a == ""):
        rew_a = no_reward
    if (rew_b == ""):
        rew_b = no_reward
    if (rew_c == ""):
        rew_c = no_reward
    reward = [rew_a, rew_b, rew_c]
    return reward


def get_reward_from_sortie() -> List[str]:
    language = OptionsHandler.get_option("Language", str)
    try:
        json_data: List[SortieFileRewards] = read_drop_file("sortie_" + language)["sortieRewards"]
    except Exception as er:
        LogHandler.err(translate("warframeUtils",
                                 "sortieRewardReadingError") + "Impossibile visualizzare la Ricompensa delle Sortie")
        LogHandler.err(str(er))
        print_traceback(translate("warframeUtils",
                                  "sortieRewardReadingError") + "Impossibile visualizzare la Ricompensa delle Sortie")
        return [translate("sortieBox", "noReward")]
    data = []
    for item in json_data:
        name = item['itemName']
        rar = get_rarity(item['rarity'].upper()) + " " + str(item['chance']) + "%"
        data.append(name + " (" + rar + ")")
    return data


def get_relic_tier_from_name(name: str) -> int:
    if ("Lith" in name):
        return 1
    elif ("Meso" in name):
        return 2
    elif ("Neo" in name):
        return 3
    elif ("Axi" in name):
        return 4
    elif ("Requiem" in name):
        return 5


def get_relic_item(name: str) -> List[Tuple[str, str]]:
    language = OptionsHandler.get_option("Language", str)
    try:
        json_data: List[RelicFileData] = read_drop_file('relic_' + language)['relics']
    except Exception as ex:
        LogHandler.err(translate("warframeUtils", "errorDropRelic") + ":\n " + str(ex))
        print_traceback(translate("warframeUtils", "errorDropRelic") + ":\n  " + str(ex))
        return []
    rewards: List[Tuple[str, str]] = []
    for relic in json_data:
        relic_name = relic["tier"] + " " + relic["relicName"]
        if (relic_name == name and relic['state'] == 'Intact'):
            for reward in relic['rewards']:
                reward_name: str = reward["itemName"]
                data = (reward_name, get_relic_rarity_from_percent(reward['chance'], "Intact"))
                rewards.append(data)
            return rewards
    return rewards


def get_relic_drop_from_name(name: str) -> str:
    language = OptionsHandler.get_option("Language", str)
    try:
        json_data: List[RelicFileData] = read_drop_file('relic_' + language)['relics']
    except Exception as ex:
        LogHandler.err(translate("warframeUtils", "errorDropRelic") + ":\n " + str(ex))
        print_traceback(translate("warframeUtils", "errorDropRelic") + ":\n  " + str(ex))
        return ""
    drop = ""
    for relic in json_data:
        if (relic['state'] == 'Intact'):
            for reward in relic['rewards']:
                if (reward['itemName'] == name):
                    relic_name = relic['tier'] + " " + relic['relicName']
                    drop += relic_name + " " + get_relic_rarity_from_percent(reward['chance'], "Intact") + "\n"
    return drop


def add_all_relic_from_file(obj: QtWidgets.QComboBox) -> None:
    language = OptionsHandler.get_option("Language", str)
    json_data: List[RelicFileData] = read_drop_file('relic_' + language)['relics']
    relics = []

    for relic in json_data:
        relic_name = relic["tier"] + " " + relic["relicName"]
        relics.append(relic_name)

    for relic in sorted(set(relics)):
        obj.addItem(relic)


def add_all_relic_item_from_file(obj: QtWidgets.QComboBox) -> None:
    language = OptionsHandler.get_option("Language", str)
    json_data: List[RelicFileData] = read_drop_file('relic_' + language)['relics']
    item = []
    for relic in json_data:
        if (relic['state'] == "Intact"):
            for reward in relic['rewards']:
                item.append(reward["itemName"])
    item.sort()
    items = set(item)
    for line in items:
        obj.addItem(line)


def get_all_relic_from_file() -> List[RelicFileData]:
    language = OptionsHandler.get_option("Language", str)
    json_data: List[RelicFileData] = read_drop_file('relic_' + language)['relics']
    return json_data


def get_relic_rarity_from_percent(rarity: float, relic_type: str) -> str:
    rarity = str(rarity)

    match relic_type:
        case "Intact":
            match rarity:
                case "2":
                    return translate("warframeUtils", "rare") + " (" + rarity + "%)"
                case "11":
                    return translate("warframeUtils", "notCommon") + " (" + rarity + "%)"
                case _:  # 25.33
                    return translate("warframeUtils", "common") + " (" + rarity + "%)"
        case  "Exceptional":
            match rarity:
                case "4":
                    return translate("warframeUtils", "rare") + " (" + rarity + "%)"
                case "13":
                    return translate("warframeUtils", "notCommon") + " (" + rarity + "%)"
                case _:  # 23.33
                    return translate("warframeUtils", "common") + " (" + rarity + "%)"
        case "Flawless":
            match rarity:
                case "6":
                    return translate("warframeUtils", "rare") + " (" + rarity + "%)"
                case "17":
                    return translate("warframeUtils", "notCommon") + " (" + rarity + "%)"
                case _:  # 20
                    return translate("warframeUtils", "common") + " (" + rarity + "%)"
        case"Radiant":
            match rarity:
                case "10":
                    return translate("warframeUtils", "rare") + " (" + rarity + "%)"
                case "20":
                    return translate("warframeUtils", "notCommon") + " (" + rarity + "%)"
                case _:  # 16.67
                    return translate("warframeUtils", "common") + " (" + rarity + "%)"


def get_relic_drop(relic_name: str) -> str:
    language = OptionsHandler.get_option("Language", str)
    try:
        json_cetus: List[BountyFileData] = read_drop_file('cetus_' + language)['cetusBountyRewards']
        json_fortuna: List[BountyFileData] = read_drop_file('fortuna_' + language)['solarisBountyRewards']
        json_deimos: List[BountyFileData] = read_drop_file('deimos_' + language)['deimosRewards']
        json_mission: dict[str, dict[str, MissionFileData]] = read_drop_file('mission_' + language)['missionRewards']
        json_key: List[KeyFileData] = read_drop_file('key_' + language)['keyRewards']
        json_transient: List[TransientFileData] = read_drop_file('transient_' + language)['transientRewards']
        json_misc: List[MiscFileData] = read_drop_file('misc_' + language)['miscItems']
    except Exception as ex:
        LogHandler.err(translate("warframeUtils", "errorDropRelic") + ":\n " + str(ex))
        print_traceback(translate("warframeUtils", "errorDropRelic") + ":\n  " + str(ex))
        return translate("warframeUtils", "errorDropRelic")
    found = 0
    if (OptionsHandler.get_option("Language", str) == "en"):
        relic_name = relic_name + " " + translate("warframeUtils", "relic")
    else:
        relic_name = translate("warframeUtils", "relic") + " " + relic_name
    mis = ""

    for bounty in json_cetus + json_fortuna + json_deimos:
        bounty_lv = bounty['bountyLevel']
        for rotation in bounty['rewards']:
            for bounty_reward in bounty['rewards'][rotation]:
                if (bounty_reward['itemName'] == relic_name):
                    drop_text = translate("warframeUtils", "bounty") + " " + get_stage_name(bounty_lv) + " ("
                    drop_text += translate("warframeUtils", "rotation")
                    if (rotation in ["A", "B", "C"]):
                        drop_text += " " + rotation
                    else:
                        drop_text += " " + get_stage_name(bounty_reward['stage'])
                    drop_text += " " + get_stage_name(bounty_reward['stage']) + ")\n"
                    mis += drop_text
                    found = 1

    for planet in json_mission:
        translated_planet = translate_planet_from_drop_file(planet)
        for mission in json_mission[planet]:
            mission_data = json_mission[planet][mission]
            mission_type = mission_data['gameMode']
            is_event = mission_data['isEvent']
            if (is_event):
                mission_name = mission + " (" + translate("warframeUtils", "event") + ")"
            else:
                mission_name = mission

            is_rotation = isinstance(mission_data['rewards'], dict)
            for mission_rewards in mission_data['rewards']:
                if (is_rotation and mission_rewards in ["A", "B", "C"]):
                    rotation_items = mission_data['rewards'][mission_rewards]
                    for rotation_reward in rotation_items:
                        item = rotation_reward['itemName']
                        if (item == relic_name):
                            mis += mission_name + " (" + translated_planet + ") (" + mission_type + " " + \
                                   translate("warframeUtils", "rotation") + " " + mission_rewards + ")\n"
                            found = 1
                else:
                    item = mission_rewards['itemName']
                    if (item == relic_name):
                        mis += mission + " (" + translated_planet + ") (" + mission_type + ")\n"
                        found = 1

    for key_mission in json_key:
        mission_name = key_mission['keyName']
        for key_rewards in key_mission['rewards']:
            rotation_items = key_mission['rewards'][key_rewards]
            for rotation_reward in rotation_items:
                item = rotation_reward['itemName']
                if (item == relic_name):
                    mis += mission_name + " (" + translate("warframeUtils", "rotation") + " " + key_rewards + ")\n"
                    found = 1

    for transient_mission in json_transient:
        mission_name = transient_mission['objectiveName']
        for transient_rewards in transient_mission['rewards']:
            item = transient_rewards['itemName']
            rotation = translate("warframeUtils", "rotation") + " " + translate("warframeUtils", "noRotation")
            if (item == relic_name):
                mis += mission_name + " (" + rotation + ")\n"
                found = 1

    for misc_mission in json_misc:
        mission_name = misc_mission['enemyName']
        for misc_rewards in misc_mission['items']:
            item = misc_rewards['itemName']
            if (item == relic_name):
                mis += mission_name + "\n"
                found = 1

    if (found == 0):
        return translate("warframeUtils", "primeVault") + "\n" + translate("warframeUtils", "relicDrop")
    else:
        return mis


def translate_planet_from_drop_file(planet: str) -> str:
    for planet_translation in REGION_MAP.values():
        if (planet in planet_translation["en"]):
            return planet_translation["it"]

    print(translate("warframeUtils", "planetNotFound") + ": " + planet)
    LogHandler.err(translate("warframeUtils", "planetNotFound") + ": " + planet)
    return planet


def translate_mission_type_from_drop_file(mission_type: str) -> str:
    for mission_type_translation in MISSION_TYPE.values():
        if (mission_type in mission_type_translation["en"]):
            return mission_type_translation["it"]

    print(translate("warframeUtils", "missionTypeNotFound") + ": " + mission_type)
    LogHandler.err(translate("warframeUtils", "missionTypeNotFound") + ": " + mission_type)
    return mission_type


def translate_item_from_drop_file(data: str) -> str:
    if (data[-1] == " "):
        data = data[:-1]
    if (data[0] == " "):
        data = data[0:]
    if ("PROFIT:" in data):
        return translate("warframeUtils", "profit") + ": " + data.split(' ')[1]
    if ('RETURN:' in data):
        return translate("warframeUtils", "return") + ": " + data.split(' ')[1]
    item = data.split(" ")
    num = item[0].replace("X", "").replace(",", "").isnumeric()
    num2 = item[0].isnumeric()
    if (num or num2):
        data_new = ""
        for i in item[1:]:
            data_new = data_new + i + " "
        return item[0].replace("X", " x") + " " + translate_item_from_drop_file(data_new)
    if (is_relic(item[0])):
        return translate_relic(data)
    elif (is_lens(item[0])):
        return translate_focus_lens(data)
    elif (is_resource(data)):
        return warframeData.RESOURCES[data]
    elif (is_item(data)):
        return warframeData.ITEMS[data]
    elif (is_arcane_item(data)):
        translate_generic_item(data)
    elif (is_special_weapon(data)):
        return translate_special_weapon(data)
    elif (is_prime_part(data)):
        return translate_prime_part(data)
    elif (is_weapon_parts(data)):
        return translate_weapon_parts(data)
    elif (is_warframe_parts(data)):
        return translate_warframe_part(data)
    elif (is_railjack_weapon(data)):
        return translate_generic_item(data)
    else:
        translate_generic_item(data)
        # print(translate("warframeUtils", "itemNotFound") + ": " + data)
        # LogHandler.err(translate("warframeUtils", "itemNotFound") + ": " + data)
        return data


def is_relic(relic: str) -> bool:
    return relic in warframeData.RELICS


def translate_relic(relic: str) -> str:
    relic = relic.split(" ")
    return "Reliquia " + str.capitalize(relic[0]) + " " + relic[1]


def is_lens(lens: str) -> bool:
    return lens in warframeData.LENS


def translate_focus_lens(focus_lens: str) -> str:
    focus_lens = focus_lens.split(" ")
    if ("EIDOLON" in focus_lens):
        if (len(focus_lens) == 3):
            return "Lente Eidolon (Schema)"
        elif (len(focus_lens) == 4):
            return "Lente Eidolon " + str.capitalize(focus_lens[1]) + " (Schema)"
    if ("LUA" in focus_lens):
        "Lente Lua (Schema)"
    elif (len(focus_lens) == 2):
        return "Lente " + str.capitalize(focus_lens[0])
    elif (len(focus_lens) == 3):
        return "Lente Maggiore " + str.capitalize(focus_lens[1])


def is_resource(resource: str) -> bool:
    return resource in warframeData.RESOURCES


def is_item(item: str) -> bool:
    return item in warframeData.ITEMS


def is_arcane_item(item: str) -> bool:
    return "ARCANE" in item


def is_special_weapon(item: str) -> bool:
    special = ["VANDAL", "WRAITH", "CARMINE"]
    for elem in special:
        if (elem in item):
            return True
    return False


def translate_special_weapon(item: str) -> str:
    if ("VANDAL" in item):
        return translate_prime_part(item, "VANDAL")
    elif ("WRAITH" in item):
        return translate_prime_part(item, "WRAITH")
    elif ("CARMINE" in item):
        return translate_carmine_part(item)


def is_prime_part(item: str) -> bool:
    return len(item.split(" ")) > 2 and "PRIME" in item


def translate_prime_part(item: str, separator: str = "PRIME") -> str:
    prime_item = item.split(" " + separator + " ")[0]
    prime_parts = item.split(" " + separator + " ")[1].split(" ")
    parts_translated = ""
    j = 0
    for i in range(0, len(prime_parts)):
        if (prime_parts[i] not in warframeData.ITEM_PARTS):
            print(translate("warframeUtils", "primeNotFound") + ": " + prime_parts[i])
            LogHandler.err(translate("warframeUtils", "primeNotFound") + ": " + prime_parts[i])
        else:
            parts_translated = parts_translated + warframeData.ITEM_PARTS[prime_parts[i]]
        j += 1
        if (j != len(prime_parts)):
            parts_translated += " "
    return prime_item.capitalize() + " " + warframeData.ITEM_PARTS[separator] + " " + parts_translated


def translate_carmine_part(item: str) -> str:
    separator = "CARMINE"
    prime_item = item.split(separator + " ")[0]
    prime_parts = item.split(separator + " ")[1].split(" ")
    parts_translated = ""
    j = 0
    for i in range(0, len(prime_parts)):
        if (i == 0):
            parts_translated += prime_parts[i].capitalize()
        elif (prime_parts[i] not in warframeData.ITEM_PARTS):
            print(translate("warframeUtils", "primeNotFound") + ": " + prime_parts[i])
            LogHandler.err(translate("warframeUtils", "primeNotFound") + ": " + prime_parts[i])
        else:
            parts_translated += warframeData.ITEM_PARTS[prime_parts[i]]
        j += 1
        if (j != len(prime_parts)):
            parts_translated += " "
    return prime_item.capitalize() + " " + warframeData.ITEM_PARTS[separator] + " " + parts_translated


def is_warframe_parts(item: str) -> bool:
    item_parts = item.split(" ")
    parts = ["NEUROPTICS", "CHASSIS", "SYSTEMS", "BLUEPRINT"]
    equal_parts = 0
    for i in range(0, len(item_parts)):
        if (item_parts[i] in parts):
            equal_parts += 1
    return equal_parts >= 2


def translate_warframe_part(item: str) -> str:
    warframe = item.split(" ")[0]
    warframe_parts = item.split(warframe + " ")[1].split(" ")
    parts_translated = ""
    j = 0
    for i in range(0, len(warframe_parts)):
        if (warframe_parts[i] not in warframeData.ITEM_PARTS):
            print(translate("warframeUtils", "primeNotFound") + ": " + warframe_parts[i])
            LogHandler.err(translate("warframeUtils", "primeNotFound") + ": " + warframe_parts[i])
        else:
            parts_translated += warframeData.ITEM_PARTS[warframe_parts[i]]
        j += 1
        if (j != len(warframe_parts)):
            parts_translated += " "
    return warframe.capitalize() + "  " + parts_translated


def is_weapon_parts(item: str) -> bool:
    item_parts = item.split(" ")
    equal_parts = 0
    for i in range(0, len(item_parts)):
        if (item_parts[i] in warframeData.ITEM_PARTS and i != 0):
            equal_parts += 1
    return equal_parts == 1


def translate_weapon_parts(item: str) -> str:
    weapon = item.split(" ")[0]
    weapon_parts = item.split(weapon + " ")[1].split(" ")
    parts_translated = ""

    item_parts = item.split(" ")
    equal_parts = 0
    for i in range(0, len(item_parts)):
        if (item_parts[i] in warframeData.ITEM_PARTS and i != 0):
            equal_parts = i

    j = 0
    for i in range(equal_parts, len(weapon_parts)):
        if (weapon_parts[i] not in warframeData.ITEM_PARTS):
            print(translate("warframeUtils", "primeNotFound") + ": " + item)
            LogHandler.err(translate("warframeUtils", "primeNotFound") + ": " + item)
        else:
            parts_translated += warframeData.ITEM_PARTS[weapon_parts[i]]
        j += 1
        if (j != len(weapon_parts)):
            parts_translated += " "
    return weapon.capitalize() + "  " + parts_translated


def is_railjack_weapon(item: str) -> bool:
    schools = ["LAVAN", "VIDAR", "ZETKI"]
    for elem in schools:
        if (elem in item):
            return True
    return False


def translate_generic_item(item: str) -> str:
    item_parts = item.split(" ") if (" " in item) else (item)
    parts_translated = ""
    j = 0
    for i in range(0, len(item_parts)):
        parts_translated += item_parts[i].capitalize()
        j += 1
        if (j != len(item_parts)):
            parts_translated += " "

    return parts_translated
