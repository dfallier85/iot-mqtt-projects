# Topic Pattern

## Goal

Keep command and response topics separate and easy to understand.

## Basic example

### Command
- `robot/test/cmd`

### Response
- `robot/test/response`

## Why this works

It keeps the pipeline readable:
- UI publishes command
- device or script listens
- device or script replies
- UI listens for response

## Good habits

- use one command topic per device or subsystem
- use one response topic per device or subsystem
- do not mix commands and responses on the same topic
- keep names boring and descriptive

## Example future topic upgrades

- `robot/ur/cmd`
- `robot/ur/response`
- `robot/abb/cmd`
- `robot/abb/response`
- `servo/esp32/cmd`
- `servo/esp32/response`
- `system/plc/status`
