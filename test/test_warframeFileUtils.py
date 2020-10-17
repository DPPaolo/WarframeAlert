# coding=utf-8
import unittest

from warframeAlert.utils.fileUtils import get_separator, check_file, delete_file
from warframeAlert.utils.warframeFileUtils import create_freeroam_drop, create_mission_drop


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


