from floodsystem.stationdata import update_water_levels
from floodsystem.station import sampledata
from floodsystem.flood import stations_highest_rel_level
from floodsystem.flood import stations_level_over_threshold

def test_stations_highest_rel_level():
    """Test for stations_highrst_rel_level function"""
    test_data = sampledata()

    # add a latest level to the sample data
    for station in test_data:

        station.latest_level = None

        station.latest_level = 1.0

    # check output is the same as the manual result
    output = stations_highest_rel_level(test_data, 3)
    assert output[0][0].name == 'Catterick Brough Park'
    assert output[1][0].name == 'Birkwood'
    assert output[2][0].name == 'Scurf Dyke'

def test_stations_level_over_threshold():
    """Test for stations_level_over_threshold function"""
    test_data = sampledata()

    # add a latest level to the sample data
    for station in test_data:

        station.latest_level = None

        station.latest_level = 1.0

    # check output is the same as the manual result
    output = stations_level_over_threshold(test_data, 1)
    assert output[0][0].name == 'Catterick Brough Park'
    assert output[1][0].name == 'Birkwood'