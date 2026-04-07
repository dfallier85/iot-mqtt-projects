# Core Rules

## Rule 1: Keep names boring

Good:
- `robot/ur/cmd`
- `servo/esp32/response`

Bad:
- `robotstuff/main/data`
- `coolproject/deviceA/outputThing`

Clear beats clever.

---

## Rule 2: Separate message types

Do not mix:
- commands
- responses
- status
- faults

into one vague topic.

Split them clearly.

---

## Rule 3: Keep hierarchy meaningful

A topic should usually answer:
- subsystem
- device or class
- message type

Example:
- `robot/ur/cmd`

This says:
- subsystem = robot
- device = ur
- message type = cmd

---

## Rule 4: Design for testing

A good topic should be easy to test with:
- `mosquitto_pub`
- `mosquitto_sub`
- Node-RED MQTT nodes

If the topic tree is too confusing to test quickly, it is probably too confusing overall.

---

## Rule 5: Leave room to grow

Pick a pattern that can handle:
- one device
- ten devices
- later subsystems
- future status topics
- future fault topics
