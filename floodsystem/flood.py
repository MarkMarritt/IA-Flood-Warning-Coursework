import numpy as np
from .station import MonitoringStation

def stations_level_over_threshold(stations, tol):
    """Create a list of tuples, where each tuple contains the name of 
    station and latest relative water level, for stations with greater 
    relative water level than the tolerance"""
    level_over_threshold_names = []
    # For each station: find relative water level, check if its not None, 
    # check if its greater than or equal to tolerance, 
    # add a tuple with its name and relative water level to the list
    for station in stations:
        water_level_fraction = MonitoringStation.relative_water_level(station)
        if water_level_fraction == None:
            pass
        else:
            if water_level_fraction >= tol:
                level_over_threshold = (station.name, water_level_fraction)
                level_over_threshold_names.append(level_over_threshold)
    # Sort by descending order of relative water levels
    level_over_threshold_names.sort(reverse = True, key=lambda x: x[1])
    return level_over_threshold_names