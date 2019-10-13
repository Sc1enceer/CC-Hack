from ltr559 import LTR559
from as7262 import AS7262
import requests
import time

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
            data+= "spectrum" +",type=spectrum " +type+ "="+str(value)+" "+timestamp
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
#setting up the spectral sensor
as7262 = AS7262()

as7262.set_gain(64)
as7262.set_integration_time(17.857)
as7262.set_measurement_mode(2)
as7262.set_illumination_led(0)

try:
    while True:
        lux = ltr559.get_lux();
        if(lux < 150):
            as7262.set_illumination_led(1)
            values = as7262.get_calibrated_values()
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