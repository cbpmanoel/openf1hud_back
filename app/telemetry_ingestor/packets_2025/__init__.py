"""
Module defining the structures for parsing F1 2025 telemetry data packets.

References:
- EA SPORTS™ F1®25 UDP SPECIFICATION forum comment: https://forums.ea.com/blog/f1-games-game-info-hub-en/ea-sports%E2%84%A2-f1%C2%AE25-udp-specification/12187347
- Data Output from F1 25 v3 (PDF): https://forums.ea.com/t5/s/tghpe58374/attachments/tghpe58374/f1-games-game-info-hub-en/61/4/Data%20Output%20from%20F1%2025%20v3.pdf
"""


from .car_telemetry_packet import PacketCarTelemetryData
from .event_data_packet import PacketEventData
from .header_packet import PacketHeader
from .lap_data_packet import PacketLapData
from .motion_packet import PacketMotionData
from .participants_data_packet import PacketParticipantsData
from .session_packet import PacketSessionData


GAME_VERSION: str = "2025"


__all__ = [
    "GAME_VERSION",
    # Packet structures
    "PacketCarTelemetryData",
    "PacketEventData",
    "PacketHeader",
    "PacketLapData",
    "PacketMotionData",
    "PacketParticipantsData",
    "PacketSessionData",
]