# coding=utf-8
from warframeAlert.constants.warframeTypes import MissionReward
from warframeAlert.utils.warframeUtils import get_image_path_from_name, get_weapon_part, get_weapon_type, \
    parse_reward, get_operation_type, get_bounty_reward


class TestWarframeUtils():
    IMAGE_NAME = "Stock"
    IMAGE_NAME_FOUND = "/Lotus/Interface/Icons/Store/GenericGunStock.png"
    IMAGE_NAME_UNKNOWN = "Sword"
    IMAGE_NAME_NOT_FOUND = "Sword"
    WEAPON_PART = "/Lotus/Interface/Icons/Store/GenericWeaponBlade.png"
    WEAPON_PART_FOUND = "Blade"
    WEAPON_PART_UNKOWN = "/Lotus/Interface/Icons/Store/GenericWeaponPart.png"
    WEAPON_PART_NOT_FOUND = "Unknown"
    WEAPON_TYPE = "/Lotus/Interface/Icons/Store/KarakWraith.png"
    WEAPON_TYPE_FOUND = "Karak Wraith"
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
        "credits": 0,
        "xp": 0,
        "items": ["/Lotus/StoreItems/Weapons/Corpus/LongGuns/CrpBFG/Vandal/VandalCrpBFG"],
        "countedItems": [{"ItemType": "/Lotus/Types/Items/Research/EnergyComponent", "ItemCount": 3}]}
    REWARDS_COUNTED_ITEMS_ONLY_TRANSLATED = "3 x Fieldron"
    REWARDS_CREDITS_ONLY_TRANSLATED = "3000 credits"
    REWARDS_ITEMS_ONLY_TRANSLATED = "Dex Furis"
    REWARDS_ALMOUST_COMPLETE_TRANSLATED = "Amalgam Shotgun Spazz + Amalgam Serration"
    REWARDS_COMPLETE_TRANSLATED = "Opticor Vandal + 3 x Fieldron"
    OPERATION_TYPE = "MULTIPLY"
    OPERATION_TYPE_UNKNOWN = "ADD"

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
        res = get_weapon_part(self.WEAPON_PART)
        assert self.WEAPON_PART_FOUND == res

    def test_get_weapon_part_not_found(self) -> None:
        res = get_weapon_part(self.WEAPON_PART_UNKOWN)
        assert self.WEAPON_PART_NOT_FOUND == res

    def test_get_weapon_part_not_weapon(self) -> None:
        res = get_weapon_part(self.IMAGE_NAME)
        assert "" == res

    def test_get_weapon_type(self) -> None:
        res = get_weapon_type(self.WEAPON_TYPE)
        assert self.WEAPON_TYPE_FOUND == res

    def test_get_weapon_type_not_found(self) -> None:
        res = get_weapon_type(self.WEAPON_TYPE_UNKOWN)
        assert self.WEAPON_TYPE_NOT_FOUND == res

    def test_get_bounty_reward(self) -> None:
        res = get_bounty_reward("/Lotus/Types/Game/MissionDecks/EidolonJobMissionRewards/TierATableBRewards", "cetus")
        assert 3 == len(res)
