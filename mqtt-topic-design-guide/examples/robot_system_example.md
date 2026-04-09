# Robot System Example

## Scenario

Node-RED sends commands to a UR robot through an MQTT bridge.

## Topics

- `robot/ur/cmd`
- `robot/ur/response`
- `robot/ur/status`
- `robot/ur/fault`

## Why this works

The UI can:
- send commands on `cmd`
- watch direct results on `response`
- monitor live state on `status`
- show alarms from `fault`
