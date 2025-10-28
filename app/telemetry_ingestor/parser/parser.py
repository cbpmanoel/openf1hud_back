"""
Module defining the structures for parsing F1 2025 telemetry data packets.

References:
- EA SPORTS™ F1®25 UDP SPECIFICATION forum comment: https://forums.ea.com/blog/f1-games-game-info-hub-en/ea-sports%E2%84%A2-f1%C2%AE25-udp-specification/12187347
- Data Output from F1 25 v3 (PDF): https://forums.ea.com/t5/s/tghpe58374/attachments/tghpe58374/f1-games-game-info-hub-en/61/4/Data%20Output%20from%20F1%2025%20v3.pdf
"""

from enum import IntEnum
from .packets.header import PacketHeader, HEADER_SIZE
from .packets.event_data import PacketEventData

class PacketID(IntEnum):
    """
    Enumeration of packet IDs for F1 2025 telemetry data packets.
    """
    MOTION = 0                  # Contains all motion data for player’s car – only sent while player is in control
    SESSION = 1                 # Data about the session – track, time left
    LAP_DATA = 2                # Data about all the lap times of cars in the session
    EVENT = 3                   # Various events that happen during a session
    PARTICIPANTS = 4            # List of participants in the session, mostly relevant for multiplayer
    CAR_SETUPS = 5              # Packet detailing car setups for cars in the race
    CAR_TELEMETRY = 6           # Telemetry data for all cars
    CAR_STATUS = 7              # Status data for all cars
    FINAL_CLASSIFICATION = 8    # Final classification confirmation at the end of a race
    LOBBY_INFO = 9              # Information about players in a multiplayer lobby
    CAR_DAMAGE = 10             # Damage status for all cars
    SESSION_HISTORY = 11        # Lap and tyre data for session
    TYRE_SETS = 12              # Extended tyre set data
    MOTION_EX = 13              # Extended motion data for player car
    TIME_TRIAL = 14             # Time Trial specific data
    LAP_POSITIONS = 15          # Lap positions on each lap so a chart can be constructed

    def __repr__(self):
        return f"PacketID.{self.name}"
    
    def __str__(self):
        return f"PacketID.{self.name}"
    
    
def parse_packet(data: bytes):
    """
    Parse the packet header from the given data bytes.

    Args:
        data (bytes): The raw data bytes received from the telemetry stream.

    Returns:
        PacketHeader: The parsed packet header.
    """
    header = PacketHeader.from_buffer_copy(data[:HEADER_SIZE])
    
    if header.packet_id == PacketID.EVENT:
        packet = PacketEventData.from_buffer_copy(data[HEADER_SIZE:])
        interpreted_packet = packet.interpret_event_payload()
        return interpreted_packet

    raise NotImplementedError(f"Parser for PacketID {header.packet_id} not implemented.")

