# Setup Steps

## Goal

Configure the Raspberry Pi to act as a standalone Wi-Fi access point with a stable local IP.

## Typical software pieces

Common AP setups on Linux-based Pi systems use:
- `hostapd` for Wi-Fi access point service
- `dnsmasq` for DHCP/DNS service

## High-level flow

### 1. Install required packages

```bash
sudo apt update
sudo apt install hostapd dnsmasq -y
```

### 2. Stop services before configuring

```bash
sudo systemctl stop hostapd
sudo systemctl stop dnsmasq
```

### 3. Give the wireless interface a static IP

A common example is:
- `192.168.4.1/24`

### 4. Configure `hostapd`

Typical things to define:
- interface
- SSID
- channel
- WPA2 passphrase

### 5. Configure `dnsmasq`

Typical things to define:
- interface
- DHCP range
- lease behavior

### 6. Enable and start the services

```bash
sudo systemctl enable hostapd
sudo systemctl enable dnsmasq
sudo systemctl start hostapd
sudo systemctl start dnsmasq
```
