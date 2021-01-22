from floodsystem.geo import rivers_with_station
from floodsystem.stationdata import build_station_list

def run():
    """Requirements for Task 1D"""

    # Create a list of stations
    stations = build_station_list()

    # Create list of rivers
    rivers = rivers_with_station(stations)

    # Display data from 10 rivers:
    river_display = rivers[:10]
    print(river_display)

    # Create River dictionary
    river_stations = stations_by_river(stations)
    print(river_stations)


if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()