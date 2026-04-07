# Integration Notes

## MQTT

A portable hub works well when the Pi also hosts the broker.

Example:
- broker IP: `192.168.4.1`
- port: `1883`

## Node-RED

If Node-RED runs on the Pi, connected clients can use the Pi as:
- broker
- dashboard host
- simple supervisory device

## Practical reminder

Keep a written network plan:
- SSID
- password
- Pi IP
- MQTT port
- Node-RED port
- topic map
