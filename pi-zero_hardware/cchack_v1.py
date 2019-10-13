from ltr559 import LTR559
from as7262 import AS7262
import requests
import time
import os
import sys
import signal
import VL53L1X

#setting up database communication
ts= time.time()

SenInput=[]

def appendtosend(type, value):
    timestamp = str("%.9f" % time.time()).replace(".", "")
    SenInput.append((type, value, timestamp))
    
def getData():
    data=""
    for type, value, timestamp in SenInput:
        data+= type +",type=" +type+ " value="+str(value)+" "+timestamp +"\n"		    
        if SenInput==SenInput[-1]:
            data+= type +",type=" +type+ " value="+str(value)+" "+timestamp
    return data

def getDataForSpectrum():
    data=""
    for type, value, timestamp in SenInput:
        data+= "spectrum" +",type=spectrum " +type+"="+str(value)+" "+timestamp +"\n"		    
        if SenInput==SenInput[-1]:
            data+= "spectrum" +",type=spectrum " +type+"="+str(value)+" "+timestamp
    return data
	
def send():
    API_ENDPOINT=url="http://us-west-2-1.aws.cloud2.influxdata.com/api/v2/write"
    request = requests.post(API_ENDPOINT,params={"org":"cchack","bucket":"Database"},
    headers={"Authorization":"Token Jj1BNzx75RudUoWlu8zuK8GNg5JoTpS5m-u0E-HeMKWvOnUzNa_0ZvO0JMxgSaYNqEQ1LJEZnVL1a1E-Rzg85w=="}, data = getData())
    print(request.text)

	
def sendSpectrum():
    API_ENDPOINT=url="http://us-west-2-1.aws.cloud2.influxdata.com/api/v2/write"
    request = requests.post(API_ENDPOINT,params={"org":"cchack","bucket":"Database"},
    headers={"Authorization":"Token Jj1BNzx75RudUoWlu8zuK8GNg5JoTpS5m-u0E-HeMKWvOnUzNa_0ZvO0JMxgSaYNqEQ1LJEZnVL1a1E-Rzg85w=="}, data = getDataForSpectrum())
    print(request.text)

#setting up the light sensor
ltr559 = LTR559()
#setting up time of flight sensor
tof = VL53L1X.VL53L1X(i2c_bus = 1,i2c_address=0x29)
tof.open()
tof.start_ranging(2)
#setting up the spectral sensor
as7262 = AS7262()
as7262.set_gain(64)
as7262.set_integration_time(17.857)
as7262.set_measurement_mode(2)
as7262.set_illumination_led(0)
#listing out useful algorithm
#Modified Chlorophyll Absorption Ratio Index => indicates the relative abundance of chlorophyll 
def MCARI(red,orange,green):
	result = ((red - orange) - 0.2*(red - green))*(red/orange)
	return result
#Carotenoid Reflectance Index 1 (CRI1) => function in light absorption processes in plants. Weakening vegetation contains higher conc. of carotenoids,measure of stressed vegetation. High CRI1 mean greater conc. than chlorophyll
def CRI1 (blue,green):
	result = ((1/blue)-(1/green))
	return result
#Photochemical Reflectance Index (PRI) => reflectance measurement that is sensitive to changes in caretenoid pigments in live foliage, indicator of photosynthetic light use efficiency, or rate of CO2 uptake, study vegetaion productivity abd stress which includes vegetation health
def PRI (orange,green):
	result = (green - orange)/(orange + green)
	return result


try:
    while True:
        lux = ltr559.get_lux();
        distance = tof.get_distance()/10
        appendtosend("ToF",distance)
        if(lux < 100):
            as7262.set_illumination_led(1)
            values = as7262.get_calibrated_values()
            average = (values.red + values.orange + values.yellow + values.green + values.blue + values.violet)/6
            appendtosend("MCARI",MCARI(values.red,values.orange,values.green))
            appendtosend("CRI1",CRI1(values.blue,values.green))
            appendtosend("PRI",PRI(values.orange,values.green))
            appendtosend("AverageSpectral",average)
            appendtosend("Lux",lux)
            appendtosend("Red",values.red)
            appendtosend("Orange",values.orange)
            appendtosend("Yellow",values.yellow)
            appendtosend("Green",values.green)
            appendtosend("Blue",values.blue)
            appendtosend("Violet",values.violet)
            sendSpectrum()
            send()
            
            
            

        else:
            as7262.set_illumination_led(0)
            values = as7262.get_calibrated_values()
            average = (values.red + values.orange + values.yellow + values.green + values.blue + values.violet)/6
            appendtosend("MCARI",MCARI(values.red,values.orange,values.green))
            appendtosend("CRI1",CRI1(values.blue,values.green))
            appendtosend("PRI",PRI(values.orange,values.green))            
            appendtosend("AverageSpectral",average)
            appendtosend("Lux",lux)
            appendtosend("Red",values.red)
            appendtosend("Orange",values.orange)
            appendtosend("Yellow",values.yellow)
            appendtosend("Green",values.green)
            appendtosend("Blue",values.blue)
            appendtosend("Violet",values.violet)
            sendSpectrum()
            send()


            


        
except KeyboardInterrupt:
    as7262.set_measurement_mode(3)
    as7262.set_illumination_led(0)
    tof.stop_ranging()
