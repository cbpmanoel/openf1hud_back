#! /usr/bin python3

import asyncio

from utils.network import get_default_ip_address
from telemetry_ingestor.listener import TelemetryListener
from telemetry_ingestor.service import process_telemetry_data

listener = TelemetryListener(data_callback=process_telemetry_data)

async def main():
    """
    Main entry point for the OpenF1 HUD backend application.
    """
    try:
        await listener.start()
        print("Listener started successfully. Press Ctrl+C to stop.")
        
        await asyncio.Future()  # Run until interrupted
        
    except KeyboardInterrupt:
        print("Keyboard interrupt received. Stopping listener...")
    except asyncio.CancelledError:
        print("Asyncio task was cancelled. Stopping listener...")
        
    finally:
        await listener.stop()
        print("Telemetry Listener stopped.")

if __name__ == "__main__":
    ip_address = get_default_ip_address()
    print(f"Configure your F1 game to send data to {ip_address}.")
    
    asyncio.run(main())
    print("Application exited.")
