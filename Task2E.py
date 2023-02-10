from floodsystem.plot import plot_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level
import datetime


def run():
    stations = build_station_list()
    highFlowStations = stations_highest_rel_level(stations, 5) # builds list of 5 highest level stations
        
    for station in highFlowStations:
        Dates, Levels = fetch_measure_levels(station.measure_id, datetime.timedelta(days = 10)) # fetches the levels for the station from past 10 days
        plot_water_levels(station, Dates, Levels)

if __name__ == "__main__":
    run()