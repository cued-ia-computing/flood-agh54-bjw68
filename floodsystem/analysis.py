from .stationdata import build_station_list, update_water_levels
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def current_highest_stations(stations, number):
    highest_stations = []
    update_water_levels(stations)
    for station in stations:
        if station.latest_level != None:
            highest_stations.append((station, station.latest_level))
    

    highest_stations_sort = sorted(highest_stations, key=lambda x: x[1], reverse=True)
    output = highest_stations_sort[0:number]
    return output

def polyfit(dates, levels, p):
    dates_num = []
    for date in dates:
        dates_num.append(matplotlib.dates.date2num(date))

    p_coeff = np.polyfit(dates_num - dates_num[0], levels, p)
    poly = np.poly1d(p_coeff)
    x1 = np.linspace(dates_num[0], dates_num[-1], 30)

    
    plt.plot(x1, poly(x1 - dates_num[0]))
    plt.tight_layout()

    return plt