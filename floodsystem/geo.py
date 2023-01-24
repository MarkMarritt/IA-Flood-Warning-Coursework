# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
import numpy as np
from .utils import sorted_by_key  # noqa
from .station import MonitoringStation

def stations_by_distance(stations, p):
    """returns a list of tuples: (name of station, distance of station from point p)"""
    dataClean(stations) # removes anything from the list that isn't a MonitoringStation
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
    stations = dataClean(stations)
    stationCoords = {}
    for station in stations:
        stationCoords[station.name] = station.coord
    return stationCoords


def stations_within_radius(stations, centre,r):
    """returns a list of any stations within a radius r of a centre"""
    stationsInR = []

    stations = dataClean(stations)
    
    distancesFromCentre = stations_by_distance(stations, centre)
    for j in distancesFromCentre:
        if j[1] < r:
            stationsInR.append(j[0])
    
    return stationsInR

def dataClean(stations):
    """removes any data types from a list that arent MonitoringStation"""
    stationRemovals = [] # creating a list of stations to be removed from the "station" list, if they are not of the type "MonitoringStation"
    for station in stations:
        if isinstance(station, MonitoringStation):
            pass
        else:
            stationRemovals.append(station)
    for i in stationRemovals:
            stations.remove(i)
    return stations


def rivers_by_station_number(stations, N):
    river_freq_dict={}
    for station in stations:
        if station.river in river_freq_dict:
            river_freq_dict[station.river]+=1
        else:
            river_freq_dict[station.river]=1   #creates a dict of river names and the number they appear
    
    river_freq_tuples=[]
    for item in river_freq_dict.items():
        river_freq_tuples.append(item)      # converts the dict to a list of tuples
    river_freq_sort=sorted_by_key(river_freq_tuples, 1, True)   # sorts the list of tuples (in reverse) by the built in util function
    
    river_freq_N=[]
    count=0
    for element in river_freq_sort: 
        if count<N:
            river_freq_N.append(element)  # adds first N tuples to the empty list
        elif river_freq_sort[count][1]==river_freq_sort[N-1][1]:  #adds any more tuples that are monitored by the same number of stations
            river_freq_N.append(element)
        count+=1
    
    return(river_freq_N) 