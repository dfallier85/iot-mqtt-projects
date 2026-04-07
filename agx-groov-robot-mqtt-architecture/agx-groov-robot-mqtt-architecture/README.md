# AGX + Groov + Robot MQTT Architecture

A practical GitHub-style guide for organizing an industrial-style MQTT system where a Jetson AGX, a groov device, and one or more robots share a clean message architecture.

This is a category capstone piece. It ties together:
- MQTT
- Node-RED
- AGX-side Python bridges
- groov / PLC-style supervisory status
- robot command routing

The main goal is to show how these devices can work together in a way that is readable, scalable, and practical to troubleshoot.

---

## What This Project Covers

- high-level AGX + groov + robot MQTT architecture
- recommended topic map
- role of the AGX in robot command handling
- role of groov / PLC-adjacent status and supervisory logic
- Node-RED flow pattern
- command routing ideas
- fault and status handling ideas
- a reusable project template

---

## Why This Matters

This is the kind of project that proves you can think in systems.

Instead of just showing that one device can publish a message, this shows:
- who owns commands
- who owns robot-specific translation
- who owns system status
- how operator-facing UI fits into the stack
- how the whole thing can grow later

That is much stronger than a one-off demo.

---

## Folder Structure

```text
agx-groov-robot-mqtt-architecture/
├── README.md
├── docs/
│   ├── system_architecture.md
│   ├── device_roles.md
│   ├── topic_map.md
│   └── fault_and_status_strategy.md
├── examples/
│   ├── command_flow_example.md
│   └── deployment_example.md
├── python/
│   └── agx_robot_mqtt_router.py
├── nodered/
│   └── flow.json
├── templates/
│   └── agx_groov_robot_project_template.md
└── .gitignore
```

---

## High-Level Architecture

```text
[Node-RED / groov UI]
          |
          v
     [MQTT Broker]
      /       \
     /         \
    v           v
[AGX Router]   [groov / PLC status publisher]
   /   \
  /     \
 v       v
[UR]   [ABB]
```

A common pattern is:
- Node-RED or groov UI sends operator commands
- AGX handles robot-specific translation and transport
- groov / PLC side publishes status, interlocks, or fault state
- robot responses return through MQTT to the UI

---

## Recommended Topic Map

### Robot commands
- `robot/ur/cmd`
- `robot/abb/cmd`

### Robot responses
- `robot/ur/response`
- `robot/abb/response`

### System / groov / PLC
- `system/plc/status`
- `system/plc/fault`
- `system/plc/interlock`

This keeps responsibilities clear.

---

## How to Use This Repo

Start with:
- `docs/system_architecture.md`
- `docs/device_roles.md`

Then review:
- `docs/topic_map.md`
- `docs/fault_and_status_strategy.md`

See examples:
- `examples/command_flow_example.md`
- `examples/deployment_example.md`

For starter references:
- `python/agx_robot_mqtt_router.py`
- `nodered/flow.json`

Use:
- `templates/agx_groov_robot_project_template.md`

for future projects.

---

## Author Notes

This repo is intentionally written as an architecture guide instead of pretending there is one exact implementation. The main value is the structure and role separation.
