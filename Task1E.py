# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.geo import *
from floodsystem.stationdata import build_station_list
#from utils import sorted_by_key

def run():
    '''Demonstrates the functionality of the deliverables required by Task1E for Milestone 1'''
    all_stations = build_station_list()
    N=9
    rivers_by_no_stations = rivers_by_station_number(all_stations, N)

    print(rivers_by_no_stations)

if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()