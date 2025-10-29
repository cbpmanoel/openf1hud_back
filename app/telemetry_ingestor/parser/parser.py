"""
Module defining the structures for parsing F1 2025 telemetry data packets.

References:
- EA SPORTS™ F1®25 UDP SPECIFICATION forum comment: https://forums.ea.com/blog/f1-games-game-info-hub-en/ea-sports%E2%84%A2-f1%C2%AE25-udp-specification/12187347
- Data Output from F1 25 v3 (PDF): https://forums.ea.com/t5/s/tghpe58374/attachments/tghpe58374/f1-games-game-info-hub-en/61/4/Data%20Output%20from%20F1%2025%20v3.pdf
"""

from enum import IntEnum
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

