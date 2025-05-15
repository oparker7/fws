from floodsystem.plot import *
from floodsystem.stationdata import * 
from floodsystem.datafetcher import *
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt

def test_plot_water_levels():
    stations = build_station_list()
    update_water_levels(stations)
    test_dates = np.empty(3, dtype=object)
    test_levels = np.empty(3, dtype=object)
    plot_water_levels(stations[0], test_dates, test_levels)#empty lists
    assert plt.show() == None
    levels = [1, 2, 3, 4]
    dates = [datetime(2016, 12, 30), datetime(2016, 12, 31), datetime(2017, 1, 1)]
    plot_water_levels(stations[0], test_dates, test_levels)#different lengths
    assert plt.show() == None
    levels = [1,2,3]
    plot_water_levels(test_dates[0], test_dates, test_levels)#not a station
    assert plt.show() == None

def test_plot_water_level_with_fit():
    stations = build_station_list()
    update_water_levels(stations)
    test_dates = np.empty(3, dtype=object)
    test_levels = np.empty(3, dtype=object)
    plot_water_level_with_fit(stations[0], test_dates, test_levels, 3)#empty lists
    assert plt.show() == None
    levels = [1, 2, 3, 4]
    dates = [datetime(2016, 12, 30), datetime(2016, 12, 31), datetime(2017, 1, 1)]
    plot_water_level_with_fit(stations[0], test_dates, test_levels, 3)#different lengths
    assert plt.show() == None
    levels = [1,2,3]
    plot_water_level_with_fit(test_dates[0], test_dates, test_levels, 3)#not a station
    assert plt.show() == None
    plot_water_level_with_fit(stations[0], test_dates, test_levels, 3.1)#p not integer
    assert plt.show() == None