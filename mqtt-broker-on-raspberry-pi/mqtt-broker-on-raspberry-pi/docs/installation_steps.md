# Installation Steps

## 1. Update packages

```bash
sudo apt update
sudo apt upgrade -y
```

## 2. Install broker and clients

```bash
sudo apt install mosquitto mosquitto-clients -y
```

## 3. Enable on boot

```bash
sudo systemctl enable mosquitto
```

## 4. Start now

```bash
sudo systemctl start mosquitto
```

## 5. Verify

```bash
sudo systemctl status mosquitto
```

Look for:
- active (running)

## 6. Check port if needed

```bash
sudo ss -tulpn | grep 1883
```
