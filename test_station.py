# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation
from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.station import sampledata

def test_inconsistent_typical_range_stations():
    test_data = sampledata()
    stations = inconsistent_typical_range_stations(test_data)
    manual_answer = ['Leeds Killingbeck Dam', 'Loftsome Bridge', 'Upton']

    # Checks the list entrys are strings
    for station in stations:
        assert type(station) == str

    #Checks duplicates have been removed
    assert len(stations) == 3
    
    # Checks that the data function gets the same answer as a manual test
    assert stations == manual_answer
    

def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town
