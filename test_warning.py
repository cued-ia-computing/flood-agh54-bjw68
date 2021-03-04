from floodsystem.warning import highest_water_level, towns_and_levels, flood_warning
from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.station import sampledata
import datetime

"""Unit test for the warning module"""

def test_highest_water_level():
    """Test for highest_water_level function"""
    test_data = build_station_list()
    dt=10
    dates, levels = fetch_measure_levels(test_data[1].measure_id, dt=datetime.timedelta(days=dt))
    p = 4
    days = 1

    highest_water_level(dates, levels, p, days)

def test_towns_and_levels():
    """Test for towns_and_levels function"""
    test_data = build_station_list()
    dt=10
    p = 4
    days = 1

    assert type(towns_and_levels(test_data[:5], p, days, dt)) == list

def test_flood_warning():
    """Test for flood_warning function"""
    test_data = build_station_list()
    dt=10
    p = 4
    days = 1
    towns = towns_and_levels(test_data[:5], p, days, dt)
    severe = 2.5
    high = 1.7
    moderate = 1
    low = 0

    s_risk, h_risk = flood_warning(towns, severe, high, moderate, low)
    assert type(s_risk) == list
    assert type(h_risk) == list




