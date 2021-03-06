# ##############################################################################
#						*** NERVOBOARD RELAY  ***
# ##############################################################################

# ##############################################################################
# 							PERSONNAL PARAMETERS
# ##############################################################################  
  
#read current service part config based on file name
ThisServicePart=inspect.getfile(inspect.currentframe()).replace('.py','')

CheckFileExist(ThisServicePart)
ThisServicePartConfig = ConfigParser.ConfigParser()
ThisServicePartConfig.read(ThisServicePart+'.config')
isNervoboardRelayActivated=0

isNervoboardRelayActivated=ThisServicePartConfig.getboolean('MAIN', 'isNervoboardRelayActivated') 


PinLeftNervoPower1=0
PinLeftNervoPower2=0
PinLeftNervoPower3=0
PinRightNervoPower1=0
PinRightNervoPower2=0
PinRightNervoPower3=0

try:
	PinLeftNervoPower1=ThisServicePartConfig.getint('MAIN', 'PinLeftNervoPower1') 
	PinLeftNervoPower2=ThisServicePartConfig.getint('MAIN', 'PinLeftNervoPower2') 
	PinLeftNervoPower3=ThisServicePartConfig.getint('MAIN', 'PinLeftNervoPower3') 
	PinRightNervoPower1=ThisServicePartConfig.getint('MAIN', 'PinRightNervoPower1') 
	PinRightNervoPower2=ThisServicePartConfig.getint('MAIN', 'PinRightNervoPower2') 
	PinRightNervoPower3=ThisServicePartConfig.getint('MAIN', 'PinRightNervoPower3') 
except:
	pass
  
# ##############################################################################
# 								SERVICE START
# ##############################################################################
def relayAction(ard,pin,value):
	ard.pinMode(pin, Arduino.OUTPUT)
	ard.digitalWrite(pin,value)

if isNervoboardRelayActivated==1:
	try:
		NervoboardRelayControlerArduino=eval(ThisServicePartConfig.get('MAIN', 'NervoboardRelayControlerArduino'))
		talkEvent(lang_startingNervoPower)
		if PinLeftNervoPower1>0:
			relayAction(NervoboardRelayControlerArduino,PinLeftNervoPower1,0)
		if PinLeftNervoPower2>0:
			relayAction(NervoboardRelayControlerArduino,PinLeftNervoPower2,0)
		if PinLeftNervoPower3>0:
			relayAction(NervoboardRelayControlerArduino,PinLeftNervoPower3,0)
		if PinRightNervoPower1>0:
			relayAction(NervoboardRelayControlerArduino,PinRightNervoPower1,0)
		if PinRightNervoPower2>0:
			relayAction(NervoboardRelayControlerArduino,PinRightNervoPower2,0)
		if PinRightNervoPower3>0:
			relayAction(NervoboardRelayControlerArduino,PinRightNervoPower3,0)
	except:
		errorSpokenFunc('BAdrduinoChoosen','nervo board relay')
		isNervoboardRelayActivated=0
		pass