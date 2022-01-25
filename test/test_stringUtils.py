# coding=utf-8
from warframeAlert.utils import stringUtils


class TestStringUtils():
    MESSAGE = "test\nmessage"
    MESSAGE_WITH_SPACE = "test message with space"
    MESSAGE_TOO_SHORT = "testmessage"

    def test_divide_for_n(self) -> None:
        res = stringUtils.divide_for_n(self.MESSAGE, 2)
        assert res == ["test\n", "message"]

    def test_divide_for_n_with_space(self) -> None:
        res = stringUtils.divide_for_n(self.MESSAGE_WITH_SPACE, 4, " ")
        assert res == ["test ", "message ", "with ", "space"]

    def test_divide_message(self) -> None:
        res = stringUtils.divide_message(self.MESSAGE_WITH_SPACE)
        assert res == "test message with space"

    def test_divide_message_too_long_line(self) -> None:
        res = stringUtils.divide_message(self.MESSAGE_WITH_SPACE, 10)
        assert res == "test\nmessage\nwith space"

    def test_divide_message_short_line(self) -> None:
        res = stringUtils.divide_message(self.MESSAGE_WITH_SPACE, 5)
        assert res == "test\nmessa\nge\nwith\nspace"

    def test_divide_message_0_dimension(self) -> None:
        res = stringUtils.divide_message(self.MESSAGE_WITH_SPACE, 0)
        assert res == "test message with space"

    def test_divide_message_too_short(self) -> None:
        res = stringUtils.divide_message(self.MESSAGE_TOO_SHORT, 6)
        assert res == "testme\nssage"

    def test_divide_for_n_with_empty_separator(self) -> None:
        res = stringUtils.divide_for_n(self.MESSAGE_WITH_SPACE, 4, "")
        assert res is None
