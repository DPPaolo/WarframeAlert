# coding=utf-8
import time
from datetime import datetime
from unittest.mock import Mock, patch

from warframeAlert.services.translationService import translate
from warframeAlert.utils import timeUtils
from warframeAlert.utils.timeUtils import get_local_time


class TestTimeUtils():
    TIME = '946684800'  # 2000/1/1 00:00
    TEN_SECONDS = 10
    ONE_MINUTE = 60
    ONE_HOUR = 3600
    ONE_DAY = 86400
    SEVEN_DAYS = 604800
    RANDOM_TIME = 106052
    BOUNTY_START_TIME = 1643133247

    mock_local_time = Mock()
    mock_local_time.return_value = (2022, 1, 1, 1, 1, 1, 1, 1, 1)

    mock_time_earth_day = Mock()
    mock_time_earth_day.return_value = time.mktime(datetime(2022, 1, 25, 16, 15).timetuple())
    mock_time_earth_night = Mock()
    mock_time_earth_night.return_value = time.mktime(datetime(2022, 1, 25, 18, 16).timetuple())

    mock_time_cetus_day = Mock()
    mock_time_cetus_day.return_value = time.mktime(datetime(2022, 1, 25, 17, 15).timetuple())

    mock_time_cetus_night = Mock()
    mock_time_cetus_night.return_value = time.mktime(datetime(2022, 1, 25, 18, 16).timetuple())

    mock_time_fortuna_heat = Mock()
    mock_time_fortuna_heat.return_value = time.mktime(datetime(2022, 1, 25, 17, 15).timetuple())

    mock_time_fortuna_freeze = Mock()
    mock_time_fortuna_freeze.return_value = time.mktime(datetime(2022, 1, 25, 18, 16).timetuple())

    mock_time_fortuna_almost_finished = Mock()
    mock_time_fortuna_almost_finished.return_value = time.mktime(datetime(2022, 1, 25, 17, 33, 31).timetuple())

    @patch('time.localtime', mock_local_time)
    def test_get_local_time(self) -> None:
        timer = get_local_time()
        assert timer == '1640991661'

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

    @patch('time.time', mock_time_earth_day)
    def test_get_earth_time_day(self) -> None:
        timer, day = timeUtils.get_earth_time()
        assert timer <= 14400
        assert day

    @patch('time.time', mock_time_earth_night)
    def test_get_earth_time_night(self) -> None:
        timer, day = timeUtils.get_earth_time()
        assert timer <= 14400
        assert not day

    @patch('time.time', mock_time_cetus_day)
    def test_get_cetus_time_day(self) -> None:
        timer, day = timeUtils.get_cetus_time(self.BOUNTY_START_TIME)
        assert timer <= 3000
        assert day

    @patch('time.time', mock_time_cetus_night)
    def test_get_cetus_time_night(self) -> None:
        timer, day = timeUtils.get_cetus_time(self.BOUNTY_START_TIME)
        assert timer <= 3000
        assert not day

    @patch('time.time', mock_time_fortuna_heat)
    def test_get_fortuna_time_heat(self) -> None:
        timer, heat = timeUtils.get_fortuna_time()
        assert timer <= 1600
        assert heat

    @patch('time.time', mock_time_fortuna_freeze)
    def test_get_fortuna_time_cold(self) -> None:
        timer, heat = timeUtils.get_fortuna_time()
        assert timer <= 1600
        assert not heat

    @patch('time.time', mock_time_fortuna_almost_finished)
    def test_get_fortuna_time_almost_finished(self) -> None:
        timer, heat = timeUtils.get_fortuna_time()
        assert timer <= 1600
        assert not heat

    def test_get_cetus_time_exception(self) -> None:
        with patch('time.time', side_effect=Exception('mocked error')):
            timer, day = timeUtils.get_cetus_time(self.BOUNTY_START_TIME)
            assert timer == 946684800
            assert not day

    def test_get_fortuna_time_exception(self) -> None:
        with patch('time.time', side_effect=Exception('mocked error')):
            timer, heat = timeUtils.get_fortuna_time()
            assert timer == 946684800
            assert not heat
