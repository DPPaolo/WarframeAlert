# coding=utf-8
import json
from itertools import groupby

from warframeAlert import warframeData
from warframeAlert.constants.events import OPERATION_TYPE
from warframeAlert.constants.syndicates import BOUNTY_RANK_LEVEL
from warframeAlert.services.optionHandlerService import OptionsHandler
from warframeAlert.services.translationService import translate
from warframeAlert.utils.commonUtils import print_traceback
from warframeAlert.utils.fileUtils import get_separator, get_asset_path
from warframeAlert.utils.gameTranslationUtils import get_item_name, get_stage_name, get_rarity
from warframeAlert.utils.logUtils import LogHandler


def parse_reward(data):
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


def get_weapon_part(part):
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


def get_weapon_type(part):
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


def get_operation_type(operation):
    if (operation in OPERATION_TYPE):
        return OPERATION_TYPE[operation]
    else:
        print(translate("warframeUtils", "operationTypeNotFound") + " " + operation)
        LogHandler.err(translate("warframeUtils", "operationTypeNotFound") + " " + operation)
        return operation


def get_image_path_from_name(name):
    if (name in warframeData.IMAGE_NAME):
        return warframeData.IMAGE_NAME[name]
    else:
        return name


def get_image_path_from_export_manifest(name):
    name = name.lower()
    try:
        fp = open(get_asset_path() + "file" + get_separator() + "ExportManifest.json")
    except Exception as err:
        LogHandler.err(translate("warframeUtils", "ExportManifestNotFound") + " :\n" + str(err))
        print_traceback(translate("warframeUtils", "ExportManifestNotFound") + " :\n" + str(err))
        return warframeData.DEFAULT_ALERT_IMAGE
    data = fp.readlines()
    fp.close()
    json_data = json.loads(data[0])
    for item in json_data['Manifest']:
        unique_name = item['uniqueName'].lower()
        if (name == unique_name):
            return item['textureLocation'].replace("\\", "/")
    return warframeData.DEFAULT_ALERT_IMAGE


def get_image_from_url_with_store_items(url):
    if ("/StoreItems/" in url):
        line = url.split("/StoreItems/")
        if (len(line) > 2):
            return line[1] + "/StoreItems/" + line[2]
        else:
            return line[1]
    else:
        return url


def get_baro_image_path_from_export_manifest(name):
    try:
        fp = open(get_asset_path() + "file" + get_separator() + "ExportManifest.json")
    except Exception as err:
        LogHandler.err(translate("warframeUtils", "ExportManifestNotFound") + " :\n" + str(err))
        print_traceback(translate("warframeUtils", "ExportManifestNotFound") + " :\n" + str(err))
        return name
    data = fp.readlines()
    fp.close()
    json_data = json.loads(data[0])
    for item in json_data['Manifest']:
        unique_name = item['uniqueName'].lower()
        if (name.lower() in unique_name or get_image_from_url_with_store_items(name).lower() in unique_name):
            return item['textureLocation'].replace("\\", "/")
    return name


def read_drop_file(name):
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
    except IndexError or Exception:
        return {}


def get_bounty_reward(reward, file_name):
    language = OptionsHandler.get_option("Language", str)
    no_reward = translate("warframeUtils", "noBountyReward").replace(" ", "\n")
    prefix = ""
    if (file_name == "cetus"):
        prefix = "cetusBountyRewards"
    elif (file_name == "fortuna"):
        prefix = "solarisBountyRewards"
    elif (file_name == "deimos"):
        prefix = "deimosRewards"
    try:
        json_data = read_drop_file(file_name + "_" + language)[prefix]
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


def get_reward_from_sortie():
    language = OptionsHandler.get_option("Language", str)
    try:
        json_data = read_drop_file("sortie_" + language)["sortieRewards"]
    except Exception as er:
        LogHandler.err(translate("warframeUtils",
                                 "sortieRewardReadingError") + "Impossibile visualizzare la Ricompensa delle Sortie")
        LogHandler.err(str(er))
        print_traceback(translate("warframeUtils",
                                  "sortieRewardReadingError") + "Impossibile visualizzare la Ricompensa delle Sortie")
        return translate("sortieBox", "noReward")
    data = []
    for item in json_data:
        name = item['itemName']
        rar = get_rarity(item['rarity'].upper()) + " " + str(item['chance']) + "%"
        data.append(name + " (" + rar + ")")
    return data


