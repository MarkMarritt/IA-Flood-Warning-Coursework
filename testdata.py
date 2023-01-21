# use this data for your tests if you want
# PLEASE CHANGE FLOW RATE AND URLS IF YOU NEED TO 

from floodsystem.station import MonitoringStation


place1 = MonitoringStation( 
"https//thishyperlinkismadeupsodontuse.com",
"https//thishyperlinkismadeupsodontuse1.com",
"churchill",
(52.213066207479, 0.10075146057338859),
(0, 1),
("amazon"),
("London")
)
place2 = MonitoringStation( 
"https//thishyperlinkismadeupsodontuse.com",
"https//thishyperlinkismadeupsodontuse1.com",
"trinity",
(52.206646, 0.113906),
(0, 4),
("nile"),
("Paris")
)
place3 = MonitoringStation( 
"https//thishyperlinkismadeupsodontuse.com",
"https//thishyperlinkismadeupsodontuse1.com",
"Homerton",
(52.185496, 0.135106),
(1, 1.5),
("Thames"),
("Berlin")
)
place4 = MonitoringStation( 
"https//thishyperlinkismadeupsodontuse.com",
"https//thishyperlinkismadeupsodontuse1.com",
"downing",
(52.201124, 0.124735),
(0.3, 1.8),
("danube"),
("Rome")
)
place5 = MonitoringStation( 
"https//thishyperlinkismadeupsodontuse.com",
"https//thishyperlinkismadeupsodontuse1.com",
"oxford",
(51.751978, -1.257894),
(0.1, 0.2),
("Thames"),
("New York")
)

data = [place1,place2,place3,place4,place5]
