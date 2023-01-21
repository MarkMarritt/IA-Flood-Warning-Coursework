"""unit test for geo submodule"""

from floodsystem.geo import havFormula, stations_by_distance
from floodsystem.stationdata import build_station_list
import pytest

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


stations = build_station_list()
p = (52.2053, 0.1218)
