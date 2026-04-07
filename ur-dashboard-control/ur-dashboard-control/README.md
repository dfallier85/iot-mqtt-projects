# UR Dashboard Control with Python

A practical guide for controlling a Universal Robots arm directly through the Dashboard Server using Python sockets.

This project skips MQTT and talks straight to the robot, which makes it a good foundational reference before adding middleware like Node-RED or MQTT.

---

## What This Project Does

- Connects to a UR robot Dashboard Server
- Sends dashboard commands over TCP
- Loads a `.urp` program
- Plays or stops the program
- Queries robot running state
- Prints robot responses in the terminal

---

## Why This Project Matters

This is one of the cleanest ways to prove you understand native UR robot control.

It shows:
- socket communication
- robot command flow
- remote program control
- practical troubleshooting foundations

---

## Folder Structure

```text
ur-dashboard-control/
├── README.md
├── python/
│   └── ur_dashboard_control.py
├── docs/
│   └── system_overview.md
└── .gitignore
```

---

## Requirements

### Hardware
- Universal Robots arm on the network

### Software
- Python 3

No external Python packages are required.

---

## Network Example

| Device | Example IP |
|---|---|
| UR Robot | `10.7.103.235` |
| Port | `29999` |

Update the IP in the script to match your robot.

---

## Dashboard Commands Used

This example includes:

- `load wave.urp`
- `play`
- `stop`
- `running`

You can expand this later with commands like:
- `robotmode`
- `programState`
- `pause`
- `power on`
- `brake release`

---

## How It Works

1. Open a TCP socket to the robot on port `29999`
2. Read the robot greeting message
3. Send a dashboard command followed by a newline
4. Read and print the robot response
5. Close the socket or keep using it for additional commands

---

## Run

```bash
python3 python/ur_dashboard_control.py
```

---

## Expected Output

You should see something like:

```text
Connected to UR Dashboard Server
Robot says: Connected: Universal Robots Dashboard Server
Sending: load wave.urp
Response: Loading program: wave.urp
Sending: play
Response: Starting program
Sending: running
Response: Program running: true
Sending: stop
Response: Stopped
```

Actual wording may vary depending on robot software version and robot state.

---

## Troubleshooting

### Connection refused
- Check robot IP
- Confirm robot is powered on
- Confirm port `29999` is reachable

### Program will not load
- Confirm the `.urp` file exists on the robot
- Check the exact filename
- Make sure the robot allows remote dashboard control in your setup

### Play does not work
- Robot may need to be in the correct mode
- A fault or protective stop may be active
- The robot may need a program loaded first

### No response or strange response
- Print the raw response from the robot
- Try sending one command at a time manually
- Confirm line endings include `\n`

---

## Expansion Ideas

- add command-line arguments for custom commands
- make an interactive shell
- add JSON logging
- integrate with MQTT or Node-RED later
- add robot state checks before play

---

## Author Notes

This repo is a simple building block for larger UR control systems. It is intentionally small and readable so it can be reused as a lab reference, a teaching example, or a starting point for more advanced robot integration work.
