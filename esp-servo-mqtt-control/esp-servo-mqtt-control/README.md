# ESP32 / ESP8266 Servo Control over MQTT

A practical GitHub-style guide for controlling servos on ESP32 and ESP8266 boards over MQTT.

This project shows how to:
- connect an ESP device to Wi-Fi
- connect it to an MQTT broker
- subscribe to a command topic
- move a servo on command
- publish a completion response back to MQTT

It is a clean stepping stone between simple MQTT tests and larger device-control systems.

---

## What This Project Covers

- ESP32 servo control over MQTT
- ESP8266 servo control over MQTT
- simple command topics and response topics
- a basic `wave` motion
- optional `center` command
- Node-RED testing flow
- a repeatable device-control template

---

## Folder Structure

```text
esp-servo-mqtt-control/
├── README.md
├── esp32/
│   └── esp32_servo_mqtt.ino
├── esp8266/
│   └── esp8266_servo_mqtt.ino
├── docs/
│   ├── wiring_notes.md
│   ├── topic_strategy.md
│   └── testing_workflow.md
├── nodered/
│   └── flow.json
├── templates/
│   └── esp_mqtt_project_template.md
└── .gitignore
```

---

## Topics

### ESP32
- Command: `servo/esp32/cmd`
- Response: `servo/esp32/response`

### ESP8266
- Command: `servo/esp8266/cmd`
- Response: `servo/esp8266/response`

---

## Example Commands

- `wave`
- `center`

---

## Why This Matters

This is a strong practical project because it proves you can connect:
- Wi-Fi
- MQTT
- embedded device control
- Node-RED or terminal-based testing

It is also a good small-scale version of the same messaging ideas used in larger robotics systems.

---

## How to Use This Repo

Start with:
- `docs/wiring_notes.md`
- `docs/topic_strategy.md`
- `docs/testing_workflow.md`

Then upload:
- `esp32/esp32_servo_mqtt.ino`
- or `esp8266/esp8266_servo_mqtt.ino`

Import:
- `nodered/flow.json`

Use:
- `templates/esp_mqtt_project_template.md`

for future device projects.

---

## Libraries Needed

### ESP32
- `PubSubClient`
- `ESP32Servo`

### ESP8266
- `PubSubClient`
- built-in `Servo` library for common Arduino ESP8266 setups

---

## Author Notes

This repo keeps the logic intentionally simple so it is easy to learn from, test, and expand later.
