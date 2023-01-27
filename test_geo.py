"""unit test for geo submodule"""

from floodsystem.geo import *
from testdata import data, dataDE
import pytest
# tests for task 1B
def test_create_havFormula():
    p1 = (52.212835, 0.120872)
    p2 = (50.131125, -5.255319)
    dis = havFormula(p1,p2)
    assert dis == 440.36063514421807
    with pytest.raises(ValueError):
        havFormula(("a","b"), ("c","d"))
        pass


def test_create_stationsbydistance():
    list = stations_by_distance(stations,p)
    if len(list) > 1:
        assert list[0][1] < list[-1][1]
        for i in range(len(list) - 1):
            assert list[i][1] < list[i+1][1] or list[i][1] == list[i+1][1]
    else:
        pass
    
    assert list[0] == ('downing', 0.505594484133292)
    assert list[-1] == ('oxford', 107.09794497503843)


stations = data
p = (52.2053, 0.1218)

# tests for task 1C
badData = data
badData.append("not a station")

def test_create_stationsRadius():
    assert stations_within_radius(data, p, 1000) == ['downing', 'trinity', 'churchill', 'Homerton', 'oxford']
    assert stations_within_radius(data, p, 100) == ['downing', 'trinity', 'churchill', 'Homerton']
    assert stations_within_radius(data, p, 1) == ['downing', 'trinity']
    assert stations_within_radius(data, p, 0) == []
    assert stations_within_radius(badData, p, 100) == ['downing', 'trinity', 'churchill', 'Homerton']

#tests for task 1D

def test_rivers_with_station():
     assert rivers_with_station(dataDE)==['Amazon', 'Danube', 'Mississippi', 'Nile', 'Thames']
def test_stations_by_river():
    assert stations_by_river(dataDE)=={'Amazon': ['London'], 'Nile': ['Paris'], 'Thames': ['Berlin'], 'Danube': ['Rome','Rome','Rome'], 'Mississippi': ['New York','New York']}


#tests for task 1E
#print(rivers_by_station_number(dataDE,6))
def test_rivers_by_station_number():
    assert rivers_by_station_number(dataDE,0)==[]
    assert rivers_by_station_number(dataDE,1)==[('Danube', 3)]
    assert rivers_by_station_number(dataDE,2)==[('Danube', 3), ('Mississippi', 2)]
    assert rivers_by_station_number(dataDE,3)==[('Danube', 3), ('Mississippi', 2), ('Amazon', 1), ('Nile', 1), ('Thames', 1)]
    assert rivers_by_station_number(dataDE,4)==[('Danube', 3), ('Mississippi', 2), ('Amazon', 1), ('Nile', 1), ('Thames', 1)]
    assert rivers_by_station_number(dataDE,5)==[('Danube', 3), ('Mississippi', 2), ('Amazon', 1), ('Nile', 1), ('Thames', 1)]
    assert rivers_by_station_number(dataDE,6)==[('Danube', 3), ('Mississippi', 2), ('Amazon', 1), ('Nile', 1), ('Thames', 1)]

