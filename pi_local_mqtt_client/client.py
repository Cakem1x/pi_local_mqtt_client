#!/usr/bin/python3

import adafruit_bmp280
import board
import paho.mqtt.client as mqtt
import time

def get_cpu_temp(cpu_temp_filename="/sys/class/thermal/thermal_zone0/temp"):
        with open(cpu_temp_filename) as cpu_temp_file:
                cpu_temp_celsius = int(cpu_temp_file.read()) / 1000.0
                return cpu_temp_celsius

# config:
broker = "127.0.0.1"
port = 1883
client_id = "mqtt_on_pi"
topic_prefix = "h10/floor1/living_room"
status_topic = f"{topic_prefix}/{client_id}/status"
bmp280_topic = f"{topic_prefix}/bmp280"
pi_topic = f"{topic_prefix}/pi"

# BMP280 sensor
bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(board.I2C(), address=0x76)

# MQTT client
client=mqtt.Client(client_id)
client.will_set(status_topic, "offline", qos=2, retain=True)
client.connect(broker, port)
client.loop_start()
client.publish(status_topic, "online", qos=2, retain=True)

while True:
        client.publish(f"{bmp280_topic}/temperature", "{:.2f}".format(bmp280.temperature), qos=0, retain=False)
        client.publish(f"{bmp280_topic}/pressure", "{:.2f}".format(bmp280.pressure), qos=0, retain=False)
        client.publish(f"{pi_topic}/cpu_temperature", "{:.2f}".format(get_cpu_temp()), qos=0, retain=False)
        time.sleep(20);

client.disconnect()
client.loop_stop()
