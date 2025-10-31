from .common import PacketStructureBase, MAX_CARS
from enum import IntEnum
import ctypes


class DRIVING_SURFACE(IntEnum):
    """
    Enumeration for different driving surface types.
    """
    TARMAC = 0
    RUMBLE_STRIP = 1
    CONCRETE = 2
    ROCK = 3
    GRAVEL = 4
    MUD = 5
    SAND = 6
    GRASS = 7
    WATER = 8
    COBBLESTONE = 9
    METAL = 10
    RIDGED = 11
    
    
class WHEEL_POSITION_INDEX(IntEnum):
    """
    Enumeration for wheel position indices.
    """
    REAR_LEFT = 0
    REAR_RIGHT = 1
    FRONT_LEFT = 2
    FRONT_RIGHT = 3


class CarTelemetryData(PacketStructureBase):
    """
    Telemetry data for a single car.   
    """
 
    _fields_ = [
        ("speed", ctypes.c_uint16),                         # Speed of car in kilometres per hour
        ("throttle", ctypes.c_float),                       # Amount of throttle applied (0.0 to 1.0)
        ("steer", ctypes.c_float),                          # Steering (-1.0 (full lock left) to 1.0 (full lock right))
        ("brake", ctypes.c_float),                          # Amount of brake applied (0.0 to 1.0)
        ("clutch", ctypes.c_uint8),                         # Amount of clutch applied (0 to 100)
        ("gear", ctypes.c_int8),                            # Gear selected (1-8, N=0, R=-1)
        ("engine_rpm", ctypes.c_uint16),                    # Engine RPM
        ("drs", ctypes.c_uint8),                            # 0 = off, 1 = on
        ("rev_lights_percent", ctypes.c_uint8),             # Rev lights indicator (percentage)
        ("rev_lights_bit_value", ctypes.c_uint16),          # Rev lights (bit 0 = leftmost LED, bit 14 = rightmost LED)
        ("brakes_temperature", ctypes.c_uint16 * 4),        # Brakes temperature (celsius)
        ("tyres_surface_temperature", ctypes.c_uint8 * 4),  # Tyres surface temperature (celsius)
        ("tyres_inner_temperature", ctypes.c_uint8 * 4),    # Tyres inner temperature (celsius)
        ("engine_temperature", ctypes.c_uint16),            # Engine temperature (celsius)
        ("tyres_pressure", ctypes.c_float * 4),             # Tyres pressure (PSI)
        ("surface_type", ctypes.c_uint8 * 4),               # Driving surface
    ]


class PacketCarTelemetryData(PacketStructureBase):
    """
    This packet details telemetry for all the cars in the race. It details various values that would be
    recorded on the car such as speed, throttle application, DRS etc. Note that the rev light configurations
    are presented separately as well and will mimic real life driver preferences.
    
    Frequency: Rate as specified in menus
    Size: 1352 bytes
    Version: 1
    """
    
    class MDF_PANEL_INDEX(IntEnum):
        """
        Enumeration for MFD (Multi-Function Display) panel indices for single player.
        May vary depending on game mode.
        """
        CLOSED = 255
        CAR_SETUP = 0
        PITS = 1
        DAMAGE = 2
        ENGINE = 3
        TEMPERATURES = 4
    
    
    _fields_ = [
        ("car_telemetry_data", CarTelemetryData * MAX_CARS),  # Array of telemetry data for all cars on track
        ("mfd_panel_index", ctypes.c_uint8),                  # Index of MFD panel open
        ("mfd_panel_index_secondary_player", ctypes.c_uint8), # Index of MFD panel open for secondary player
        ("suggested_gear", ctypes.c_int8),                    # Suggested gear for the player (1-8, 0 if no gear suggested)
    ]

    def by_car_index(self, index: int) -> CarTelemetryData:
        """
        Get the CarTelemetryData for a specific car index.
        """
        if 0 <= index < 22:
            return self.car_telemetry_data[index]
        raise IndexError("Car index out of range.")