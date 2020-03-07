# coding=utf-8
import unittest

from warframeAlert.utils.warframeUtils import get_image_path_from_name, get_weapon_part, get_weapon_type, \
    get_image_path_from_export_manifest, parse_reward


class TestWarframeUtils(unittest.TestCase):
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
    IMAGE_EXPORT_MANIFEST = "/Lotus/Weapons/Tenno/Melee/MeleeTrees/WhipCmbOneMeleeTree"
    IMAGE_EXPORT_MANIFEST_FOUND = "/Lotus/Interface/Cards/Images/Stances/WhipCombo1a.jpeg"
    IMAGE_EXPORT_MANIFEST_UNKNOWN = "/Lotus/Tenno/Melee/MeleeTrees/WhipCmbOneMeleeTree"
    IMAGE_EXPORT_MANIFEST_NOT_FOUND = "/Lotus/Interface/Icons/Store/CorpusCreditCardHigh.png"
    REWARDS_COUNTED_ITEMS_ONLY = {'countedItems': [{'ItemType': '/Lotus/Types/Items/Research/EnergyComponent',
                                                    'ItemCount': 3}]}
    REWARDS_CREDITS_ONLY = {'credits': 3000}
    REWARDS_ITEMS_ONLY = {'items': ['/Lotus/StoreItems/Weapons/Tenno/Pistols/DexFuris/DexFuris']}
    REWARDS_ALMOUST_COMPLETE = {'credits': 0,
                                'xp': 0,
                                'items': ['/Lotus/StoreItems/Upgrades/Mods/DualSource/Shotgun/ShotgunMedicMod',
                                          '/Lotus/StoreItems/Upgrades/Mods/DualSource/Rifle/SerratedRushMod'],
                                'countedItems': []}
    REWARDS_COMPLETE = {
                    "credits": 0,
                    "xp": 0,
                    "items": ["/Lotus/StoreItems/Weapons/Corpus/LongGuns/CrpBFG/Vandal/VandalCrpBFG"],
                    "countedItems": [{"ItemType": "/Lotus/Types/Items/Research/EnergyComponent", "ItemCount": 3}]}
    REWARDS_COUNTED_ITEMS_ONLY_TRANSLATED = "3 x Fieldron"
    REWARDS_CREDITS_ONLY_TRANSLATED = "3000 credits"
    REWARDS_ITEMS_ONLY_TRANSLATED = "Dex Furis"
    REWARDS_ALMOUST_COMPLETE_TRANSLATED = "Amalgam Shotgun Spazz + Amalgam Serration"
    REWARDS_COMPLETE_TRANSLATED = "Opticor Vandal + 3 x Fieldron"

    def test_parse_reward_only_counted_complete(self):
        res = parse_reward(self.REWARDS_COUNTED_ITEMS_ONLY)
        self.assertEqual(self.REWARDS_COUNTED_ITEMS_ONLY_TRANSLATED, res)

    def test_parse_reward_only_credits(self):
        res = parse_reward(self.REWARDS_CREDITS_ONLY)
        self.assertEqual(self.REWARDS_CREDITS_ONLY_TRANSLATED, res)

    def test_parse_reward_only_items(self):
        res = parse_reward(self.REWARDS_ITEMS_ONLY)
        self.assertEqual(self.REWARDS_ITEMS_ONLY_TRANSLATED, res)

    def test_parse_reward_almoust_complete(self):
        res = parse_reward(self.REWARDS_ALMOUST_COMPLETE)
        self.assertEqual(self.REWARDS_ALMOUST_COMPLETE_TRANSLATED, res)

    def test_parse_reward_complete(self):
        res = parse_reward(self.REWARDS_COMPLETE)
        self.assertEqual(self.REWARDS_COMPLETE_TRANSLATED, res)

    def test_get_image_path_from_name_found(self):
        res = get_image_path_from_name(self.IMAGE_NAME)
        self.assertEqual(self.IMAGE_NAME_FOUND, res)

    def test_get_image_path_from_name_not_found(self):
        res = get_image_path_from_name(self.IMAGE_NAME_UNKNOWN)
        self.assertEqual(self.IMAGE_NAME_NOT_FOUND, res)

    def test_get_weapon_part(self):
        res = get_weapon_part(self.WEAPON_PART)
        self.assertEqual(self.WEAPON_PART_FOUND, res)

    def test_get_weapon_part_not_found(self):
        res = get_weapon_part(self.WEAPON_PART_UNKOWN)
        self.assertEqual(self.WEAPON_PART_NOT_FOUND, res)

    def test_get_weapon_part_not_weapon(self):
        res = get_weapon_part(self.IMAGE_NAME)
        self.assertEqual("", res)

    def test_get_weapon_type(self):
        res = get_weapon_type(self.WEAPON_TYPE)
        self.assertEqual(self.WEAPON_TYPE_FOUND, res)

    def test_get_weapon_type_not_found(self):
        res = get_weapon_type(self.WEAPON_TYPE_UNKOWN)
        self.assertEqual(self.WEAPON_TYPE_NOT_FOUND, res)

    def test_get_image_path_from_export_manifest(self):
        res = get_image_path_from_export_manifest(self.IMAGE_EXPORT_MANIFEST)
        self.assertEqual(self.IMAGE_EXPORT_MANIFEST_FOUND, res)

    def test_get_image_path_from_export_manifest_not_found(self):
        res = get_image_path_from_export_manifest(self.IMAGE_EXPORT_MANIFEST_UNKNOWN)
        self.assertEqual(self.IMAGE_EXPORT_MANIFEST_NOT_FOUND, res)
