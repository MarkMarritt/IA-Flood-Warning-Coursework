from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level
from floodsystem.station import MonitoringStation

def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    # For 10 stations with highest relative water level, print name and relative water level
    highest_rel_level_stations = stations_highest_rel_level(stations, 10)
    for station in highest_rel_level_stations:
        rel_level = MonitoringStation.relative_water_level(station)
        print(station.name, rel_level)

if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()
