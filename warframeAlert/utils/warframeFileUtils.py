# coding=utf-8
import copy
import json
import lzma
from typing import List

import requests as requests

from warframeAlert.constants.files import MOBILE_MANIFEST_ID_SITE
from warframeAlert.constants.warframeFileTypes import RelicFile, BountyFileData, SortieFileData, \
    MissionFile, TransientFile, KeyFile, BpByItemFile, BpBySourceFile, ModByItemFile, ModBySourceFile
from warframeAlert.utils.fileUtils import get_separator, decompress_lzma
from warframeAlert.utils.warframeUtils import translate_item_from_drop_file, read_drop_file, \
    translate_mission_type_from_drop_file


def decompress_export_manifest_index() -> str:
    response = requests.get(MOBILE_MANIFEST_ID_SITE)
    if (response.status_code != 200):
        return ""
    data = response.content
    byte_data = bytes(data)
    length = len(data)
    stay = True
    decompressed_data = ""
    while stay:
        stay = False
        try:
            decompressed_data = decompress_lzma(byte_data[0:length])
        except lzma.LZMAError:
            length -= 1
            stay = True

    export_id = str(decompressed_data).replace("'", "").split("ExportManifest.json")[1]
    return "ExportManifest.json" + export_id


def write_json_drop() -> None:
    translate_sortie_drop()
    translate_free_roam_drop("cetus")
    translate_free_roam_drop("fortuna")
    translate_free_roam_drop("deimos")
    translate_relic_drop()
    translate_mission_drop()
    translate_key_drop()
    translate_transient_drop()
    translate_bp_by_item_drop()
    translate_bp_by_source_drop()
    translate_mod_by_item_drop()
    translate_mod_by_source_drop()


def translate_sortie_drop() -> None:
    json_data: SortieFileData = read_drop_file("sortie_en")

    new_json_data = {'sortieRewards': []}
    rewards = []

    for drop in json_data['sortieRewards']:
        new_reward = copy.deepcopy(drop)
        new_reward["itemName"] = translate_item_from_drop_file(drop['itemName'].upper())
        rewards.append(new_reward)
    new_json_data['sortieRewards'] = rewards

    json_data: str = json.dumps(new_json_data)
    fp = open("data" + get_separator() + "sortie_it.json", "w")
    fp.write(json_data)
    fp.flush()
    fp.close()


def translate_free_roam_drop(file_name: str) -> None:
    prefix = ""
    if (file_name == "cetus"):
        prefix = "cetusBountyRewards"
    elif (file_name == "fortuna"):
        prefix = "solarisBountyRewards"
    elif (file_name == "deimos"):
        prefix = "deimosRewards"
    # TODO: decomment when python 3.10 is ready
    # match file_name:
    #     case "cetus":
    #         prefix = "cetusBountyRewards"
    #     case "fortuna":
    #         prefix = "solarisBountyRewards"
    #     case "deimos":
    #         prefix = "deimosRewards"
    json_data: List[BountyFileData] = read_drop_file(file_name + "_en")[prefix]

    new_json_data = {prefix: []}

    for bounty_level in json_data:
        new_bounty_level = copy.deepcopy(bounty_level)

        for rotation_name in bounty_level["rewards"]:
            new_bounty_level["rewards"][rotation_name] = []
            rotation_rewards = []

            for drops in bounty_level["rewards"][rotation_name]:
                new_rotation_reward = drops
                new_rotation_reward["itemName"] = translate_item_from_drop_file(drops['itemName'].upper())
                rotation_rewards.append(new_rotation_reward)
            new_bounty_level["rewards"][rotation_name] = rotation_rewards

        new_json_data[prefix].append(new_bounty_level)

    json_data: str = json.dumps(new_json_data)
    fp = open("data" + get_separator() + file_name + "_it.json", "w")
    fp.write(json_data)
    fp.flush()
    fp.close()


def translate_relic_drop() -> None:
    json_data: RelicFile = read_drop_file("relic_en")

    new_json_data = {'relics': []}
    relics = []

    for relic in json_data['relics']:
        new_relic = copy.deepcopy(relic)
        new_relic["rewards"] = []
        relic_rewards = []
        for reward in relic['rewards']:
            new_relic_reward = reward
            new_relic_reward["itemName"] = translate_item_from_drop_file(reward['itemName'].upper())
            relic_rewards.append(new_relic_reward)
        new_relic["rewards"] = relic_rewards
        relics.append(new_relic)

    new_json_data['relics'] = relics

    json_data: str = json.dumps(new_json_data)
    fp = open("data" + get_separator() + "relic_it.json", "w")
    fp.write(json_data)
    fp.flush()
    fp.close()


