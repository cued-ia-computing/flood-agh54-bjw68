
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_levels
import datetime

def run():
    """Requirements for Task 2E"""

    # Build list of stations
    stations = build_station_list()

    highest_stations = []
    update_water_levels(stations)
    for station in stations:
        if station.latest_level != None:
            highest_stations.append((station, station.latest_level))
    

    highest_stations_sort = sorted(highest_stations, key=lambda x: x[1], reverse=True)

    dt = 10
    for num in range(5):
        station_nom = highest_stations_sort[num][0]
        dates, levels = fetch_measure_levels(station_nom.measure_id, dt=datetime.timedelta(days=dt))
        plot_water_levels(station_nom, dates, levels)


if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()