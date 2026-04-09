# System Overview

## Basic Flow

```text
[Python Script] -> [TCP Socket :29999] -> [UR Dashboard Server]
```

## What the Dashboard Server Is

The Dashboard Server is a built-in TCP interface on Universal Robots controllers.

It allows a remote client to send plain-text commands like:
- load
- play
- stop
- running

## Why Start Here

This is the direct control layer.

Once this works reliably, you can build larger systems on top of it:
- MQTT bridges
- Node-RED dashboards
- PLC command routing
- automated test sequences
