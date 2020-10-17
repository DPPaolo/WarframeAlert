# coding=utf-8
import json
from enum import Enum

from warframeAlert import warframeData
from warframeAlert.components.common.MessageBox import MessageBox, MessageBoxType
from warframeAlert.services.translationService import translate
from warframeAlert.utils import commonUtils
from warframeAlert.utils.fileUtils import get_separator
from warframeAlert.utils.warframeUtils import translate_item_from_drop_file, translate_mission_name_from_drop_file


class StageTypeEnum(Enum):
    START = 0
    MISSION_NAME = 1
    ROTATION_NAME = 2
    STAGE_NAME = 3
    DROP = 4


StageName = [
    "Rotation",
    "Completion"
]


def write_json_drop():
    try:
        fp = open("data" + get_separator() + warframeData.OTHER_FILE_NAME[0], "r")
    except Exception as err:
        error_message = "File " + warframeData.OTHER_FILE_NAME[0] + translate("warframeFileUtils", "notFound")
        MessageBox("", error_message, MessageBoxType.ERROR)
        commonUtils.print_traceback(error_message + ":\n  " + str(err))
        return

    data = fp.readlines()[0]
    fp.close()

    # Mission Rewards
    data = data.split('<h3 id="missionRewards">Missions:</h3>')[1]
    mission = data.split('<h3 id="relicRewards">Relics:</h3>')[0]
    # Relics
    data = data.split('<h3 id="relicRewards">Relics:</h3>')[1]
    relics = data.split('<h3 id="keyRewards">Keys:</h3>')[0]
    # Key Rewards
    data = data.split('<h3 id="keyRewards">Keys:</h3>')[1]
    key = data.split('<h3 id="transientRewards">Dynamic Location Rewards:</h3>')[0]
    # Dynamic Location Rewards (multiple drop from various source)
    data = data.split('<h3 id="transientRewards">Dynamic Location Rewards:</h3>')[1]
    transient = data.split('<h3 id="sortieRewards">Sorties:</h3>')[0]
    # Sortie Rewards
    data = data.split('<h3 id="sortieRewards">Sorties:</h3>')[1]
    sortie = data.split('<h3 id="cetusRewards">Cetus Bounty Rewards:</h3>')[0]
    # Cetus Rewards
    data = data.split('<h3 id="cetusRewards">Cetus Bounty Rewards:</h3>')[1]
    cetus = data.split('<h3 id="solarisRewards">Orb Vallis Bounty Rewards:</h3>')[0]
    # Fortuna Rewards
    data = data.split('<h3 id="solarisRewards">Orb Vallis Bounty Rewards:</h3>')[1]
    fortuna = data.split('<h3 id="deimosRewards">Cambion Drift Bounty Rewards:</h3>')[0]
    # Deimos Rewards
    data = data.split('<h3 id="deimosRewards">Cambion Drift Bounty Rewards:</h3>')[1]
    deimos = data.split('<h3 id="modByAvatar">Mod Drops by Source:</h3>')[0]
    # # Mod Drops by Enemy
    # data = data.split('<h3 id="modByAvatar">Mod Drops by Source:</h3>')[1]
    # mod_by_enemy = data.split('<h3 id="modByDrop">Mod Drops by Mod:</h3>')[0]
    # # Mod Drops by Mod
    # data = data.split('<h3 id="modByDrop">Mod Drops by Mod:</h3>')[1]
    # mod_by_mob = data.split('<h3 id="blueprintByAvatar">Blueprint/Item Drops by Source:</h3>')[0]
    # # BP Drops by Enemy
    # data = data.split('<h3 id="blueprintByAvatar">Blueprint/Item Drops by Source:</h3>')[1]
    # bp_by_enemy = data.split('<h3 id="blueprintByDrop">Blueprint/Item Drops by Blueprint/Item::</h3>')[0]
    # # BP Drops by BP
    # data = data.split('<h3 id="blueprintByDrop">Blueprint/Item Drops by Blueprint/Item:</h3>')[1]
    # bp_by_bp = data.split('<h3 id="resourceByAvatar">Resource Drops by Source:</h3>')[0]
    # # Resource Drops by Enemy
    # data = data.split('<h3 id="resourceByAvatar">Resource Drops by Source:</h3>')[1]
    # resource_by_resource = data.split('<h3 id="sigilByAvatar">Sigil Drops by Source:</h3>')[0]
    # # Sigil Drop by Enemy
    # data = data.split('<h3 id="sigilByAvatar">Sigil Drops by Source:</h3>')[1]
    # sigil_per_enemy = data.split('<h3 id="additionalItemByAvatar">Additional Item Drops by Source:</h3>')[0]
    # # Extra Drop by Enemy
    # extra_per_enemy = data.split('<h3 id="additionalItemByAvatar">Additional Item Drops by Source:</h3>')[1]

    try:
        create_sortie_drop(sortie)
    except Exception as err:
        commonUtils.print_traceback(translate("warframeFileUtils", "errorSortie") + ":\n" + str(err))
        return
    try:
        create_freeroam_drop(cetus, "cetus")
    except Exception as err:
        commonUtils.print_traceback(translate("warframeFileUtils", "errorCetus") + ":\n" + str(err))
        return
    try:
        create_freeroam_drop(fortuna, "fortuna")
    except Exception as err:
        commonUtils.print_traceback(translate("warframeFileUtils", "errorFortuna") + ":\n" + str(err))
        return
    try:
        create_freeroam_drop(deimos, "deimos")
    except Exception as err:
        commonUtils.print_traceback(translate("warframeFileUtils", "errorDeimos") + ":\n" + str(err))
        return
    try:
        create_relic_drop(relics)
    except Exception as err:
        commonUtils.print_traceback(translate("warframeFileUtils", "errorRelics") + ":\n" + str(err))
        return
    try:
        create_mission_drop(mission, key, transient)
    except Exception as err:
        commonUtils.print_traceback(translate("warframeFileUtils", "errorDropMission") + ":\n" + str(err))
        return

    # mod_by_enemy
    # mod_by_mod
    # bp_by_enemy
    # bp_by_bp
    # resoruce_by_enemy
    # resource_by_resource
    # sigil_per_enemy
    # extra_per_enemy


