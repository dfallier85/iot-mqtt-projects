# How to Send Commands from Node-RED to a UR Robot Using MQTT

A practical project for sending commands from a Node-RED dashboard to a Universal Robots arm using MQTT and a Python bridge running on an edge device such as a Jetson AGX Orin.

---

## Overview

This project uses Node-RED to publish robot commands over MQTT. A Python script running on an AGX subscribes to those commands, forwards them to the UR robot through the Dashboard Server, and publishes a response back to MQTT so Node-RED can display the result.

This setup is simple, scalable, and useful for demos, training, and early-stage industrial integrations.

---

## What This Project Does

- Sends a command from a Node-RED dashboard button
- Publishes the command over MQTT
- Receives the command on an AGX or similar edge device
- Sends the command to a UR robot using the Dashboard Server
- Publishes the robot response back to MQTT
- Displays the result in Node-RED

---

## System Architecture

```text
[Node-RED Dashboard]
        |
        | MQTT publish
        v
   [MQTT Broker]
        |
        | MQTT subscribe
        v
 [Python Bridge on AGX]
        |
        | TCP socket :29999
        v
 [UR Dashboard Server]
```

---

## Hardware Used

- Universal Robots arm
- Jetson AGX Orin, Raspberry Pi, or Linux PC
- Network switch or shared LAN connection

---

## Software Used

- Node-RED
- Mosquitto MQTT broker
- Python 3
- `paho-mqtt`
- UR Dashboard Server

---

## Network Example

| Device | Example IP |
|---|---|
| MQTT Broker | `192.168.4.1` |
| AGX / Python Bridge | `192.168.4.10` |
| UR Robot | `10.7.103.235` |

Update these values to match your own setup.

---

## Project Folder Structure

```text
ur-mqtt-control/
├── README.md
├── .gitignore
├── python/
│   └── ur_mqtt_bridge.py
├── nodered/
│   └── flow.json
└── docs/
    └── system_overview.md
```

---

## MQTT Topics

| Purpose | Topic |
|---|---|
| Send robot command | `robot/ur/cmd` |
| Receive robot response | `robot/ur/response` |

---

## Supported Command Example

This guide uses a simple test command:

- `wave`

When the Python bridge receives `wave`, it tells the UR robot to:
1. Load `wave.urp`
2. Play the program
3. Report back whether the robot is running

---

## Setup Instructions

### 1. Install Mosquitto

```bash
sudo apt update
sudo apt install mosquitto mosquitto-clients -y
sudo systemctl enable mosquitto
sudo systemctl start mosquitto
```

### 2. Verify MQTT Works

Open one terminal:

```bash
mosquitto_sub -t test/topic
```

Open another terminal:

```bash
mosquitto_pub -t test/topic -m "hello"
```

If everything is working, the subscriber terminal should print `hello`.

### 3. Install Python Dependency

```bash
pip3 install paho-mqtt
```

### 4. Save the Python Bridge Script

The script is already included in `python/ur_mqtt_bridge.py`.

### 5. Run the Python Bridge

```bash
python3 python/ur_mqtt_bridge.py
```

### 6. Import the Node-RED Flow

Import `nodered/flow.json` into Node-RED.

The included flow contains:
- a dashboard button labeled `Wave`
- an MQTT output node publishing to `robot/ur/cmd`
- an MQTT input node subscribed to `robot/ur/response`
- a dashboard text widget for status
- a debug node for troubleshooting

---

## How to Test

1. Make sure the robot is powered on and reachable
2. Make sure the AGX can ping the robot
3. Start Mosquitto
4. Start the Python bridge script
5. Import and deploy the Node-RED flow
6. Open the Node-RED dashboard
7. Press the `Wave` button
8. Confirm the robot loads and plays the program
9. Confirm a response appears in Node-RED

---

## Expected Result

When the button is pressed:

- Node-RED publishes `wave`
- The AGX receives the message
- The Python script tells the robot to load `wave.urp`
- The robot starts running the program
- A status message is published back to Node-RED

---

## Troubleshooting

### Robot does not respond

- Confirm the robot IP address is correct
- Confirm port `29999` is reachable
- Confirm the robot is in a state that allows dashboard commands
- Confirm `wave.urp` exists on the robot

### MQTT message is not received

- Confirm the broker IP is correct
- Confirm both Node-RED and Python are using the same topics
- Confirm Mosquitto is running

### Program fails to load

- Check the exact program filename on the robot
- Make sure the file is stored on the robot controller
- Make sure remote loading is allowed in your setup

### Python socket errors

- Test network communication with `ping`
- Verify the robot and AGX are on reachable networks
- Check firewall rules if applicable

---

## Expansion Ideas

- Add more robot commands such as `home`, `pick`, or `place`
- Add ABB and Fanuc robots on separate MQTT topics
- Add safety checks before sending the play command
- Add robot status monitoring in Node-RED
- Add logging to file for command history

---

## Why This Project Matters

This project demonstrates:

- MQTT-based industrial communication
- Robot command routing from a UI
- Python socket programming
- Integration between OT and IT-style systems
- A clean foundation for multi-robot control

---

## Author Notes

This guide is based on a real working lab-style setup using Node-RED, MQTT, an AGX device, and a UR robot. It is meant to be practical, readable, and easy to expand into a larger controls or robotics portfolio.
