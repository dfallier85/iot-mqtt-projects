# Deployment Example

## Example network roles

### Raspberry Pi
- hosts MQTT broker
- IP example: `192.168.4.1`

### AGX
- runs Python robot router
- subscribes to robot command topics
- publishes robot responses

### groov device
- publishes supervisory machine state
- may host or feed UI data depending on setup

### Node-RED
- sends operator commands
- displays responses, faults, and status

## Example startup order

1. broker starts
2. AGX bridge starts
3. groov / PLC status publisher starts
4. UI connects
5. operator sends commands
