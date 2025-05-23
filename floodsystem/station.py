# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


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
        ''' Returns true if the typical range is consistent, i.e. it exists and max>min'''
        if type(self.typical_range) != tuple:
            return False
        if type(self.typical_range[0]) != float:
            return False
        if type(self.typical_range[1]) != float:
            return False
        if len(self.typical_range) != 2:
            return False
        if self.typical_range[1] <= self.typical_range[0]: #if there is data and typical max <= min
            return False
        else:
            return True #otherwise return true


    def relative_water_level(self):

        if self.typical_range_consistent() == False:    # check that typical range is consistent
            return None 
        elif self.latest_level == None or self.typical_range[0] == None or self.typical_range[1] == None:
            return None
        else:
            l_now = self.latest_level
            l_min = self.typical_range[0]
            l_max = self.typical_range[1]

        
        risk_factor = (l_now - l_min)/(l_max - l_min)       # calculate risk factor
        
        return float(risk_factor)               # return risk factor 





def inconsistent_typical_range_stations(stations):
    '''From a list stations, this function will return a list of stations that have inconsistent data'''
    #test:
    assert stations
    #
    inconsistent = []
    for s in stations:
        if not s.typical_range_consistent():
            inconsistent.append(s.name)
    return inconsistent