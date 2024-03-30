import time

import logging
import socket

from waveshare_POE_HAT_B import LED

logging.basicConfig(level=logging.INFO)

def main():
    LED.LED().string(socket.gethostname())

if __name__== "__main__" :
    main()
