# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
import numpy as np
from .utils import sorted_by_key  # noqa


def stations_by_distance(stations, p):
    """returns a list of tuples: (name of station, distance of station from point p)"""
    if isinstance(p, tuple) and isinstance(stations, list):
        pass
    else:
        raise ValueError("Second arguement (coordinate) needs to be a tuple.")
    

    distDict = stationCoordinates(stations) # make a dictionary of all staions and their coordinates
    
    tupleList = []
    for i in distDict:
        newEntry = (i, havFormula(distDict[i], p)) # applies the distance formula and appends to a list of tuples
        
        tupleList.append(newEntry)
    
    tupleList = sorted_by_key(tupleList, 1) # sort using the .utils module
    return tupleList

    
    


def havFormula(point1, point2):
    """determines the geographic distance in km of two points"""
    # earth diameter = 12742km
    lat1, long1 = point1[0], point1[1]
    lat2, long2 = point2[0], point2[1]
    for i in [lat1, lat2, long1, long2]:
        if isinstance(i, int) or isinstance(i, float):
            pass
        else:
            raise ValueError("Data type is not an integer/float!")
            
    lat1, lat2, long1, long2 = np.radians(lat1), np.radians(lat2), np.radians(long1), np.radians(long2)
    
    distance = 12742*np.arcsin(np.sqrt( np.sin((lat2 - lat1)*0.5)**2 + (np.cos(lat1) * np.cos(lat2) * np.sin((long2 - long1)*0.5)**2))) # haversine formula, from wikipedia
    return distance


def stationCoordinates(stations):
    """takes the stations and their coordinates as a dictionary"""
    stationCoords = {}
    for station in stations:
        stationCoords[station.name] = station.coord
    return stationCoords