def get_relic_tier_from_name(name):
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


def get_relic_item(name):
    language = OptionsHandler.get_option("Language", str)
    try:
        json_data = read_drop_file('relic_' + language)['relics']
    except Exception as ex:
        LogHandler.err(translate("warframeUtils", "errorDropRelic") + ":\n " + str(ex))
        print_traceback(translate("warframeUtils", "errorDropRelic") + ":\n  " + str(ex))
        return []
    rewards = []
    for relic in json_data:
        relic_name = relic["tier"] + " " + relic["relicName"]
        if (relic_name == name and relic['state'] == 'Intact'):
            for reward in relic['rewards']:
                reward_name = reward["itemName"]
                data = (reward_name, get_relic_rarity_from_percent(reward['chance'], "Intact"))
                rewards.append(data)
            return rewards
    return rewards


def get_relic_drop_from_name(name):
    language = OptionsHandler.get_option("Language", str)
    try:
        json_data = read_drop_file('relic_' + language)['relics']
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


def add_all_relic_from_file(obj):
    language = OptionsHandler.get_option("Language", str)
    json_data = read_drop_file('relic_' + language)['relics']
    relics = []

    for relic in json_data:
        relic_name = relic["tier"] + " " + relic["relicName"]
        relics.append(relic_name)

    for relic in sorted(set(relics)):
        obj.addItem(relic)


def add_all_relic_item_from_file(obj):
    language = OptionsHandler.get_option("Language", str)
    json_data = read_drop_file('relic_' + language)['relics']
    item = []
    for relic in json_data:
        if (relic['state'] == "Intact"):
            for reward in relic['rewards']:
                item.append(reward["itemName"])
    item.sort()
    items = set(item)
    for line in items:
        obj.addItem(line)


def get_all_relic_from_file():
    language = OptionsHandler.get_option("Language", str)
    json_data = read_drop_file('relic_' + language)['relics']
    return json_data


def get_relic_rarity_from_percent(rarity, relic_type):
    rarity = str(rarity)

    if (relic_type == "Intact"):
        if (rarity == "2"):
            return translate("warframeUtils", "rare") + " (" + rarity + "%)"
        elif (rarity == "11"):
            return translate("warframeUtils", "notCommon") + " (" + rarity + "%)"
        else:
            # 25.33
            return translate("warframeUtils", "common") + " (" + rarity + "%)"
    elif (relic_type == "Exceptional"):
        if (rarity == "4"):
            return translate("warframeUtils", "rare") + " (" + rarity + "%)"
        elif (rarity == "13"):
            return translate("warframeUtils", "notCommon") + " (" + rarity + "%)"
        else:
            # 23.33
            return translate("warframeUtils", "common") + " (" + rarity + "%)"
    elif (relic_type == "Flawless"):
        if (rarity == "6"):
            return translate("warframeUtils", "rare") + " (" + rarity + "%)"
        elif (rarity == "17"):
            return translate("warframeUtils", "notCommon") + " (" + rarity + "%)"
        else:
            # 20
            return translate("warframeUtils", "common") + " (" + rarity + "%)"
    elif (relic_type == "Radiant"):
        if (rarity == "10"):
            return translate("warframeUtils", "rare") + " (" + rarity + "%)"
        elif (rarity == "20"):
            return translate("warframeUtils", "notCommon") + " (" + rarity + "%)"
        else:
            # 16.67
            return translate("warframeUtils", "common") + " (" + rarity + "%)"


def translate_item_from_drop_file(data):
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
    # TODO: continue the translation
    # elif (is_mod(data)):
    #     return data.lower().title()
    # elif (is_warframe(item[0])):
    #     return prime(data)
    # elif (is_prime(item[0])):
    #     return prime(data)
    # elif (is_resource(data)):
    #     return warframeData.RISORSA[data]
    # elif (is_item(data)):
    #     return warframeData.OGGETTI[data]
    else:
        print(translate("warframeUtils", "itemNotFound") + ": " + data)
        LogHandler.err(translate("warframeUtils", "itemNotFound") + ": " + data)
        return data


def is_relic(relic):
    return relic in warframeData.RELICS


def translate_relic(relic):
    relic = relic.split(" ")
    return "Reliquia " + str.capitalize(relic[0]) + " " + relic[1]


def is_lens(lens):
    return lens in warframeData.LENS


def translate_focus_lens(focus_lens):
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
