# marks property don't change or ill fight you

from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

def run():
    stations = build_station_list()
    stationNames = stations_within_radius(stations,  (52.2053, 0.1218), 10)
    stationNames.sort()
    print(stationNames)

if __name__ == "__main__":
    run()