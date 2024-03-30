import time

import logging

from waveshare_POE_HAT_B import FAN
from waveshare_POE_HAT_B import LED

logging.basicConfig(level=logging.INFO)

# will turn on FAN and off the LED

def main():
    FAN.FAN().FAN_ON()
    LED.LED().ClearBlack()

if __name__== "__main__" :
    main()
