from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

# Output the list of station names with inconsistent data 
def run():
    stations = build_station_list()
    station_Names = inconsistent_typical_range_stations(stations)
    station_Names.sort()
    print(station_Names)

if __name__ == "__main__":
    run()