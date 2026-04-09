# Fault and Status Strategy

## Goal

Make it obvious why a command succeeded, failed, or was blocked.

## Good response behavior

A robot bridge should publish useful responses such as:

```json
{
  "target": "ur",
  "requested_command": "wave",
  "result": "ok"
}
```

Or on failure:

```json
{
  "target": "abb",
  "requested_command": "home",
  "result": "error",
  "reason": "robot not reachable"
}
```

## System-side status

The groov / PLC side should publish state like:
- ready
- not ready
- interlock false
- auto mode active
- reset required

## Why this matters

When something fails, the operator should not have to guess whether:
- MQTT failed
- AGX bridge failed
- robot failed
- interlock blocked the action
