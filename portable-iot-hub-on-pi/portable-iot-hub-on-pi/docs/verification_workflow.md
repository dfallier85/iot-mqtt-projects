# Verification Workflow

## Step 1: Confirm the AP is visible

On another device, scan for the SSID.

Example:
- `ESP32-Hub`

## Step 2: Connect to the AP

Use the configured password.

## Step 3: Confirm the Pi IP

From a connected device, try to reach:
- `192.168.4.1`

## Step 4: Verify DHCP behavior

Confirm the client device received an address in the expected subnet.

Example:
- `192.168.4.x`

## Step 5: Verify hosted services

If the Pi is running:
- MQTT broker
- Node-RED
- custom scripts

confirm those are reachable over the AP network.
