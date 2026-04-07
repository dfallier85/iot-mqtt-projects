# Portable IoT Hub on Raspberry Pi

A practical GitHub-style guide for turning a Raspberry Pi into a portable Wi-Fi access point and IoT hub.

This project is useful when you want the Pi to act as a self-contained field hub for devices such as:
- ESP32
- ESP8266
- Jetson or Linux edge devices
- Node-RED dashboards
- MQTT-based robot or sensor demos

The goal is to give your devices a dedicated network instead of depending on outside Wi-Fi.

## Folder Structure

```text
portable-iot-hub-on-pi/
├── README.md
├── docs/
│   ├── architecture_overview.md
│   ├── setup_steps.md
│   ├── verification_workflow.md
│   └── integration_notes.md
├── scripts/
│   └── ap_config_example.sh
├── templates/
│   └── portable_iot_project_template.md
└── .gitignore
```

## Example Network Plan

- SSID: `ESP32-Hub`
- Password: `Tryptol1n3!`
- Pi AP IP: `192.168.4.1`

## Why This Matters

This is a clean way to make your IoT and robotics demos portable.
The Pi can become:
- the Wi-Fi network
- the MQTT broker host
- the Node-RED host
- the small local edge server
