# Reconnect and Startup Notes

## Why this matters

A system may work fine once and then fail after:
- power cycle
- Wi-Fi dropout
- broker restart
- script crash

That usually means the problem is not the command logic itself.  
It is often reconnect or startup behavior.

---

## Common cases

### ESP device does not reconnect
If the board loses Wi-Fi or MQTT, it may never come back unless reconnect logic exists in `loop()`.

### Python bridge not restarted
A script that worked manually may not be running after reboot.

### Node-RED uses old broker config
Flow imported correctly before, but broker node points to the wrong host now.

### Startup order issue
The device starts before the broker is ready, then never reconnects.

---

## Good practices

- include reconnect logic in device firmware
- make bridge scripts restartable
- document startup order
- test after reboot, not just after manual launch
- log connection events when possible
