from floodsystem.stationdata import *
from floodsystem.geo import *
from floodsystem.flood import *


station_list = build_station_list()
consistent_stations = []
for i in station_list:
    if i.relative_water_level() != None:
        consistent_stations.append(i)


# Test for 2B function stations_level_over_threshold
def test_stations_level_over_threshold():
    stations_over_threshold = stations_level_over_threshold(consistent_stations, 0.5)
    for i in stations_over_threshold:
        assert(i[1] >= 0.5)


# Test for 2C function stations_highest_rel_level
def test_stations_highest_rel_level():
    list = stations_highest_rel_level(station_list, 10)
    for i in range(len(list)):
        assert(i.relative_water_level > (i+1).relative_water_level)


# Test for 2G function issue_flood_warnings
def test_issue_flood_warnings():
    station_dict = issue_flood_warnings(consistent_stations)
    assert(type(station_dict) == dict)
    for i in station_dict.items():
        assert(type(i[0]) == str)
        assert(type(i[1]) == str)