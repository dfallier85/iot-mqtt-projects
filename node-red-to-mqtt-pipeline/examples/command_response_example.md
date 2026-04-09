# Command / Response Example

## Example sequence

1. Operator presses `Send Wave`
2. Node-RED publishes `wave` to `robot/test/cmd`
3. A device, script, or test subscriber receives `wave`
4. That device publishes `wave complete` to `robot/test/response`
5. Node-RED debug panel shows the response

## Why this matters

This is the basic pattern that later becomes:
- robot control
- device control
- sensor requests
- alarm acknowledgments
- system status queries
