import unittest
from warframeAlert.utils.commonUtils import get_last_item_with_backslash


class TestCommonUtils(unittest.TestCase):

    def test_get_last_item_with_backslash(self):
        text = "/Lotus/Types/Enemies/Grineer/Vip/CaptainVorBossAgent"
        res = get_last_item_with_backslash(text)
        self.assertEqual("CaptainVorBossAgent", res)

    def test_get_last_item_with_backslash_with_multiple_slash(self):
        text = "/Lotus/Types/Enemies/Grineer/Vip//CaptainVorBossAgent"
        res = get_last_item_with_backslash(text)
        self.assertEqual("CaptainVorBossAgent", res)
