# Payload Strategy

## Start simple

For small systems, plain strings are fine.

Examples:
- `wave`
- `home`
- `stop`
- `connected`

That is often enough for:
- quick testing
- demos
- single-device systems

---

## Move to JSON when needed

Switch to JSON when you need:
- metadata
- IDs
- timestamps
- richer error reporting
- structured state data

Example:

```json
{
  "command": "home",
  "source": "nodered",
  "timestamp": "2026-04-07T10:30:00"
}
```

Example response:

```json
{
  "result": "ok",
  "detail": "home complete"
}
```

---

## Practical advice

Do not jump to JSON for everything on day one.

But do not stay on ambiguous string payloads once the system gets more complex.

Use the simplest payload that still keeps the system understandable.
