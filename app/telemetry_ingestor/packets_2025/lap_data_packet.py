import ctypes
from enum import IntEnum
from .common import PacketStructureBase, MAX_CARS


class PIT_STATUS(IntEnum):
    """
    Enumeration for pit status.
    """
    NONE = 0
    PITTING = 1
    IN_PIT_AREA = 2


class CURRENT_SECTOR(IntEnum):
    """
    Enumeration for current sector.
    """
    SECTOR1 = 0
    SECTOR2 = 1
    SECTOR3 = 2


class CURRENT_LAP_VALIDITY(IntEnum):
    """
    Enumeration for current lap validity.
    """
    VALID = 0
    INVALID = 1


class DRIVER_STATUS(IntEnum):
    """
    Enumeration for driver status.
    """
    IN_GARAGE = 0
    FLYING_LAP = 1
    IN_LAP = 2
    OUT_LAP = 3
    ON_TRACK = 4


class RESULT_STATUS(IntEnum):
    """
    Enumeration for result status.
    """
    INVALID = 0
    INACTIVE = 1
    ACTIVE = 2
    FINISHED = 3
    DID_NOT_FINISH = 4
    DISQUALIFIED = 5
    NOT_CLASSIFIED = 6
    RETIRED = 7


class PITLANE_TIMER_ACTIVE(IntEnum):
    """
    Enumeration for pit lane timer active status.
    """
    INACTIVE = 0
    ACTIVE = 1
    


class LapData(PacketStructureBase):
    """
    Structure representing lap data for a single car.
    """

    _fields_ = [
        ("last_lap_time_in_ms", ctypes.c_uint32),               # Last lap time in milliseconds
        ("current_lap_time_in_ms", ctypes.c_uint32),            # Current time around the lap in milliseconds
        ("sector1_time_ms_part", ctypes.c_uint16),              # Sector 1 time milliseconds part
        ("sector1_time_minutes_part", ctypes.c_uint8),          # Sector 1 whole minute part
        ("sector2_time_ms_part", ctypes.c_uint16),              # Sector 2 time milliseconds part
        ("sector2_time_minutes_part", ctypes.c_uint8),          # Sector 2 whole minute part
        ("delta_to_car_in_front_ms_part", ctypes.c_uint16),     # Time delta to car in front milliseconds part
        ("delta_to_car_in_front_minutes_part", ctypes.c_uint8), # Time delta to car in front whole minute part
        ("delta_to_race_leader_ms_part", ctypes.c_uint16),      # Time delta to race leader milliseconds part
        ("delta_to_race_leader_minutes_part", ctypes.c_uint8),  # Time delta to race leader whole minute part
        ("lap_distance", ctypes.c_float),                       # Distance vehicle is around current lap in metres - could be negative if line hasn’t been crossed yet
        ("total_distance", ctypes.c_float),                     # Total distance travelled in session in metres - could be negative if line hasn’t been crossed yet
        ("safety_car_delta", ctypes.c_float),                   # Delta in seconds for safety car
        ("car_position", ctypes.c_uint8),                       # Car race position
        ("current_lap_num", ctypes.c_uint8),                    # Current lap number
        ("pit_status", ctypes.c_uint8),                         # Pit status (PIT_STATUS)
        ("num_pit_stops", ctypes.c_uint8),                      # Number of pit stops taken in this race
        ("sector", ctypes.c_uint8),                             # Current sector (CURRENT_SECTOR)
        ("current_lap_invalid", ctypes.c_uint8),                # Whether the current lap is invalid (CURRENT_LAP_VALIDITY)
        ("penalties", ctypes.c_uint8),                          # Accumulated time penalties in seconds to be added
        ("total_warnings", ctypes.c_uint8),                     # Accumulated number of warnings issued
        ("corner_cutting_warnings", ctypes.c_uint8),            # Accumulated number of corner cutting warnings issued
        ("num_unserved_drive_through_pens", ctypes.c_uint8),    # Num drive through pens left to serve
        ("num_unserved_stop_go_pens", ctypes.c_uint8),          # Num stop go pens left to serve
        ("grid_position", ctypes.c_uint8),                      # Grid position the vehicle started the race in
        ("driver_status", ctypes.c_uint8),                      # Status of driver (DRIVER_STATUS)
        ("result_status", ctypes.c_uint8),                      # Result status (RESULT_STATUS)
        ("pit_lane_timer_active", ctypes.c_uint8),              # Whether pit lane timing is active (PITLANE_TIMER_ACTIVE)
        ("pit_lane_time_in_lane_in_ms", ctypes.c_uint16),       # If active, the current time spent in the pit lane in ms
        ("pit_stop_timer_in_ms", ctypes.c_uint16),              # Time of the actual pit stop in ms
        ("pit_stop_should_serve_pen", ctypes.c_uint8),          # Whether the car should serve a penalty at this stop
        ("speed_trap_fastest_speed", ctypes.c_float),           # Fastest speed through speed trap for this car in kmph
        ("speed_trap_fastest_lap", ctypes.c_uint8),             # Lap no the fastest speed was achieved, 255 = not set
    ]
    
    
class PacketLapData(PacketStructureBase):
    """
    The lap data packet gives details of all the cars in the session.

    Frequency: Rate as specified in menus
    Size: 1285 bytes
    Version: 1
    """

    _fields_ = [
        ("lap_data", LapData * MAX_CARS),               # Lap data for all cars on track
        ("time_trial_pb_car_index", ctypes.c_uint8),    # Index of personal best car in time trial (255 if invalid)
        ("time_trial_rival_car_index", ctypes.c_uint8), # Index of rival car in time trial (255 if invalid)
    ]