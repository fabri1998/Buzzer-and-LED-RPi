#!/usr/bin/python

import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time
import json

topic_write = "set/test/buzzer1"
buzzer = 17

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(buzzer, GPIO.OUT)

client = mqtt.Client()
client.connect("localhost")

def on_message(client, userdata, message):
    payload = json.loads(message.payload)
    if message.topic == topic_write:
        if payload["value"] == 0:
            print("Turning buzzer off")
            GPIO.output(buzzer, 0)
        else:
            print("Turning buzzer on")
            GPIO.output(buzzer, 1)
    else:
        print("Ignoring " + message.topic)

print("Subscribing to topic " + topic_write)
client.subscribe(topic_write)
client.on_message = on_message

client.loop_forever()
