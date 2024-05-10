#!/usr/bin/python

import RPi.GPIO as GPIO
import time

buzzer = 17

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(led,GPIO.OUT)

# Turn on the BUZZER
GPIO.output(led,1)

#Wait 0.5s
time.sleep(0.5)

#Turn off the BUZZER
GPIO.output(led,0)
