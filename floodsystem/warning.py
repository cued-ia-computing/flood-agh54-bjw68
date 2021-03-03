from .datafetcher import fetch_measure_levels
from .plot import plot_water_levels
from .analysis import current_highest_stations, polyfit
from .stationdata import build_station_list, update_water_levels
from .station import MonitoringStation
from .utils import sorted_by_key
import datetime
import matplotlib
import matplotlib.pyplot as plt
import numpy as np



# Create a modification of the function in 2F that predicts the future water levels for a certain number of days and returns the highest value
def highest_water_level(dates, levels, p, days):
    """Outputs the predicted highest water level for a station"""

    #Convert the date into a number and add to new dates list
    dates_num = []
    for date in dates:
        dates_num.append(matplotlib.dates.date2num(date))

    #Find polynomial coefficents using shifted dates, historic water levels and desired polynomial order
    p_coeff = np.polyfit(dates_num - dates_num[0], levels, p)

    #Creates polynomial using the produced coefficient
    poly = np.poly1d(p_coeff)

    # list of future dates
    future_dates = []
    for i in range(4*24*days):
        future_dates.append(dates_num[0]+(dates_num[0]-dates_num[(4*24*days)-i]))

    
    #Create a new list of date spaces for plotting
    x1 = np.linspace(future_dates[0], future_dates[-1], 30)
    
    #create list of predicted levels
    water_levels = poly(x1 - dates_num[0])

    # finds the average of the 3 highest values for water level
    levels_sort = sorted(water_levels, reverse=True)
    highest_average = sum(levels_sort[:3])/3

    #Returns the value
    return highest_average

# This function creates a list of stations with their highest level
def towns_and_levels(stations, p, days, dt):
    # creates an empty list
    data = []

    # for each station works out the highest predicted water level and adds the information to the list above
    for i in range(len(stations)):
        if stations[i].typical_range_consistent() == True:
            try:
                dates, levels = fetch_measure_levels(stations[i].measure_id, dt=datetime.timedelta(days=dt))
            except:
                dates = []
                levels = []
            if len(dates) == 0 or len(levels) == 0 or len(dates) != len(levels):
                pass
            else:
                try:
                    highest = highest_water_level(dates, levels, p, days)
                except:
                    pass
                stations[i].latest_level = highest
                ratio = stations[i].relative_water_level()
                data.append((stations[i].town, ratio))

    #return data
    return data


# This function returns a list of towns at severe risk of flooding
def flood_warning(towns_levels, severe, high, moderate, low):
    # first we remove towns where there is a duplicate, keeping the higher value of relative level
    
    #sort in decending order
    sorted_by_level = sorted_by_key(towns_levels, 1, reverse=True)

    #initialise the lists
    severe_risk = []
    high_risk = []
    moderate_risk = []
    low_risk = []

    # iterate through sorted list, adding only new towns
    for town in sorted_by_level:
        if town[0] in severe_risk:
            break
        elif town[1] > severe:
            severe_risk.append(town)
        elif town[0] in high_risk:
            break
        elif town[1] > high:
            high_risk.append(town)
        elif town[0] in moderate_risk:
            break
        elif town[1] > moderate:
            moderate_risk.append(town)
        elif town[0] in low_risk:
            break
        else:
            low_risk.append(town)

    # only the towns at severe risk need to be returned, hence:
    return severe_risk, high_risk