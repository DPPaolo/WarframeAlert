# coding=utf-8
import json

from warframeAlert import warframeData
from warframeAlert.services.translationService import translate
from warframeAlert.utils.commonUtils import print_traceback
from warframeAlert.utils.fileUtils import get_separator
from warframeAlert.utils.gameTranslationUtils import get_item_name
from warframeAlert.utils.logUtils import LogHandler


def parse_reward(data):
    temp_rew = ""
    if ('randomizedItems' in data):
        temp_rew += translate("warframeUtils", "randomItem") + " " + data['randomizedItems']

    if ('items' in data):
        len_data = len(data['items'])
        for i in range(0, len_data):
            temp_rew += get_item_name(data['items'][i])
            if (i+1 < len_data or len(data['countedItems']) > 0):
                temp_rew += " + "

    if ('countedItems' in data):
        len_data = len(data['countedItems'])
        if (len_data > 0):
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
        temp_rew += " + " + str(data['xp']) + " " + translate("warframeUtils", "affinity")

    if ('credits' in data):
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


def get_image_path_from_name(name):
    if (name in warframeData.IMAGE_NAME):
        return warframeData.IMAGE_NAME[name]
    else:
        return name


def get_image_path_from_export_manifest(name):
    name = name.lower()
    try:
        fp = open("data" + get_separator() + "ExportManifest.json")
    except Exception as err:
        LogHandler.err(translate("warframeUtils", "ExportManifestNotFound") + " :\n " + str(err))
        print_traceback(translate("warframeUtils", "ExportManifestNotFound") + " :\n  " + str(err))
        return warframeData.DEFAULT_ALERT_IMAGE
    data = fp.readlines()
    fp.close()
    json_data = json.loads(data[0])
    for item in json_data['Manifest']:
        unique_name = item['uniqueName'].lower()
        if (name == unique_name):
            return item['textureLocation'].replace("\\", "/")
    return warframeData.DEFAULT_ALERT_IMAGE
