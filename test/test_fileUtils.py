import unittest

from warframeAlert.utils.fileUtils import check_file, check_folder


class TestFileUtils(unittest.TestCase):

    def test_check_file_not_exist(self):
        exist = check_file("test2_commonUtils.py")
        self.assertFalse(exist)

    def test_check_file_exist(self):
        exist = check_file("test_commonUtils.py")
        self.assertTrue(exist)

    def test_check_folder_not_exist(self):
        exist = check_folder("datas")
        self.assertFalse(exist)

    def test_check_folder_exist(self):
        exist = check_folder("data")
        self.assertTrue(exist)
