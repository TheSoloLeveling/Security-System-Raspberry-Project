from datetime import datetime
import time
import paho.mqtt.client as mqtt
import json
import csv 
import cv2
import os
import random

Access = "1111"
global i
i = 1
client_id = "74ea23df-6639-44b0-bcd5-f3debb1bb18c"
client_lightTelemetry_topic = client_id + '/lightTelemetry'
client_command_topic = client_id + '/command'
csvFilePath1= r'lightTelemetry.csv'
jsonFilePath1 = r'C:\Users\bouzi\Desktop\Github\Security-System-Raspberry-Project\app\front\src\data\data1.json'
csvFilePath2 = r'cameraTelemetry.csv'
jsonFilePath2 = r'C:\Users\bouzi\Desktop\Github\Security-System-Raspberry-Project\app\front\src\data\data2.json'


def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []
      
    #read csv file
    with open(csvFilePath, encoding='utf-8') as csvf: 
        #load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf) 

        #convert each csv row into python dict
        for row in csvReader: 
            #add this python dict to json array
            jsonArray.append(row)
  
    #convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)


def handle_telemetry(client, userdata, message):
    payload = json.loads(message.payload.decode())
    data = [payload['value'], datetime.now().strftime("%H:%M:%S")]
    
    if (payload['value'] != Access):
        command = json.dumps({'gate' : 'Intruder', 'password' : payload['value'], 'timestamp' : datetime.now().strftime("%H:%M:%S")})
        data = ["Intruder", payload['value'], datetime.now().strftime("%H:%M:%S")]
        print("Sending by cloud to gateway", command)
        
        step = 1
        frames_count = 10
        cam = cv2.VideoCapture('http://10.202.40.78:4747/video')
       
        currentframe = 0
        frame_per_second = cam.get(cv2.CAP_PROP_FPS) 
        frames_captured = 0

        while (True):
            
            ret, frame = cam.read()
            if ret:
                if currentframe > (step*frame_per_second):  
                    currentframe = 0
                    name = 'frame' + str(random.randint(1, 5000)) + '.jpg'
                    
                    print(name)
                    cv2.imwrite(r'C:\Users\bouzi\Desktop\Github\Security-System-Raspberry-Project\app\front\src\data\{}'.format(name), frame)
                    c = ["http://127.0.0.1:8080/" + name, datetime.now().strftime("%H:%M:%S")]
                    f = open('cameraTelemetry.csv', 'a', newline='')  
                    writer = csv.writer(f)
                    writer.writerow(c)
                    f.close()
                    csv_to_json(csvFilePath2, jsonFilePath2)
                    break          
                    frames_captured+=1
                    if frames_captured>frames_count-1:
                        ret = False
                currentframe += 1           
            if ret==False:
                break
        cam.release()
        cv2.destroyAllWindows()
        
        mqtt_client.publish(client_command_topic, command, qos=1)

    elif(payload['value'] == Access) :
        command = json.dumps({'gate' : 'Valid', 'password' : payload['value'], 'timestamp' : datetime.now().strftime("%H:%M:%S")})
        data = ["Valid", payload['value'], datetime.now().strftime("%H:%M:%S")]
        print("Sending by cloud to gateway", command)

        step = 1
        frames_count = 10
        cam = cv2.VideoCapture('http://10.202.40.78:4747/video')
       
        currentframe = 0
        frame_per_second = cam.get(cv2.CAP_PROP_FPS) 
        frames_captured = 0

        while (True):
            
            ret, frame = cam.read()
            if ret:
                if currentframe > (step*frame_per_second):  
                    currentframe = 0
                    name = 'frame' + str(random.randint(1, 5000)) + '.jpg'
                    
                    print(name)
                    cv2.imwrite(r'C:\Users\bouzi\Desktop\Github\Security-System-Raspberry-Project\app\front\src\data\{}'.format(name), frame)
                    c = ["http://127.0.0.1:8080/" + name, datetime.now().strftime("%H:%M:%S")]
                    f = open('cameraTelemetry.csv', 'a', newline='')  
                    writer = csv.writer(f)
                    writer.writerow(c)
                    f.close()
                    csv_to_json(csvFilePath2, jsonFilePath2)
                    break          
                    frames_captured+=1
                    if frames_captured>frames_count-1:
                        ret = False
                currentframe += 1           
            if ret==False:
                break
        cam.release()
        cv2.destroyAllWindows()

        mqtt_client.publish(client_command_topic, command, qos=1)

    e = open('lightTelemetry.csv', 'a', newline='')  
    writer = csv.writer(e)
    writer.writerow(data)
    e.close()
    csv_to_json(csvFilePath1, jsonFilePath1)

mqtt_client = mqtt.Client(client_id + "cloud")
mqtt_client.connect('test.mosquitto.org')
mqtt_client.loop_start()
mqtt_client.subscribe(client_lightTelemetry_topic, qos=1)
mqtt_client.on_message = handle_telemetry

while True:
    time.sleep(3)