# Node-RED UI to MQTT Command Pipeline

A practical GitHub-style guide for building a simple command pipeline from Node-RED into MQTT.

This project is the next layer after getting a broker running. It shows how to use Node-RED to:
- send commands to an MQTT topic
- receive responses from another MQTT topic
- create a clean operator-facing control layer

---

## What This Project Covers

- Basic Node-RED to MQTT command flow
- Publish and subscribe node setup
- A simple command / response topic pattern
- Example flow export
- Tips for keeping Node-RED readable
- A reusable template for later UI-driven projects

---

## Why This Matters

This is the bridge between a raw broker and a usable system.

Once this works, you can build:
- robot command dashboards
- ESP32 control panels
- sensor monitors
- alarm displays
- multi-device test interfaces

---

## Folder Structure

```text
node-red-to-mqtt-pipeline/
├── README.md
├── docs/
│   ├── setup_steps.md
│   ├── topic_pattern.md
│   └── testing_notes.md
├── nodered/
│   └── flow.json
├── examples/
│   └── command_response_example.md
├── templates/
│   └── node_red_mqtt_project_template.md
└── .gitignore
```

---

## Basic Flow

```text
[Node-RED Button / Inject]
          ->
      [MQTT Out]
          ->
     [MQTT Broker]
          ->
   [Subscriber / Device]

[Device / Script]
          ->
      [MQTT Response Topic]
          ->
      [MQTT In]
          ->
      [Debug / UI Display]
```

---

## Example Topics

- Command topic: `robot/test/cmd`
- Response topic: `robot/test/response`

You can later change these to things like:
- `robot/ur/cmd`
- `robot/ur/response`
- `servo/esp32/cmd`
- `system/plc/status`

---

## How to Use This Repo

Start with:
- `docs/setup_steps.md`

Then review:
- `docs/topic_pattern.md`
- `docs/testing_notes.md`

Import:
- `nodered/flow.json`

Read:
- `examples/command_response_example.md`

Use:
- `templates/node_red_mqtt_project_template.md`

for future projects.

---

## Author Notes

This repo is intentionally simple. The goal is to make Node-RED a clear, reliable front end for MQTT-based systems before adding more logic.
