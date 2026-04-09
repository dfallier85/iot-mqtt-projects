# Testing Notes

## First test goal

Confirm that Node-RED really publishes to MQTT and can receive a response back.

## Easy test method

### 1. Subscribe in a terminal

```bash
mosquitto_sub -h <BROKER_IP> -t robot/test/cmd
```

### 2. Press a button in Node-RED

Use:
- `Send Wave`
- `Send Home`

You should see the payload arrive in the terminal.

## Response test

### 1. Publish a fake response manually

```bash
mosquitto_pub -h <BROKER_IP> -t robot/test/response -m "response ok"
```

### 2. Watch Node-RED debug panel

You should see:
- `response ok`

## What to confirm

- Node-RED can publish
- broker receives the message
- Node-RED can subscribe
- response topic appears in debug panel
