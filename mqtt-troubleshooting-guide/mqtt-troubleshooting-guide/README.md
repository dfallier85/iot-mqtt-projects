# MQTT Troubleshooting Guide

A practical GitHub-style guide for finding and fixing common MQTT problems in real projects.

This repo is meant for systems involving things like:
- Raspberry Pi brokers
- Node-RED
- Jetson or Linux bridges
- ESP32 / ESP8266 devices
- robots
- PLC-adjacent status and interlock messaging

It focuses on debugging method, not just random fixes.

---

## What This Project Covers

- a repeatable MQTT troubleshooting workflow
- broker-side checks
- publisher / subscriber checks
- network checks
- topic mismatch problems
- payload mismatch problems
- startup and reconnect issues
- a checklist and reusable report template

---

## Why This Matters

MQTT failures often look vague:
- "it doesn't work"
- "the message never shows up"
- "Node-RED isn't seeing it"
- "the device stopped responding"

Most of the time, the problem is one of a small number of things:
- broker offline
- wrong IP
- wrong port
- wrong topic
- publisher not publishing
- subscriber not subscribed
- payload unexpected
- device disconnected

This repo helps narrow those down fast.

---

## Folder Structure

```text
mqtt-troubleshooting-guide/
├── README.md
├── docs/
│   ├── troubleshooting_workflow.md
│   ├── broker_checks.md
│   ├── topic_and_payload_checks.md
│   └── reconnect_and_startup_notes.md
├── checklists/
│   └── mqtt_fault_checklist.md
├── examples/
│   ├── common_failure_cases.md
│   └── terminal_test_examples.md
├── templates/
│   └── mqtt_issue_report_template.md
└── .gitignore
```

---

## Core Troubleshooting Philosophy

Do not guess.

Work through MQTT issues in layers:

1. Is the broker running?
2. Can the device reach the broker?
3. Is the publisher actually publishing?
4. Is the subscriber actually subscribed?
5. Are both sides using the same topic?
6. Is the payload what the receiver expects?
7. Is a reconnect or startup problem involved?

That structure will solve a lot of problems faster than changing five things at once.

---

## Common Failure Buckets

### Broker problem
- Mosquitto not running
- wrong broker IP
- wrong broker port
- broker unreachable over network

### Topic problem
- typo in topic name
- publisher and subscriber using different topic strings
- command sent to response topic by mistake

### Payload problem
- device expects `wave` but got `Wave`
- device expects string but receives JSON
- response format changed but UI not updated

### Device / startup problem
- ESP device never reconnected after Wi-Fi drop
- bridge script not running
- Node-RED flow deployed with old config
- startup order issue after reboot

---

## How to Use This Repo

Start with:
- `docs/troubleshooting_workflow.md`

Then review:
- `docs/broker_checks.md`
- `docs/topic_and_payload_checks.md`
- `docs/reconnect_and_startup_notes.md`

Use:
- `checklists/mqtt_fault_checklist.md`

for real troubleshooting sessions.

Examples:
- `examples/common_failure_cases.md`
- `examples/terminal_test_examples.md`

For documentation:
- `templates/mqtt_issue_report_template.md`

---

## Author Notes

This repo is intentionally practical. The goal is to help you troubleshoot MQTT systems quickly and document what was actually tested.
