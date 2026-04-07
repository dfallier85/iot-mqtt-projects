# MQTT Broker on Raspberry Pi

A practical GitHub-style guide for setting up an MQTT broker on a Raspberry Pi using Mosquitto.

This is a clean foundation for later projects involving:
- Node-RED
- Jetson
- ESP32
- ESP8266
- robot control
- sensor networks

## Folder Structure

```text
mqtt-broker-on-raspberry-pi/
├── README.md
├── docs/
│   ├── installation_steps.md
│   ├── testing_workflow.md
│   └── configuration_notes.md
├── scripts/
│   ├── test_publish.sh
│   └── test_subscribe.sh
├── templates/
│   └── mqtt_project_template.md
└── .gitignore
```

## Quick Start

```bash
sudo apt update
sudo apt upgrade -y
sudo apt install mosquitto mosquitto-clients -y
sudo systemctl enable mosquitto
sudo systemctl start mosquitto
sudo systemctl status mosquitto
```

## Local Test

Terminal 1:

```bash
mosquitto_sub -t test/topic
```

Terminal 2:

```bash
mosquitto_pub -t test/topic -m "hello from pi"
```

If the subscriber sees the message, the broker is working locally.

## Why This Matters

Once this works, you can stack on:
- Node-RED UI control
- device messaging
- MQTT robot commands
- portable IoT hub ideas
