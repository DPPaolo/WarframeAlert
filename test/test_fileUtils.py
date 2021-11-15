# coding=utf-8
from warframeAlert.utils.fileUtils import check_file, check_folder


class TestFileUtils():

    def test_check_file_not_exist(self) -> None:
        exist = check_file("test2_commonUtils.py")
        assert not exist

    def test_check_file_exist(self) -> None:
        exist = check_file("test_commonUtils.py")
        assert exist

    def test_check_file_data_not_exist(self) -> None:
        exist = check_file("test2_commonUtils.py")
        assert not exist

    def test_check_file_data_exist(self) -> None:
        exist = check_file("Language.json")
        assert exist

    def test_check_folder_not_exist(self) -> None:
        exist = check_folder("datas")
        assert not exist

    def test_check_folder_exist(self) -> None:
        exist = check_folder("data")
        assert exist
