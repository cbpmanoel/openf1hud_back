from .parser.parser import parse_packet

async def process_telemetry_data(data):
    packet = parse_packet(data)
    # Process the packet as needed
    print(f"Processed packet: {packet}")