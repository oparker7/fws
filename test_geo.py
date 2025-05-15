from floodsystem.geo import *
from floodsystem.stationdata import build_station_list as bsl
from floodsystem.geo import haversine as h

def test_stations_by_distance():
    stations_list = [s, s2, s3]  # creating input argument of dummy station list.
    q = (0.0, 0.0)
    stations_distanced = stations_by_distance(stations_list, q)
    assert(type(stations_distanced) == list)
    assert(len(stations_distanced) > 0)
    assert(stations_by_distance(stations_list, q) == [(s, h(s.coord,q)), (s2, h(s2.coord, q)), (s3, h(s3.coord, q))])  # ensuring that the list contains the correct elements in the correct order


def test_haversine():
    p = (52.2053, 0.1218)  # Cambridge city centre coordinate
    a = (52.212835, 0.120872)  # Jesus lock coordinate
    b = (52.197227, 0.087527) # Bin brook coordinate
    assert(haversine(a, p) == 0.8402364350834112)
    assert(haversine(b, p) == 2.5022740869515525) 
    # ^^above^^ ensuring that the haversine function calculates correct distances confirmed by cued 



def test_stations_within_radius():
    stations_list = [s, s2, s3]
    q = (0.0, 0.0)
    assert(stations_within_radius(stations_list, q, 400) == [s, s2])
























from floodsystem.station import MonitoringStation
from floodsystem.geo import *
 # Create a station
s_id = "test-s-id"
m_id = "test-m-id"
label = "some station"
coord = (1.0, 1.0)
trange = (-2.3, 3.4445)
river = "River X"
town = "My Town"
s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
# Create a station
s_id = "test-s-id2"
m_id = "test-m-id2"
label = "some station2"
coord = (2.0, 2.0)
trange = (-2.3, 3.4445)
river = "River X"
town = "My Town2"
s2 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
# Create a station
s_id = "test-s-id3"
m_id = "test-m-id3"
label = "some station3"
coord = (3.0, 3.0)
trange = (-2.3, 3.4445)
river = "River Y"
town = "My Town3"
s3 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

s4 = MonitoringStation(None, None, None, None, None, "River X", None)
s5 = MonitoringStation(None, None, None, None, None, "River Y", None)
s6 = MonitoringStation(None, None, None, None, None, "River Y", None)
s7 = MonitoringStation(None, None, None, None, None, "River Z", None)
def test_rivers_with_station():
    assert({"River X", "River Y"}==rivers_with_station([s,s2,s3]))

def test_stations_by_river():
    test_dict = {}
    test_dict["River X"] = [s, s2]
    test_dict["River Y"] = [s3]
    assert(stations_by_river([s,s2,s3]) == test_dict)

def test_rivers_by_station_number():
    assert(rivers_by_station_number([s, s2, s3],1) == [("River X", 2)]) #normal test
    assert(rivers_by_station_number([s, s2, s3, s5, s7],1) == [("River X", 2),("River Y", 2)] or [("River Y", 2),("River X", 2)]) #two rivers have two stations -- does utils sorted_by_key always return same order for items with same key value?
    assert(rivers_by_station_number([s5, s7, s2, s, s3],2) == [("River X", 2),("River Y", 2)] or [("River Y", 2),("River X", 2)])#as above but order changed
    assert(rivers_by_station_number([s, s2, s6, s3, s5, s7],3) == [("River Y", 3),("River X", 2),("River Z", 1) ])
