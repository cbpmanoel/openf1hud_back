import ctypes
from enum import IntEnum
from .common import PacketStructureBase

#TODO: Find a good way to return enums/raw values

class ZONE_FLAG(IntEnum):
    """
    Enumeration for marshal zone flags.
    """
    INVALID = -1
    NONE = 0
    GREEN = 1
    BLUE = 2
    YELLOW = 3


class SESSION_TYPE(IntEnum):
    """
    Enumeration for different session types.
    """
    UNKNOWN = 0
    PRACTICE_1 = 1
    PRACTICE_2 = 2
    PRACTICE_3 = 3
    SHORT_PRACTICE = 4
    QUALIFYING_1 = 5
    QUALIFYING_2 = 6
    QUALIFYING_3 = 7
    SHORT_QUALIFYING = 8
    ONE_SHOT_QUALIFYING = 9
    SPRINT_SHOOTOUT_1 = 10
    SPRINT_SHOOTOUT_2 = 11
    SPRINT_SHOOTOUT_3 = 12
    SHORT_SPRINT_SHOOTOUT = 13
    ONE_SHOT_SPRINT_SHOOTOUT = 14
    RACE = 15
    RACE_2 = 16
    RACE_3 = 17
    TIME_TRIAL = 18


class WEATHER_TYPE(IntEnum):
    """
    Enumeration for different weather types.
    """
    CLEAR = 0
    LIGHT_CLOUD = 1
    OVERCAST = 2
    LIGHT_RAIN = 3
    HEAVY_RAIN = 4
    STORM = 5


class TEMPERATURE_CHANGE(IntEnum):
    """
    Enumeration for temperature change types.
    """
    UP = 0
    DOWN = 1
    NO_CHANGE = 2


class FORMULA_TYPE(IntEnum):
    """
    Enumeration for different formula types.
    """
    F1_MODERN = 0
    F1_CLASSIC = 1
    F2 = 2
    F1_GENERIC = 3
    BETA = 4
    ESPORTS = 6
    F1_WORLD = 8
    F1_ELIMINATION = 9


class TRACK_ID(IntEnum):
    """
    Enumeration for different track IDs.
    """
    UNKNOWN = -1
    MELBOURNE_AU = 0
    SHANGHAI_CN = 2
    SAKHIR_BA = 3
    CATALUNYA_ES = 4
    MONACO_MC = 5
    MONTREAL_CA = 6
    SILVERSTONE_GB = 7
    HUNGARORING_HU = 9
    SPA_BE = 10
    MONZA_IT = 11
    SINGAPORE_SG = 12
    SUZUKA_JP = 13
    ABU_DHABI_AE = 14
    TEXAS_US = 15
    BRAZIL_BR = 16
    AUSTRIA_AT = 17
    MEXICO_MX = 19
    BAKU_AZ = 20
    ZANDVOORT_NL = 26
    IMOLA_IT = 27
    JEDDAH_SA = 29
    MIAMI_US = 30
    LAS_VEGAS_US = 31
    LOSAIL_QA = 32
    SILVERSTONE_REVERSE_GB = 39
    AUSTRIA_REVERSE_AT = 40
    ZANDVOORT_REVERSE_NL = 41


class SLI_PRO_NATIVE_SUPPORT(IntEnum):
    """
    Enumeration for SLI Pro native support status.
    """
    INACTIVE = 0
    ACTIVE = 1


class SAFETY_CAR_STATUS(IntEnum):
    """
    Enumeration for different safety car statuses.
    """
    NO_SAFETY_CAR = 0
    FULL_SAFETY_CAR = 1
    VIRTUAL_SAFETY_CAR = 2
    FORMATION_LAP = 3


class NETWORK_GAME_STATUS(IntEnum):
    """
    Enumeration for network game status.
    """
    OFFLINE = 0
    ONLINE = 1


class FORECAST_ACCURACY(IntEnum):
    """
    Enumeration for weather forecast accuracy.
    """
    PERFECT = 0
    APPROXIMATE = 1


class STEERING_ASSIST_LEVEL(IntEnum):
    """
    Enumeration for steering assist levels.
    """
    OFF = 0
    ON = 1


class BRAKING_ASSIST_LEVEL(IntEnum):
    """
    Enumeration for braking assist levels.
    """
    OFF = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    
    
