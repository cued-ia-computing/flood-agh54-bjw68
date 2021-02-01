from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance
from floodsystem.utils import sorted_by_key

def run():
    """Requirements for Task 1B"""

    # Create a list of stations
    stations = build_station_list()
    
    # Establish point to calculate distance from
    p = 52.2053, 0.1218

    # Run stations by distance, creating a list of stations from a point
    distances = stations_by_distance(stations, p)

    # Display data; closest and furthest 10 stations:
    stations_close = distances[:10]
    print('The ten closest stations to (52.2053, 0.1218) are {}' .format(stations_close))
    stations_far = distances[-10:]
    print('The ten furthest stations to (52.2053, 0.1218) are {}' .format(stations_far))


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()