# Wiring Notes

## Important Reminder

Do not power a larger servo directly from the microcontroller if the servo current draw is too high.

For reliable operation, many servos should use:
- external 5V supply
- shared ground between supply and microcontroller

## Basic Wiring

### Servo
- signal -> device GPIO pin
- VCC -> 5V supply
- GND -> common ground

### ESP32 / ESP8266
- powered normally by USB or appropriate regulated source
- ground tied to servo power ground

## Example pin used here

- GPIO2 / D4

That matches your earlier small-scale servo wave setup.

## Common problems

- servo jitters
- servo resets board
- servo does not move fully
- Wi-Fi drops during motion

These often come from power issues, not code issues.
