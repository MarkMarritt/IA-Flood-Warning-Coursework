# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data"""


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

    def typical_range_consistent(self):
        """Method that checks typical high/low range data for inconsistency"""
        # Return False if there is no data for typical high/low range 
        # Return False if low range is greater than high range
        if not self.typical_range or self.typical_range[0] > self.typical_range[1]:
            return False
        else:
            return True
    
    def relative_water_level(self):
        """Method that returns the latest water level as a fraction of the typical range"""
        # Check for inconsistency of typical range data - return None if inconsistent
        if MonitoringStation.typical_range_consistent(self) == False or self.latest_level == None:
            water_level_fraction = None
        # Calculate latest level as fraction of typical range
        # Fraction = 1 if latest level = typical high
        # Fraction = 0 if latest level = typical low
        elif MonitoringStation.typical_range_consistent(self) == True:
            range = self.typical_range[1] - self.typical_range[0]
            water_level_fraction = (self.latest_level - self.typical_range[0])/range
        return water_level_fraction

# Creating list of stations with inconsistent typical range data
def inconsistent_typical_range_stations(stations):
    station_Names = []
    for station in stations:
        if MonitoringStation.typical_range_consistent(station) == False:
            station_Names.append(station.name)
        else:
            pass
    return station_Names