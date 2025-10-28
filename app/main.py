#! /usr/bin python3

import time

from utils.network import get_default_ip_address
from telemetry_ingestor.service import start_packet_listener_service, shutdown_listener_service

def main():
    """
    Main entry point for the OpenF1 HUD backend application.
    """
    ip_address = get_default_ip_address()
    
    print(f"Configure your F1 game to send data to {ip_address}.")

    start_packet_listener_service()
    print("Telemetry Listener started. Press Ctrl+C to stop the listener.")

    try:
        while True:
            time.sleep(0.1)
        
    except KeyboardInterrupt:
        shutdown_listener_service()
        print("Telemetry Listener stopped.")

if __name__ == "__main__":
    main()
