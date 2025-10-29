import ctypes
from .common import PacketStructureBase, PacketID


HEADER_SIZE = 29  # Size of the packet header in bytes


class PacketHeader(PacketStructureBase):
    """
    Structure representing the header of an F1 2025 telemetry data packet, present in all packets.
    """

    _fields_ = [
        ("packet_format", ctypes.c_uint16),                 # 2025
        ("game_year", ctypes.c_uint8),                      # Game year - last two digits e.g. 25
        ("game_major_version", ctypes.c_uint8),             # Game major version - "X.00"
        ("game_minor_version", ctypes.c_uint8),             # Game minor version - "1.XX"
        ("packet_version", ctypes.c_uint8),                 # Version of this packet type, all start from 1
        ("packet_id", ctypes.c_uint8),                      # Identifier for the packet type
        ("session_uid", ctypes.c_uint64),                   # Unique identifier for the session
        ("session_time", ctypes.c_float),                   # Session timestamp
        ("frame_identifier", ctypes.c_uint32),              # Identifier for the frame the data was retrieved on
        ("overall_frame_identifier", ctypes.c_uint32),      # Overall identifier for the frame the data was retrieved on, doesn't go back after flashbacks
        ("player_car_index", ctypes.c_uint8),               # Index of player's car in the array
        ("secondary_player_car_index", ctypes.c_uint8),     # Index of secondary player's car in the array (splitscreen), 255 if no second player
    ]
    
    def get_packet_id(self) -> PacketID:
        """
        Get the PacketID enum for this packet header.
        """
        return PacketID(self.packet_id)
