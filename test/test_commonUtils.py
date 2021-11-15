# coding=utf-8
from warframeAlert.utils.commonUtils import get_last_item_with_backslash, bool_to_yes_no, bool_to_int


class TestCommonUtils():

    def test_get_last_item_with_backslash(self) -> None:
        text = "/Lotus/Types/Enemies/Grineer/Vip/CaptainVorBossAgent"
        res = get_last_item_with_backslash(text)
        assert "CaptainVorBossAgent" == res

    def test_get_last_item_with_backslash_with_multiple_slash(self) -> None:
        text = "/Lotus/Types/Enemies/Grineer/Vip//CaptainVorBossAgent"
        res = get_last_item_with_backslash(text)
        assert "CaptainVorBossAgent" == res

    def test_bool_to_yes_no_with_true(self) -> None:
        res = bool_to_yes_no(True)
        assert "yes" == res

    def test_bool_to_yes_no_with_false(self) -> None:
        res = bool_to_yes_no(False)
        assert "no" == res

    def test_bool_to_yes_no_with_int(self) -> None:
        res = bool_to_yes_no(1)
        assert "yes" == res

    def test_bool_to_int_true(self) -> None:
        res = bool_to_int(True)
        assert 1 == res

    def test_bool_to_int_false(self) -> None:
        res = bool_to_int(False)
        assert 0 == res
