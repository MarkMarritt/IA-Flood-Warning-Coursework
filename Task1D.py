import numpy as np
from floodsystem.utils import sorted_by_key  # noqa
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list
from floodsystem.geo import *

def run():
    stations=build_station_list()
    rivers=rivers_with_station(stations)
    first10=rivers[0:10]
    print("{} stations. First 10 - {}".format(len(rivers),first10))
    stationdict=stations_by_river(stations)
    print(stationdict["River Aire"])
    print(stationdict["River Cam"])
    print(stationdict["River Thames"])

if __name__=="__main__":
    run()
