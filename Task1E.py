from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list

def run():
    """Requirements for Task 1E"""

    stations = build_station_list()

    river_num = rivers_by_station_number(stations, 15)
    print(river_num)


if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()