class GEARBOX_ASSIST_LEVEL(IntEnum):
    """
    Enumeration for gearbox assist levels.
    """
    MANUAL = 1
    MANUAL_SUGGESTED = 2
    AUTOMATIC = 3
    
    
class PIT_ASSIST_LEVEL(IntEnum):
    """
    Enumeration for whether pit assist is enabled.
    """
    OFF = 0
    ON = 1


class PIT_RELEASE_ASSIST_LEVEL(IntEnum):
    """
    Enumeration for whether pit release assist is enabled.
    """
    OFF = 0
    ON = 1


class ERS_ASSIST_LEVEL(IntEnum):
    """
    Enumeration for whether ERS assist is enabled.
    """
    OFF = 0
    ON = 1


class DRS_ASSIST_LEVEL(IntEnum):
    """
    Enumeration for whether DRS assist is enabled.
    """
    OFF = 0
    ON = 1


class DYNAMIC_RACING_LINE(IntEnum):
    """
    Enumeration for dynamic racing line settings.
    """
    OFF = 0
    CORNERS_ONLY = 1
    FULL = 2
    

class DYNAMIC_RACING_LINE_TYPE(IntEnum):
    """
    Enumeration for dynamic racing line types.
    """
    LINE_2D = 0
    LINE_3D = 1


class GAME_MODE(IntEnum):
    """
    Enumeration for different game modes.
    """
    GRAND_PRIX_23 = 4
    TIME_TRIAL = 5
    SPLITSCREEN = 6
    ONLINE_CUSTOM = 7
    ONLINE_WEEKLY_EVENT = 15
    STORY_MODE_BRAKING_POINT = 17
    MY_TEAM_CAREER_25 = 27
    DRIVER_CAREER_25 = 28
    CAREER_25_ONLINE = 29
    CHALLENGE_CAREER_25 = 30
    STORY_MODE_APXGP = 75
    BENCHMARK = 127
    
    
class RULESET(IntEnum):
    """
    Enumeration for different rulesets.
    """
    PRACTICE_AND_QUALIFYING = 0
    RACE = 1
    TIME_TRIAL = 2
    ELIMINATION = 3


class SESSION_LENGTH_TYPE(IntEnum):
    """
    Enumeration for different session length types.
    """
    NONE = 0
    VERY_SHORT = 2
    SHORT = 3
    MEDIUM = 4
    MEDIUM_LONG = 5
    LONG = 6
    FULL = 7
    
    
class SPEED_UNITS(IntEnum):
    """
    Enumeration for speed units.
    """
    MPH = 0
    KPH = 1


class TEMPERATURE_UNITS(IntEnum):
    """
    Enumeration for temperature units.
    """
    CELSIUS = 0
    FAHRENHEIT = 1
    
    
class EQUAL_CAR_PERFORMANCE(IntEnum):
    """
    Enumeration for whether equal car performance is enabled.
    """
    OFF = 0
    ON = 1


class RECOVERY_MODE(IntEnum):
    """
    Enumeration for recovery modes.
    """
    NONE = 0
    FLASHBACKS = 1
    AUTO_RECOVERY = 2
    
    
class FLASHBACK_LIMIT(IntEnum):
    """
    Enumeration for flashback limits.
    """
    LOW = 0
    MEDIUM = 1
    HIGH = 2
    UNLIMITED = 3
    
    
class SURFACE_TYPE(IntEnum):
    """
    Enumeration for surface types.
    """
    SIMPLIFIED = 0
    REALISTIC = 1
    

class LOW_FUEL_MODE(IntEnum):
    """
    Enumeration for low fuel modes.
    """
    EASY = 0
    HARD = 1
    

class RACE_STARTS(IntEnum):
    """
    Enumeration for race start types.
    """
    MANUAL = 0
    ASSISTED = 1
    
    
class TYRE_TEMPERATURE(IntEnum):
    """
    Enumeration for tyre temperature settings.
    """
    SURFACE_ONLY = 0
    SURFACE_AND_CARCASS = 1
    
    
class PIT_LANE_TYRE_SIM(IntEnum):
    """
    Enumeration for pit lane tyre simulation settings.
    """
    ON = 0
    OFF = 1
    
    
class CAR_DAMAGE_LEVEL(IntEnum):
    """
    Enumeration for car damage levels.
    """
    OFF = 0
    REDUCED = 1
    STANDARD = 2
    SIMULATION = 3
    
    
