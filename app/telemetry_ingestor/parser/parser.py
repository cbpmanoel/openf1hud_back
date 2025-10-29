from .packets.header import PacketHeader, HEADER_SIZE
from .packets.event_data import PacketEventData
from .packets.common import PacketID

    
def parse_packet(data: bytes):
    """
    Parse the packet header from the given data bytes.

    Args:
        data (bytes): The raw data bytes received from the telemetry stream.

    Returns:
        An instance of the appropriate packet data structure based on the PacketID.
    """
    header = PacketHeader.from_buffer_copy(data[:HEADER_SIZE])
    
    if header.packet_id == PacketID.EVENT:
        packet = PacketEventData.from_buffer_copy(data[HEADER_SIZE:])
        interpreted_packet = packet.unpack_event_data()
        return interpreted_packet

    raise NotImplementedError(f"Parser for PacketID {header.packet_id} not implemented.")

