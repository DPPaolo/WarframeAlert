# coding=utf-8
import unittest

from warframeAlert.utils.fileUtils import get_separator, check_file, delete_file
from warframeAlert.utils.warframeFileUtils import create_freeroam_drop, create_mission_drop, create_drop_by_item, \
    create_drop_by_source


class TestWarframeUtils(unittest.TestCase):

    def test_create_freeroam_drop_cetus(self):
        delete_file("data" + get_separator() + "cetus.json")
        fp = open("data" + get_separator() + "drop.html", "r")
        data = fp.readlines()[0]
        fp.close()

        data = data.split('<h3 id="cetusRewards">Cetus Bounty Rewards:</h3>')[1]
        cetus = data.split('<h3 id="solarisRewards">Orb Vallis Bounty Rewards:</h3>')[0]

        create_freeroam_drop(cetus, "cetus")
        self.assertEqual(check_file("cetus.json"), True)

    def test_create_freeroam_drop_fortuna(self):
        delete_file("data" + get_separator() + "fortuna.json")
        fp = open("data" + get_separator() + "drop.html", "r")
        data = fp.readlines()[0]
        fp.close()

        data = data.split('<h3 id="solarisRewards">Orb Vallis Bounty Rewards:</h3>')[1]
        fortuna = data.split('<h3 id="deimosRewards">Cambion Drift Bounty Rewards:</h3>')[0]

        create_freeroam_drop(fortuna, "fortuna")
        self.assertEqual(check_file("fortuna.json"), True)

    def test_create_freeroam_drop_deimos(self):
        delete_file("data" + get_separator() + "deimos.json")
        fp = open("data" + get_separator() + "drop.html", "r")
        data = fp.readlines()[0]
        fp.close()

        data = data.split('<h3 id="deimosRewards">Cambion Drift Bounty Rewards:</h3>')[1]
        deimos = data.split('<h3 id="modByAvatar">Mod Drops by Source:</h3>')[0]

        create_freeroam_drop(deimos, "deimos")
        self.assertEqual(check_file("deimos.json"), True)

    def test_create_mission_drop(self):
        delete_file("data" + get_separator() + "mission.json")
        fp = open("data" + get_separator() + "drop.html", "r")
        data = fp.readlines()[0]
        fp.close()

        data = data.split('<h3 id="missionRewards">Missions:</h3>')[1]
        mission = data.split('<h3 id="relicRewards">Relics:</h3>')[0]
        data = data.split('<h3 id="keyRewards">Keys:</h3>')[1]
        key = data.split('<h3 id="transientRewards">Dynamic Location Rewards:</h3>')[0]
        data = data.split('<h3 id="transientRewards">Dynamic Location Rewards:</h3>')[1]
        transient = data.split('<h3 id="sortieRewards">Sorties:</h3>')[0]

        create_mission_drop(mission, key, transient)
        self.assertEqual(check_file("mission.json"), True)

    def test_create_drop_by_item_mod_by_mod(self):
        delete_file("data" + get_separator() + "mod_by_item.json")
        fp = open("data" + get_separator() + "drop.html", "r")
        data = fp.readlines()[0]
        fp.close()

        data = data.split('<h3 id="modByDrop">Mod Drops by Mod:</h3>')[1]
        mod_by_mob = data.split('<h3 id="blueprintByAvatar">Blueprint/Item Drops by Source:</h3>')[0]

        create_drop_by_item(mod_by_mob, "mod_by_item")
        self.assertEqual(check_file("mod_by_item.json"), True)

    def test_create_drop_by_item_bp_by_bp(self):
        delete_file("data" + get_separator() + "bp_by_item.json")
        fp = open("data" + get_separator() + "drop.html", "r")
        data = fp.readlines()[0]
        fp.close()

        data = data.split('<h3 id="blueprintByDrop">Blueprint/Item Drops by Blueprint/Item:</h3>')[1]
        bp_by_bp = data.split('<h3 id="resourceByAvatar">Resource Drops by Source:</h3>')[0]

        create_drop_by_item(bp_by_bp, "bp_by_item")
        self.assertEqual(check_file("bp_by_item.json"), True)

    def test_create_drop_by_source_mod_by_enemy(self):
        delete_file("data" + get_separator() + "mod_by_source.json")
        fp = open("data" + get_separator() + "drop.html", "r")
        data = fp.readlines()[0]
        fp.close()

        data = data.split('<h3 id="modByAvatar">Mod Drops by Source:</h3>')[1]
        mod_by_enemy = data.split('<h3 id="modByDrop">Mod Drops by Mod:</h3>')[0]

        create_drop_by_source(mod_by_enemy, "mod_by_source")
        self.assertEqual(check_file("mod_by_source.json"), True)

    def test_create_drop_by_source_bp_by_enemy(self):
        delete_file("data" + get_separator() + "bp_by_source.json")
        fp = open("data" + get_separator() + "drop.html", "r")
        data = fp.readlines()[0]
        fp.close()

        data = data.split('<h3 id="blueprintByAvatar">Blueprint/Item Drops by Source:</h3>')[1]
        bp_by_enemy = data.split('<h3 id="blueprintByDrop">Blueprint/Item Drops by Blueprint/Item:</h3>')[0]

        create_drop_by_source(bp_by_enemy, "mod_by_source")
        self.assertEqual(check_file("mod_by_source.json"), True)

    def test_create_drop_by_source_resource_by_resource(self):
        delete_file("data" + get_separator() + "resource_by_source.json")
        fp = open("data" + get_separator() + "drop.html", "r")
        data = fp.readlines()[0]
        fp.close()

        data = data.split('<h3 id="resourceByAvatar">Resource Drops by Source:</h3>')[1]
        resource_by_resource = data.split('<h3 id="sigilByAvatar">Sigil Drops by Source:</h3>')[0]

        create_drop_by_source(resource_by_resource, "resource_by_source")
        self.assertEqual(check_file("resource_by_source.json"), True)

    def test_create_drop_by_source_sigil_by_source(self):
        delete_file("data" + get_separator() + "sigil_by_source.json")
        fp = open("data" + get_separator() + "drop.html", "r")
        data = fp.readlines()[0]
        fp.close()

        data = data.split('<h3 id="sigilByAvatar">Sigil Drops by Source:</h3>')[1]
        sigil_by_enemy = data.split('<h3 id="additionalItemByAvatar">Additional Item Drops by Source:</h3>')[0]

        create_drop_by_source(sigil_by_enemy, "sigil_by_source")
        self.assertEqual(check_file("sigil_by_source.json"), True)

    def test_create_drop_by_source_extra_by_source(self):
        delete_file("data" + get_separator() + "extra_by_source.json")
        fp = open("data" + get_separator() + "drop.html", "r")
        data = fp.readlines()[0]
        fp.close()

        extra_by_enemy = data.split('<h3 id="additionalItemByAvatar">Additional Item Drops by Source:</h3>')[1]

        create_drop_by_source(extra_by_enemy, "extra_by_source")
        self.assertEqual(check_file("extra_by_source.json"), True)
