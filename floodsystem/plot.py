import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from floodsystem.stationdata import *
from floodsystem.station import *
import numpy as np
import matplotlib.dates as mpd
from floodsystem.analysis import polyfit
from floodsystem.datafetcher import fetch_measure_levels
def plot_water_levels(station, dates, levels):
    '''Creates a plot of the given station's water levels over the specified dates
    it also marks on the typical levels as passed in the function parameters
    station should be one station
    dates should be a list of dates
    levels is the typical_range for the station''' 
    #checks
    plottable = True
    try:
        assert(len(dates) == len(levels)) #check the lists have the same length
        assert(isinstance(station,MonitoringStation))
        for n in range (len(dates)): #check each element is of the correct type
            assert(type(dates[n]) == datetime)
            assert(type(levels[n]) == float)
    except:
        plottable =False
    if plottable == True:
        # Plot
        plt.plot(dates, levels, color = "b")
        #add typical range
        #if typical range is inconsistent it is better to plot the graph without the range than to cause an error
        #this will be important in testing
        try:
            assert(station.typical_range_consistent())
            plt.axhline(y = station.typical_range[0], color = 'r', linestyle = '--')
            plt.axhline(y = station.typical_range[1], color = 'r', linestyle = '--')
        except:
            print(str(station.name) + " has inconsistent typical range data")
        ##########
        
        
        # Add axis labels, rotate date labels and add plot title
        plt.xlabel('Date')
        plt.ylabel('Water level (m)')
        plt.xticks(rotation=45);
        plt.title(station.name)

        # Display plot
        plt.tight_layout()  # This makes sure plot does not cut off date labels

        plt.show()


def plot_water_level_with_fit(station, dates, levels, p):
    '''Creates a plot of the given station's water levels over the specified dates
    it also marks on the typical levels as passed in the function parameters
    station should be one station and plots a best fit line
    dates should be a list of dates
    levels is the typical_range for the station'''
    plottable = True
    #checks
    try:
        assert(isinstance(p, int))
        assert(isinstance(station,MonitoringStation))
        assert(len(dates) == len(levels)) #check the lists have the same length
        for n in range (len(dates)): #check each element is of the correct type
            assert(type(dates[n]) == datetime)
            assert(type(levels[n]) == float)
    except:
        plottable = False
    if plottable == True:
        # Plot orginal points
        plt.plot(dates, levels, color = "b")
        try:
            assert(station.typical_range_consistent())
            plt.axhline(y = station.typical_range[0], color = 'r', linestyle = '--')
            plt.axhline(y = station.typical_range[1], color = 'r', linestyle = '--')
        except:
            print(str(station.name) + " has inconsistent typical range data")
        
        # Add axis labels, rotate date labels and add plot title
        plt.xlabel('Date')
        plt.ylabel('Water level (m)')
        plt.xticks(rotation=45);
        plt.title(station.name)
        ##########
        dates_as_nums = mpd.date2num(dates)
        y = levels
        x = dates_as_nums
        #########
        # Plot polynomial fit at 30 points along interval
        x1 = np.linspace(x[0], x[-1], 30)

        poly, d0 = polyfit(dates, levels, p)

        plt.plot(x1, poly(x1-d0), color = "g")

        # Display plot
        plt.tight_layout()  # This makes sure plot does not cut off date labels

        plt.show()