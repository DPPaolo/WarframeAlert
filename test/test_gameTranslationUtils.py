import unittest

from warframeAlert.utils.gameTranslationUtils import get_node, get_enemy_name


class TestGameTranslationsUtils(unittest.TestCase):
    NODE = "SolNode145"
    NODE_NOT_EXISTING = "SolNode789453"
    NODE_TRANSLATED = ("Egera", "(Cerere)")
    NODE_NOT_FOUND = (NODE_NOT_EXISTING), "(????)"
    ENEMY_NAME = "/Lotus/Types/Enemies/Grineer/AIWeek/ShieldLancer"
    ENEMY_NAME_UNKNOWN = "/Lotus/Types/Enemies/Grineer/AIWeek/RandomEnemy"
    ENEMY_TRANSLATED = "Shield Launcher"
    ENEMY_NOT_FOUND = "RandomEnemy"

    def test_get_node_found(self):
        res = get_node(self.NODE)
        self.assertEqual(self.NODE_TRANSLATED, res)

    def test_get_node_not_found(self):
        res = get_node(self.NODE_NOT_EXISTING)
        self.assertEqual(self.NODE_NOT_FOUND, res)

    def test_get_enemy_name_found(self):
        res = get_enemy_name(self.ENEMY_NAME)
        self.assertEqual(self.ENEMY_TRANSLATED, res)

    def test_get_enemy_name_not_found(self):
        res = get_enemy_name(self.ENEMY_NAME_UNKNOWN)
        self.assertEqual(self.ENEMY_NOT_FOUND, res)

