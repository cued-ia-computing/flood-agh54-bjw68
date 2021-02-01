# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
import plotly.express as px
import geopandas
import pandas as pd
from haversine import haversine, Unit


def rivers_with_station(stations):
    """Created a sorted list of Rivers with stations on them"""
    # Initialise rivers list
    rivers = []

    # Add river to list from station, if river is not present
    for station in stations:
        if station.river in rivers:
            pass
        else:
            rivers.append(station.river)

    # Sort list
    rivers.sort()
    return rivers

def stations_by_river(stations):
    """Create a dictionary of all Rivers with a corresponding station list"""

    # Initialise river dictionary
    rivers_dict = {}

    # Create list of valid rivers
    rivers = rivers_with_station(stations)

    # Create a station list for each river
    for river in rivers:
        river_list = []
        
        # If the river value of a station matches the current river, add it to the list
        checked_stations = []
        for station in stations:
            if station.name not in checked_stations:
                if station.river == river:
                    river_list.append(station.name)
                checked_stations.append(station.name)
        river_list.sort()
        rivers_dict[river] = river_list
    return rivers_dict

def rivers_by_station_number(stations, N):
    """Create a dictionary of stations and corresponding number"""

    # Initialise station list and container for all rivers
    river_stations = stations_by_river(stations)
    river_number = []

    # Find number for all rivers
    for river in river_stations:

        # Sum number of stations on each river
        total = 0
        for station in river_stations[river]:
            total += 1

        # Create a container for the river and its value
        river_value = (river, total)
        river_number.append(river_value)

    # Sort total list by number in reverse order
    river_num_sorted = sorted(river_number, key=lambda x: x[1], reverse=True)


    # Iterate through list of rivers
    count = 0
    top_N_rivers = []

    # Break when desired value is reached
    while count < N and count < len(river_num_sorted):

        # Add top river
        if count == 0:
            top_N_rivers.append(river_num_sorted[0])
            count += 1

        # Add river and to the count provided the entry is smaller than the last
        elif (river_num_sorted[count][1]) < (river_num_sorted[count-1][1]):
            top_N_rivers.append(river_num_sorted[count])
            count += 1

        # Add river when it has the same as the previous number, but add to N as well to preserve distance
        else:
            top_N_rivers.append(river_num_sorted[count])
            count += 1
            N += 1

    # Return list
    return top_N_rivers


def map_station(stations):
    """Function to plot the locations of the pumping stations"""

    #Create coordiante lists
    coordx = []
    coordy = []
    name = []

    # Stores coordinate data per station
    for station in stations:
        coordx.append(station.coord[0])
        coordy.append(station.coord[1])
        name.append(station.name)
    
    # Creates a dataframe of names and coordinates
    df = pd.DataFrame(
    {'City': name,
     'Latitude': coordx,
     'Longitude': coordy})

    # Convert to geo-dataframe storage type for access
    gdf = geopandas.GeoDataFrame(df, geometry=geopandas.points_from_xy(df.Longitude, df.Latitude))

    # Output dataframe
    return gdf


def position_plotter(geodf):
    # Creates a map image with points plotted at coordiantes, labelled with their name
    fig = px.scatter_geo(geodf,
                    lat=geodf.geometry.y,
                    lon=geodf.geometry.x,
                    hover_name="City", )

    # Fits the view around the input data
    fig.update_geos(fitbounds="locations")

    # Modifies plot window and margins
    fig.update_layout(height=300, margin={"r":0,"t":0,"l":0,"b":0})

    # Plots the result
    fig.show()

    gdf = geopandas.GeoDataFrame(df, geometry=geopandas.points_from_xy(df.Longitude, df.Latitude))
    fig = px.scatter_geo(gdf,
                    lat=gdf.geometry.y,
                    lon=gdf.geometry.x,
                    hover_name="City")
    fig.show()

def stations_by_distance(stations, p):
    """Create a list of stations ordered by distance from a specified location"""

    # Create list
    distances = []

    # Calculate the distance from the point to each station use the haversine library function and add to list
    for station in stations:
        if station in distances:
            pass
        else:
            distance = haversine(station.coord,p)
            distances.append((station.name,distance))
    
    # Sort by distance and return this list
    distances_sorted = sorted_by_key(distances,1)
    return distances_sorted

def stations_within_radius(stations, centre, r):
    """Create a list of stations within a certain radius of a specified location"""

    # Create list
    close_stations = []

    # Adds valid stations to the list
    for station in stations:
        if station in close_stations:
            pass
        else:
            # works out distance of station from centre
            distance = haversine(station.coord,centre)
            if distance < r:
                close_stations.append(station.name)
            else:
                pass
    
    # Sort by distance and return this list
    stations_sorted = sorted(close_stations)
    return stations_sorted
