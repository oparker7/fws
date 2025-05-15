# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

#added tests:
def test_inconsistent_typical_range_stations():
    ######### test typical_range_consistent ##########
    test_1_pass = MonitoringStation(None, None, None, None, (0.1, 1.0), None, None) #a fake station with consistent typical range
    assert(test_1_pass.typical_range_consistent() == True)
    test_2_fail = MonitoringStation(None, None, None, None, None, None, None)       #a fake station with no typical range
    assert(not test_2_fail.typical_range_consistent())
    test_3_fail = MonitoringStation(None, None, None, None, (1.1, 1.0), None, None) #a fake station with inconsistent stypical range
    assert(not test_3_fail.typical_range_consistent())
    ##################################################