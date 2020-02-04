#!/usr/bin/env python3

import sys
import os
import time
import vcgencmd as vc
from gpiozero import OutputDevice

def main():
    fan = OutputDevice(18)
    while True:
        temp = int(vc.measure_temp())
        print(temp)
        if  temp >= 50:
            fan.on()
            print("fan.on()")
        elif temp <= 45:
            fan.off()
            print("fan.off()")
        time.sleep(1)

if __name__ == '__main__':
    main()
