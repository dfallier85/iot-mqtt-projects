# Troubleshooting Workflow

## Goal

Find the cause of an MQTT issue without making random changes.

## Step 1: Define the symptom clearly

Start with facts:
- What is not working?
- Who is supposed to publish?
- Who is supposed to subscribe?
- What exact topic is involved?
- What exact payload is expected?
- Did it ever work before?

Write the symptom down.

---

## Step 2: Check the broker first

Before blaming devices, confirm:
- broker service is running
- broker IP is correct
- broker port is correct
- network path is valid

If the broker is down, everything above it will fail.

---

## Step 3: Prove publish independently

Use a terminal or test node to prove that a message is actually being published.

Do not assume the app is publishing just because a button was pressed.

---

## Step 4: Prove subscribe independently

Use a terminal or separate subscriber to prove that the expected topic is being watched.

Do not assume the subscriber is listening to the right topic.

---

## Step 5: Compare topic strings exactly

MQTT topic mismatches are one of the most common problems.

Check:
- spelling
- slashes
- uppercase vs lowercase
- `cmd` vs `response`
- extra device names in the path

---

## Step 6: Check payload expectations

Examples:
- sender publishes `wave`
- receiver expects `WAVE`
- sender publishes JSON
- receiver only handles plain text
- Node-RED debug shows payload, but script rejects it

---

## Step 7: Check reconnect / startup behavior

A lot of systems fail only after reboot or Wi-Fi drop.

Ask:
- did the device reconnect?
- did the Python bridge restart?
- did Node-RED come up with the correct broker settings?
- did service startup order matter?

---

## Step 8: State the conclusion cleanly

Use statements like:
- broker was offline
- topic mismatch found between publisher and subscriber
- subscriber was listening on wrong topic
- payload format mismatch caused command rejection
- device failed to reconnect after network interruption
