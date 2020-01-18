import json

from warframeAlert import warframeData
from warframeAlert.services.optionHandlerService import OptionsHandler
from warframeAlert.services.translationService import translate
from warframeAlert.utils.commonUtils import get_last_item_with_backslash, get_cur_dir, get_separator
from warframeAlert.utils.logUtils import LogHandler


def get_node(name):
    if (name in warframeData.NODE_NAME_IT):
        return warframeData.NODE_NAME_IT[name][0], "(" + warframeData.NODE_NAME_IT[name][1] + ")"
    elif (name == ""):
        return "", "(????)"
    else:
        print(translate("gameTranslation", "unknownNode") + ": " + name)
        LogHandler.err(translate("gameTranslation", "unknownNode") + ": " + name)
        return name, "(????)"


def get_item_name(name):
    print(get_cur_dir())
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
        fp = open(translation_path, "r")
        data = fp.read()
    except KeyError:
        print(translate("gameTranslation", "errorFileLanguage"))
        LogHandler.err(translate("gameTranslation", "errorFileLanguage"))
        return get_last_item_with_backslash(name)
    fp.close()
    json_data = json.loads(data)
    name_lower = name.lower()
    trovato = 0
    if (name_lower in json_data):
        return json_data[name_lower]['value'].replace("\n", "")
    if (trovato == 0):
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
