import ctypes
from enum import IntEnum

MAX_CARS = 22  # Maximum number of cars in an F1 2025 session

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
    
    
class ON_OFF_SETTING(IntEnum):
    """
    Enumeration for On/Off settings.
    """
    OFF = 0
    ON = 1


class PacketStructureBase(ctypes.LittleEndianStructure):
    """
    Base class for packet structures to provide common functionality.
    """
    _pack_ = 1  # Ensure no padding is added by the compiler

    def __repr__(self):
        field_values = ', '.join(f"{field[0]}={getattr(self, field[0])}" for field in self._fields_)
        return f"{self.__class__.__name__}({field_values})"
    
    @classmethod
    def sizeof(cls):
        """
        Get the size of the structure in bytes.
        """
        return ctypes.sizeof(cls)
