#!/bin/bash
TOPIC="test/topic"
MESSAGE="hello from pi"
mosquitto_pub -t "$TOPIC" -m "$MESSAGE"
