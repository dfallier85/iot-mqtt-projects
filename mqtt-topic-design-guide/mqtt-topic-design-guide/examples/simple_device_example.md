# Simple Device Example

## Scenario

One ESP32 controls one servo.

## Topics

- `servo/esp32/cmd`
- `servo/esp32/response`
- `servo/esp32/status`

## Example sequence

1. publish `wave` to `servo/esp32/cmd`
2. device moves servo
3. device publishes `wave complete` to `servo/esp32/response`
4. device optionally publishes `idle` to `servo/esp32/status`
