# System Overview

This project connects a user-facing dashboard to a Universal Robots arm using MQTT and a lightweight Python bridge.

## Purpose

The goal is to let an operator press a button in Node-RED and trigger a robot action without manually interacting with the robot controller.

## Main Components

### 1. Node-RED
Node-RED provides the user interface. In this project, a dashboard button publishes the command `wave` on the MQTT topic `robot/ur/cmd`.

### 2. MQTT Broker
Mosquitto acts as the message broker. It passes messages between Node-RED and the Python bridge.

### 3. Python Bridge
The Python script subscribes to the MQTT command topic. When it receives a command, it connects to the UR Dashboard Server over TCP and sends the proper robot command.

### 4. UR Dashboard Server
The UR robot listens for dashboard commands on port `29999`. In this project, the bridge sends commands such as:

- `load wave.urp`
- `play`
- `running`

## Command Flow

```text
Operator presses button in Node-RED
        ↓
Node-RED publishes MQTT command
        ↓
Python bridge receives the command
        ↓
Python bridge sends dashboard command to UR robot
        ↓
UR robot responds
        ↓
Python bridge publishes status back to MQTT
        ↓
Node-RED displays the result
```

## Why MQTT Was Used

MQTT is a good fit here because it is lightweight, simple, and easy to scale. Once the pattern is working for one robot, more robots can be added on separate topics.

Example future topics:

- `robot/ur/cmd`
- `robot/ur/response`
- `robot/abb/cmd`
- `robot/abb/response`
- `robot/fanuc/cmd`
- `robot/fanuc/response`

## Why This Architecture Matters

This setup separates the user interface, messaging layer, and robot control layer. That makes the project easier to troubleshoot, easier to expand, and more realistic as a portfolio piece.
