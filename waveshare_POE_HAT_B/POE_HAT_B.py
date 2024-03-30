import socket

from .LED import LED
from .FAN import FAN
import os

class POE_HAT_B:

    def __init__(self):
        self.fan = FAN()
        self.led = LED()
        self.hostname = socket.gethostname()
        self.fan.FAN_ON()
        self.FAN_MODE = True
        self.temp = None
        
    def GET_IP(self):
        s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.connect(('8.8.8.8',80))
        ip=s.getsockname()[0]
        s.close()
        return ip
        
    def GET_Temp(self):
        with open('/sys/class/thermal/thermal_zone0/temp', 'rt') as f:
            temp = (int)(f.read() ) / 1000.0
        return temp
    
    def POE_HAT_Display(self, FAN_TEMP, safevalue = 1.0):
        # var to use to diaplay LED or not
        changed = False

        # get info
        temp = self.GET_Temp()
        if temp != self.temp:
            self.temp = temp
            changed = True

        # set fan
        if(temp>=(FAN_TEMP+safevalue)):
            if(self.FAN_MODE==False):
                self.FAN_MODE=True
                changed = True
                self.fan.FAN_ON()
                print("Debug: FAN On")
                os.system("logger POE_HAT_B fan on")

        elif(temp<(FAN_TEMP-safevalue)):
            if(self.FAN_MODE==True):
                self.FAN_MODE=False
                changed = True
                self.fan.FAN_OFF()
                print("Debug: FAN Off")
                os.system("logger POE_HAT_B fan off")
        
        # led display
        if changed:
            self.led.display(self.hostname,temp,self.FAN_MODE)

    # to support old code
    def FAN_OFF(self):
        self.fan.FAN_OFF()
