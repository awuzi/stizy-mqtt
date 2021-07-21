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
client = mqtt.Client("client")
client.username_pw_set(username=MQTT_USERNAME, password=MQTT_PASSWORD)
client.connect(MQTT_BROKER)


def generateSensorValue(sensor_id: int, min_value: int, max_value: int):
    print("-------- MQTT Mise à jour du capteur %s --------" % sensor_id)
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


def run():
    while datetime.now().minute not in {0, 1, 2, 3,4, 5, 6, 7, 8, 9, 7, 8, 9, 10, 15, 20, 25, 29, 30, 31, 34, 35, 38, 39, 40, 41, 42, 44, 45, 49, 50, 53, 54, 58, 59, 55}:
        sleep(1)

    generateSensorValue(112, 23, 29)
    generateSensorValue(114, 0, 100)
    generateSensorValue(122, 0, 20)
    generateSensorValue(107, 0, 150)
    generateSensorValue(121, 0, 200000)
    while True:
        sleep(60 * 15)
        generateSensorValue(112, 23, 29)
        generateSensorValue(114, 0, 100)
        generateSensorValue(122, 0, 50)
        generateSensorValue(107, 0, 150)
        generateSensorValue(121, 0, 200000)


run()
