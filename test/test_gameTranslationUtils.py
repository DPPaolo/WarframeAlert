# coding=utf-8
import unittest

from warframeAlert.services.optionHandlerService import OptionsHandler
from warframeAlert.utils.gameTranslationUtils import get_node, get_enemy_name, get_simaris_target, get_item_name, \
    get_faction, get_invasion_loctag


class TestGameTranslationsUtils(unittest.TestCase):
    NODE = "SolNode145"
    NODE_NOT_EXISTING = "SolNode789453"
    NODE_TRANSLATED_IT = ("Egeria", "(Cerere)")
    NODE_TRANSLATED_EN = ("Egeria", "(Ceres)")
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
    FACTION_NAME = "FC_INFESTATION"
    FACTION_NAME_TRANSLATED = "Infested"
    FACTION_NAME_UNKNOWN = "FC_GRINIIER"
    FACTION_NAME_NOT_FOUND = "FC_GRINIIER"
    LOC_TAG_NAME_IT = "/Lotus/Language/Menu/GrineerInvasionGeneric"
    LOC_TAG_NAME_IT_TRANSLATED = "Offensiva Grineer"
    LOC_TAG_NAME_EN = "/Lotus/Language/Menu/CorpusInvasionGeneric"
    LOC_TAG_NAME_EN_TRANSLATED = "Corpus Siege"
    LOC_TAG_NAME_UNKNOWN = "/Lotus/Language/Menu/SentientsInvasion"
    LOC_TAG_NAME_NOT_FOUND = "SentientsInvasion"

    def test_get_node_it_found(self):
        res = get_node(self.NODE)
        self.assertEqual(self.NODE_TRANSLATED_IT, res)

    def test_get_node_it_not_found(self):
        res = get_node(self.NODE_NOT_EXISTING)
        self.assertEqual(self.NODE_NOT_FOUND, res)

    def test_get_node_en_found(self):
        OptionsHandler.set_option("Language", "en")
        res = get_node(self.NODE)
        self.assertEqual(self.NODE_TRANSLATED_EN, res)
        OptionsHandler.set_option("Language", "it")

    def test_get_node_en_not_found(self):
        OptionsHandler.set_option("Language", "en")
        res = get_node(self.NODE_NOT_EXISTING)
        self.assertEqual(self.NODE_NOT_FOUND, res)
        OptionsHandler.set_option("Language", "it")

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

    def test_get_faction_found(self):
        res = get_faction(self.FACTION_NAME)
        self.assertEqual(self.FACTION_NAME_TRANSLATED, res)

    def test_get_faction_not_found(self):
        res = get_faction(self.FACTION_NAME_UNKNOWN)
        self.assertEqual(self.FACTION_NAME_NOT_FOUND, res)

    def test_get_loc_tag_it_found(self):
        res = get_invasion_loctag(self.LOC_TAG_NAME_IT)
        self.assertEqual(self.LOC_TAG_NAME_IT_TRANSLATED, res)

    def test_get_loc_tag_it_not_found(self):
        res = get_invasion_loctag(self.LOC_TAG_NAME_UNKNOWN)
        self.assertEqual(self.LOC_TAG_NAME_NOT_FOUND, res)

    def test_get_loc_tag_en_found(self):
        OptionsHandler.set_option("Language", "en")
        res = get_invasion_loctag(self.LOC_TAG_NAME_EN)
        self.assertEqual(self.LOC_TAG_NAME_EN_TRANSLATED, res)
        OptionsHandler.set_option("Language", "it")

    def test_get_loc_tag_en_not_found(self):
        OptionsHandler.set_option("Language", "en")
        res = get_invasion_loctag(self.LOC_TAG_NAME_UNKNOWN)
        self.assertEqual(self.LOC_TAG_NAME_NOT_FOUND, res)
        OptionsHandler.set_option("Language", "it")

