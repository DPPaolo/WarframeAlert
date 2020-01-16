from warframeAlert import warframeData
from warframeAlert.services.translationService import translate
from warframeAlert.utils.commonUtils import get_last_item_with_backslash
from warframeAlert.utils.logUtils import LogHandler
from warframeAlert.warframeData import ALERT_ENEMY


def get_node(name):
    if (name in warframeData.NODE_NAME_IT):
        return warframeData.NODE_NAME_IT[name][0], "(" + warframeData.NODE_NAME_IT[name][1] + ")"
    elif (name == ""):
        return "", "(????)"
    else:
        print(translate("gameTranslation", "unknownNode") + ": " + name)
        LogHandler.err(translate("gameTranslation", "unknownNode") + ": " + name)
        return name, "(????)"


def get_enemy_name(name):
    if (name in ALERT_ENEMY):
        return ALERT_ENEMY[name]
    else:
        print(translate("gameTranslation", "unknownEnemy") + ": " + name)
        LogHandler.err(translate("gameTranslation", "unknownEnemy") + ": " + name)
        return get_last_item_with_backslash(name)
