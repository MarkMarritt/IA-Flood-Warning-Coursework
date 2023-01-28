# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation
from floodsystem.station import inconsistent_typical_range_stations
from testdata import data1F

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

# Test method that finds stations with inconsistent typical range data
def test_typical_range_consistent ():
    
    assert MonitoringStation.typical_range_consistent(data1F[0]) == False
    assert MonitoringStation.typical_range_consistent(data1F[1]) == True
    assert MonitoringStation.typical_range_consistent(data1F[2]) == True
    assert MonitoringStation.typical_range_consistent(data1F[3]) == False
    assert MonitoringStation.typical_range_consistent(data1F[4]) == True
    assert MonitoringStation.typical_range_consistent(data1F[5]) == False

def test_inconsistent_typical_range_stations():
    testdata = inconsistent_typical_range_stations(data1F)

    assert testdata == ['churchill', 'downing', 'queens']