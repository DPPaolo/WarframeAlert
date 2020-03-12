# coding=utf-8
import json

from warframeAlert import warframeData
from warframeAlert.services.optionHandlerService import OptionsHandler
from warframeAlert.services.translationService import translate
from warframeAlert.utils.commonUtils import get_last_item_with_backslash, print_traceback
from warframeAlert.utils.fileUtils import get_separator
from warframeAlert.utils.logUtils import LogHandler


def get_node(name):
    if (OptionsHandler.get_option("Language", str) == "it"):
        return get_node_it(name)
    else:
        return get_node_en(name)


def get_node_it(name):
    if (name in warframeData.NODE_NAME_IT):
        return warframeData.NODE_NAME_IT[name][0], "(" + warframeData.NODE_NAME_IT[name][1] + ")"
    elif (name == ""):
        return "", "(????)"
    else:
        print(translate("gameTranslation", "unknownNode") + ": " + name)
        LogHandler.err(translate("gameTranslation", "unknownNode") + ": " + name)
        return name, "(????)"


def get_node_en(name):
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
        data = json_data[name]['value'].replace("\n", "").split(" ")
        return data[0], data[1]
    if (found == 0):
        return name, "(????)"


def get_faction(name):
    faction = name.replace("\n", "")
    if (faction in warframeData.FACTION):
        return warframeData.FACTION[faction]
    else:
        print(translate("gameTranslation", "unknownFaction") + ": " + faction)
        LogHandler.err(translate("gameTranslation", "unknownFaction") + ": " + faction)
        return faction


def get_item_name(name):
    if (OptionsHandler.get_option("Language", str) == "it"):
        return get_item_name_it(name)
    else:
        return get_item_name_en(name)


def get_item_name_it(name):
    if (name in warframeData.ITEM_NAME_IT):
        return warframeData.ITEM_NAME_IT[name]
    else:
        print(translate("gameTranslation", "unknownItemName") + ": " + name)
        LogHandler.err(translate("gameTranslation", "unknownItemName") + ": " + name)
        return get_last_item_with_backslash(name)


def get_item_name_en(name):
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


def get_enemy_name(name):
    if (name in warframeData.ALERT_ENEMY):
        return warframeData.ALERT_ENEMY[name]
    else:
        print(translate("gameTranslation", "unknownEnemy") + ": " + name)
        LogHandler.err(translate("gameTranslation", "unknownEnemy") + ": " + name)
        return get_last_item_with_backslash(name)


def get_simaris_target(simaris_target):
    if (simaris_target in warframeData.SIMARIS_TARGET):
        return warframeData.SIMARIS_TARGET[simaris_target]
    else:
        print(translate("gameTranslation", "unknownSimarisTarget") + ": " + simaris_target)
        LogHandler.err(translate("gameTranslation", "unknownSimarisTarget") + ": " + simaris_target)
        return get_last_item_with_backslash(simaris_target)


def get_invasion_loctag(loctag):
    if (loctag in warframeData.INVASION_LOCTAG):
        return warframeData.INVASION_LOCTAG[loctag][OptionsHandler.get_option("Language", str)]
    else:
        print(translate("gameTranslation", "unknownInvasionLocTag") + ": " + loctag)
        LogHandler.err(translate("gameTranslation", "unknownInvasionLocTag") + ": " + loctag)
        return get_last_item_with_backslash(loctag)


def get_accolyte_name(name):
    if (name in warframeData.ACCOLYTE_NAME):
        return warframeData.ACCOLYTE_NAME[name]
    else:
        print(translate("gameTranslation", "unknownAccolyte") + ": " + name)
        LogHandler.err(translate("gameTranslation", "unknownAccolyte") + ": " + name)
        return get_last_item_with_backslash(name)


def get_upgrade_type(upgrade):
    if (upgrade in warframeData.UPGRADE_TYPE):
        return warframeData.UPGRADE_TYPE[upgrade][OptionsHandler.get_option("Language", str)]
    else:
        print(translate("gameTranslation", "unknownupgradeType") + ": " + str(upgrade))
        LogHandler.err(translate("gameTranslation", "unknownupgradeType") + ": " + str(upgrade))
        return upgrade


def get_region(region):
    if (region in warframeData.REGION_MAP):
        return warframeData.REGION_MAP[int(region)][OptionsHandler.get_option("Language", str)]
    else:
        print(translate("gameTranslation", "unknownRegion") + ": " + str(region))
        LogHandler.err(translate("gameTranslation", "unknownRegion") + ": " + str(region))
        return str(region)


def get_mission_from_starchart(node, planet):
    if (OptionsHandler.get_option("Language", str) == "it"):
        return get_mission_from_starchart_it(node, planet)
    else:
        return get_mission_from_starchart_en(node + " (" + planet + ")")


def get_mission_from_starchart_it(node, planet):
    file_path = "data" + get_separator() + "starchart.txt"
    try:
        fp = open(file_path)
    except Exception as er:
        LogHandler.err(str(er))
        print_traceback(translate("gameTranslation", "errorFileStarchart") + str(er))
        return ""
    found = 0
    for line in fp.readlines():
        line = line.replace("\n", "")
        if ("[" in line):
            line = line.replace("]", "")
            data = line.split("[Pianeta ")
            if (data[1] == planet[1:-1]):
                found = 1
        elif (found == 1):
            line = line.split(":")
            if (line[0] == "Nome Nodo"):
                if (line[1] == " " + node):
                    found = 2
        elif (found == 2):
            line = line.split(":")
            if (line[0] == "Tipo Missione"):
                fp.close()
                return line[1][1:]
    fp.close()
    if (found == 0):
        print(translate("gameTranslation", "noStarchartNode") + ": " + node)
        LogHandler.err(translate("gameTranslation", "noStarchartNode") + ": " + node)
        return ""


def get_mission_from_starchart_en(node):
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
        if (name == node):
            return json_data[elem]['type']
    return ""