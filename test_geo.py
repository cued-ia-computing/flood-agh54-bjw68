from floodsystem.geo import rivers_with_station
from floodsystem.station import MonitoringStation
from floodsystem.station import sampledata
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_by_station_number
from floodsystem.geo import map_station
from floodsystem.geo import position_plotter

"""Unit test for the geo module"""

def test_rivers_with_station():
    test_data = sampledata()
    rivers = rivers_with_station(test_data)

    # Checks rivers list isn't empty
    assert len(rivers) != 0

    #Checks list has been correctly sorted
    assert rivers[0] < rivers[len(rivers)-1]

    #Uses example data to check duplicates are being removed
    assert len(rivers) < len(test_data)

def test_stations_by_river():
    test_data = sampledata()
    rivers = stations_by_river(test_data)

    assert len(rivers) != 0
    
    for river in rivers:
        assert type(rivers[river]) == list
        
        for station in rivers[river]:
            assert type(station) == str

    assert len(rivers) < len(test_data)

def test_rivers_by_station_number():
    testvalue = 3
    test_data = sampledata()
    rivers = rivers_by_station_number(test_data, testvalue)
    
    count = 0
    for river in rivers:
        assert type(river) == tuple
        assert type(river[1]) == int
        assert river[1] != 0
        if count > 0:
            assert river[count] > river[count-1]
    
    assert len(rivers) >= testvalue

    assert rivers != None

def test_map_station():
    test_data = sampledata()
    pos = map_station(test_data)
    
    for coord in pos.geometry.x:
        assert (type(coord)) == float
    for coord in pos.geometry.y:
        assert (type(coord)) == float
    
    assert len(pos.geometry.x) == len(pos.geometry.y) and len(pos.geometry.x) <= len(test_data)
    assert len(pos.geometry.x) == len(pos['City'])

    for city in pos['City']:    
        assert city != None
        assert type(city) == str

def test_position_plotter():
    pass


test_rivers_with_station()
test_stations_by_river()
test_rivers_by_station_number()
test_map_station()