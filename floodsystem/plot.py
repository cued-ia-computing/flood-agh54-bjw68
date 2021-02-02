"""This module contains a collection of functions related to
plotting data.
"""

from .datafetcher import fetch_measure_levels
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


def plot_water_levels(station, dates, levels):
    """Plot water level with time"""
    low_level = station.typical_range[0]
    high_level = station.typical_range[1]

    low_level_list = [low_level] * len(dates)
    high_level_list = [high_level] * len(dates)

    plt.plot(dates, levels)
    plt.plot(dates, low_level_list)
    plt.plot(dates, high_level_list)
    plt.xlabel('Date')
    plt.ylabel('Water level (m)')
    plt.xticks(rotation=45);
    plt.title("Station: {}".format(str(station.name)))

    plt.tight_layout()
    plt.show()