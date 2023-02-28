from floodsystem.geo import *
from floodsystem.datafetcher import *
from floodsystem.analysis import *
from floodsystem.flood import *
from floodsystem.station import *
from floodsystem.stationdata import *
from floodsystem.plot import *
import datetime
from matplotlib import dates
from floodsystem.analysis import datesToTime
import copy

def run(p,h,n):
    stations = build_station_list()
    update_water_levels(stations)
    highFlowStations = stations_highest_rel_level(stations, n) #gets stations with current largest relative flow
    # its not practical to find the predicted rel flow of all stations as there are 2000 and it takes to find predicted rel flow for each station
    # especially since the predicted change is not going to drastically change the relative flow, taking the past x amount should be enough to find the stations most at risk

        
    for station in highFlowStations:
        Dates, Levels = fetch_measure_levels(station.measure_id, datetime.timedelta(days=2)) # fetches the levels for the station from past 10 days

        
        
        times,shift=datesToTime(Dates[:4*h])           #times are in units of 15mins so x hours ago is 4x in the list, ill pick 12 hours ago
        poly, shift = polyfit(Dates[:4*h], Levels[:4*h], p)      # finds polynomial(usually 1 so line of best fit) for data in the past h hours
        predicted_l2=poly(times[0]+h/24)-poly(times[0])+Levels[0] #adds on change in the past h hours from line of best fit to latest level
        station.latest_level=predicted_l2   #sets current level to predicted level so stations_level_over_threshold function can be used
    
    pred_lvl_above_0=stations_level_over_threshold(highFlowStations,0)
    for i in pred_lvl_above_0:
        print(i[0].name,i[1])    # prints ordered list of stations predicted relative flows

    severe,high,moderate,low=[],[],[],[]     
    for i in pred_lvl_above_0:      #makes lists of the rivers based on where they fit, the values for severe,high,moderate,low are arbitrary and can be changed
        if i[1]>2:
            severe.append(i)
        elif i[1]>1.5:
            high.append(i)
        elif i[1]>1:
            moderate.append(i)
        else:
            low.append(i)

    print("At severe risk: ")  #prints list of rivers in their designated risk regions
    for i in severe:
        print(i[0].name)
    print("At high risk: ")
    for i in high:
        print(i[0].name)
    print("At moderate risk: ")
    for i in moderate:
        print(i[0].name)
    print("At low risk: ")
    for i in low:
        print(i[0].name)
   






        
        
        
        
        
        # predicted_l2=current_l+Levels[0]-Levels[4*h]       #adds on change in past h hours from difference between current and value from h hours ago
        # print(Dates[0],times[0],Levels[0])
        # print(predicted_l,predicted_l2)
        # print(Levels[0],Levels[2*h],Levels[4*h])
        
        # x=np.linspace(max(times),0,len(times))
        
    
        # y=poly(x)
        # plt.plot(Dates[:4*h],y)
        # plot_water_levels(station, Dates[:4*h], Levels[:4*h], show= True)
    
    
     #line of best fit for data over the past h hours from most recent time
     #finds pedicted value h hours from now using this line of best fit



def run2():
    y=[1,2,5,4,6,7,7,9]
    x=datetime(1,2,3,4,5,6,7,8)
    p_coeff=polyfit(x,y,1)
    poly=np.poly1d(p_coeff)
    a=np.linspace(min(x),max(x),100)
    b=poly(a)
    plt.plot(x,y,'.')
    plt.plot(a,b)
    plt.show


if __name__ == "__main__":
    run(1,12,15)