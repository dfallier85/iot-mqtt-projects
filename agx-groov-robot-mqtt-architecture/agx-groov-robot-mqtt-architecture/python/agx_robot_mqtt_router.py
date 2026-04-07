"""
agx_robot_mqtt_router.py

Reference example for an AGX-side Python process that:
- subscribes to robot MQTT command topics
- routes commands to robot-specific handlers
- publishes responses back to robot response topics

This example uses stub handler functions for clarity.
Replace those with real UR dashboard, ABB socket, or other robot APIs.
"""

import json
import paho.mqtt.client as mqtt

MQTT_BROKER = "192.168.4.1"
MQTT_PORT = 1883

TOPIC_UR_CMD = "robot/ur/cmd"
TOPIC_UR_RESP = "robot/ur/response"

TOPIC_ABB_CMD = "robot/abb/cmd"
TOPIC_ABB_RESP = "robot/abb/response"

TOPIC_PLC_STATUS = "system/plc/status"


def handle_ur_command(command: str) -> dict:
    return {
        "target": "ur",
        "requested_command": command,
        "result": "ok",
        "detail": f"Simulated UR command handling for: {command}",
    }


def handle_abb_command(command: str) -> dict:
    return {
        "target": "abb",
        "requested_command": command,
        "result": "ok",
        "detail": f"Simulated ABB command handling for: {command}",
    }


def on_connect(client, userdata, flags, rc):
    print(f"Connected to MQTT broker with result code {rc}")
    client.subscribe(TOPIC_UR_CMD)
    client.subscribe(TOPIC_ABB_CMD)


def on_message(client, userdata, msg):
    topic = msg.topic
    payload = msg.payload.decode().strip()

    if topic == TOPIC_UR_CMD:
        response = handle_ur_command(payload)
        client.publish(TOPIC_UR_RESP, json.dumps(response))

    elif topic == TOPIC_ABB_CMD:
        response = handle_abb_command(payload)
        client.publish(TOPIC_ABB_RESP, json.dumps(response))


def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(MQTT_BROKER, MQTT_PORT, 60)

    # Optional startup status publish.
    client.publish(TOPIC_PLC_STATUS, json.dumps({
        "source": "agx_router",
        "status": "starting"
    }))

    client.loop_forever()


if __name__ == "__main__":
    main()
