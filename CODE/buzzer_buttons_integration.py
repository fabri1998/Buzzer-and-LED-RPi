#!/usr/bin/python

import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time
import json

topic_read="obj/tuc/button"
button_on = 14
button_off = 15

client = mqtt.Client()
client.connect("localhost")

GPIO.setmode(GPIO.BCM)

last_pressed_button = 0

def button_callback(gpio):
    global last_pressed_button
    now=time.time()


    # Ignore repeated press on the same button
    if last_pressed_button == gpio:
        return
    
    if gpio == button_on:
        client.publish(topic_read, '{"value":1, "timestamp":' + str(now) + '}')
        print("Button ON pushed! ")
    elif gpio == button_off:
        client.publish(topic_read, '{"value":0, "timestamp":' + str(now) + '}')
        print("Button OFF pushed! ")
        
    last_pressed_button = gpio



GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(14,GPIO.RISING,callback=button_callback)

GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(15,GPIO.RISING,callback=button_callback)

client.loop_forever()
