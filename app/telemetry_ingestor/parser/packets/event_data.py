import ctypes
from enum import StrEnum
from .common import PacketStructureBase


class EventDataFastestLap(PacketStructureBase):
    """
    Structure representing the event data for a fastest lap event.
    """
    _fields_ = [
        ("vehicle_idx", ctypes.c_uint8),    # Vehicle index of car achieving fastest lap
        ("lap_time", ctypes.c_float),       # Lap time is in seconds
    ]


class EventDataRetirement(PacketStructureBase):
    """
    Structure representing the event data for a retirement event.
    """
    RETIREMENT_REASON = {
        0: "Invalid",
        1: "Retired",
        2: "Finished",
        3: "Terminal Damage",
        4: "Inactive",
        5: "Not Enough Laps Completed",
        6: "Black Flagged",
        7: "Red Flagged",
        8: "Mechanical Failure",
        9: "Session Skipped",
        10: "Session Simulated"
    }

    _fields_ = [
        ("vehicle_idx", ctypes.c_uint8),    # Vehicle index of car retiring
        ("reason", ctypes.c_uint8),         # Reason for retirement
    ]

    def get_reason(self) -> str:
        return self.RETIREMENT_REASON.get(self.reason, "Unknown")


class EventDataDRSDisabled(PacketStructureBase):
    """
    Structure representing the event data for a DRS disabled event.
    """
    DRS_DISABLE_REASON = {
        0: "Wet Track",
        1: "Safety Car Deployed",
        2: "Red Flag",
        3: "Min Lap Not Reached"
    }

    _fields_ = [
        ("reason", ctypes.c_uint8),  # Vehicle index of car DRS disabled for
    ]


class EventDataRaceWinner(PacketStructureBase):
    """
    Structure representing the event data for a race winner event.
    """
    _fields_ = [
        ("vehicle_idx", ctypes.c_uint8),  # Vehicle index of the race winner
    ]


class EventDataPenalty(PacketStructureBase):
    """
    Structure representing the event data for a penalty issued event.
    """
    PENALTY_TYPES = {
        0: "Drive Through",
        1: "Stop Go",
        2: "Grid Penalty",
        3: "Penalty Reminder",
        4: "Time Penalty",
        5: "Warning",
        6: "Disqualified",
        7: "Removed from Formation Lap",
        8: "Parked Too Long Timer",
        9: "Tyre Regulations",
        10: "This Lap Invalidated",
        11: "This and Next Lap Invalidated",
        12: "This Lap Invalidated Without Reason",
        13: "This and Next Lap Invalidated Without Reason",
        14: "This and Previous Lap Invalidated",
        15: "This and Previous Lap Invalidated Without Reason",
        16: "Retired",
        17: "Black Flag Timer"
    }

    INFRINGEMENT_TYPES = {
        0: "Blocking By Slow Driving",
        1: "Blocking By Wrong Way Driving",
        2: "Reversing Off The Start Line",
        3: "Big Collision",
        4: "Small Collision",
        5: "Collision Failed To Hand Back Position Single",
        6: "Collision Failed To Hand Back Position Multiple",
        7: "Corner Cutting Gained Time",
        8: "Corner Cutting Overtake Single",
        9: "Corner Cutting Overtake Multiple",
        10: "Crossed Pit Exit Lane",
        11: "Ignoring Blue Flags",
        12: "Ignoring Yellow Flags",
        13: "Ignoring Drive Through",
        14: "Too Many Drive Throughs",
        15: "Drive Through Reminder Serve Within N Laps",
        16: "Drive Through Reminder Serve This Lap",
        17: "Pit Lane Speeding",
        18: "Parked For Too Long",
        19: "Ignoring Tyre Regulations",
        20: "Too Many Penalties",
        21: "Multiple Warnings",
        22: "Approaching Disqualification",
        23: "Tyre Regulations Select Single",
        24: "Tyre Regulations Select Multiple",
        25: "Lap Invalidated Corner Cutting",
        26: "Lap Invalidated Running Wide",
        27: "Corner Cutting Ran Wide Gained Time Minor",
        28: "Corner Cutting Ran Wide Gained Time Significant",
        29: "Corner Cutting Ran Wide Gained Time Extreme",
        30: "Lap Invalidated Wall Riding",
        31: "Lap Invalidated Flashback Used",
        32: "Lap Invalidated Reset To Track",
        33: "Blocking The Pitlane",
        34: "Jump Start",
        35: "Safety Car To Car Collision",
        36: "Safety Car Illegal Overtake",
        37: "Safety Car Exceeding Allowed Pace",
        38: "Virtual Safety Car Exceeding Allowed Pace",
        39: "Formation Lap Below Allowed Speed",
        40: "Formation Lap Parking",
        41: "Retired Mechanical Failure",
        42: "Retired Terminally Damaged",
        43: "Safety Car Falling Too Far Back",
        44: "Black Flag Timer",
        45: "Unserved Stop Go Penalty",
        46: "Unserved Drive Through Penalty",
        47: "Engine Component Change",
        48: "Gearbox Change",
        49: "Parc Fermé Change",
        50: "League Grid Penalty",
        51: "Retry Penalty",
        52: "Illegal Time Gain",
        53: "Mandatory Pitstop",
        54: "Attribute Assigned"
    }

    _fields_ = [
        ("penalty_type", ctypes.c_uint8),       # Penalty type
        ("infringement_type", ctypes.c_uint8),  # Infringement type
        ("vehicle_idx", ctypes.c_uint8),        # Vehicle index of the car the penalty is applied to
        ("other_vehicle_idx", ctypes.c_uint8),  # Vehicle index of the other car involved
        ("time", ctypes.c_uint8),               # Time gained, or time spent doing action in seconds
        ("lap_num", ctypes.c_uint8),            # Lap the penalty occurred on
        ("places_gained", ctypes.c_uint8),      # Number of places gained by this
    ]

    def get_penalty_type(self) -> str:
        return self.PENALTY_TYPES.get(self.penalty_type, "Unknown")

    def get_infringement_type(self) -> str:
        return self.INFRINGEMENT_TYPES.get(self.infringement_type, "Unknown")


