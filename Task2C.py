from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import update_water_levels

def run():
    """Requirements for Task 2C"""

    # Create a list of stations
    stations = build_station_list()

    #Updates water levels for all stations
    update_water_levels(stations)

    # Finds the stations currently at risk of flooding
    highest_level = stations_highest_rel_level(stations, 10)
    # Display data
    for station in highest_level:
        print(station[0].name,station[1])

if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()