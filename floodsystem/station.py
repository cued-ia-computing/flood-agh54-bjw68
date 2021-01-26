# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d

def sampledata():
    station1 = MonitoringStation(station_id='Leeds Killingbeck Dam',
                measure_id='http://environment.data.gov.uk/flood-monitoring/id/stations/L17014',
                label='http://environment.data.gov.uk/flood-monitoring/id/measures/L17014-level-stage-i-15_min-m',
                coord=(53.807923, -1.487022),
                typical_range=(1.03, 1.306),
                river='Wyke Beck',
                town='Leeds Killingbeck Dam')
    station2 = MonitoringStation(station_id='Scurf Dyke',
                measure_id='http://environment.data.gov.uk/flood-monitoring/id/stations/L3010',
                label='http://environment.data.gov.uk/flood-monitoring/id/measures/L3010-level-stage-i-15_min-m',
                coord=(54.006951, -0.250223),
                typical_range=(1.03, 1.306),
                river='Glenridding Beck',
                town='Barmston Main Drain')
    station3 = MonitoringStation(station_id='Loftsome Bridge',
                measure_id='http://environment.data.gov.uk/flood-monitoring/id/stations/F2802',
                label='http://environment.data.gov.uk/flood-monitoring/id/measures/F2802-level-stage-i-15_min-mAOD',
                coord=(53.759195, -0.936675),
                typical_range=(41.225, 42.9),
                river='River Derwent',
                town='Loftsome Bridge')
    station4 = MonitoringStation(station_id='Upton',
                measure_id='http://environment.data.gov.uk/flood-monitoring/id/stations/45188',
                label='http://environment.data.gov.uk/flood-monitoring/id/measures/45188-level-stage-i-15_min-m',
                coord=(51.050366, -3.444914),
                typical_range=(0.084, 0.85),
                river='River Haddeo',
                town='Upton')
    station5 = MonitoringStation(station_id='Catterick Brough Park',
                measure_id='http://environment.data.gov.uk/flood-monitoring/id/stations/45188',
                label='http://environment.data.gov.uk/flood-monitoring/id/measures/45188-level-stage-i-15_min-m',
                coord=(54.374006, -1.650387),
                typical_range=(-0.02, 0.463),
                river='Brough Beck',
                town='Catterick FAS Brough Park')
    stationlist = [station1, station2, station3, station4, station5, station1]
    return stationlist
