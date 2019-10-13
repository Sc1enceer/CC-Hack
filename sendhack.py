
import time 
ts= time.time()
#value=ToF
#value=Prox
#value=Lux
#value=SpecRed
#value=SpecGreen
#value=SpecBlue
#value=SpecYellow
#value=SpecWhite
#value=SpecBlack
#type=temperature
#type=humidity
#unit=Lux
#unit=degree

SenInput=[]

def appendToSenInput (type, value):
	timestamp = str("%.20f" % time.time()).replace(".", "")
	SenInput.append((type, value, timestamp))

def send(SenInput):
	#the URL and token
	for type,value, timestamp in SenInput:
		data+= type +", type=" +type+ " "+unit+"="+str(value)+" "+timestamp +"\n"
		if SenInput==SenInput[-1]:
			data+= type +", type=" +type+ " "+unit+"="+str(value)+" "+timestamp
		
		
			
		
		