class EventDataSpeedTrap(PacketStructureBase):
    """
    Structure representing the event data for a speed trap event.
    """

    _fields_ = [
        ("vehicle_idx", ctypes.c_uint8),                        # Vehicle index of the vehicle triggering speed trap
        ("speed", ctypes.c_float),                              # Top speed achieved in kilometres per hour
        ("is_overall_fastest_in_session", ctypes.c_uint8),      # Overall fastest speed in session = 1, otherwise 0
        ("is_driver_fastest_in_session", ctypes.c_uint8),       # Fastest speed for driver in session = 1, otherwise 0
        ("fastest_vehicle_idx_in_session", ctypes.c_uint8),     # Vehicle index of the vehicle that is the fastest
        ("fastest_speed_in_session", ctypes.c_float),           # Speed of the vehicle that is the fastest in this session
    ]


class EventDataStartLights(PacketStructureBase):
    """
    Structure representing the event data for the start lights.
    """
    _fields_ = [
        ("num_lights", ctypes.c_uint8),  # Number of lights showing
    ]


class EventDataDriveThroughPenaltyServed(PacketStructureBase):
    """
    Structure representing the event data for a drive through penalty served event.
    """

    _fields_ = [
        ("vehicle_idx", ctypes.c_uint8),  # Vehicle index of the vehicle serving drive through
    ]


class EventDataStopGoPenaltyServed(PacketStructureBase):
    """
    Structure representing the event data for a stop go penalty served event.
    """
    _fields_ = [
        ("vehicle_idx", ctypes.c_uint8),    # Vehicle index of the vehicle serving stop go
        ("stop_time", ctypes.c_float),      # Time spent serving stop go in seconds
    ]


class EventDataFlashback(PacketStructureBase):
    """
    Structure representing the event data for a flashback event.
    """

    _fields_ = [
        ("flashback_frame_identifier", ctypes.c_uint32),    # Frame identifier flashed back to
        ("flashback_session_time", ctypes.c_float),         # Session time flashed back to
    ]


class EventDataButtons(PacketStructureBase):
    """
    Structure representing the event data for button presses.
    """
    BUTTON_FLAGS = {
        0x00000001: "Cross or A",
        0x00000002: "Triangle or Y",
        0x00000004: "Circle or B",
        0x00000008: "Square or X",
        0x00000010: "D-pad Left",
        0x00000020: "D-pad Right",
        0x00000040: "D-pad Up",
        0x00000080: "D-pad Down",
        0x00000100: "Options or Menu",
        0x00000200: "L1 or LB",
        0x00000400: "R1 or RB",
        0x00000800: "L2 or LT",
        0x00001000: "R2 or RT",
        0x00002000: "Left Stick Click",
        0x00004000: "Right Stick Click",
        0x00008000: "Right Stick Left",
        0x00010000: "Right Stick Right",
        0x00020000: "Right Stick Up",
        0x00040000: "Right Stick Down",
        0x00080000: "Special",
        0x00100000: "UDP Action 1",
        0x00200000: "UDP Action 2",
        0x00400000: "UDP Action 3",
        0x00800000: "UDP Action 4",
        0x01000000: "UDP Action 5",
        0x02000000: "UDP Action 6",
        0x04000000: "UDP Action 7",
        0x08000000: "UDP Action 8",
        0x10000000: "UDP Action 9",
        0x20000000: "UDP Action 10",
        0x40000000: "UDP Action 11",
        0x80000000: "UDP Action 12",
    }
    
    _fields_ = [
        ("button_status", ctypes.c_uint32),  # Bit flags specifying which buttons are being pressed
    ]
    
    def get_pressed_buttons(self) -> list[str]:
        pressed = [f"{name}" for flag, name in self.BUTTON_FLAGS.items() if self.button_status & flag]
        return pressed


class EventDataOvertake(PacketStructureBase):
    """
    Structure representing the event data for an overtake event.
    """
    _fields_ = [
        ("overtaking_vehicle_idx", ctypes.c_uint8),         # Vehicle index of the vehicle overtaking
        ("being_overtaken_vehicle_idx", ctypes.c_uint8),    # Vehicle index of the vehicle being overtaken
    ]


