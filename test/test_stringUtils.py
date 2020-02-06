# coding=utf-8
import unittest
from warframeAlert.utils import stringUtils


class TestStringUtils(unittest.TestCase):
    MESSAGE = "test\nmessage"
    MESSAGE_WITH_SPACE = "test message with space"

    def test_divide_for_n(self):
        res = stringUtils.divide_for_n(self.MESSAGE, 2)
        self.assertListEqual(res, ["test\n", "message"])

    def test_divide_for_n_with_space(self):
        res = stringUtils.divide_for_n(self.MESSAGE_WITH_SPACE, 4, " ")
        self.assertListEqual(res, ["test ", "message ", "with ", "space"])

    def test_divide_for_n_with_empty_separator(self):
        res = stringUtils.divide_for_n(self.MESSAGE_WITH_SPACE, 4, "")
        self.assertIsNone(res)
