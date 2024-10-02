import time
import logging
import os

from waveshare_POE_HAT_B.POE_HAT_B import POE_HAT_B

logging.basicConfig(level=logging.INFO)

def getenv_float(env_name:str,default_if_null:float) -> float:
    temp = os.getenv(env_name)
    try:
        return float(temp)
    except:
        return float(default_if_null)
        
POE_HAT_TEMPERATURE = getenv_float('POE_HAT_TEMPERATURE', 50.0)
POE_HAT_DELTA = getenv_float('POE_HAT_DELTA', 10.0)
print(f"Debug: POE_HAT_TEMPERATURE = {POE_HAT_TEMPERATURE} , POE_HAT_DELTA = {POE_HAT_DELTA}")

def main():
    
    POE = POE_HAT_B()

    try:  
        while(1):
            POE.POE_HAT_Display(POE_HAT_TEMPERATURE,POE_HAT_DELTA)
            time.sleep(10)
            
    except KeyboardInterrupt:    
        print("ctrl + c:")
        POE.FAN_OFF()
 

if __name__== "__main__" :
    main()
