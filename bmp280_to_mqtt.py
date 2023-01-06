#!/usr/bin/python3

import adafruit_bmp280
import board
import paho.mqtt.client as mqtt
import time

# config:
broker='127.0.0.1'
port=1883
topic_prefix="h10/floor1/living_room/bmp280"
clientid='python-mqtt-bmp280'

# BMP280 sensor
bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(board.I2C(), address=0x76)

# MQTT client
client=mqtt.Client(clientid)
client.will_set(f"{topic_prefix}/status", "offline", qos=2, retain=True)
client.connect(broker, port)
client.loop_start()
client.publish(f"{topic_prefix}/status", "online", qos=2, retain=True)

while True:
        client.publish(f"{topic_prefix}/temperature", "{:.2f}".format(bmp280.temperature), qos=0, retain=False)
        client.publish(f"{topic_prefix}/pressure", "{:.2f}".format(bmp280.pressure), qos=0, retain=False)
        time.sleep(60);

client.disconnect()
client.loop_stop()
