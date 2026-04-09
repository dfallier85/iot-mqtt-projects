# Command, Response, Status, Fault

## Command

Use `cmd` for messages that tell something to do an action.

Examples:
- `robot/ur/cmd`
- `servo/esp32/cmd`

Typical payloads:
- `wave`
- `home`
- `stop`

---

## Response

Use `response` for direct replies to commands.

Examples:
- `robot/ur/response`
- `servo/esp32/response`

Typical payloads:
- `wave complete`
- `home done`
- JSON result object

---

## Status

Use `status` for normal ongoing state reporting.

Examples:
- `robot/ur/status`
- `system/plc/status`
- `servo/esp32/status`

Typical payloads:
- `idle`
- `running`
- `connected`
- JSON state object

---

## Fault

Use `fault` for error or alarm conditions.

Examples:
- `robot/ur/fault`
- `system/plc/fault`

Typical payloads:
- `protective stop`
- `interlock false`
- JSON error object

---

## Why this separation helps

It keeps:
- UI flows cleaner
- terminal tests easier
- logs easier to read
- debugging faster
