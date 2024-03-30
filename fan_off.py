import time

import logging

from waveshare_POE_HAT_B.FAN import FAN

logging.basicConfig(level=logging.INFO)

def main():
    FAN().FAN_OFF()

if __name__== "__main__" :
    main()
