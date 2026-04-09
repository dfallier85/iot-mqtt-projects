#!/bin/bash
# ap_config_example.sh
#
# Starter reference script for a Raspberry Pi AP setup.
# Adapt it to your Pi image and network manager.

set -e

echo "Updating package lists..."
sudo apt update

echo "Installing hostapd and dnsmasq..."
sudo apt install hostapd dnsmasq -y

echo "Stopping services before configuration..."
sudo systemctl stop hostapd || true
sudo systemctl stop dnsmasq || true

echo
echo "Next manual steps usually include:"
echo "1. Set static IP on wlan interface, such as 192.168.4.1/24"
echo "2. Create hostapd config with SSID and WPA2 password"
echo "3. Create dnsmasq config with DHCP range"
echo "4. Enable and start hostapd and dnsmasq"
