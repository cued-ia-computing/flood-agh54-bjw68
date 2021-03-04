from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import update_water_levels

def run():
    """Requirements for Task 2B"""

    # Create a list of stations
    stations = build_station_list()

    #Updates water levels for all stations
    update_water_levels(stations)

    # Finds the stations currently at risk of flooding
    over_threshold = stations_level_over_threshold(stations, 0.8)

    # Display data
    for station in over_threshold:
        print(station[0].name,station[1])

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()