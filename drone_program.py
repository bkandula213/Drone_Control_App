from dronekit import connect, VehicleMode, LocationGlobalRelative,APIException
import time
import socket
#import exceptions
import math
# Connect to the vehicle
class Connect_vehicle:
    def __init__(self):
        self.connection_string = 'udp:127.0.0.1:14550' 
        self.vehicle = connect(self.connection_string, wait_ready=False)
        self.throttle=self.vehicle.channels['3']
        self.pitch=self.vehicle.channels['2']
        self.rudder=self.vehicle.channels['4']
        self.aileron=self.vehicle.channels['1']
    
    def overrideChannels(self,ch,val):
        for i in range(0,len(ch)):
            self.vehicle.channels.overrides[ch[i]]=val[i]

    def armDrone(self):
        print(self.vehicle)
        self.vehicle.mode = VehicleMode("MANUAL")
        self.vehicle.armed = True
        print(self.vehicle.channels)

    def changeThrottle(self,tVal):
        tVal_updated=self.throttle+tVal
        if tVal_updated>1000 and tVal_updated<2000:
            self.overrideChannels(['3'],[tVal_updated])
            self.throttle=tVal_updated
        print(self.vehicle.channels)
    
    def changeElevation(self,pVal):
        if pVal>1000 and pVal<2000:
            self.overrideChannels(['3','2','1','4'],[self.throttle,pVal,1500,1500])
            self.pitch=pVal
        print(self.vehicle.channels)

    def changeRudder(self,rVal):
        if rVal>1000 and rVal<2000:
            self.overrideChannels(['3','2','1','4'],[self.throttle,1500,self.aileron,rVal])
            self.rudder=rVal
        print(self.vehicle.channels)

    def changeAileron(self,aVal):
        if aVal>1000 and aVal<2000:
            self.overrideChannels(['3','2','1','4'],[self.throttle,1500,aVal,self.rudder])
            self.aileron=aVal
        print(self.vehicle.channels)
            

        

