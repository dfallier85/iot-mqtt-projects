# Testing Workflow

## Step 1: Confirm broker is running

Make sure the MQTT broker is online and reachable.

## Step 2: Upload firmware

Upload either:
- ESP32 sketch
- ESP8266 sketch

Update:
- SSID
- password
- broker IP

before uploading.

## Step 3: Watch responses

Subscribe in a terminal:

### ESP32
```bash
mosquitto_sub -h <BROKER_IP> -t servo/esp32/response
```

### ESP8266
```bash
mosquitto_sub -h <BROKER_IP> -t servo/esp8266/response
```

## Step 4: Publish commands manually

### ESP32 wave
```bash
mosquitto_pub -h <BROKER_IP> -t servo/esp32/cmd -m "wave"
```

### ESP8266 wave
```bash
mosquitto_pub -h <BROKER_IP> -t servo/esp8266/cmd -m "wave"
```

## Step 5: Test with Node-RED

Import the example flow and try the inject buttons.

## What to confirm

- board connects to Wi-Fi
- board connects to MQTT
- servo moves correctly
- response topic confirms completion
