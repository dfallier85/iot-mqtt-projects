# Topic and Payload Checks

## Topic checks

Compare publisher and subscriber side by side.

Examples of common mistakes:
- `robot/test/cmd` vs `robot/tests/cmd`
- `servo/esp32/cmd` vs `servo/esp32/command`
- `robot/ur/response` vs `robot/ur/status`

## Good habit

Copy and paste topic strings when possible.  
Do not rely on memory for long paths.

---

## Payload checks

Examples of mismatch:
- sender publishes `wave`
- receiver expects `Wave`
- sender publishes `{"command":"wave"}`
- receiver expects plain string `wave`

## Node-RED reminder

Node-RED may publish:
- string
- number
- object / JSON

Check what the downstream device actually expects.

## Practical advice

When in doubt:
1. print raw payload
2. print raw topic
3. compare against known-good expected values
