# coding=utf-8
import copy
import json

from warframeAlert.utils.fileUtils import get_separator
from warframeAlert.utils.warframeUtils import translate_item_from_drop_file, read_drop_file


def write_json_drop():
    translate_sortie_drop()
    translate_free_roam_drop("cetus")
    translate_free_roam_drop("fortuna")
    translate_free_roam_drop("deimos")
    translate_relic_drop()
    translate_mission_drop()
    translate_key_drop()
    translate_transient_drop()
    translate_misc_drop()
    translate_bp_by_item_drop()
    translate_bp_by_source_drop()
    translate_mod_by_item_drop()
    translate_mod_by_source_drop()


def translate_sortie_drop():
    json_data = read_drop_file("sortie_en")

    new_json_data = {'sortieRewards': []}
    rewards = []

    for drop in json_data['sortieRewards']:
        new_reward = copy.deepcopy(drop)
        new_reward["itemName"] = translate_item_from_drop_file(drop['itemName'].upper())
        rewards.append(new_reward)
    new_json_data['sortieRewards'] = rewards

    json_data = json.dumps(new_json_data)
    fp = open("data" + get_separator() + "sortie_it.json", "w")
    fp.write(json_data)
    fp.flush()
    fp.close()


def translate_free_roam_drop(file_name):
    json_data = read_drop_file(file_name + "_en")
    prefix = file_name
    if (file_name == "cetus"):
        prefix = "cetusBountyRewards"
    elif (file_name == "fortuna"):
        prefix = "solarisBountyRewards"
    elif (file_name == "deimos"):
        prefix = "deimosRewards"
    json_data = json_data[prefix]

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

    json_data = json.dumps(new_json_data)
    fp = open("data" + get_separator() + file_name + "_it.json", "w")
    fp.write(json_data)
    fp.flush()
    fp.close()


def translate_relic_drop():
    json_data = read_drop_file("relic_en")

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

    json_data = json.dumps(new_json_data)
    fp = open("data" + get_separator() + "relic_it.json", "w")
    fp.write(json_data)
    fp.flush()
    fp.close()


def translate_mission_drop():
    # TODO: parse the file
    json_data = read_drop_file("mission" + "_en")


def translate_key_drop():
    # TODO: parse the file
    json_data = read_drop_file("key" + "_en")


def translate_transient_drop():
    # TODO: parse the file
    json_data = read_drop_file("transient" + "_en")


def translate_misc_drop():
    # TODO: parse the file
    json_data = read_drop_file("misc" + "_en")


def translate_bp_by_item_drop():
    # TODO: parse the file
    json_data = read_drop_file("bp_by_item" + "_en")


def translate_bp_by_source_drop():
    # TODO: parse the file
    json_data = read_drop_file("bp_by_source" + "_en")


def translate_mod_by_item_drop():
    # TODO: parse the file
    json_data = read_drop_file("mod_by_item" + "_en")


def translate_mod_by_source_drop():
    # TODO: parse the file
    json_data = read_drop_file("mod_by_source" + "_en")
