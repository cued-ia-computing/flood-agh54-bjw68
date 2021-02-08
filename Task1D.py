from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list

def run():
    """Requirements for Task 1D"""

    # Create a list of stations
    stations = build_station_list()

    # Create list of rivers
    rivers = rivers_with_station(stations)

    # Display data from 10 rivers:
    river_display = rivers[:10]
    number_of_rivers = len(rivers)
    print('There are {} rivers with at least one station. The first ten rivers are {}' .format(number_of_rivers, river_display))

    # Create River dictionary
    river_stations = stations_by_river(stations)

    # Display desired rivers
    print('The stations on the River Aire are {}'.format(river_stations['River Aire']))
    print('The stations on the River Cam are {}'.format(river_stations['River Cam']))
    print('The stations on the River Thames are {}'.format(river_stations['River Thames']))


if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()