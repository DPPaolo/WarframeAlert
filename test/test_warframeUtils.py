# coding=utf-8
from unittest.mock import patch

from PyQt6 import QtWidgets

from warframeAlert.constants.warframeTypes import MissionReward
from warframeAlert.services.optionHandlerService import OptionsHandler
from warframeAlert.utils.warframeUtils import get_image_path_from_name, get_weapon_part, get_weapon_type, \
    parse_reward, get_operation_type, get_bounty_reward, read_drop_file, get_reward_from_sortie, \
    get_relic_tier_from_name, get_relic_item, get_relic_drop_from_name, add_all_relic_from_file, \
    add_all_relic_item_from_file, get_all_relic_from_file, get_relic_rarity_from_percent, get_relic_drop, \
    translate_planet_from_drop_file, translate_mission_type_from_drop_file, translate_focus_lens, \
    translate_prime_part, translate_warframe_part, translate_weapon_parts


class TestWarframeUtils():
    IMAGE_NAME = "Stock"
    IMAGE_NAME_FOUND = "/Lotus/Interface/Icons/Store/GenericGunStock.png"
    IMAGE_NAME_UNKNOWN = "Sword"
    IMAGE_NAME_NOT_FOUND = "Sword"
    WEAPON_PART_UNKOWN = "/Lotus/Interface/Icons/Store/GenericWeaponPart.png"
    WEAPON_PART_NOT_FOUND = "Unknown"
    WEAPON_TYPE_UNKOWN = "/Lotus/Interface/Icons/Store/GlaxionVandal.png"
    WEAPON_TYPE_NOT_FOUND = "Unknown"
    REWARDS_COUNTED_ITEMS_ONLY: MissionReward = {'countedItems': [
                                                    {'ItemType': '/Lotus/Types/Items/Research/EnergyComponent',
                                                     'ItemCount': 3}]}
    REWARDS_CREDITS_ONLY: MissionReward = {'credits': 3000}
    REWARDS_ITEMS_ONLY: MissionReward = {'items': ['/Lotus/StoreItems/Weapons/Tenno/Pistols/DexFuris/DexFuris']}
    REWARDS_ALMOUST_COMPLETE: MissionReward = {'credits': 0,
                                               'xp': 0,
                                               'items': [
                                                   '/Lotus/StoreItems/Upgrades/Mods/DualSource/Shotgun/ShotgunMedicMod',
                                                   '/Lotus/StoreItems/Upgrades/Mods/DualSource/Rifle/SerratedRushMod'],
                                               'countedItems': []}
    REWARDS_COMPLETE: MissionReward = {
        "credits": 1000,
        "xp": 500,
        "randomizedItems": "/Lotus/Types/Game/MissionDecks/SortieRewards",
        "items": ["/Lotus/StoreItems/Weapons/Corpus/LongGuns/CrpBFG/Vandal/VandalCrpBFG"],
        "countedItems": [{"ItemType": "/Lotus/Types/Items/Research/EnergyComponent", "ItemCount": 3}],
        "countedStoreItems": [{"StoreItem": "/Lotus/Types/Items/Research/EnergyComponent", "ItemCount": 3}]}
    REWARDS_COUNTED_ITEMS_ONLY_TRANSLATED = "3 x Fieldron"
    REWARDS_CREDITS_ONLY_TRANSLATED = "3000 credits"
    REWARDS_ITEMS_ONLY_TRANSLATED = "Dex Furis"
    REWARDS_ALMOUST_COMPLETE_TRANSLATED = "Amalgam Shotgun Spazz + Amalgam Serration"
    REWARDS_COMPLETE_TRANSLATED = "randomItem /Lotus/Types/Game/MissionDecks/SortieRewards Opticor Vandal + 3 x " \
                                  "Fieldron + 3 x Fieldron + 500 affinity + 1000 credits"
    OPERATION_TYPE = "MULTIPLY"
    OPERATION_TYPE_UNKNOWN = "ADD"

    def test_read_drop_file_fine_not_found(self) -> None:
        res = read_drop_file("sddfsbja")
        assert res == {}

    def test_read_drop_file_index_error(self) -> None:
        with patch('json.loads', side_effect=IndexError('mocked error')):
            res = read_drop_file("cetus_en")
            assert res == {}

    def test_get_operation_type(self) -> None:
        res = get_operation_type(self.OPERATION_TYPE)
        assert " x " == res

    def test_get_operation_type_unknown(self) -> None:
        res = get_operation_type(self.OPERATION_TYPE_UNKNOWN)
        assert self.OPERATION_TYPE_UNKNOWN == res

    def test_parse_reward_only_counted_complete(self) -> None:
        res = parse_reward(self.REWARDS_COUNTED_ITEMS_ONLY)
        assert self.REWARDS_COUNTED_ITEMS_ONLY_TRANSLATED == res

    def test_parse_reward_only_credits(self) -> None:
        res = parse_reward(self.REWARDS_CREDITS_ONLY)
        assert self.REWARDS_CREDITS_ONLY_TRANSLATED == res

    def test_parse_reward_only_items(self) -> None:
        res = parse_reward(self.REWARDS_ITEMS_ONLY)
        assert self.REWARDS_ITEMS_ONLY_TRANSLATED == res

    def test_parse_reward_almoust_complete(self) -> None:
        res = parse_reward(self.REWARDS_ALMOUST_COMPLETE)
        assert self.REWARDS_ALMOUST_COMPLETE_TRANSLATED == res

    def test_parse_reward_complete(self) -> None:
        res = parse_reward(self.REWARDS_COMPLETE)
        assert self.REWARDS_COMPLETE_TRANSLATED == res

    def test_get_image_path_from_name_found(self) -> None:
        res = get_image_path_from_name(self.IMAGE_NAME)
        assert self.IMAGE_NAME_FOUND == res

    def test_get_image_path_from_name_not_found(self) -> None:
        res = get_image_path_from_name(self.IMAGE_NAME_UNKNOWN)
        assert self.IMAGE_NAME_NOT_FOUND == res

    def test_get_weapon_part(self) -> None:
        res = get_weapon_part("/Lotus/Interface/Icons/Store/GenericWeaponBlueprint.png")
        assert "Blueprint" == res
        res = get_weapon_part("/Lotus/Interface/Icons/Store/GenericWeaponBlade.png")
        assert "Blade" == res
        res = get_weapon_part("/Lotus/Interface/Icons/Store/GenericWeaponStock.png")
        assert "Stock" == res
        res = get_weapon_part("/Lotus/Interface/Icons/Store/GenericWeaponBarrel.png")
        assert "Barrel" == res
        res = get_weapon_part("/Lotus/Interface/Icons/Store/GenericWeaponReceiver.png")
        assert "Receiver" == res
        res = get_weapon_part("/Lotus/Interface/Icons/Store/GenericWeaponHandle.png")
        assert "Handle" == res
        res = get_weapon_part("/Lotus/Interface/Icons/Store/GenericWeaponComponentLink.png")
        assert "Link" == res
        res = get_weapon_part("/Lotus/Interface/Icons/Store/GenericWeaponComponentHeatsink.png")
        assert "Heatsink" == res
        res = get_weapon_part("/Lotus/Interface/Icons/Store/GenericWeaponComponentLimb.png")
        assert "Limb" == res
        res = get_weapon_part("/Lotus/Interface/Icons/Store/GenericWeaponComponentGrip.png")
        assert "Grip" == res
        res = get_weapon_part("/Lotus/Interface/Icons/Store/GenericWeaponComponentString.png")
        assert "String" == res
        res = get_weapon_part("/Lotus/Interface/Icons/Store/GenericWeaponComponentHead.png")
        assert "Head" == res
        res = get_weapon_part("/Lotus/Interface/Icons/Store/GenericWeaponComponentHilt.png")
        assert "Hilt" == res
        res = get_weapon_part("/Lotus/Interface/Icons/Store/GenericWeaponComponentPouch.png")
        assert "Pouch" == res
        res = get_weapon_part("/Lotus/Interface/Icons/Store/GenericWeaponComponentStars.png")
        assert "Stars" == res
        res = get_weapon_part("/Lotus/Interface/Icons/Store/GenericWeaponComponentGauntlet.png")
        assert "Gauntlet" == res
        res = get_weapon_part("/Lotus/Interface/Icons/Store/GenericWeaponComponentDisc.png")
        assert "Disc" == res

    def test_get_weapon_part_not_found(self) -> None:
        res = get_weapon_part(self.WEAPON_PART_UNKOWN)
        assert self.WEAPON_PART_NOT_FOUND == res

    def test_get_weapon_part_not_weapon(self) -> None:
        res = get_weapon_part(self.IMAGE_NAME)
        assert "" == res

    def test_get_weapon_type(self) -> None:
        res = get_weapon_type("/Lotus/Interface/Icons/Store/KarakWraith.png")
        assert "Karak Wraith" == res
        res = get_weapon_type("/Lotus/Interface/Icons/Store/WraithLatron.png")
        assert "Latron Wraith" == res
        res = get_weapon_type("/Lotus/Interface/Icons/Store/VandalStrun.png")
        assert "Strun Wraith" == res
        res = get_weapon_type("/Lotus/Interface/Icons/Store/WraithTwinVipers.png")
        assert "Twin Vipers Wraith" == res
        res = get_weapon_type("/Lotus/Interface/Icons/Store/DeraVandal.png")
        assert "Dera Vandal" == res
        res = get_weapon_type("/Lotus/Interface/Icons/Store/SnipetronVandal.png")
        assert "Snipetron Vandal" == res
        res = get_weapon_type("/Lotus/Interface/Icons/Store/GrineerCombatKnife.png")
        assert "Sheev" == res

    def test_get_weapon_type_not_found(self) -> None:
        res = get_weapon_type(self.WEAPON_TYPE_UNKOWN)
        assert self.WEAPON_TYPE_NOT_FOUND == res

    def test_get_bounty_reward(self) -> None:
        res = get_bounty_reward("/Lotus/Types/Game/MissionDecks/EidolonJobMissionRewards/TierATableBRewards", "cetus")
        assert 3 == len(res)

    def test_get_bounty_reward_not_found(self) -> None:
        res = get_bounty_reward("/Lotus/Types/Game/MissionDecks/EidolonJobMissionRewards/TierATasdbleBRewasdrds",
                                "fortuna")
        assert 3 == len(res)
        assert res == ["noBountyReward", "noBountyReward", "noBountyReward"]

    def test_get_bounty_reward_exception(self) -> None:
        with patch('warframeAlert.utils.warframeUtils.read_drop_file', side_effect=KeyError('mocked error')):
            res = get_bounty_reward("/Lotus/Types/Game/MissionDecks/EidolonJobMissionRewards/TierATableBRewards",
                                    "deimos")
            assert 3 == len(res)
            assert res == ["noBountyReward", "noBountyReward", "noBountyReward"]

    def test_get_bounty_reward_plague_star(self) -> None:
        res = get_bounty_reward("/Lotus/Types/Game/MissionDecks/EidolonJobMissionRewards/PlagueStarTable", "cetus")
        assert 3 == len(res)

    def test_get_bounty_reward_ghoul_bounty(self) -> None:
        res = get_bounty_reward("/Lotus/Types/Game/MissionDecks/EidolonJobMissionRewards/GhoulBountyTableARewards",
                                "cetus")
        assert 3 == len(res)

    def test_get_bounty_reward_profit_taker(self) -> None:
        res = get_bounty_reward("/Lotus/Types/Game/MissionDecks/VenusJobMissionRewards/ProfitTakerDTableCRewards",
                                "fortuna")
        assert 3 == len(res)

    def test_get_reward_from_sortie(self) -> None:
        res = get_reward_from_sortie()
        assert 17 == len(res)

    def test_get_reward_from_sortie_exception(self) -> None:
        with patch('json.loads', side_effect=IndexError('mocked error')):
            res = get_reward_from_sortie()
            assert 1 == len(res)
            assert "noReward" in res

    def test_get_relic_tier_from_name(self) -> None:
        res = get_relic_tier_from_name("Lith")
        assert 1 == res
        res = get_relic_tier_from_name("Meso")
        assert 2 == res
        res = get_relic_tier_from_name("Neo")
        assert 3 == res
        res = get_relic_tier_from_name("Axi")
        assert 4 == res
        res = get_relic_tier_from_name("Requiem")
        assert 5 == res

    def test_get_relic_item(self) -> None:
        res = get_relic_item("Axi A1")
        assert 6 == len(res)

    def test_get_relic_item_not_found(self) -> None:
        res = get_relic_item("Axi A0")
        assert 0 == len(res)
        assert [] == res

    def test_get_relic_item_exception(self) -> None:
        with patch('json.loads', side_effect=IndexError('mocked error')):
            res = get_relic_item("Axi A1")
            assert 0 == len(res)
            assert [] == res

    def test_get_relic_drop_from_name(self) -> None:
        res = get_relic_drop_from_name("Astilla Prime Calcio")
        assert "Lith T8 notCommon (11%)\nMeso T5 notCommon (11%)\nNeo P3 notCommon (11%)\n" == res

    def test_get_relic_drop_from_name_exception(self) -> None:
        with patch('json.loads', side_effect=IndexError('mocked error')):
            res = get_relic_drop_from_name("Astilla Prime Calcio")
            assert "" == res

    def test_add_all_relic_from_file(self, qtbot) -> None:
        combo_box = QtWidgets.QComboBox()
        qtbot.addWidget(combo_box)
        add_all_relic_from_file(combo_box)
        assert combo_box.count() > 0

    def test_add_all_relic_item_from_file(self, qtbot) -> None:
        combo_box = QtWidgets.QComboBox()
        qtbot.addWidget(combo_box)
        add_all_relic_item_from_file(combo_box)
        assert combo_box.count() > 0

    def test_get_all_relic_from_file(self) -> None:
        res = get_all_relic_from_file()
        assert len(res) > 0

    def test_get_relic_rarity_from_percent(self) -> None:
        res = get_relic_rarity_from_percent(2, "Intact")
        assert res == "rare (2%)"
        res = get_relic_rarity_from_percent(11, "Intact")
        assert res == "notCommon (11%)"
        res = get_relic_rarity_from_percent(25.33, "Intact")
        assert res == "common (25.33%)"

        res = get_relic_rarity_from_percent(4, "Exceptional")
        assert res == "rare (4%)"
        res = get_relic_rarity_from_percent(13, "Exceptional")
        assert res == "notCommon (13%)"
        res = get_relic_rarity_from_percent(23.33, "Exceptional")
        assert res == "common (23.33%)"

        res = get_relic_rarity_from_percent(6, "Flawless")
        assert res == "rare (6%)"
        res = get_relic_rarity_from_percent(17, "Flawless")
        assert res == "notCommon (17%)"
        res = get_relic_rarity_from_percent(20, "Flawless")
        assert res == "common (20%)"

        res = get_relic_rarity_from_percent(10, "Radiant")
        assert res == "rare (10%)"
        res = get_relic_rarity_from_percent(20, "Radiant")
        assert res == "notCommon (20%)"
        res = get_relic_rarity_from_percent(16.67, "Radiant")
        assert res == "common (16.67%)"

    def test_get_relic_drop(self) -> None:
        res = get_relic_drop("Axi A1")
        assert res == "primeVault\nrelicDrop"

    def test_get_relic_drop_en(self) -> None:
        OptionsHandler.set_option("Language", "en")
        res = get_relic_drop("Axi A1")
        assert res == "primeVault\nrelicDrop"
        OptionsHandler.set_option("Language", "it")

    def test_get_relic_drop_bounty_en(self) -> None:
        OptionsHandler.set_option("Language", "en")
        res = get_relic_drop("Lith B4")
        assert res != "primeVault\nrelicDrop"
        OptionsHandler.set_option("Language", "it")

    def test_get_relic_drop_mission_en(self) -> None:
        OptionsHandler.set_option("Language", "en")
        res = get_relic_drop("Neo N16")
        assert res != "primeVault\nrelicDrop"
        OptionsHandler.set_option("Language", "it")

    def test_get_relic_drop_mission_no_rotation_en(self) -> None:
        OptionsHandler.set_option("Language", "en")
        res = get_relic_drop("Lith G4")
        assert res != "primeVault\nrelicDrop"
        OptionsHandler.set_option("Language", "it")

    def test_get_relic_drop_key_mission_en(self) -> None:
        OptionsHandler.set_option("Language", "en")
        res = get_relic_drop("Lith G4")
        assert res != "primeVault\nrelicDrop"
        OptionsHandler.set_option("Language", "it")

    def test_get_relic_drop_transient_en(self) -> None:
        OptionsHandler.set_option("Language", "en")
        res = get_relic_drop("Requiem I")
        assert res != "primeVault\nrelicDrop"
        OptionsHandler.set_option("Language", "it")

    def test_get_relic_drop_exception(self) -> None:
        with patch('json.loads', side_effect=IndexError('mocked error')):
            res = get_relic_drop("Axi A1")
            assert "errorDropRelic" == res

    def test_translate_planet_from_drop_file_not_found(self) -> None:
        res = translate_planet_from_drop_file("planetX")
        assert "planetX" == res

    def test_translate_mission_type_from_drop_file_not_found(self) -> None:
        res = translate_mission_type_from_drop_file("MT_UNKNOWN")
        assert "MT_UNKNOWN" == res

    def test_translate_focus_lens_eidolon(self) -> None:
        res = translate_focus_lens("EIDOLON ZENURIK GREATER LENS")
        assert "Lente Eidolon Zenurik (Schema)" == res

    def test_translate_focus_lens_greater(self) -> None:
        res = translate_focus_lens("GREATER ZENURIK LENS")
        assert "Lente Maggiore Zenurik" == res

    def test_translate_prime_part_not_found(self) -> None:
        res = translate_prime_part("UNKNOWN PRIME UNKNOWN")
        assert "Unknown Prime UNKNOWN" == res

    def test_translate_warframe_part_not_found(self) -> None:
        res = translate_warframe_part("NEKROS ARMS BLUEPRINT")
        assert "Nekros ARMS (Schema)" == res

    def test_translate_weapon_parts_not_found(self) -> None:
        res = translate_weapon_parts("STUBBA UNKNOWN")
        assert "Stubba UNKNOWN" == res

    def test_translate_weapon_parts_not_found2(self) -> None:
        res = translate_weapon_parts("STUBBA HANDLE UNKNOWN")
        assert "Stubba Manico UNKNOWN" == res
