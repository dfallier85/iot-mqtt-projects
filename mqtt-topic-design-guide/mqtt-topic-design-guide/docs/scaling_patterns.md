# Scaling Patterns

## Single-device pattern

Example:
- `servo/esp32/cmd`
- `servo/esp32/response`

Good for:
- one small project
- simple testing
- learning

---

## Per-device pattern

Example:
- `servo/esp32_1/cmd`
- `servo/esp32_2/cmd`
- `servo/esp32_1/status`

Good for:
- multiple devices of same type
- identifying which device responded

---

## Per-subsystem pattern

Example:
- `robot/ur/cmd`
- `robot/abb/cmd`
- `system/plc/status`

Good for:
- mixed systems
- robots plus support systems
- larger demos

---

## Supervisor pattern

Example:
- `system/all/status`
- `system/all/fault`

Useful when you want:
- one dashboard summary
- one place for overall machine state

---

## Key point

Do not overdesign too early.  
But do not trap yourself in a naming scheme that only works for one device if you know expansion is coming.
