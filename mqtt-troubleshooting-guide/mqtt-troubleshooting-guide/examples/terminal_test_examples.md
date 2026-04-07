# Terminal Test Examples

## Basic publish / subscribe test

Subscriber:

```bash
mosquitto_sub -h <BROKER_IP> -t test/topic
```

Publisher:

```bash
mosquitto_pub -h <BROKER_IP> -t test/topic -m "hello"
```

## Test a real command topic

Subscriber:

```bash
mosquitto_sub -h <BROKER_IP> -t servo/esp32/cmd
```

Publisher:

```bash
mosquitto_pub -h <BROKER_IP> -t servo/esp32/cmd -m "wave"
```

## Test a response topic

Subscriber:

```bash
mosquitto_sub -h <BROKER_IP> -t robot/ur/response
```

Publisher:

```bash
mosquitto_pub -h <BROKER_IP> -t robot/ur/response -m "wave complete"
```

## Why this helps

These tests separate MQTT transport problems from app logic problems.
