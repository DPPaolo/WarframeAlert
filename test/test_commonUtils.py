# coding=utf-8
import unittest
from warframeAlert.utils.commonUtils import get_last_item_with_backslash, bool_to_yes_no, bool_to_int


class TestCommonUtils(unittest.TestCase):

    def test_get_last_item_with_backslash(self):
        text = "/Lotus/Types/Enemies/Grineer/Vip/CaptainVorBossAgent"
        res = get_last_item_with_backslash(text)
        self.assertEqual("CaptainVorBossAgent", res)

    def test_get_last_item_with_backslash_with_multiple_slash(self):
        text = "/Lotus/Types/Enemies/Grineer/Vip//CaptainVorBossAgent"
        res = get_last_item_with_backslash(text)
        self.assertEqual("CaptainVorBossAgent", res)

    def test_bool_to_yes_no_True(self):
        res = bool_to_yes_no(True)
        self.assertEqual("yes", res)

    def test_bool_to_yes_no_false(self):
        res = bool_to_yes_no(False)
        self.assertEqual("no", res)

    def test_bool_to_yes_no_string(self):
        res = bool_to_yes_no("true")
        self.assertEqual("yes", res)

    def test_bool_to_int_true(self):
        res = bool_to_int(True)
        self.assertEqual(1, res)

    def test_bool_to_int_false(self):
        res = bool_to_int(False)
        self.assertEqual(0, res)

