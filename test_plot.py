from floodsystem.plot import plot_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.station import sampledata
import datetime


"""Unit test for the geo module"""

def test_plot_water_levels():
    """Test for rivers_with_station function"""
    test_data = sampledata()

    dt = 10
    checked_list = []
    for num in range(len(test_data)):
        if test_data[num].name not in checked_list:
            station_nom = test_data[num].name
            dates, levels = fetch_measure_levels(test_data[num].measure_id, dt=datetime.timedelta(days=dt))
            plot = plot_water_levels(test_data[num], dates, levels)

            checked_list.append(station_nom)

            assert plot != None
    assert len(checked_list) < len(test_data)
    for station in checked_list:
        assert type(station) == str

    
test_plot_water_levels()
