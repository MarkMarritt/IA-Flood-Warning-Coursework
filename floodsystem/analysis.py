import numpy as np
import matplotlib
from datetime import datetime
from matplotlib import dates

def polyfit(dates, levels, p):
    """returns a polynomial with order p, fitting levels agaisnt dates"""

    for i in levels:
        if isinstance(dates and levels, list) and isinstance(p, int): # checks data to make sure they are correct data type
            pass
        else:
            raise TypeError("Data types entered are not valid for function.")
    if len(dates) != len(levels): # checks that the data is consistent
        raise ValueError("The lengths of the two strings are not the same")
    else:
        pass

    times, shift = datesToTime(dates)
    coefficients = np.polyfit(times, levels, p) # uses numpy to generate a polynomial
    polynomial = np.poly1d(coefficients)
    
    return polynomial, shift

def datesToTime(dates, final = False):
    """converts a list of dates to a list with values in days"""

    for i in dates:
        if isinstance(i, datetime):
            pass
        else:
            raise TypeError("The dates are not of the class 'datetime'")
    timeValues = matplotlib.dates.date2num(dates) # converts dates to a set of time values
    shift = min(timeValues) # takes away the lowest value from the rest
    for i in range(len(timeValues)):
        timeValues[i] = timeValues[i] - shift
    if final == True:
        return timeValues, max(timeValues)
    else:
        return timeValues, shift

