# MQTT Fault Checklist

## 1. Symptom capture
- [ ] Record what is failing
- [ ] Record expected topic
- [ ] Record expected payload
- [ ] Record publisher device
- [ ] Record subscriber device

## 2. Broker checks
- [ ] Broker service running
- [ ] Broker IP correct
- [ ] Broker port correct
- [ ] Broker reachable over network

## 3. Publish checks
- [ ] Publisher confirmed to send
- [ ] Topic string confirmed
- [ ] Payload confirmed

## 4. Subscribe checks
- [ ] Subscriber confirmed connected
- [ ] Subscriber confirmed on correct topic
- [ ] Message visible in test subscriber if needed

## 5. Payload interpretation
- [ ] Receiver expects same payload type
- [ ] Case and formatting confirmed
- [ ] JSON vs plain text confirmed

## 6. Reconnect / startup
- [ ] Device reconnect logic checked
- [ ] Script or service running after reboot
- [ ] Startup order considered

## 7. Conclusion
- [ ] Root cause identified
- [ ] Fix applied
- [ ] Retest completed
- [ ] Findings documented
