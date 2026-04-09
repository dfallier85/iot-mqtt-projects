# Device Roles

## AGX

The AGX typically owns:
- robot-side bridge scripts
- command translation
- robot sockets or APIs
- logging
- optional vision or edge logic

## groov / PLC-adjacent layer

This layer typically owns:
- machine state
- status publication
- interlocks
- alarm or fault state
- operator-facing supervisory logic

## MQTT broker host

This may run on:
- Raspberry Pi
- AGX
- other Linux device

Its job is transport, not decision making.

## Node-RED / UI

This layer should stay readable:
- send command
- show response
- show system status
- show faults
- avoid hiding critical logic in messy flows
