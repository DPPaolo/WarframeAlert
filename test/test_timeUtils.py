# coding=utf-8
import time

from warframeAlert.services.translationService import translate
from warframeAlert.utils import timeUtils


class TestTimeUtils():
    TIME = '946684800'  # 2000/1/1 00:00
    TEN_SECONDS = 10
    ONE_MINUTE = 60
    ONE_HOUR = 3600
    ONE_DAY = 86400
    SEVEN_DAYS = 604800
    RANDOM_TIME = 106052

    def test_get_time(self) -> None:
        timer = timeUtils.get_time(self.TIME)
        light_saving = time.gmtime(int(self.TIME)).tm_isdst
        timer_expected = "01/01/2000 0" + str(1 + light_saving) + ":00"  # GMT +1
        assert timer == timer_expected

    def test_get_date_time(self) -> None:
        timer = timeUtils.get_date_time(self.TIME)
        assert timer == "01/01/2000"

    def test_alert_time_timed_out(self) -> None:
        timer = timeUtils.get_alert_time(translate("timeUtils", "Timed Out"))
        assert timer == translate("timeUtils", "Timed Out")

    def test_alert_time_with_ten_seconds(self) -> None:
        timer = timeUtils.get_alert_time(self.TEN_SECONDS)
        assert timer == "10s"

    def test_alert_time_with_one_minute(self) -> None:
        timer = timeUtils.get_alert_time(self.ONE_MINUTE)
        assert timer == "1m "

    def test_alert_time_with_one_hour(self) -> None:
        timer = timeUtils.get_alert_time(self.ONE_HOUR)
        assert timer == "1h "

    def test_alert_time_with_one_day(self) -> None:
        timer = timeUtils.get_alert_time(self.ONE_DAY)
        assert timer == "1 " + translate("timeUtils", "Day") + " "

    def test_alert_time_with_seven_days(self) -> None:
        timer = timeUtils.get_alert_time(self.SEVEN_DAYS)
        assert timer == "7 " + translate("timeUtils", "Days") + " "

    def test_alert_time_with_random_time(self) -> None:
        timer = timeUtils.get_alert_time(self.RANDOM_TIME)
        assert timer == "1 " + translate("timeUtils", "Day") + " 5h 27m 32s"

    def test_get_earth_time(self) -> None:
        timer, day = timeUtils.get_earth_time()
        assert timer <= 14400
        assert day in [True, False]

    def test_get_cetus_time(self) -> None:
        timer, heat = timeUtils.get_cetus_time(self.RANDOM_TIME)
        assert timer <= 3000
        assert heat in [True, False]

    def test_get_fortuna_time(self) -> None:
        timer, heat = timeUtils.get_fortuna_time()
        assert timer <= 1600
        assert heat in [True, False]
