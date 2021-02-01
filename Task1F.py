from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

def run():
    """Requirements for Task 1F"""

    # Create a list of stations
    stations = build_station_list()

    # Run inconsistent typical range stations
    inconsistent_stations = inconsistent_typical_range_stations(stations)

    # Sort data
    inconsistent_stations_sort = sorted(inconsistent_stations)

    # Display data; stations in the given radius of the centre:
    print('The stations that have inconsistent data for their typical range are {}' .format(inconsistent_stations_sort))


if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()