from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level
from testdata import data2BC

def test_stations_level_over_threshold():
    testdata = stations_level_over_threshold(data2BC, 0.8)
    testlist = []
    for tupple in testdata:
        for station in data2BC:
            if tupple[0] == station:
                outputdata = (station.name, tupple[1])
                testlist.append(outputdata)
    assert testlist == [('oxford', 10.0), ('churchill', 1.12), ('trinity', 1.0)]
    

def test_stations_highest_rel_level():
    testdata = stations_highest_rel_level(data2BC, 3)
    testlist = []
    for station in testdata:
        rel_level = MonitoringStation.relative_water_level(station)
        testlist.append((station.name, rel_level))
    assert testlist == [('oxford', 10.0), ('churchill', 1.12), ('trinity', 1.0)]
