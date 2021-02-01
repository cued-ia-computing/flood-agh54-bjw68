from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

def run():
    """Requirements for Task 1B"""

    # Create a list of stations
    stations = build_station_list()
    
    # Establish point to be centre
    p = 52.2053, 0.1218

    # Run stations by distance, creating a list of stations from a point
    stations_in_radius = stations_within_radius(stations, p, 10)

    # Display data; stations in the given radius of the centre:
    print('The stations that are within 10km from (52.2053, 0.1218) are {}' .format(stations_in_radius))


if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()