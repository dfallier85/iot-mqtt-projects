# System Architecture

## Basic Flow

```text
[Operator UI]
     ->
 [MQTT Broker]
     ->
 [AGX Router]
   /      \
  v        v
[UR]     [ABB]

[groov / PLC]
     ->
 [MQTT Broker]
     ->
 [UI status / interlock display]
```

## Main Idea

The AGX is a good place to host robot-specific bridge logic because it can run:
- Python
- socket clients
- custom adapters
- logging
- supervisory helper logic

The groov / PLC side is a good place to represent:
- machine readiness
- interlocks
- status
- faults
- operator-facing supervisory state

## Why this split works

It prevents robot-specific communication details from being buried inside the UI or PLC logic.
