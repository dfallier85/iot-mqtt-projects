# Configuration Notes

## Keep it simple first

A basic Mosquitto install is enough for early testing.

Do not overconfigure before the base system works.

## Record these

- Pi hostname
- Pi IP address
- broker port
- config file location

## Common config paths

- `/etc/mosquitto/mosquitto.conf`
- `/etc/mosquitto/conf.d/`

## Good early decisions

- keep the broker IP stable
- use clear topic names
- test with simple topics first

Examples:
- `robot/ur/cmd`
- `robot/ur/response`
- `system/plc/status`
- `servo/esp32/cmd`