def translate_mission_drop() -> None:
    json_data: MissionFile = read_drop_file("mission_en")

    new_json_data = {'missionRewards': {}}

    for planet in json_data['missionRewards']:
        new_planet = {}

        for mission in json_data['missionRewards'][planet]:
            new_mission = json_data['missionRewards'][planet][mission]
            new_mission['gameMode'] = translate_mission_type_from_drop_file(new_mission['gameMode'])

            rewards_list = []
            rewards_map = {}

            for reward in json_data['missionRewards'][planet][mission]['rewards']:

                if (reward in ["A", "B", "C"]):
                    rotation = json_data['missionRewards'][planet][mission]['rewards'][reward]

                    rotation_drops = []
                    for rotation_reward in rotation:
                        new_reward = rotation_reward
                        new_reward['itemName'] = translate_item_from_drop_file(rotation_reward['itemName'].upper())
                        rotation_drops.append(new_reward)

                    rewards_map[reward] = rotation_drops
                else:
                    new_reward = reward
                    new_reward['itemName'] = translate_item_from_drop_file(reward['itemName'].upper())
                    rewards_list.append(new_reward)

            if (rewards_list == []):
                new_mission['rewards'] = rewards_map
            else:
                new_mission['rewards'] = rewards_list

            new_planet[mission] = new_mission

        new_json_data['missionRewards'][planet] = new_planet

    json_data: str = json.dumps(new_json_data)
    fp = open("data" + get_separator() + "mission_it.json", "w")
    fp.write(json_data)
    fp.flush()
    fp.close()


def translate_key_drop() -> None:
    json_data: KeyFile = read_drop_file("key_en")

    new_json_data = {'keyRewards': []}

    for key_drop in json_data['keyRewards']:
        rewards_map = {}

        for reward in key_drop['rewards']:

            rotation = key_drop['rewards'][reward]

            rotation_drops = []
            for rotation_reward in rotation:
                new_reward = rotation_reward
                new_reward['itemName'] = translate_item_from_drop_file(rotation_reward['itemName'].upper())
                rotation_drops.append(new_reward)

            rewards_map[reward] = rotation_drops

        key_drop['rewards'] = rewards_map

        new_json_data['keyRewards'].append(key_drop)

    json_data: str = json.dumps(new_json_data)
    fp = open("data" + get_separator() + "key_it.json", "w")
    fp.write(json_data)
    fp.flush()
    fp.close()


def translate_transient_drop() -> None:
    json_data: TransientFile = read_drop_file("transient_en")

    new_json_data = {'transientRewards': []}

    for transient_drop in json_data['transientRewards']:
        rewards_list = []

        for reward in transient_drop['rewards']:
            new_reward = reward
            new_reward['itemName'] = translate_item_from_drop_file(reward['itemName'].upper())
            rewards_list.append(new_reward)

        transient_drop['rewards'] = rewards_list

        new_json_data['transientRewards'].append(transient_drop)

    json_data: str = json.dumps(new_json_data)
    fp = open("data" + get_separator() + "transient_it.json", "w")
    fp.write(json_data)
    fp.flush()
    fp.close()


def translate_bp_by_item_drop() -> None:
    json_data: BpByItemFile = read_drop_file("bp_by_item_en")

    new_json_data = {'blueprintLocations': []}

    for blueprint_drop in json_data['blueprintLocations']:
        blueprint_drop['itemName'] = translate_item_from_drop_file(blueprint_drop['itemName'].upper())
        blueprint_drop['blueprintName'] = translate_item_from_drop_file(blueprint_drop['blueprintName'].upper())
        new_json_data['blueprintLocations'].append(blueprint_drop)

    json_data: str = json.dumps(new_json_data)
    fp = open("data" + get_separator() + "bp_by_item_it.json", "w")
    fp.write(json_data)
    fp.flush()
    fp.close()


def translate_bp_by_source_drop() -> None:
    json_data: BpBySourceFile = read_drop_file("bp_by_source_en")

    new_json_data = {'enemyBlueprintTables': []}

    for blueprint_drop in json_data['enemyBlueprintTables']:
        rewards_list = []

        for reward in blueprint_drop['items']:
            new_reward = reward
            new_reward['itemName'] = translate_item_from_drop_file(reward['itemName'].upper())
            rewards_list.append(new_reward)

        blueprint_drop['items'] = rewards_list

        new_json_data['enemyBlueprintTables'].append(blueprint_drop)

    json_data: str = json.dumps(new_json_data)
    fp = open("data" + get_separator() + "bp_by_source_it.json", "w")
    fp.write(json_data)
    fp.flush()
    fp.close()


def translate_mod_by_item_drop() -> None:
    json_data: ModByItemFile = read_drop_file("mod_by_item_en")

    new_json_data = {'modLocations': []}

    for mod_drop in json_data['modLocations']:
        mod_drop['modName'] = translate_item_from_drop_file(mod_drop['modName'].upper())
        new_json_data['modLocations'].append(mod_drop)

    json_data: str = json.dumps(new_json_data)
    fp = open("data" + get_separator() + "mod_by_item_it.json", "w")
    fp.write(json_data)
    fp.flush()
    fp.close()


def translate_mod_by_source_drop() -> None:
    json_data: ModBySourceFile = read_drop_file("mod_by_source_en")

    new_json_data = {'enemyModTables': []}

    for mod_drop in json_data['enemyModTables']:
        rewards_list = []

        for reward in mod_drop['mods']:
            new_reward = reward
            new_reward['modName'] = translate_item_from_drop_file(reward['modName'].upper())
            rewards_list.append(new_reward)

        mod_drop['mods'] = rewards_list

        new_json_data['enemyModTables'].append(mod_drop)

    json_data: str = json.dumps(new_json_data)
    fp = open("data" + get_separator() + "mod_by_source_it.json", "w")
    fp.write(json_data)
    fp.flush()
    fp.close()
