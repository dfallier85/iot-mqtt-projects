# Topic Map

## Robot command topics
- `robot/ur/cmd`
- `robot/abb/cmd`

## Robot response topics
- `robot/ur/response`
- `robot/abb/response`

## System status topics
- `system/plc/status`
- `system/plc/interlock`
- `system/plc/fault`

## Why this works

Each subsystem gets:
- one clear command path
- one clear response path
- separate system-level status topics

That helps with:
- debugging
- testing
- future scaling
- Node-RED clarity
