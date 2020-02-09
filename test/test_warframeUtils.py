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
    COUNTED_ITEMS = {"credits": 0,
                     "xp": 0,
                     "items": ["/Lotus/StoreItems/Weapons/Corpus/LongGuns/CrpBFG/Vandal/VandalCrpBFG"],
                     "countedItems": [{"ItemType": "/Lotus/Types/Items/Research/EnergyComponent", "ItemCount": 3}]}
    COUNTED_ITEMS_TRANSLATED = "Opticor Vandal + 3 x Fieldron + 0 affinity + 0 credits"

    def test_parse_reward(self):
        res = parse_reward(self.COUNTED_ITEMS)
        self.assertEqual(self.COUNTED_ITEMS_TRANSLATED, res)

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