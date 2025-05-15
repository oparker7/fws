# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.geo import *
from floodsystem.stationdata import build_station_list
#from utils import sorted_by_key

def run():
    '''Demonstrates the functionality of the deliverables required by Task1D for Milestone 1'''
    #demonstration 1
    all_stations = build_station_list() #gets a list of all stations
    all_rivers = rivers_with_station(all_stations)
    print("\nNumber of rivers with a station: ")
    print(len(all_rivers))
    list_rivers = []
    for i in all_rivers:
        list_rivers.append(i)
    list_rivers.sort()
    print("\nFirst ten rivers sorted alphabetically: ")
    print(list_rivers[:10])

    #demonstration 2
    stat_by_riv = stations_by_river(all_stations) #dictionary
    for riv in ["River Aire", "River Cam", "River Thames"]:
        names = []
        stat_list = stat_by_riv[riv] #list of stations
        for stat in stat_list:
            names.append(stat.name)
        names.sort()
        print("\nStations on river "+riv+": ")
        print(names)

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()