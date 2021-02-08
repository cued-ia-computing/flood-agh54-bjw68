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

    # Create new list which includes the town
    distances_with_towns = []

    # Fill the list
    for distance in distances:
        for station in stations:
            if distance[0] == station.name:
                town = station.town
        data = (distance[0], town, distance[1])
        distances_with_towns.append(data)

    # Display data; closest and furthest 10 stations:
    stations_close = distances_with_towns[:10]
    print('The ten closest stations to (52.2053, 0.1218) are {}' .format(stations_close))
    stations_far = distances_with_towns[-10:]
    print('The ten furthest stations to (52.2053, 0.1218) are {}' .format(stations_far))


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()