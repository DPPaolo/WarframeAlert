import unittest
from warframeAlert.utils import commonUtils


class TestCommonUtils(unittest.TestCase):

    def test_check_file_not_exist(self):
        exist = commonUtils.check_file("test2_commonUtils.py")
        self.assertFalse(exist)

    def test_check_file_exist(self):
        exist = commonUtils.check_file("test_commonUtils.py")
        self.assertTrue(exist)
