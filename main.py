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


def task(sensor_id: int, min_value: int, max_value: int):
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
        print("MQTT Mis à jour - Node %s Timestamp : %s" % (node, int(time.time())))


def run():
    while datetime.now().minute not in {0, 1, 2, 3, 5, 6, 7, 8, 9, 7, 8, 9, 10, 15, 20, 25, 30, 34, 35, 38, 39, 40, 41, 42, 44, 45, 50, 58, 59, 55}:
        sleep(1)

    task(112, 23, 29)
    task(114, 0, 100)
    task(122, 0, 50)
    task(107, 0, 150)
    task(121, 0, 200000)
    while True:
        sleep(60 * 15)
        task(112, 23, 29)
        task(114, 0, 100)
        task(122, 0, 50)
        task(107, 0, 150)
        task(121, 0, 200000)


run()
