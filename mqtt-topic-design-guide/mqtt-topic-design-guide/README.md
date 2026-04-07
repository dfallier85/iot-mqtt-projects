# MQTT Topic Naming and System Design Guide

A practical GitHub-style guide for organizing MQTT topics so systems stay understandable, debuggable, and scalable.

This repo is meant for real projects involving:
- Raspberry Pi brokers
- Node-RED dashboards
- ESP32 / ESP8266 devices
- Jetson / Linux bridges
- robots
- PLC-adjacent systems

---

## What This Project Covers

- how to name MQTT topics clearly
- how to separate commands, responses, status, and faults
- topic patterns for devices, robots, and systems
- common mistakes that make MQTT systems hard to maintain
- payload strategy notes
- examples for single-device and multi-device projects
- a reusable documentation template

---

## Why This Matters

A lot of MQTT systems work at first and then become a mess.

The broker is fine.  
The code is fine.  
The problem is usually that the topic tree turned into spaghetti.

Good topic design makes it easier to:
- debug
- expand
- document
- hand off to someone else
- build multi-device systems without confusion

---

## Folder Structure

```text
mqtt-topic-design-guide/
├── README.md
├── docs/
│   ├── core_rules.md
│   ├── command_response_status_fault.md
│   ├── payload_strategy.md
│   └── scaling_patterns.md
├── examples/
│   ├── simple_device_example.md
│   ├── robot_system_example.md
│   └── multi_device_example.md
├── templates/
│   └── mqtt_topic_template.md
└── .gitignore
```

---

## Core Idea

A good MQTT topic tree answers these questions quickly:

- who is this for?
- what kind of message is this?
- where should replies go?
- how would I debug this at 2 AM?

If the topic tree does not answer those questions, it probably needs cleanup.

---

## Recommended Message Types

The four message types you should usually think about first are:

- `cmd`
- `response`
- `status`
- `fault`

That one decision alone will clean up a lot of systems.

---

## Example Topic Patterns

### Simple device
- `servo/esp32/cmd`
- `servo/esp32/response`
- `servo/esp32/status`

### Robot
- `robot/ur/cmd`
- `robot/ur/response`
- `robot/ur/status`

### PLC / system
- `system/plc/status`
- `system/plc/fault`
- `system/plc/interlock`

### Multi-robot
- `robot/ur/cmd`
- `robot/abb/cmd`
- `robot/ur/response`
- `robot/abb/response`

---

## Design Goals

A good topic strategy should be:

- boring
- descriptive
- predictable
- expandable
- easy to test from a terminal
- easy to understand in Node-RED

---

## How to Use This Repo

Start with:
- `docs/core_rules.md`
- `docs/command_response_status_fault.md`

Then review:
- `docs/payload_strategy.md`
- `docs/scaling_patterns.md`

Examples:
- `examples/simple_device_example.md`
- `examples/robot_system_example.md`
- `examples/multi_device_example.md`

For your own projects:
- `templates/mqtt_topic_template.md`

---

## Author Notes

This repo is intentionally about structure more than code.  
The topic tree is one of the most important design choices in an MQTT system, and it is usually much easier to fix early than late.
