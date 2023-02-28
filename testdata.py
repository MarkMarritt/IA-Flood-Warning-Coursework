# use this data for your tests if you want
# PLEASE CHANGE FLOW RATE AND URLS IF YOU NEED TO 
from datetime import datetime 
from floodsystem.station import MonitoringStation


place1 = MonitoringStation( 
"https//thishyperlinkismadeupsodontuse.com",
"https//thishyperlinkismadeupsodontuse1.com",
"churchill",
(52.213066207479, 0.10075146057338859),
(1, 0),
("amazon"),
("London")
)
place1.latest_level = 0.56
place2 = MonitoringStation( 
"https//thishyperlinkismadeupsodontuse.com",
"https//thishyperlinkismadeupsodontuse1.com",
"trinity",
(52.206646, 0.113906),
(0, 4),
("nile"),
("Paris")
)
place2.latest_level = None
place3 = MonitoringStation( 
"https//thishyperlinkismadeupsodontuse.com",
"https//thishyperlinkismadeupsodontuse1.com",
"Homerton",
(52.185496, 0.135106),
(1, 1.5),
("Thames"),
("Berlin")
)
place3.latest_level = 0.03
place4 = MonitoringStation( 
"https//thishyperlinkismadeupsodontuse.com",
"https//thishyperlinkismadeupsodontuse1.com",
"downing",
(52.201124, 0.124735),
(3.0, 1.8),
("danube"),
("Rome")
)
place4.latest_level = 2.99
place5 = MonitoringStation( 
"https//thishyperlinkismadeupsodontuse.com",
"https//thishyperlinkismadeupsodontuse1.com",
"oxford",
(51.751978, -1.257894),
(0.1, 0.2),
("Thames"),
("New York")
)
place5.latest_level = 1.1
place6 = MonitoringStation( 
"https//thishyperlinkismadeupsodontuse.com",
"https//thishyperlinkismadeupsodontuse1.com",
"queens",
(50.752988, 4.259894),
(0.17, 0.02),
("Cam"),
("London")
)
place7 = MonitoringStation( 
"https//thishyperlinkismadeupsodontuse.com",
"https//thishyperlinkismadeupsodontuse1.com",
"churchill",
(52.213066207479, 0.10075146057338859),
(0, 1),
("Amazon"),
("London")
)
place7.latest_level = 1.12
place8 = MonitoringStation( 
"https//thishyperlinkismadeupsodontuse.com",
"https//thishyperlinkismadeupsodontuse1.com",
"trinity",
(52.206646, 0.113906),
(0, 4),
("Nile"),
("Paris")
)
place8.latest_level = 4.0
place9 = MonitoringStation( 
"https//thishyperlinkismadeupsodontuse.com",
"https//thishyperlinkismadeupsodontuse1.com",
"Homerton",
(52.185496, 0.135106),
(1, 1.5),
("Thames"),
("Berlin")
)
place10 = MonitoringStation( 
"https//thishyperlinkismadeupsodontuse.com",
"https//thishyperlinkismadeupsodontuse1.com",
"downing",
(52.201124, 0.124735),
(0.3, 1.8),
("Danube"),
("Rome")
)
place11 = MonitoringStation( 
"https//thishyperlinkismadeupsodontuse.com",
"https//thishyperlinkismadeupsodontuse1.com",
"oxford",
(51.751978, -1.257894),
(0.1, 0.2),
("Mississippi"),
("New York")
)
place12= MonitoringStation(
"https//thishyperlinkismadeupsodontuse.com",
"https//thishyperlinkismadeupsodontuse1.com",
"Peterborough",
(52.56488223412364, -0.2870650916542047),
(0.5,2.1),
("Hand")
,(None)
)
place13= MonitoringStation(
"https//thishyperlinkismadeupsodontuse.com",
"https//thishyperlinkismadeupsodontuse1.com",
"Peterborough",
(52.56488223412364, -0.2870650916542047),
(0.5,2.1),
("Hand")
,(None)
)


data = [place1,place2,place3,place4,place5]
dataDE=[place7,place8,place9,place10,place11,place12,place13,place11,place10,place10]
data1F = [place1,place2,place3,place4,place5,place6]
data2BC = [place1, place2, place3, place4, place5, place7, place8]

# data for test_plot
waterLevel10 = [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]
badWaterLevel10 = [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,"ten"]
dates10 = [datetime(2017, 1, 1), datetime(2017, 1, 2), datetime(2017, 1, 3),
     datetime(2017, 1, 4), datetime(2017, 1, 5), datetime(2017, 1, 6),
     datetime(2017, 1, 7), datetime(2017, 1, 8), datetime(2017, 1, 9),
     datetime(2017, 1, 10)]
dates11 = [datetime(2016, 12, 30), datetime(2016, 12, 31), datetime(2017, 1, 1),
     datetime(2017, 1, 2), datetime(2017, 1, 3), datetime(2017, 1, 4),
     datetime(2017, 1, 5), datetime(2017, 1, 6), datetime(2017, 1, 7),
     datetime(2017, 1, 8), datetime(2017, 1, 9)]
baddates10 = [datetime(2016, 12, 30), datetime(2016, 12, 31), datetime(2017, 1, 1),
     datetime(2017, 1, 2), (2017, 1, 3), datetime(2017, 1, 4),
     datetime(2017, 1, 5), datetime(2017, 1, 6), datetime(2017, 1, 7),
     datetime(2017, 1, 8)]

# data for test_analysis
yconstant = [1,1,1,1,1,1,1,1,1,1]
ylinear = [0,1,2,3,4,5,6,7,8,9]
yquadratic = [0,1,4,9,16,25,36,49,64,81]
ybad = [0,1,2]