from .station import MonitoringStation
from .utils import sorted_by_key

def stations_level_over_threshold(stations, tol):
    # creates an empty list
    flood = []

    # iterates through the list and adds a stationif its data is consistent and its above the tolerance
    for station in stations:
        if station.typical_range_consistent() == False or station.relative_water_level() == None:
            pass
        elif station.relative_water_level() > tol:
                data = (station, station.relative_water_level())
                flood.append(data)
    
    #sorts the list in decending order
    flood_sorted = sorted_by_key(flood,1, reverse=True)
    return flood_sorted