from floodsystem.stationdata import build_station_list
from floodsystem.utils import sorted_by_key
from floodsystem.geo import rivers_by_station_number

def run():
    stations=build_station_list()
    print(rivers_by_station_number(stations,9))

if __name__=="__main__":
    run()

