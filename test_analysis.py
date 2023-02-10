"""unit tests for the analysis sub module"""
import matplotlib
import math
import pytest
import numpy as np
from floodsystem.analysis import polyfit
from testdata import dates10, ybad, yconstant, ylinear, yquadratic



def test_polyfit():
    poly1, shift = polyfit(dates10, yconstant, 5)
    values = matplotlib.dates.date2num(dates10)
    for i in range(len(values)):
        values[i] = values[i] - shift
        assert math.isclose(poly1(values[i]), yconstant[i], abs_tol= 1E-09)

    poly2, shift = polyfit(dates10, ylinear, 5)
    values = matplotlib.dates.date2num(dates10)
    for i in range(len(values)):
        values[i] = values[i] - shift
        assert math.isclose(poly2(values[i]), ylinear[i], abs_tol= 1E-09)


    poly3, shift = polyfit(dates10, yquadratic, 5)
    values = matplotlib.dates.date2num(dates10)
    for i in range(len(values)):
        values[i] = values[i] - shift
        assert math.isclose(poly3(values[i]), yquadratic[i], abs_tol= 1E-09)

    with pytest.raises(ValueError):
        poly4, shift = polyfit(dates10, ybad, 5)


    



test_polyfit()