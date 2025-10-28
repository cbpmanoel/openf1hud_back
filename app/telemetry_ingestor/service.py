from .parser.parser import parse_packet
from .listener import TelemetryListener

def telemetry_data_callback(data):
    packet = parse_packet(data)
    print(f"Received telemetry data: {packet}")

listener = TelemetryListener(data_callback=telemetry_data_callback)

def start_packet_listener_service() -> None:
    listener.start()
    
def shutdown_listener_service() -> None:
    if listener and listener.is_running():
        listener.stop()