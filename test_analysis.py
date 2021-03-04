from floodsystem.analysis import current_highest_stations, polyfit, flow_range_colours
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.station import sampledata
import datetime
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation


"""Unit test for the analysis module"""

def test_current_highest_stations():
    """Test for current_highest_stations function"""
    # Imports sample data for testing
    test_data = sampledata()

    #Creates a list containing all the test data
    highest_list_1 = current_highest_stations(test_data, len(test_data))

    # Checks duplicates are removed
    assert len(highest_list_1) < len(test_data)

    # Checks output is not empty
    assert highest_list_1 != None

    # Initialises a variable for the highest list length
    num = 10

    # Gets a live station list for testing
    stations = build_station_list()   

    # Creates list of highest length stations of length num
    highest_list_2 = current_highest_stations(stations, num) 

     # Checks output is not empty
    assert highest_list_2 != None

    for value in range(len(highest_list_2)):

        # Checks the water level item is a float
        assert type(highest_list_2[value][1]) == float

        # Checks monitoring station item has correct type
        assert type(highest_list_2[value][0]) == MonitoringStation

        # Checks the current value is smaller than the previous water level value (correctly ordered)
        if value > 0:
            assert highest_list_2[value][1] < highest_list_2[value -1][1]

    # Checks the list is correct length
    assert len(highest_list_2) <= num


def test_polyfit():
    """Test for polyfit function"""

    # Creates a station list for testing
    stations = build_station_list() 

    # Collates highest station list for testing
    highest_stations = current_highest_stations(stations, 5)

    # Sets number of days for analysis
    dt = 10

    # Iterate over highest station list
    for num in range(len(highest_stations)):
        # Creates variables for each station for name, dates and corresponding levels
        station_nom = highest_stations[num][0]
        dates, levels = fetch_measure_levels(station_nom.measure_id, dt=datetime.timedelta(days=dt))

        # Checks lists are the same length
        assert len(dates) == len(levels)

        # Checks lists are correct type
        assert type(levels) == list
        assert type(dates) == list

        for num in range(len(dates)):

            # Checks levels list is storing floats
            assert type(levels[num]) == float

            # Checks dates list is storing correct type
            assert type(dates[num]) == datetime.datetime

        # Sets polyfit order
        order = 3

        # Checks we can call the function
        plot = polyfit(dates, levels, order)

        # Checks output is not empty
        assert plot != None


def test_flow_range_colours():
    """Test for flow_range function"""

    # Creates a live station list for testing
    stations = build_station_list() 

    # Creates a colours list for the stations
    colours = flow_range_colours(stations)

    # Initialises a list of valid expected output colours
    colour_list = ["goldenrod", "blue", "red", "green"]

    # Checks function outputs the expected list
    assert type(colours) == list

    # Checks lists are the same length
    assert len(colours) == len(stations)

    for colour in colours:
        # Checks the list stores strings
        assert type(colour) == str

        # Checks each item in the list can be found in the expected colour list
        assert colour in colour_list
