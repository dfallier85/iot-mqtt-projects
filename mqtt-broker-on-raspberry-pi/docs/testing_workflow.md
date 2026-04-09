# Testing Workflow

## Step 1: Local test

Subscriber:

```bash
mosquitto_sub -t test/topic
```

Publisher:

```bash
mosquitto_pub -t test/topic -m "hello from pi"
```

## Step 2: Network test

From another machine:

```bash
mosquitto_pub -h <PI_IP_ADDRESS> -t test/topic -m "hello over network"
```

## Step 3: Reverse direction

Subscriber on another machine:

```bash
mosquitto_sub -h <PI_IP_ADDRESS> -t test/topic
```

Then publish from the Pi:

```bash
mosquitto_pub -t test/topic -m "hello from broker host"
```

## What to confirm

- broker running
- local publish works
- local subscribe works
- network devices can reach port 1883
