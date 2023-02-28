from floodsystem.plot import plot_water_level_with_fit
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level
import datetime

def run():
    stations = build_station_list()
    update_water_levels(stations)
    highFlowStations = stations_highest_rel_level(stations, 5) # same as in task 2e

    for station in highFlowStations:
        Dates, Levels = fetch_measure_levels(station.measure_id, datetime.timedelta(days = 2))
        plot_water_level_with_fit(station, Dates, Levels, 4)

if __name__ == "__main__":
    run()