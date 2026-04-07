"""
ur_dashboard_control.py

Simple Python example for controlling a Universal Robots arm
through the Dashboard Server on port 29999.

This script:
- connects to the robot
- reads the greeting
- sends a few sample commands
- prints each response

Update ROBOT_IP before running.
"""

import socket


ROBOT_IP = "10.7.103.235"
ROBOT_PORT = 29999
BUFFER_SIZE = 1024


def send_dashboard_command(sock: socket.socket, command: str) -> str:
    """
    Send one dashboard command and return the robot response.
    """
    print(f"Sending: {command}")
    sock.sendall((command + "\n").encode())
    response = sock.recv(BUFFER_SIZE).decode().strip()
    print(f"Response: {response}")
    return response


def main():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((ROBOT_IP, ROBOT_PORT))
            print("Connected to UR Dashboard Server")

            # Read the robot's initial greeting message.
            greeting = sock.recv(BUFFER_SIZE).decode().strip()
            print(f"Robot says: {greeting}")

            # Example command sequence.
            send_dashboard_command(sock, "load wave.urp")
            send_dashboard_command(sock, "play")
            send_dashboard_command(sock, "running")
            send_dashboard_command(sock, "stop")

    except Exception as exc:
        print(f"ERROR: {exc}")


if __name__ == "__main__":
    main()
