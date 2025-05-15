# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
import unittest
from .utils import sorted_by_key  # noqa
from floodsystem.stationdata import build_station_list #imported for stations_by_river(station)

def rivers_with_station(stations):
    '''Takes a list of stations and returns a set of the rivers which have at least one of those stations on it'''
    ########## tests ##########
    assert(type(stations)==list)    #checks stations is a list
    for s in stations:
        #assert(s is a station object)                                #wasn't sure how to test if s is a station object
        pass
    ###########################
    rivers = set() #initialise set
    for station in stations: #for each station
        rivers.add(station.river) #add the river of that station to the set of rivers, since it is a set there will be no duplications
    

    
    return rivers #return the set

def stations_by_river(stations):
    '''Takes a list of stations and returns a dictionary of {"river_name": "list_of_stations_on_the_river"}'''

    ########## tests ##########
    assert(type(stations)==list)                #checks stations is a list
    for st in stations:
        #assert(s is a station object)          #wasn't sure how to test if s is a station object
        pass
    ###########################

    rivers = rivers_with_station(stations) #sets rivers to a set of river names which have a station from the list on them
    #stationlist = build_station_list() #gets a list of all the stations
    my_dict = {}
    for river in rivers: #for each river - will become dictionary key
        stations_on_river = [] #the list of stations on that river - this list will become dictionary value
        for s in stations: #for each station
            if s.river == river: #if the station is on the river in questions
                stations_on_river.append(s) #add the station to the list
                #could also remove s from stations so less to loop through next time?
        my_dict[river] = stations_on_river #once all stations have been looped through then create new dictionary value
    ########## tests ##########
    assert(type(my_dict)==dict)
    assert(type(list(my_dict.keys())[0]) == str) #checks the first key is a string (seems unessecary to check all keys but could do with a for loop)
    assert(type(list(my_dict.values())[0]) == list) #checks the first key is a list
    ###########################

    return my_dict # then return dictionary

def rivers_by_station_number(stations, N):
    '''Takes a list of stations and a number. Outputs a list of N tuples: (river name, number of stations).
    The list is sorted in descending order of number of stations
    In the case that there are more rivers with the same number of stations as the N th entry, these rivers are included in the list'''
    stat_by_riv_dict = stations_by_river(stations) #a dictionary of {"river_name": "list_of_stations_on_the_river"}
    riv_num_list = [] #will be a list of tuples: (river name, number of stations)
    for r in stat_by_riv_dict: #for each river in the dictionary
        riv_num_list.append((r, len(stat_by_riv_dict[r]))) #add to the list a tuple (river name, number of stations)
    riv_num_list = sorted_by_key(riv_num_list, 1, True) #sort the list of tuples by number of rivers decsending
    nth = riv_num_list[N-1][1] #the number of stations on the nth river
    i = 1 #dummy variable for counting rivers
    while riv_num_list[i-1][1]>= nth: #going through the list checking number of stations is at least as great as the nth river
        i+=1 #increment
        if i-1 == len(riv_num_list):
            break
    n_riv_num_list = riv_num_list[:i-1]

    ########## tests ##########
    assert(type(n_riv_num_list) == list)     #ensures n_riv_num_list is a list
    assert(len(n_riv_num_list) >= N)         #ensures there are (at least) N rivers
    fewest = n_riv_num_list[0][1] #initialise for later test
    for j in n_riv_num_list:
        assert(type(j) == tuple)                    #ensures it is a list of tuples
        assert(len(j) == 2)                         #ensures the tuples are all of length 2
        assert(type(j[0]) == str)                   #ensures the first element of each tuple is a string
        assert(type(j[1]) == int)                   #ensures the second element of each tuple is an integer
        assert(j[1] <= fewest)                      #ensures the list is sorted
        fewest = j[1] #for above test next iteration
        assert(j[1]>=n_riv_num_list[N-1][1])   #ensures all rivers have at least the number of stations the Nth river has
    ###########################

    return n_riv_num_list #once the number of stations is less than for the nth river, we have the list


from math import *

def haversine(a, b):
    # implements the haversine formula between two coordinate tuples a and b
    lat_1 = a[0]
    lat_2 = b[0]
    long_1 = a[1]
    long_2 = b[1]
    d = 2*6371*asin(sqrt(sin(pi*(lat_2-lat_1)/360)**2+cos(lat_2*pi/180)*cos(lat_1*pi/180)*sin(pi*(long_2-long_1)/360)**2))
    assert(type(a) == tuple) # asserts that the coords passed in are tuples
    assert(type(b) == tuple)
    return d

def stations_by_distance(stations, p):
    # generates a list of tuples of stations and distance from a coordinate p, sorted by distance from p
    station_distances = [] #initialse output list
    for station in stations:
            station_data = (station, haversine(station.coord, p)) # generates a 'placeholder' tuple of station and calculated distance
            station_distances.append(station_data) # adds the current placeholder to an unsorted list
    stations_distanced = sorted(station_distances, key=lambda t: t[1]) #sort by second entry in tuple

    #tests
    assert(type(stations_distanced) == list) # asserts a list is returns

    for i in range(len(stations_distanced)-1):
        assert(type(stations_distanced[i]) == tuple)  # asserts that the list is made of tuples
        assert(type(stations_distanced[i][1]) == float)  # asserts that the second entry of each tuple is a floating point number
        assert(len(stations_distanced[i]) == 2) # asserts that each tuple is of length 2

    return stations_distanced



def stations_within_radius(stations, centre, r):
    # returns a list of stations within a radius r of a central point
    nearby_stations = []
    for station in stations:
        if haversine(station.coord, centre) < r:
            nearby_stations.append(station)


    # tests
    assert(type(centre) == tuple)  # assert that the given centre coord is a tuple
    assert(type(centre[0]) == float)  # assert that the lat and long are floating point numbers
    assert(type(centre[1]) == float)
    assert(type(r) == float or int) # assert that the radius given is a number

    return nearby_stations

