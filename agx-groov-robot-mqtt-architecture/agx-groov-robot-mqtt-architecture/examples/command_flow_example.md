# Command Flow Example

## Scenario

Operator presses `UR Wave`.

## Flow

1. UI publishes `wave` to `robot/ur/cmd`
2. AGX router receives the message
3. AGX runs UR-specific bridge logic
4. UR response is published to `robot/ur/response`
5. UI displays result

## Parallel status path

At the same time, groov / PLC status may publish:
- `system/plc/status`
- `system/plc/interlock`

So the UI can show whether the machine was ready when the command was issued.
