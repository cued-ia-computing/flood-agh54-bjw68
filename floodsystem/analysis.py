from .stationdata import build_station_list, update_water_levels
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def current_highest_stations(stations, number):
    """Output list of the n stations with the current highest water level, including that water level"""

    #Create list of highest stations and get current levels
    highest_stations = []
    update_water_levels(stations)

    
    checked_list = []
    for station in stations:
        #If the station has a valid water level, add tuple of name and water level
        if station.latest_level != None and station.latest_level < 1000 and station.name not in checked_list:
            highest_stations.append((station, station.latest_level))

            #List to stop duplicates
            checked_list.append(station.name)
    
    #Sort the list by water level
    highest_stations_sort = sorted(highest_stations, key=lambda x: x[1], reverse=True)

    #Only output the desired first n stations
    output = highest_stations_sort[0:number]
    return output


def polyfit(dates, levels, p):
    """Output polynomial plot that is fitted to the historic water level"""


    #Convert the date into a number and add to new dates list
    dates_num = []
    for date in dates:
        dates_num.append(matplotlib.dates.date2num(date))

    #Find polynomial coefficents using shifted dates, historic water levels and desired polynomial order
    p_coeff = np.polyfit(dates_num - dates_num[0], levels, p)

    #Creates polynomial using the produced coefficient
    poly = np.poly1d(p_coeff)

    #Create a new list of date spaces for plotting
    x1 = np.linspace(dates_num[0], dates_num[-1], 30)

    #Plot the polynomial fit, calculated at shifted time values, against the time values
    plt.plot(x1, poly(x1 - dates_num[0]))
    plt.tight_layout()

    #Return plot to be plotted
    return plt


def flow_range(stations):
    update_water_levels(stations)
    colours = []
    for station in stations:
        current_level = station.latest_level 
        flow_r = station.typical_range


        if current_level == None or station.typical_range == None:
            colour = "red"
            colours.append(colour)

        elif current_level <= flow_r[0]:
            colour = "green"
            colours.append(colour)

        elif flow_r[0] < current_level < flow_r[1]:
            colour = "blue"
            colours.append(colour)
        
        elif current_level >= flow_r[1]:
            colour = "goldenrod"
            colours.append(colour)

    return colours




