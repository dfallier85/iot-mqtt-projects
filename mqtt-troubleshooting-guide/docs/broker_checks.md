# Broker Checks

## Basic checks

### Service status

```bash
sudo systemctl status mosquitto
```

Look for:
- active (running)

### Port check

```bash
sudo ss -tulpn | grep 1883
```

### Restart if needed

```bash
sudo systemctl restart mosquitto
```

---

## Network checks

### Ping the broker host

```bash
ping <BROKER_IP>
```

### Try direct terminal test

Subscriber:

```bash
mosquitto_sub -h <BROKER_IP> -t test/topic
```

Publisher:

```bash
mosquitto_pub -h <BROKER_IP> -t test/topic -m "hello"
```

If this fails, fix broker reachability before debugging Node-RED, Python, or ESP code.

---

## Common broker-side problems

- service not started
- wrong IP configured in client
- wrong port configured in client
- firewall or network isolation issue
- broker moved to a new IP after reboot
