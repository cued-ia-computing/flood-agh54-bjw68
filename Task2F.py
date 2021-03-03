from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from floodsystem.plot import plot_water_levels_with_fit
from floodsystem.analysis import current_highest_stations, polyfit
import datetime


def run():
    """Requirements for Task 2F"""

    #Build station list
    stations = build_station_list()

    #Obtain list of the 5 stations with the highest water level
    highest_stations = current_highest_stations(stations, 5)

    #Set number of days back we want to consider
    dt = 10

    #For each station, get the name, water levels and corresponding dates 
    for num in range(len(highest_stations)):
        station_nom = highest_stations[num][0]
        dates, levels = fetch_measure_levels(station_nom.measure_id, dt=datetime.timedelta(days=dt))

        #Pass the information to the polynomial plotting function
        plot = plot_water_levels_with_fit(station_nom, dates, levels, 3)

        #Output the graph for each river
        plot.show()


if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()