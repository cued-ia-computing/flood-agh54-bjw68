from floodsystem.geo import rivers_with_station
from floodsystem.station import MonitoringStation
from floodsystem.station import sampledata
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_by_station_number
from floodsystem.geo import map_station
from floodsystem.geo import position_plotter
from floodsystem.geo import stations_by_distance
from floodsystem.geo import stations_within_radius

"""Unit test for the geo module"""

def test_rivers_with_station():
    """Test for rivers_with_station function"""
    test_data = sampledata()
    rivers = rivers_with_station(test_data)

    # Checks rivers list isn't empty
    assert len(rivers) != 0

    #Checks list has been correctly sorted
    assert rivers[0] < rivers[len(rivers)-1]

    #Uses example data to check duplicates are being removed
    assert len(rivers) < len(test_data)

def test_stations_by_river():
    """Test for stations_by_river function"""
    test_data = sampledata()
    rivers = stations_by_river(test_data)

    # Checks rivers dict is not empty
    assert len(rivers) != 0
    
    # Checks each item is a list for the dictionary value
    for river in rivers:
        assert type(rivers[river]) == list
        
        # Checks the list of stations stores strings
        for station in rivers[river]:
            assert type(station) == str

    # Checks we have removed the duplicate from our data
    assert len(rivers) < len(test_data)


def test_rivers_by_station_number():
    """Test for rivers_by_station_number function"""
    testvalue = 3
    test_data = sampledata()
    rivers = rivers_by_station_number(test_data, testvalue)
    

    count = 0
    for river in rivers:

        # Checks the river list stores tuples
        assert type(river) == tuple

        # Checks the tuple stores an int for the number
        assert type(river[1]) == int

        # Checks each river has a station, as expected
        assert river[1] != 0

        # Checks the value of the previous number is greater than the current value
        if count > 0:
            assert river[count] > river[count-1]
    
    # Checks the list of rivers output is greater than or equal to the test value
    assert len(rivers) >= testvalue

    # Checks rivers list is not empty
    assert rivers != None


def test_map_station():
    test_data = sampledata()
    pos = map_station(test_data)
    
    # Checks the coordinates are stored as floats
    # Checks the coordinates are within bounds for lat and long
    for coord in pos.geometry.x:
        assert (type(coord)) == float
        assert (abs(coord)) < 85
    for coord in pos.geometry.y:
        assert (type(coord)) == float
        assert (abs(coord)) < 180
    
    # Checks the coordinate lists are the same length
    assert len(pos.geometry.x) == len(pos.geometry.y) 

    # Checks the coordinate lists is the same length as the input data
    assert len(pos.geometry.x) <= len(test_data)

    # Checks the coordinate list and name list are same length
    assert len(pos.geometry.x) == len(pos['City'])

    # Checks the coordinate list and colour list are same length
    assert len(pos.geometry.x) == len(pos['Colour'])

    # Checks the cities are string and are not empty
    for city in pos['City']:    
        assert city != None
        assert type(city) == str

    # Checks the cities are string and are not empty
    colour_list = ["goldenrod", "blue", "red", "green"]
    for colour in pos['Colour']:    
        assert colour != None
        assert type(colour) == str
        assert colour in colour_list


def test_position_plotter():
    test_data = sampledata()
    pos = map_station(test_data)
    # Checks we an call the plotter
    plot = position_plotter(pos)
    return plot

def test_stations_by_distance():
    test_data = sampledata()
    test_value = 52.2053, 0.1218
    stations = stations_by_distance(test_data, test_value)

    # Checks the list isn't empty
    assert len(stations) != 0

    for station in stations:
        # Checks that the list stores tuples, and that the tuples have the right type of value in each entry
        assert type(station) == tuple
        assert type(station[0]) == str
        assert type(station[1]) == float

        # Checks distance is positive
        assert station[1] > 0

    # Checks sort
    for i in range(len(stations)-1):
        assert stations[i][1] <= stations[i+1][1]
    
    # Checks the duplicate hasn't been inclueded twice
    assert len(stations) < len(test_data)

def test_stations_within_radius():
    test_data = sampledata()
    test_value1 = 52.2053, 0.1218
    test_value2 = 250
    stations = stations_within_radius(test_data, test_value1, test_value2)

    # Check length from code matches manual compute of data
    assert len(stations) == 3

    for station in stations:
        # Checks that the list stores strings
        assert type(station) == str

    # Checks sort
    test_sorted = sorted(stations)
    assert test_sorted == stations
    
    # Checks the duplicate hasn't been inclueded twice
    assert len(stations) < len(test_data)