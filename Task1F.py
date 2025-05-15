# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.geo import *
from floodsystem.station import inconsistent_typical_range_stations, MonitoringStation
from floodsystem.stationdata import build_station_list
#from utils import sorted_by_key

def run():
    '''Demonstrates the functionality of the deliverables required by Task1F for Milestone 1'''
    all_stations = build_station_list()
    inconsistent = inconsistent_typical_range_stations(all_stations)
    inconsistent.sort()
    print(inconsistent)



if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()