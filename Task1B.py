# marks property don't change or ill fight you
# stations by distance module
from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

def run():
    stations = build_station_list()
    point = (52.2053, 0.1218)
    stationInfo = stations_by_distance(stations, point)

    closeTen = stationInfo[:10]
    farTen = stationInfo[-10:]
    
    def addTown(list, stations): # makes a new tuple with the town in the middle 
        newList = []
        for i in list:
            stationName = i[0]
            stationDist = i[1]
            for station in stations:
                if station.name == stationName:
                    newitem = (stationName, station.town, stationDist)
                    newList.append(newitem)
        return newList

    closeTen = addTown(closeTen, stations)
    farTen = addTown(farTen, stations)
    
    print(closeTen)
    print(farTen)

if __name__ == "__main__":
    run()