from matplotlib import pyplot as plt
from .station import MonitoringStation
from .analysis import polyfit, datesToTime
import numpy as np
from datetime import datetime

def plot_water_levels(station, dates, levels, show = True ):
    """plots dates against levels with title as station name."""

    if isinstance(levels and dates, list):
        pass
    else:
        raise TypeError("Levels needs to be a list")
    for i in levels:
        if isinstance(station, MonitoringStation) and isinstance(i, float): # checks data to make sure they are correct data type
            pass
        else:
            raise TypeError("Data types entered are not valid for function.")
    for i in dates:
        if isinstance(i, datetime):
            pass
        else:
            raise TypeError("The dates are not all of correct type")
    if len(dates) != len(levels):
        raise ValueError("The lengths of the two lists are not the same")
    else:
        pass
    
    typicalRange = station.typical_range

    plt.plot(dates, levels, label = "river level",  color = "black") # plots the two lists of data agianst each other
    plt.axhline(typicalRange[0], label = "Typical range low", color = "pink")
    plt.axhline(typicalRange[1], label = "Typical range high", color = "purple")
    plt.xlabel("dates")
    plt.xticks(rotation = 45)
    plt.ylabel("levels")
    plt.title(station.name)
    plt.legend()
    if show == True:
        plt.show()
    else:
        pass


def plot_water_level_with_fit(station, dates, levels, p, show = True):
    """plots water levels and the fitted graph for the data on the same graph"""
    plot_water_levels(station,dates, levels, show = False) # plots the data onto a graph

    poly, shift = polyfit(dates, levels, p) # get the fitted polynomial
    times, finalTime  = datesToTime(dates, final=True)
    
    x = np.linspace(0, finalTime, len(times)) # generate a numpy array of length dates, from 0 to the latest time
    y = poly(x) # puts array through polynomial
    typicalRange = station.typical_range

    plt.plot(dates, y, label = "fitted", color = "green") # plot the fitted data on the same graph
    plt.title(station.name)
    plt.xlabel("dates")
    plt.xticks(rotation = 45)
    plt.ylabel("levels")
    plt.title(station.name)
    plt.legend()
    if show == True:
        plt.show()
    else:
        pass

    

