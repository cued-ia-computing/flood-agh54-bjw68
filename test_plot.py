from floodsystem.plot import plot_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.station import sampledata
import datetime


"""Unit test for the geo module"""

def test_plot_water_levels():
    """Test for rivers_with_station function"""

    # Initialises dummy data for testing
    test_data = sampledata()

    # Sets time length for our analysis
    dt = 10

    # Creates a list of checked stations
    checked_list = []

    # Iterates through test data
    for num in range(len(test_data)):

        # Checks if the station has already been checked
        if test_data[num].name not in checked_list:

            # Initialises station name, dates and corresponding water levels
            station_nom = test_data[num].name
            dates, levels = fetch_measure_levels(test_data[num].measure_id, dt=datetime.timedelta(days=dt))

            # Plots water levels with time
            plot = plot_water_levels(test_data[num], dates, levels)

            # Adds station to the checked list
            checked_list.append(station_nom)

            # Checks the output is not empty
            assert plot != None

    # Checks duplicate data is removed
    assert len(checked_list) < len(test_data)

    # Checks we are correctly storing names for the data test
    for station in checked_list:
        assert type(station) == str
