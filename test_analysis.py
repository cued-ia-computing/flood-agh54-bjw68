from floodsystem.analysis import current_highest_stations, polyfit, flow_range
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.station import sampledata
import datetime
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation


"""Unit test for the analysis module"""

def test_current_highest_stations():
    test_data = sampledata()
    highest_list_1 = current_highest_stations(test_data, len(test_data))
    assert len(highest_list_1) < len(test_data)
    assert highest_list_1 != None

    num = 10
    stations = build_station_list()   
    highest_list_2 = current_highest_stations(stations, num) 
    for value in range(len(highest_list_2)):
        assert type(highest_list_2[value][1]) == float
        assert type(highest_list_2[value][0]) == MonitoringStation
        if value > 0:
            assert highest_list_2[value][1] < highest_list_2[value -1][1]

    assert len(highest_list_2) <= num
    assert highest_list_2 != None


def test_polyfit():
    stations = build_station_list() 

    highest_stations = current_highest_stations(stations, 5)

    dt = 10

    for num in range(len(highest_stations)):
        station_nom = highest_stations[num][0]
        dates, levels = fetch_measure_levels(station_nom.measure_id, dt=datetime.timedelta(days=dt))

        assert len(dates) == len(levels)
        for num in range(len(dates)):
            assert type(levels) == list
            assert type(dates) == list
            assert type(levels[num]) == float
            assert type(dates[num]) == datetime.datetime

        plot = polyfit(dates, levels, 3)
        assert plot != None
        return plot

def test_flow_range():
    stations = build_station_list() 
    colours = flow_range(stations)

    colour_list = ["goldenrod", "blue", "red", "green"]
    assert type(colours) == list
    assert len(colours) == len(stations)
    for colour in colours:
        assert type(colour) == str
        assert colour in colour_list
