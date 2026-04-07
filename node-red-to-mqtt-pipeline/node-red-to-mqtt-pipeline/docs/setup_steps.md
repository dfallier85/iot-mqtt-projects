# Setup Steps

## 1. Make sure Node-RED is running

If Node-RED is already installed, start it and open the editor in your browser.

Typical local editor address:
- `http://<DEVICE_IP>:1880`

## 2. Make sure MQTT broker is reachable

Record:
- broker IP
- broker port

Typical example:
- IP: `192.168.4.1`
- Port: `1883`

## 3. Import the example flow

Open Node-RED:
- Menu
- Import
- Select `nodered/flow.json`

## 4. Check the MQTT broker config node

Make sure it points to your broker IP and port.

## 5. Deploy the flow

After import and broker check, press Deploy.

## 6. Test commands

Use the inject nodes:
- `Send Wave`
- `Send Home`

These publish to:
- `robot/test/cmd`

## 7. Watch for responses

The flow subscribes to:
- `robot/test/response`

Any returned message should appear in the debug panel.
