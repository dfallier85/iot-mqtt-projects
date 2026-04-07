# Common Failure Cases

## Case 1: Button pressed, nothing happens

Possible causes:
- Node-RED published to wrong topic
- no subscriber running
- broker offline

## Case 2: Terminal subscriber works, device does not

Possible causes:
- device subscribed to wrong topic
- device disconnected from broker
- payload not recognized by firmware

## Case 3: Device worked yesterday, fails after reboot

Possible causes:
- broker IP changed
- script did not auto-start
- device did not reconnect
- startup order issue

## Case 4: Response never appears in UI

Possible causes:
- response published to wrong topic
- UI subscribed to wrong topic
- JSON / payload format not handled in UI
