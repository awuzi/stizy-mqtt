import json
import random
import time
from datetime import datetime
from time import sleep

import paho.mqtt.client as mqtt

GROUPNAME = "WEB3-GROUPE10"
MQTT_BROKER = "hetic.arcplex.fr"
MQTT_USERNAME = "GROUPE10"
MQTT_PASSWORD = "14991799"
# un ID différent par Node
NODE_ID = ["12345678", "7654321", "987654543", "58381714", "13960537", "68191831", "54158491", "69607072", "51488201", "22361595", "24114793", "62061965", "73214383", "60052006", "94981317"]

def generateSensorValue(sensor_id: int, min_value: int, max_value: int):
    print("-------- MQTT Mise à jour du capteur %s --------" % sensor_id)
    client = mqtt.Client("client")
    client.username_pw_set(username=MQTT_USERNAME, password=MQTT_PASSWORD)
    client.connect(MQTT_BROKER)
    for node in NODE_ID:
        MQTT_TOPIC = GROUPNAME + "/" + node + "/" + str(sensor_id)
        MQTT_MSG = json.dumps({
            "source_address": node,
            "sensor_id": sensor_id,
            "tx_time_ms_epoch": int(time.time()),
            "data": {
                "value": round(random.uniform(min_value, max_value), 2)
            }
        })
        client.publish(MQTT_TOPIC, MQTT_MSG)
        # print("NODE_ID %s Timestamp : %s" % (node, int(time.time())))
    client.disconnect()

def run():
    while datetime.now().minute not in {0, 2, 4, 6, 8, 10, 12, 14, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58 }:
        sleep(1)

    generateSensorValue(112, 23, 29) # temp
    generateSensorValue(114, 25, 100) # humidite
    generateSensorValue(122, 0, 200) # compteur personne
    generateSensorValue(107, 0, 70) # bruit
    generateSensorValue(121, 0, 200000) # lumiere
    while True:
        sleep(120)
        generateSensorValue(112, 23, 29) # temp
        generateSensorValue(114, 25, 100) # humidite
        generateSensorValue(122, 0, 200) # compteur personne
        generateSensorValue(107, 0, 70) # bruit
        generateSensorValue(121, 0, 200000) # lumiere

run()