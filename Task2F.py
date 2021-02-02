from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from floodsystem.plot import plot_water_levels
from floodsystem.analysis import current_highest_stations, polyfit
import datetime


def run():
    """Requirements for Task 2F"""

    stations = build_station_list()

    highest_stations = current_highest_stations(stations, 5)

    dt = 10
    for num in range(len(highest_stations)):
        station_nom = highest_stations[num][0]
        dates, levels = fetch_measure_levels(station_nom.measure_id, dt=datetime.timedelta(days=dt))
        plot = plot_water_levels(station_nom, dates, levels)
        plot = polyfit(dates, levels, 3)
        plot.show()


if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()