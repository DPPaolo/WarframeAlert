# coding=utf-8
import json

from warframeAlert import warframeData
from warframeAlert.services.optionHandlerService import OptionsHandler
from warframeAlert.services.translationService import translate
from warframeAlert.utils.commonUtils import get_last_item_with_backslash, get_separator
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