def create_sortie_drop(data):
    data = data.replace("/", "").replace("<table>", "")
    data = data.split('<tr>')
    sorties = {}
    sortie = []
    for line in data:
        if ('<td>' in line):
            line = line.split("<td>")
            item = {"name_it": translate_item_from_drop_file(line[1].upper()), "name_en": line[1], "rarity": line[3]}
            sortie.append(item)
    sorties["Sortie"] = sortie
    json_data = json.dumps(sorties)
    fp = open("data" + get_separator() + "sortie.json", "w")
    fp.write(json_data)
    fp.flush()
    fp.close()


def create_freeroam_drop(data, name):
    data = data.replace("/", "").replace("<table>", "")
    data = data.split('<tr>')
    data = [value for value in data if value != '']

    bounty_reward = {'bounty': []}
    rewards = {'rotations': {}}
    level_stage = ""
    stage_name = ""
    rotation_name = ""
    stage = []

    actual_stage = StageTypeEnum.START
    for line in data:
        if ('blank-row' in line):
            continue
        # Check if drops are finished
        if (actual_stage == StageTypeEnum.DROP):
            if ('pad-cell' in line):  # drop finished for the stage
                if (stage != []):
                    rewards['rotations'][rotation_name][stage_name] = stage
                actual_stage = StageTypeEnum.STAGE_NAME
            elif (any(elem in line for elem in StageName)):  # drop finished for the rotation
                if (stage != []):
                    rewards['rotations'][rotation_name][stage_name] = stage
                actual_stage = StageTypeEnum.ROTATION_NAME
            elif ('<th>' in line):  # drop finished for level
                if (stage != []):
                    rewards['rotations'][rotation_name][stage_name] = stage
                rewards['level'] = level_stage
                bounty_reward['bounty'].append(rewards)
                rewards = {'rotations': {}}
                actual_stage = StageTypeEnum.START

        if (actual_stage == StageTypeEnum.START and '<th' in line and
                '<td><th' not in line and not any(elem in line for elem in StageName)):
            # Name of the level of the drop
            level_stage = line.replace(" ", "").split(">")[1].split("<")[0].replace("Level", "").replace("Bounty", "")
            actual_stage = StageTypeEnum.ROTATION_NAME
            continue

        if (actual_stage == StageTypeEnum.ROTATION_NAME and any(elem in line for elem in StageName)):
            # Name of the rotation of the drop
            if ('Rotation' in line):
                rotation_name = line[-5]
            else:
                rotation_name = line.split(">")[1].split("<")[0]
            rewards['rotations'][rotation_name] = {}
            actual_stage = StageTypeEnum.STAGE_NAME
            continue

        if (actual_stage == StageTypeEnum.STAGE_NAME):
            # Name of the stage of the drop
            stage_name = line.split('>')[-2].split('<th')[0]
            actual_stage = StageTypeEnum.DROP
            stage = []
            continue

        if (actual_stage == StageTypeEnum.DROP):
            line = line.split('<td>')
            item = {"name_it": translate_item_from_drop_file(line[3].upper()), "name_en": line[3], "rarity": line[5]}
            stage.append(item)

    # add the last rotation to the rewards
    rewards['rotations'][rotation_name][stage_name] = stage
    rewards['level'] = level_stage
    # add the last rewards before saving to file
    bounty_reward['bounty'].append(rewards)

    # save the file with the drop
    json_data = json.dumps(bounty_reward)
    fp = open("data" + get_separator() + name + ".json", "w")
    fp.write(json_data)
    fp.flush()
    fp.close()


