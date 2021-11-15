# coding=utf-8
from warframeAlert.services.optionHandlerService import OptionsHandler
from warframeAlert.utils.gameTranslationUtils import get_node, get_enemy_name, get_simaris_target, get_item_name, \
    get_faction, get_invasion_loc_tag, get_acolyte_name, get_region, get_upgrade_type


class TestGameTranslationsUtils():
    NODE = "SolNode145"
    NODE_NOT_EXISTING = "SolNode789453"
    NODE_TRANSLATED_IT = ("Egeria", "(Cerere)")
    NODE_TRANSLATED_EN = ("Egeria", "(Ceres)")
    NODE_NOT_FOUND = (NODE_NOT_EXISTING), "(????)"
    ITEM_NAME_UNKNOWN = "/Lotus/Types/Items/MiscItems/FormaSpecial"
    ITEM_NAME_NOT_FOUND = "FormaSpecial"
    LOC_TAG_NAME_IT = "/Lotus/Language/Menu/GrineerInvasionGeneric"
    LOC_TAG_NAME_IT_TRANSLATED = "Offensiva Grineer"
    LOC_TAG_NAME_EN = "/Lotus/Language/Menu/CorpusInvasionGeneric"
    LOC_TAG_NAME_EN_TRANSLATED = "Corpus Siege"
    LOC_TAG_NAME_UNKNOWN = "/Lotus/Language/Menu/SentientsInvasion"
    LOC_TAG_NAME_NOT_FOUND = "SentientsInvasion"
    UPGRADE_TYPE = "GAMEPLAY_PICKUP_AMOUNT"
    UPGRADE_TYPE_IT = "Bonus Drop Risorse"
    UPGRADE_TYPE_EN = "Resource Drop Chance"

    def test_get_node_it_found(self) -> None:
        res = get_node(self.NODE)
        assert self.NODE_TRANSLATED_IT == res

    def test_get_node_it_not_found(self) -> None:
        res = get_node(self.NODE_NOT_EXISTING)
        assert self.NODE_NOT_FOUND == res

    def test_get_node_en_found(self) -> None:
        OptionsHandler.set_option("Language", "en")
        res = get_node(self.NODE)
        assert self.NODE_TRANSLATED_EN == res
        OptionsHandler.set_option("Language", "it")

    def test_get_node_en_not_found(self) -> None:
        OptionsHandler.set_option("Language", "en")
        res = get_node(self.NODE_NOT_EXISTING)
        assert self.NODE_NOT_FOUND == res
        OptionsHandler.set_option("Language", "it")

    def test_get_enemy_name_found(self) -> None:
        self.ENEMY_NAME = "/Lotus/Types/Enemies/Grineer/AIWeek/ShieldLancer"
        self.ENEMY_TRANSLATED = "Shield Launcher"
        res = get_enemy_name(self.ENEMY_NAME)
        assert self.ENEMY_TRANSLATED == res

    def test_get_enemy_name_not_found(self) -> None:
        self.ENEMY_NAME_UNKNOWN = "/Lotus/Types/Enemies/Grineer/AIWeek/RandomEnemy"
        self.ENEMY_NOT_FOUND = "RandomEnemy"
        res = get_enemy_name(self.ENEMY_NAME_UNKNOWN)
        assert self.ENEMY_NOT_FOUND == res

    def test_get_simaris_target_found(self) -> None:
        self.SYMARIS_TARGET = "/Lotus/Types/Game/Library/Targets/Research7Target"
        self.SYMARIS_TARGET_TRANSLATED = "Guardsman"
        res = get_simaris_target(self.SYMARIS_TARGET)
        assert self.SYMARIS_TARGET_TRANSLATED == res

    def test_get_simaris_target_not_found(self) -> None:
        self.SYMARIS_TARGET_UNKNOWN = "/Lotus/Types/Game/Library/Targets/Research0Target"
        self.SYMARIS_TARGET_NOT_FOUND = "Research0Target"
        res = get_simaris_target(self.SYMARIS_TARGET_UNKNOWN)
        assert self.SYMARIS_TARGET_NOT_FOUND == res

    def test_get_item_name_found_it(self) -> None:
        self.ITEM_NAME = "/Lotus/StoreItems/Types/Items/MiscItems/FormaAura"
        self.ITEM_NAME_TRANSLATED = "Forma Aura"
        res = get_item_name(self.ITEM_NAME)
        assert self.ITEM_NAME_TRANSLATED == res

    def test_get_get_item_name_not_found_it(self) -> None:
        res = get_item_name(self.ITEM_NAME_UNKNOWN)
        assert self.ITEM_NAME_NOT_FOUND == res

    def test_get_item_name_found_en(self) -> None:
        self.ITEM_NAME_EN = "/Lotus/StoreItems/Upgrades/Focus/PowerLensGreater"
        self.ITEM_NAME_TRANSLATED_EN = "Greater Zenurik Lens"
        OptionsHandler.set_option("Language", "en")
        res = get_item_name(self.ITEM_NAME_EN)
        assert self.ITEM_NAME_TRANSLATED_EN == res
        OptionsHandler.set_option("Language", "it")

    def test_get_get_item_name_not_found_en(self) -> None:
        OptionsHandler.set_option("Language", "en")
        res = get_item_name(self.ITEM_NAME_UNKNOWN)
        assert self.ITEM_NAME_NOT_FOUND == res
        OptionsHandler.set_option("Language", "it")

    def test_get_faction_found(self) -> None:
        self.FACTION_NAME = "FC_INFESTATION"
        self.FACTION_NAME_TRANSLATED = "Infested"
        res = get_faction(self.FACTION_NAME)
        assert self.FACTION_NAME_TRANSLATED == res

    def test_get_faction_not_found(self) -> None:
        self.FACTION_NAME_UNKNOWN = "FC_GRINIIER"
        self.FACTION_NAME_NOT_FOUND = "FC_GRINIIER"
        res = get_faction(self.FACTION_NAME_UNKNOWN)
        assert self.FACTION_NAME_NOT_FOUND == res

    def test_get_loc_tag_it_found(self) -> None:
        res = get_invasion_loc_tag(self.LOC_TAG_NAME_IT)
        assert self.LOC_TAG_NAME_IT_TRANSLATED == res

    def test_get_loc_tag_it_not_found(self) -> None:
        res = get_invasion_loc_tag(self.LOC_TAG_NAME_UNKNOWN)
        assert self.LOC_TAG_NAME_NOT_FOUND == res

    def test_get_loc_tag_en_found(self) -> None:
        OptionsHandler.set_option("Language", "en")
        res = get_invasion_loc_tag(self.LOC_TAG_NAME_EN)
        assert self.LOC_TAG_NAME_EN_TRANSLATED == res
        OptionsHandler.set_option("Language", "it")

    def test_get_loc_tag_en_not_found(self) -> None:
        OptionsHandler.set_option("Language", "en")
        res = get_invasion_loc_tag(self.LOC_TAG_NAME_UNKNOWN)
        assert self.LOC_TAG_NAME_NOT_FOUND == res
        OptionsHandler.set_option("Language", "it")

    def test_get_accolyte_name_found(self) -> None:
        self.ACCOLYTE_NAME = "/Lotus/Types/Enemies/Acolytes/StrikerAcolyteAgent"
        self.ACCOLYTE_NAME_TRANSLATED = "Angst"
        res = get_acolyte_name(self.ACCOLYTE_NAME)
        assert self.ACCOLYTE_NAME_TRANSLATED == res

    def test_get_accolyte_name_not_found(self) -> None:
        self.ACCOLYTE_NAME_UNKNOWN = "/Lotus/Types/Enemies/Acolytes/GuardianAcolyteAgent"
        self.ACCOLYTE_NAME_NOT_FOUND = "GuardianAcolyteAgent"
        res = get_acolyte_name(self.ACCOLYTE_NAME_UNKNOWN)
        assert self.ACCOLYTE_NAME_NOT_FOUND == res

    def test_get_region_it_found(self) -> None:
        res = get_region(4)
        assert "Giove" == res

    def test_get_region_it_not_found(self) -> None:
        res = get_region(-2)
        assert "-2" == res

    def test_get_region_en_found(self) -> None:
        OptionsHandler.set_option("Language", "en")
        res = get_region(4)
        assert "Jupiter" == res
        OptionsHandler.set_option("Language", "it")

    def test_get_upgrade_type_it(self) -> None:
        res = get_upgrade_type(self.UPGRADE_TYPE)
        assert self.UPGRADE_TYPE_IT == res

    def test_get_upgrade_type_en(self) -> None:
        OptionsHandler.set_option("Language", "en")
        res = get_upgrade_type(self.UPGRADE_TYPE)
        assert self.UPGRADE_TYPE_EN == res
        OptionsHandler.set_option("Language", "it")
