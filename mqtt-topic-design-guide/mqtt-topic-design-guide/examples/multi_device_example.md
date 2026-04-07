# Multi-Device Example

## Scenario

A system has:
- UR robot
- ABB robot
- PLC
- ESP32 device

## Topics

### Robots
- `robot/ur/cmd`
- `robot/ur/response`
- `robot/abb/cmd`
- `robot/abb/response`

### PLC
- `system/plc/status`
- `system/plc/fault`
- `system/plc/interlock`

### ESP32
- `servo/esp32/cmd`
- `servo/esp32/response`

## Why this scales

Each subsystem has:
- a clear namespace
- a clear message purpose
- less collision risk
- easier debugging