def create_relic_drop(data):
    data = data.replace("/", "").replace("<table>", "")
    data = data.split('<tr>')
    name = ""
    relic_type = ""
    items = []
    item = {}
    relic_reward = {'relic': {}}
    for line in data:
        if (line == ""):
            continue
        if ('class="blank-row"' in line):
            relic_reward['relic'][name][relic_type] = items
        if ('<th>' in line):
            if ('Relic' in line):
                # name and grade of relic
                name = line.split(">")[1].split(" (")[0].replace(" Relic", "")
                relic_type = line.split("(")[1].split(")")[0]
                if (name not in relic_reward['relic']):
                    relic_reward['relic'][name] = {}
                items = []
        elif ('<td>' in line and 'class="blank-row"' not in line):
            line = line.split('<td>')
            item = {"name_it": translate_item_from_drop_file(line[1].upper()), "name_en": line[1],
                    "rarity": line[3].split("(")[1].split(")")[0]}
            items.append(item)

    items.append(item)
    relic_reward['relic'][name][relic_type] = items

    json_data = json.dumps(relic_reward)
    fp = open("data" + get_separator() + "relic.json", "w")
    fp.write(json_data)
    fp.flush()
    fp.close()


def create_mission_drop(mission, key, transient):
    mission = mission.replace("<table>", "")
    mission = mission.split('<tr>')
    key = key.replace("<table>", "")
    key = key.split('<tr>')
    transient = transient.replace("<table>", "")
    transient = transient.split('<tr>')

    mission = [value for value in mission if value != '']
    key = [value for value in key if value != '']
    transient = [value for value in transient if value != '']
    data = mission + key + transient

    # {
    #     "reward": [
    #         {
    #             "planet": "Mercurio",
    #             "node": "Apollodorus",
    #             "missionType": "Sopravvivenza",
    #             "rewards": { <-- se non c'è la rotation vi è direttamente una lista
    #                 "A" : []
    #             }
    #         },
    # }

    mission_reward = {'reward': []}
    mission = {'planet': "", 'node': "", 'missionType': "", 'reward': []}
    mission_drop = {}
    rotation_name = ""

    new_data = []
    for line in data:
        if ('blank-row' in line and "id=" in line):
            line = line.split("<th colspan=\"2\"")
            new_data.append(line[0])
            new_data.append(line[1])
        else:
            new_data.append(line)

    data = new_data

    actual_stage = StageTypeEnum.MISSION_NAME
    for line in data:
        # Check if drops are finished
        if (actual_stage == StageTypeEnum.DROP):
            if ('Rotation' in line):  # drop finished for rotation
                mission['rewards'] = mission_drop
                actual_stage = StageTypeEnum.ROTATION_NAME
            elif (('<th' in line or '</th></tr>' in line) and 'Rotation' not in line):  # drop finished for the mission
                mission['rewards'] = mission_drop
                mission_reward['reward'].append(mission)
                actual_stage = StageTypeEnum.MISSION_NAME
        elif (actual_stage == StageTypeEnum.MISSION_NAME):
            if ('Rotation' in line):
                actual_stage = StageTypeEnum.ROTATION_NAME
            elif ('<td>' in line):
                rotation_name = translate("warframeUtils", "noRotation")
                mission_drop = {rotation_name: []}
                actual_stage = StageTypeEnum.DROP

        if (actual_stage == StageTypeEnum.MISSION_NAME and ('<th' in line or '</th></tr>' in line)):
            mission = {}
            mission_drop = {}

            # Name of the mission of the drop
            mission_name = line.split(">")[1].split("<")[0]
            planet, node, mission_type = translate_mission_name_from_drop_file(mission_name)
            mission['planet'] = planet
            mission['node'] = node
            mission['missionType'] = mission_type
            mission['rewards'] = {}
            continue

        if (actual_stage == StageTypeEnum.ROTATION_NAME):
            # Name of the rotation of the drop
            rotation_name = line.split(">Rotation ")[1][0]
            actual_stage = StageTypeEnum.DROP
            mission_drop[rotation_name] = []
            continue

        if (actual_stage == StageTypeEnum.DROP):
            line = line.replace("/", "")
            line = line.split('<td>')
            item = {"name_it": translate_item_from_drop_file(line[1].upper()), "name_en": line[1], "rarity": line[3]}
            mission_drop[rotation_name].append(item)
            continue

    mission['rewards'] = mission_drop
    mission_reward['reward'].append(mission)

    json_data = json.dumps(mission_reward)
    fp = open("data" + get_separator() + "mission.json", "w")
    fp.write(json_data)
    fp.flush()
    fp.close()
