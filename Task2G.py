from floodsystem.warning import highest_water_level, towns_and_levels, flood_warning
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
import datetime

def run():
    """Requirements for Task 2B"""

    # Create a list of stations
    stations = build_station_list()

    # Set parameters
    dt = 10
    p = 4
    days = 1
    severe = 2.5
    high = 1.7
    moderate = 1
    low = 0

    #Creates a list of towns with their highest projected level in the next day
    towns_water_levels=towns_and_levels(stations, p, days, dt)

    # Finds the stations currently at risk of flooding
    s_risk, h_risk = flood_warning(towns_water_levels, severe, high, moderate, low)

    # Display data
    print("The towns at severe risk of flooding are: ")
    for town in s_risk:
        print(town[0])
    
    print("The towns at high risk of flooding are: ")
    for town in h_risk:
        print(town[0])

if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()