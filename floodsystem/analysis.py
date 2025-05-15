import numpy as np
import matplotlib.dates as mpd
from datetime import *
from floodsystem.stationdata import *
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level
def polyfit(dates, levels, p):
    '''A function which, given a list of dates and a list of levels and an integer p
    returns a polynomial function to fit the data and an axis shift if necessary'''
    #checks
    assert(isinstance(p, int)) #to ensure p is a integer
    assert(len(dates) == len(levels)) #check the lists have the same length
    for n in range (len(dates)): #check each element is of the correct type
        assert(type(dates[n]) == datetime)
        assert(type(levels[n]) == float)

    dates_as_nums = mpd.date2num(dates)
    y = [0.1, 0.09, 0.23, 0.34, 0.78, 0.74, 0.43, 0.31, 0.01, -0.05]
    y = levels
    x = np.linspace(0, 2, len(y))
    x = dates_as_nums
    #y = [1,0.5,1]
    #x = np.linspace(0, 2, len(y))
    # Find coefficients of best-fit polynomial f(x) of degree 4
    p_coeff = np.polyfit(x-x[0], y, p)

    # Convert coefficient into a polynomial that can be evaluated,
    # e.g. poly(0.3)
    poly = np.poly1d(p_coeff)
    return poly, x[0] #returns the polynomial and the axis shift