class CAR_DAMAGE_RATE(IntEnum):
    """
    Enumeration for car damage rates.
    """
    REDUCED = 0
    STANDARD = 1
    SIMULATION = 2

    
class COLLISION_SETTING(IntEnum):
    """
    Enumeration for collision settings.
    """
    OFF = 0
    PLAYER_TO_PLAYER_OFF = 1
    ON = 2
    
    
class COLLISIONS_OFF_FIRST_LAP_ONLY(IntEnum):
    """
    Enumeration for collisions off for first lap only setting.
    """
    DISABLED = 0
    ENABLED = 1


class MP_UNSAFE_PIT_RELEASE(IntEnum):
    """
    Enumeration for MP unsafe pit release setting.
    """
    ON = 0
    OFF = 1


class MP_OFF_FOR_GRIEFING(IntEnum):
    """
    Enumeration for MP off for griefing setting.
    """
    OFF = 0
    ON = 1


class CORNER_CUTTING_STRINGENCY(IntEnum):
    """
    Enumeration for corner cutting stringency levels.
    """
    REGULAR = 0
    STRICT = 1


class PARC_FERME_RULES_SETTING(IntEnum):
    """
    Enumeration for whether parc ferme rules are enabled.
    """
    OFF = 0
    ON = 1


class PIT_STOP_EXPERIENCE(IntEnum):
    """
    Enumeration for pit stop experience levels.
    """
    AUTOMATIC = 0
    BROADCAST = 1
    IMMERSIVE = 2
    
    
class SAFETY_CAR_LEVEL(IntEnum):
    """
    Enumeration for safety car levels.
    """
    OFF = 0
    REDUCED = 1
    STANDARD = 2
    INCREASED = 3
    
    
class SAFETY_CAR_EXPERIENCE(IntEnum):
    """
    Enumeration for safety car experience levels.
    """
    BROADCAST = 0
    IMMERSIVE = 1
    
    
class FORMATION_LAP_SETTING(IntEnum):
    """
    Enumeration for formation lap settings.
    """
    OFF = 0
    ON = 1


class FORMATION_LAP_EXPERIENCE(IntEnum):
    """
    Enumeration for formation lap experience levels.
    """
    BROADCAST = 0
    IMMERSIVE = 1
    
    
class RED_FLAGS_LEVEL(IntEnum):
    """
    Enumeration for red flags levels.
    """
    OFF = 0
    REDUCED = 1
    STANDARD = 2
    INCREASED = 3


class AFFECTS_LICENCE_LEVEL_SOLO(IntEnum):
    """
    Enumeration for whether affects licence level in solo game is enabled.
    """
    OFF = 0
    ON = 1


class AFFECTS_LICENCE_LEVEL_MULTIPLAYER(IntEnum):
    """
    Enumeration for whether affects licence level in multiplayer is enabled.
    """
    OFF = 0
    ON = 1


class MarshalZone(PacketStructureBase):
    """
    Structure representing a marshal zone in the session.
    """

    _fields_ = [
        ("zone_start", ctypes.c_float),  # Fraction (0..1) of way through the lap the marshal zone starts
        ("zone_flag", ctypes.c_int8),    # See ZONE_FLAG enum
    ]


class WeatherForecastSample(PacketStructureBase):
    """
    Structure representing a weather forecast sample.
    """

    _fields_ = [
        ("session_type", ctypes.c_uint8),               # Session type - see SESSION_TYPE enum
        ("time_offset", ctypes.c_uint8),                # Time in minutes the forecast is for
        ("weather", ctypes.c_uint8),                    # Weather - see WEATHER_TYPE enum
        ("track_temperature", ctypes.c_int8),           # Track temp. in degrees Celsius
        ("track_temperature_change", ctypes.c_int8),    # Track temp. change - See TEMPERATURE_CHANGE enum
        ("air_temperature", ctypes.c_int8),             # Air temp. in degrees celsius
        ("air_temperature_change", ctypes.c_int8),      # Air temp. change - See TEMPERATURE_CHANGE enum
        ("rain_percentage", ctypes.c_uint8),            # Percentage chance of rain (0-100)
    ]


