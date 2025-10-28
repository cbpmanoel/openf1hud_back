#! /usr/bin python3

import time

from telemetry_ingestor.listener import TelemetryListener
from telemetry_ingestor.parser.parser import parse_packet

from utils.network import get_default_ip_address


def telemetry_data_callback(data):
    # Print the hex representation of the data
    packet = parse_packet(data)
    print(f"Received telemetry data: {packet}")


def main():
    """
    Main entry point for the OpenF1 HUD backend application.
    """
    ip_address = get_default_ip_address()
    
    print(f"Configure your F1 game to send data to {ip_address}.")
    
    listener = TelemetryListener(data_callback=telemetry_data_callback)
    listener.start()

    print("Telemetry Listener started. Press Ctrl+C to stop the listener.")

    try:
        while True:
            time.sleep(0.1)
        
    except KeyboardInterrupt:
        listener.stop()
        print("Telemetry Listener stopped.")

if __name__ == "__main__":
    main()
