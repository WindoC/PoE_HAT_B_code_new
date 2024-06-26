import socket

from .LED import LED
from .FAN import FAN
import os

class POE_HAT_B:

    def __init__(self):
        self.fan = FAN()
        self.led = LED()
        self.hostname = socket.gethostname()
        self.temp = None
        # default turn fan on
        self.FAN_MODE = True
        self.FAN_ON()
        
    def GET_Temp(self):
        with open('/sys/class/thermal/thermal_zone0/temp', 'rt') as f:
            temp = (int)(f.read() ) / 1000.0
        return temp
    
    def POE_HAT_Display(self, FAN_TEMP, safevalue = 1.0):
        # var to use to diaplay LED or not
        changed = False

        # get info
        temp = self.GET_Temp()
        if int(temp) != self.temp:
            self.temp = int(temp)
            changed = True

        # set fan
        if temp>=(FAN_TEMP+safevalue):
            if self.FAN_MODE==False:
                changed = True
                self.FAN_MODE=True
                self.FAN_ON()

        elif temp<(FAN_TEMP-safevalue):
            if self.FAN_MODE==True:
                changed = True
                self.FAN_MODE=False
                self.FAN_OFF()
        
        # led display
        if changed:
            self.led.display(self.hostname,temp,self.FAN_MODE)
            print(f"Debug: display H:{self.hostname} Temp:{int(temp)} FAN:{'ON' if self.FAN_MODE else 'OFF'}")

    # to support old code
    def FAN_ON(self):
        self.fan.FAN_ON()
        print("Debug: FAN On")
        os.system("logger POE_HAT_B fan on")

    def FAN_OFF(self):
        self.fan.FAN_OFF()
        print("Debug: FAN Off")
        os.system("logger POE_HAT_B fan off")