class PacketSessionData(PacketStructureBase):
    """
    This packet contains details about the current session in progress.

    Frequency: 2 per second
    Size: 1107 bytes
    Version: 1
    """
    
    MAX_MARSHAL_ZONES = 21
    WEATHER_FORECAST_SAMPLES = 64
    
    _fields_ = [
        ("weather", ctypes.c_uint8),                          # Weather (WEATHER_TYPE)
        ("track_temperature", ctypes.c_int8),                 # Track temp. in degrees celsius
        ("air_temperature", ctypes.c_int8),                   # Air temp. in degrees celsius
        ("total_laps", ctypes.c_uint8),                       # Total number of laps in this race
        ("track_length", ctypes.c_uint16),                    # Track length in metres
        ("session_type", ctypes.c_uint8),                     # Session type (SESSION_TYPE)
        ("track_id", ctypes.c_int8),                          # Track ID (TRACK_ID)
        ("formula", ctypes.c_uint8),                          # Formula (FORMULA_TYPE)
        ("session_time_left", ctypes.c_uint16),               # Time left in session in seconds
        ("session_duration", ctypes.c_uint16),                # Session duration in seconds
        ("pit_speed_limit", ctypes.c_uint8),                  # Pit speed limit in kilometres per hour
        ("game_paused", ctypes.c_uint8),                      # Whether the game is paused - network game only
        ("is_spectating", ctypes.c_uint8),                    # Whether the player is spectating
        ("spectator_car_index", ctypes.c_uint8),              # Index of the car being spectated
        ("sli_pro_native_support", ctypes.c_uint8),           # SLI Pro Support (SLI_PRO_NATIVE_SUPPORT)
        ("num_marshal_zones", ctypes.c_uint8),                # Number of marshal zones to follow
        ("marshal_zones", MarshalZone * MAX_MARSHAL_ZONES),   # List of marshal zones - max 21
        ("safety_car_status", ctypes.c_uint8),                # Safety Car Status (SAFETY_CAR_STATUS)
        ("network_game", ctypes.c_uint8),                     # 0 = offline, 1 = online
        ("num_weather_forecast_samples", ctypes.c_uint8),     # Number of weather samples to follow
        ("weather_forecast_samples", WeatherForecastSample * WEATHER_FORECAST_SAMPLES), # Array of weather forecast samples
        ("forecast_accuracy", ctypes.c_uint8),                # Forecast accuracy (FORECAST_ACCURACY)
        ("ai_difficulty", ctypes.c_uint8),                    # AI Difficulty rating - 0-110
        ("season_link_identifier", ctypes.c_uint32),          # Identifier for season - persists across saves
        ("weekend_link_identifier", ctypes.c_uint32),         # Identifier for weekend - persists across saves
        ("session_link_identifier", ctypes.c_uint32),         # Identifier for session - persists across saves
        ("pit_stop_window_ideal_lap", ctypes.c_uint8),        # Ideal lap to pit on for current strategy (player)
        ("pit_stop_window_latest_lap", ctypes.c_uint8),       # Latest lap to pit on for current strategy (player)
        ("pit_stop_rejoin_position", ctypes.c_uint8),         # Predicted position to rejoin at (player)
        ("steering_assist", ctypes.c_uint8),                  # Whether steering assist is enabled (STEERING_ASSIST_LEVEL)
        ("braking_assist", ctypes.c_uint8),                   # Braking assist level (BRAKING_ASSIST_LEVEL)
        ("gearbox_assist", ctypes.c_uint8),                   # Gearbox assist level (GEARBOX_ASSIST_LEVEL)
        ("pit_assist", ctypes.c_uint8),                       # Whether pit assist is enabled (PIT_ASSIST_LEVEL)
        ("pit_release_assist", ctypes.c_uint8),               # Whether pit release assist is enabled (PIT_RELEASE_ASSIST_LEVEL)
        ("ers_assist", ctypes.c_uint8),                       # Whether ERS assist is enabled (ERS_ASSIST_LEVEL)
        ("drs_assist", ctypes.c_uint8),                       # Whether DRS assist is enabled (DRS_ASSIST_LEVEL)
        ("dynamic_racing_line", ctypes.c_uint8),              # Dynamic racing line (DYNAMIC_RACING_LINE)
        ("dynamic_racing_line_type", ctypes.c_uint8),         # Dynamic racing line type (DYNAMIC_RACING_LINE_TYPE)
        ("game_mode", ctypes.c_uint8),                        # Game mode id (GAME_MODE)
        ("rule_set", ctypes.c_uint8),                         # Ruleset (RULESET)
        ("time_of_day", ctypes.c_uint32),                     # Local time of day - minutes since midnight
        ("session_length", ctypes.c_uint8),                   # Session length type (SESSION_LENGTH_TYPE)
        ("speed_units_lead_player", ctypes.c_uint8),          # Speed units (SPEED_UNITS)
        ("temperature_units_lead_player", ctypes.c_uint8),    # Temperature units (TEMPERATURE_UNITS)
        ("speed_units_secondary_player", ctypes.c_uint8),     # Speed units (SPEED_UNITS)
        ("temperature_units_secondary_player", ctypes.c_uint8),# Temperature units (TEMPERATURE_UNITS)
        ("num_safety_car_periods", ctypes.c_uint8),           # Number of safety cars called during session
        ("num_virtual_safety_car_periods", ctypes.c_uint8),   # Number of virtual safety cars called
        ("num_red_flag_periods", ctypes.c_uint8),             # Number of red flags called during session
        ("equal_car_performance", ctypes.c_uint8),            # Whether equal car performance is enabled (EQUAL_CAR_PERFORMANCE)
        ("recovery_mode", ctypes.c_uint8),                    # Recovery mode type (RECOVERY_MODE)
        ("flashback_limit", ctypes.c_uint8),                  # Flashback limit (FLASHBACK_LIMIT)
        ("surface_type", ctypes.c_uint8),                     # Surface type (SURFACE_TYPE)
        ("low_fuel_mode", ctypes.c_uint8),                    # Low fuel mode (LOW_FUEL_MODE)
        ("race_starts", ctypes.c_uint8),                      # Race starts (RACE_STARTS)
        ("tyre_temperature", ctypes.c_uint8),                 # Tyre temperature (TYRE_TEMPERATURE)
        ("pit_lane_tyre_sim", ctypes.c_uint8),                # Pit lane tyre simulation (PIT_LANE_TYRE_SIM)
        ("car_damage", ctypes.c_uint8),                       # Car damage level (CAR_DAMAGE_LEVEL)
        ("car_damage_rate", ctypes.c_uint8),                  # Car damage rate (CAR_DAMAGE_RATE)
        ("collisions", ctypes.c_uint8),                       # Collisions (COLLISION_SETTING)
        ("collisions_off_for_first_lap_only", ctypes.c_uint8), # Collisions off for first lap only (COLLISIONS_OFF_FIRST_LAP_ONLY)
        ("mp_unsafe_pit_release", ctypes.c_uint8),            # MP unsafe pit release (MP_UNSAFE_PIT_RELEASE)
        ("mp_off_for_griefing", ctypes.c_uint8),              # MP off for griefing (MP_OFF_FOR_GRIEFING)
        ("corner_cutting_stringency", ctypes.c_uint8),        # Corner cutting stringency (CORNER_CUTTING_STRINGENCY)
        ("parc_ferme_rules", ctypes.c_uint8),                 # Whether parc ferme rules are enabled (PARC_FERME_RULES)
        ("pit_stop_experience", ctypes.c_uint8),              # Pit stop experience (PIT_STOP_EXPERIENCE)
        ("safety_car", ctypes.c_uint8),                       # Safety car (SAFETY_CAR_LEVEL)
        ("safety_car_experience", ctypes.c_uint8),            # Safety car experience (SAFETY_CAR_EXPERIENCE)
        ("formation_lap", ctypes.c_uint8),                    # Whether formation lap is enabled (FORMATION_LAP_SETTING)
        ("formation_lap_experience", ctypes.c_uint8),         # Formation lap experience (FORMATION_LAP_EXPERIENCE)
        ("red_flags", ctypes.c_uint8),                        # Red flags (RED_FLAGS_LEVEL)
        ("affects_licence_level_solo", ctypes.c_uint8),       # Whether affects licence level in solo (AFFECTS_LICENSE_LEVEL_SOLO)
        ("affects_licence_level_mp", ctypes.c_uint8),         # Whether affects licence level in multiplayer (AFFECTS_LICENCE_LEVEL_MULTIPLAYER)
        ("num_sessions_in_weekend", ctypes.c_uint8),          # Number of session in following array
        ("weekend_structure", ctypes.c_uint8 * 12),           # List of session types to show weekend structure (SESSION_TYPE)
        ("sector2_lap_distance_start", ctypes.c_float),       # Distance in m around track where sector 2 starts
        ("sector3_lap_distance_start", ctypes.c_float),       # Distance in m around track where sector 3 starts
    ]
