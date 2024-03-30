import time

import logging

from waveshare_POE_HAT_B.LED import LED

logging.basicConfig(level=logging.INFO)

# will turn on FAN and off the LED

def main():
    LED().ClearBlack()

if __name__== "__main__" :
    main()
