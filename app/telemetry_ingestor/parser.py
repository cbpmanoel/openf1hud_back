import ctypes

HEADER_SIZE = 29

class PacketHeader(ctypes.LittleEndianStructure):
    _pack_ = 1
    _fields_ = [
        ("packet_format", ctypes.c_uint16),
        ("game_year", ctypes.c_uint8),
        ("game_major_version", ctypes.c_uint8),
        ("game_minor_version", ctypes.c_uint8),
        ("packet_version", ctypes.c_uint8),
        ("packet_id", ctypes.c_uint8),
        ("session_uid", ctypes.c_uint64),
        ("session_time", ctypes.c_float),
        ("frame_identifier", ctypes.c_uint32),
        ("overall_frame_identifier", ctypes.c_uint32),
        ("player_car_index", ctypes.c_uint8),
        ("secondary_player_car_index", ctypes.c_uint8),
    ]
    
    def __repr__(self):
        return (f"PacketHeader(packet_format={self.packet_format}, "
                f"game_year={self.game_year}, "
                f"game_major_version={self.game_major_version}, "
                f"game_minor_version={self.game_minor_version}, "
                f"packet_version={self.packet_version}, "
                f"packet_id={self.packet_id}, "
                f"session_uid={self.session_uid}, "
                f"session_time={self.session_time}, "
                f"frame_identifier={self.frame_identifier}, "
                f"overall_frame_identifier={self.overall_frame_identifier}, "
                f"player_car_index={self.player_car_index}, "
                f"secondary_player_car_index={self.secondary_player_car_index})")