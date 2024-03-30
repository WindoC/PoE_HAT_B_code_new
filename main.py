import time

import logging

from waveshare_POE_HAT_B.POE_HAT_B import POE_HAT_B

logging.basicConfig(level=logging.INFO)

def main():
    
    POE = POE_HAT_B()

    try:  
        while(1):
            POE.POE_HAT_Display(50.0,10.0)
            time.sleep(10)
            
    except KeyboardInterrupt:    
        print("ctrl + c:")
        POE.FAN_OFF()
 

if __name__== "__main__" :
    main()
