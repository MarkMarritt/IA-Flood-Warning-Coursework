from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold


def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    # Print all names and relative water levels of stations with relative water 
    # levels greater than 0.8
    level_over_threshold_names = stations_level_over_threshold(stations, 0.8)
    for station in level_over_threshold_names:
        print(station[0], station[1])

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()
