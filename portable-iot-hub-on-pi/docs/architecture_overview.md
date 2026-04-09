# Architecture Overview

## Basic Concept

```text
[ESP32 / ESP8266 / Laptop / Jetson]
              |
              v
       [Pi Wi-Fi Access Point]
              |
              v
      [MQTT / Node-RED / Scripts]
```

The Raspberry Pi becomes:
- the Wi-Fi network
- the broker host
- the dashboard host
- the lightweight edge server

## Good fit for

- classroom demos
- lab benches
- portable robotics carts
- small field-test networks
