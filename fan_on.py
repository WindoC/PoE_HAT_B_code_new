import time

import logging

from waveshare_POE_HAT_B import FAN

logging.basicConfig(level=logging.INFO)

def main():
    FAN.FAN().FAN_ON()

if __name__== "__main__" :
    main()
