import time
import paho.mqtt.client as mqtt
import json

import serial
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

state = 0

port = "/dev/rfcomm0"
ser = serial.Serial(port, 9600, timeout=None)

client_id = "74ea23df-6639-44b0-bcd5-f3debb1bb18c"
client_lightTelemetry_topic = client_id + '/lightTelemetry'
client_command_topic = client_id + '/command'

mqtt_client = mqtt.Client(client_id + "gateway")
mqtt_client.connect('test.mosquitto.org')
mqtt_client.loop_start()


def handle_command(client, userdata, message):
    global state
    payload = json.loads(message.payload.decode())
    if (payload["gate"] == "Intruder"):
        state = 2
    elif (payload["gate"] == "Valid"):
        state = 1


mqtt_client.subscribe(client_command_topic, qos=1)
mqtt_client.on_message = handle_command

while True:
    time.sleep(2)
    if (state == 1):
        print("Valid password, Weclome back:")
        print("wait 10 seconds to enter password again:")
        GPIO.setup(27,GPIO.OUT)
        GPIO.output(27,GPIO.HIGH)
        time.sleep(10)
        GPIO.output(27,GPIO.LOW)
        state = 0

    elif (state == 2):
        
        print("Invalid password, wait 10 seconds to enter again:")
        GPIO.setup(17,GPIO.OUT)
        for i in range(0, 10):
            GPIO.output(17,GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(17,GPIO.LOW)
            time.sleep(0.5)

        GPIO.output(17,GPIO.LOW)  
        
        state = 0
    elif (state == 0):
        
        print("Enter password in the keypad :")
        byte_data = ser.readline()
        string_data = byte_data.decode('UTF-8') #
        telemetry = json.dumps({'value' : string_data[:4]})
        print("Sending by gateway to cloud ", telemetry)
        mqtt_client.publish(client_lightTelemetry_topic, telemetry, qos=1)
        time.sleep(2)
    
    