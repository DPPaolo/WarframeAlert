# coding=utf-8
import time
import unittest

from warframeAlert.services.translationService import translate
from warframeAlert.utils import timeUtils


class TestTimeUtils(unittest.TestCase):
    TIME = '946684800'  # 2000/1/1 00:00
    TEN_SECONDS = 10
    ONE_MINUTE = 60
    ONE_HOUR = 3600
    ONE_DAY = 86400
    SEVEN_DAYS = 604800
    RANDOM_TIME = 106052

    def test_get_time(self):
        timer = timeUtils.get_time(self.TIME)
        light_saving = time.gmtime(int(self.TIME)).tm_isdst
        timer_expected = "01/01/2000 0" + str(1 + light_saving) + ":00"  # GMT +1
        self.assertEqual(timer, timer_expected)

    def test_get_date_time(self):
        timer = timeUtils.get_date_time(self.TIME)
        self.assertEqual(timer, "01/01/2000")

    def test_alert_time_timed_out(self):
        timer = timeUtils.get_alert_time(translate("timeUtils", "Timed Out"))
        self.assertEqual(timer, translate("timeUtils", "Timed Out"))

    def test_alert_time_with_ten_seconds(self):
        timer = timeUtils.get_alert_time(self.TEN_SECONDS)
        self.assertEqual(timer, "10s")

    def test_alert_time_with_one_minute(self):
        timer = timeUtils.get_alert_time(self.ONE_MINUTE)
        self.assertEqual(timer, "1m ")

    def test_alert_time_with_one_hour(self):
        timer = timeUtils.get_alert_time(self.ONE_HOUR)
        self.assertEqual(timer, "1h ")

    def test_alert_time_with_one_day(self):
        timer = timeUtils.get_alert_time(self.ONE_DAY)
        self.assertEqual(timer, "1 " + translate("timeUtils", "Day") + " ")

    def test_alert_time_with_seven_days(self):
        timer = timeUtils.get_alert_time(self.SEVEN_DAYS)
        self.assertEqual(timer, "7 " + translate("timeUtils", "Days") + " ")

    def test_alert_time_with_random_time(self):
        timer = timeUtils.get_alert_time(self.RANDOM_TIME)
        self.assertEqual(timer, "1 " + translate("timeUtils", "Day") + " 5h 27m 32s")

    def test_get_earth_time(self):
        timer, day = timeUtils.get_earth_time()
        self.assertLessEqual(timer, 14400)
        self.assertIn(day, [True, False])

    def test_get_cetus_time(self):
        timer, heat = timeUtils.get_cetus_time(self.RANDOM_TIME)
        self.assertLessEqual(timer, 3000)
        self.assertIn(heat, [True, False])

    def test_get_fortuna_time(self):
        timer, heat = timeUtils.get_fortuna_time()
        self.assertLessEqual(timer, 1600)
        self.assertIn(heat, [True, False])
