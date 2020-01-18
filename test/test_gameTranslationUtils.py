import unittest

from warframeAlert.services.optionHandlerService import OptionsHandler
from warframeAlert.utils.gameTranslationUtils import get_node, get_enemy_name, get_simaris_target, get_item_name


class TestGameTranslationsUtils(unittest.TestCase):
    NODE = "SolNode145"
    NODE_NOT_EXISTING = "SolNode789453"
    NODE_TRANSLATED = ("Egera", "(Cerere)")
    NODE_NOT_FOUND = (NODE_NOT_EXISTING), "(????)"
    ENEMY_NAME = "/Lotus/Types/Enemies/Grineer/AIWeek/ShieldLancer"
    ENEMY_NAME_UNKNOWN = "/Lotus/Types/Enemies/Grineer/AIWeek/RandomEnemy"
    ENEMY_TRANSLATED = "Shield Launcher"
    ENEMY_NOT_FOUND = "RandomEnemy"
    SYMARIS_TARGET = "/Lotus/Types/Game/Library/Targets/Research7Target"
    SYMARIS_TARGET_TRANSLATED = "Guardsman"
    SYMARIS_TARGET_UNKNOWN = "/Lotus/Types/Game/Library/Targets/Research0Target"
    SYMARIS_TARGET_NOT_FOUND = "Research0Target"
    ITEM_NAME = "/Lotus/StoreItems/Types/Items/MiscItems/FormaAura"
    ITEM_NAME_TRANSLATED = "Forma Aura"
    ITEM_NAME_UNKNOWN = "/Lotus/Types/Items/MiscItems/FormaSpecial"
    ITEM_NAME_NOT_FOUND = "FormaSpecial"
    ITEM_NAME_EN = "/Lotus/StoreItems/Upgrades/Focus/PowerLensGreater"
    ITEM_NAME_TRANSLATED_EN = "Greater Zenurik Lens"

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

    def test_get_simaris_target_found(self):
        res = get_simaris_target(self.SYMARIS_TARGET)
        self.assertEqual(self.SYMARIS_TARGET_TRANSLATED, res)

    def test_get_simaris_target_not_found(self):
        res = get_simaris_target(self.SYMARIS_TARGET_UNKNOWN)
        self.assertEqual(self.SYMARIS_TARGET_NOT_FOUND, res)

    def test_get_item_name_found_it(self):
        res = get_item_name(self.ITEM_NAME)
        self.assertEqual(self.ITEM_NAME_TRANSLATED, res)

    def test_get_get_item_name_not_found_it(self):
        res = get_item_name(self.ITEM_NAME_UNKNOWN)
        self.assertEqual(self.ITEM_NAME_NOT_FOUND, res)

    def test_get_item_name_found_en(self):
        OptionsHandler.set_option("Language", "en")
        res = get_item_name(self.ITEM_NAME_EN)
        self.assertEqual(self.ITEM_NAME_TRANSLATED_EN, res)
        OptionsHandler.set_option("Language", "it")

    def test_get_get_item_name_not_found_en(self):
        OptionsHandler.set_option("Language", "en")
        res = get_item_name(self.ITEM_NAME_UNKNOWN)
        self.assertEqual(self.ITEM_NAME_NOT_FOUND, res)
        OptionsHandler.set_option("Language", "it")

