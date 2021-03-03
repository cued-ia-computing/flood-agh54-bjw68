from floodsystem.warning import highest_water_level, towns_and_levels, flood_warning
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_levels
from floodsystem.analysis import current_highest_stations, polyfit
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import MonitoringStation
from floodsystem.utils import sorted_by_key
import datetime
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

stations = build_station_list()
dt = 10
p = 4
days = 1
severe = 2
high = 1.5
moderate = 1
low = 0

towns_water_levels=(towns_and_levels(stations, p, days))

print(flood_warning(towns_water_levels, severe, high, moderate, low))
