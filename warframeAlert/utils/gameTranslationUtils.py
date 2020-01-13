from warframeAlert import warframeData
from warframeAlert.services.translationService import translate
from warframeAlert.utils.logUtils import LogHandler


def get_node(name):
    if (name in warframeData.NODE_NAME_IT):
        return warframeData.NODE_NAME_IT[name][0], "(" + warframeData.NODE_NAME_IT[name][1] + ")"
    elif (name == ""):
        return "", "(????)"
    else:
        print("Nodo non tradotto: " + name)
        LogHandler.err(translate("gameTranslation", "unknownNode") + ": " + name)
        return name, "(????)"
