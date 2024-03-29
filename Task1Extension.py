from floodsystem.geo import map_station
from floodsystem.stationdata import build_station_list
from floodsystem.geo import position_plotter

def run():
    """Maps a desired list of stations"""

    # Create station list
    stations = build_station_list()

    # Obtain the N rivers with most stations
    dataframe = map_station(stations)

    position_plotter(dataframe)


if __name__ == "__main__":
    print("*** Task 1Extension: CUED Part IA Flood Warning System ***")
    run()
