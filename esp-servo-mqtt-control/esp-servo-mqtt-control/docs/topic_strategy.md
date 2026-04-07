# Topic Strategy

## ESP32 topics
- `servo/esp32/cmd`
- `servo/esp32/response`

## ESP8266 topics
- `servo/esp8266/cmd`
- `servo/esp8266/response`

## Why this works

Each device family has:
- one command topic
- one response topic

That keeps testing and debugging simple.

## Example commands

- `wave`
- `center`

## Future expansions

- `servo/esp32/status`
- `servo/esp8266/status`
- per-device topic names if you have multiple boards
