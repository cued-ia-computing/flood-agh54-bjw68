from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list

def run():
    """Requirements for Task 1E"""

    # Create station list
    stations = build_station_list()

    # Obtain the N rivers with most stations
    river_num = rivers_by_station_number(stations, 9)

    # Print list
    print(river_num)


if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()