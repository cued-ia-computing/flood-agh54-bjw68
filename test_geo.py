from floodsystem.geo import rivers_with_station
from floodsystem.station import MonitoringStation
from floodsystem.station import sampledata
from floodsystem.geo import stations_by_river
import floodsystem.geo import rivers_by_station_number

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

def rivers_by_station_number():
    pass



test_rivers_with_station()
test_stations_by_river()