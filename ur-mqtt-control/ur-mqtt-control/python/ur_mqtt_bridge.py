#!/usr/bin/env python3
"""
ur_mqtt_bridge.py

Bridge MQTT commands from Node-RED to a Universal Robots arm using the
Dashboard Server on port 29999.

Flow:
Node-RED -> MQTT -> this script -> UR Dashboard Server -> MQTT response -> Node-RED
"""

import socket
import time
from typing import Optional

import paho.mqtt.client as mqtt


# =============================
# User configuration
# =============================
MQTT_BROKER = "192.168.4.1"
MQTT_PORT = 1883
MQTT_TOPIC_CMD = "robot/ur/cmd"
MQTT_TOPIC_RESP = "robot/ur/response"
MQTT_CLIENT_ID = "ur-mqtt-bridge"

ROBOT_IP = "10.7.103.235"
ROBOT_PORT = 29999
SOCKET_TIMEOUT_SEC = 3.0

PROGRAM_NAME = "wave.urp"


def send_ur_command(command: str, read_banner: bool = True) -> str:
    """
    Connect to the UR Dashboard Server, optionally read its greeting banner,
    send one command, then return the response.
    """
    try:
        with socket.create_connection((ROBOT_IP, ROBOT_PORT), timeout=SOCKET_TIMEOUT_SEC) as sock:
            sock.settimeout(SOCKET_TIMEOUT_SEC)

            # Some UR dashboard connections send a greeting banner first.
            if read_banner:
                try:
                    _ = sock.recv(1024)
                except socket.timeout:
                    pass

            sock.sendall((command + "\n").encode("utf-8"))
            response = sock.recv(1024).decode("utf-8", errors="replace").strip()
            return response or "<no response>"
    except Exception as exc:
        return f"ERROR: {exc}"


def publish_status(client: mqtt.Client, message: str) -> None:
    """Publish a status message for Node-RED or other subscribers."""
    client.publish(MQTT_TOPIC_RESP, message)
    print(f"Published status: {message}")


def handle_wave_command(client: mqtt.Client) -> None:
    """Load and play the configured UR program, then report status."""
    load_reply = send_ur_command(f"load {PROGRAM_NAME}")
    time.sleep(0.2)
    play_reply = send_ur_command("play")
    time.sleep(0.2)
    running_reply = send_ur_command("running")

    summary = (
        f"load: {load_reply} | "
        f"play: {play_reply} | "
        f"running: {running_reply}"
    )
    publish_status(client, summary)


def handle_custom_command(client: mqtt.Client, command: str) -> None:
    """
    Optional passthrough handler for simple dashboard commands.
    This keeps the script flexible if more commands are added later.
    """
    safe_commands = {
        "stop": "stop",
        "pause": "pause",
        "running": "running",
        "robotmode": "robotmode",
        "power on": "power on",
        "power off": "power off",
        "brake release": "brake release",
    }

    if command not in safe_commands:
        publish_status(client, f"Unknown command: {command}")
        return

    reply = send_ur_command(safe_commands[command])
    publish_status(client, f"{command}: {reply}")


def on_connect(client: mqtt.Client, userdata, flags, rc, properties: Optional[dict] = None) -> None:
    """Subscribe to the command topic once the broker connection is established."""
    print(f"Connected to MQTT broker with result code: {rc}")
    client.subscribe(MQTT_TOPIC_CMD)
    publish_status(client, "UR bridge online")


def on_message(client: mqtt.Client, userdata, msg: mqtt.MQTTMessage) -> None:
    """Process inbound MQTT messages from Node-RED."""
    command = msg.payload.decode("utf-8", errors="replace").strip().lower()
    print(f"Received MQTT command: {command}")

    if command == "wave":
        handle_wave_command(client)
    else:
        handle_custom_command(client, command)


def main() -> None:
    """Create the MQTT client and run forever."""
    client = mqtt.Client(client_id=MQTT_CLIENT_ID)
    client.on_connect = on_connect
    client.on_message = on_message

    print(f"Connecting to MQTT broker at {MQTT_BROKER}:{MQTT_PORT}...")
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    client.loop_forever()


if __name__ == "__main__":
    main()
