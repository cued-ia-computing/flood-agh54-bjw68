"""This module contains a collection of functions related to
plotting data.
"""

from .datafetcher import fetch_measure_levels
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


def plot_water_levels(station, dates, levels):
    """Plot water level with time"""

    #Create  variables for low and high range
    low_level = station.typical_range[0]
    high_level = station.typical_range[1]

    #Create low and high lists of the correct length for plotting
    low_level_list = [low_level] * len(dates)
    high_level_list = [high_level] * len(dates)

    # Plot the water level against date
    plt.plot(dates, levels)

    #Plot low and high levels at all dates
    plt.plot(dates, low_level_list)
    plt.plot(dates, high_level_list)

    #Add correct axes labels
    plt.xlabel('Date')
    plt.ylabel('Water level (m)')

    #Orient labels and add title
    plt.xticks(rotation=45);
    plt.title("Station: {}".format(str(station.name)))

    #Set layout and return graph so it can be plotted
    plt.tight_layout()
    return plt