class EventDataSafetyCar(PacketStructureBase):
    """
    Structure representing the event data for a safety car event.
    """
    SAFETY_CAR_TYPES = {
        0: "No Safety Car",
        1: "Full Safety Car",
        2: "Virtual Safety Car",
        3: "Formation Lap Safety Car"
    }

    EVENT_TYPES = {
        0: "Deployed",
        1: "Returning",
        2: "Returned",
        3: "Resume Race"
    }

    _fields_ = [
        ("safety_car_type", ctypes.c_uint8),    # Type of safety car deployment
        ("event_type", ctypes.c_uint8),         # Event type
    ]


class EventDataCollision(PacketStructureBase):
    """ 
    Structure representing the event data for a collision event.
    """

    _fields_ = [
        ("vehicle1_idx", ctypes.c_uint8),  # Vehicle index of the first vehicle involved in the collision
        ("vehicle2_idx", ctypes.c_uint8),  # Vehicle index of the second vehicle involved in the collision
    ]


################################################################


class EventStringCode(StrEnum):
    """
    Enumeration of event string codes for F1 2025 telemetry data events.
    Each code represents a specific event that can occur.
    """
    SESSION_STARTED = "SSTA"        # Sent when the session starts
    SESSION_ENDED = "SEND"          # Sent when the session ends
    FASTEST_LAP = "FTLP"            # When a driver achieves the fastest lap
    RETIREMENT = "RTMT"             # When a driver retires
    DRS_ENABLED = "DRSE"            # Race control have enabled DRS
    DRS_DISABLED = "DRSD"           # Race control have disabled DRS
    TEAM_MATE_IN_PITS = "TMPT"      # Your team mate has entered the pits
    CHEQUERED_FLAG = "CHQF"         # The chequered flag has been waved
    RACE_WINNER = "RCWN"            # The race winner is announced
    PENALTY_ISSUED = "PENA"         # A penalty has been issued - details in event
    SPEED_TRAP_TRIGGERED = "SPTP"   # Speed trap has been triggered by fastest speed
    START_LIGHTS = "STLG"           # Start lights - number shown
    LIGHTS_OUT = "LGOT"             # Lights out
    DRIVE_THROUGH_SERVED = "DTSV"   # Drive through penalty served
    STOP_GO_SERVED = "SGSV"         # Stop go penalty served
    FLASHBACK = "FLBK"              # Flashback activated
    BUTTON_STATUS = "BUTN"          # Button status changed
    RED_FLAG = "RDFL"               # Red flag shown
    OVERTAKE = "OVTK"               # Overtake occurred
    SAFETY_CAR = "SCAR"             # Safety car event - details in event
    COLLISION = "COLL"              # Collision between two vehicles has occurred


EVENT_DATA_STRUCTURES_MAPPING = {
    EventStringCode.FASTEST_LAP: EventDataFastestLap,
    EventStringCode.RETIREMENT: EventDataRetirement,
    EventStringCode.DRS_DISABLED: EventDataDRSDisabled,
    EventStringCode.RACE_WINNER: EventDataRaceWinner,
    EventStringCode.PENALTY_ISSUED: EventDataPenalty,
    EventStringCode.SPEED_TRAP_TRIGGERED: EventDataSpeedTrap,
    EventStringCode.START_LIGHTS: EventDataStartLights,
    EventStringCode.DRIVE_THROUGH_SERVED: EventDataDriveThroughPenaltyServed,
    EventStringCode.STOP_GO_SERVED: EventDataStopGoPenaltyServed,
    EventStringCode.FLASHBACK: EventDataFlashback,
    EventStringCode.BUTTON_STATUS: EventDataButtons,
    EventStringCode.OVERTAKE: EventDataOvertake,
    EventStringCode.SAFETY_CAR: EventDataSafetyCar,
    EventStringCode.COLLISION: EventDataCollision,
}


class PacketEventData(PacketStructureBase):
    """
    Structure representing the event data packet for F1 2025 telemetry data.
    
    Frequency: When the event occurs
    Size: 45 bytes (29 bytes header + 4 bytes event code + 12 bytes event data)
    Version: 1
    """
    _fields_ = [
        ("event_string_code", ctypes.c_char * 4),   # Event string code
        ("event_data", ctypes.c_uint8 * 12),        # Event data - structure depends on event type
    ]
    
    def interpret_event_payload(self) -> 'PacketStructureBase':
        """
        Interpret the event data based on the event string code.

        Returns:
            PacketStructureBase: The interpreted event data structure.
        """
        event_code = self.event_string_code.decode('utf-8')
        
        if event_code in EVENT_DATA_STRUCTURES_MAPPING:
            event_data_class = EVENT_DATA_STRUCTURES_MAPPING[event_code]
            raw_data = bytes(self.event_data)
            return event_data_class.from_buffer_copy(raw_data)
        
        raise NotImplementedError(f"Event data structure for event code {event_code} not implemented.")
