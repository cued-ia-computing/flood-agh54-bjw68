# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa

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
        
        # If the river value of a station matches the current river, add it to the lisr
        for station in stations:
            if station.river == river:
                river_list.append(station)
        river_list.sort()
        rivers_dict[river] = river_list

    return rivers_dict