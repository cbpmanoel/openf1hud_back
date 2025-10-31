import ctypes
from .common import PacketStructureBase, MAX_CARS


class MotionData(PacketStructureBase):
    """
    Structure representing motion data for a single car.
    """
    
    _fields_ = [
        ("world_position_x", ctypes.c_float),        # World space X position - metres
        ("world_position_y", ctypes.c_float),        # World space Y position
        ("world_position_z", ctypes.c_float),        # World space Z position
        ("world_velocity_x", ctypes.c_float),        # Velocity in world space X – metres/s
        ("world_velocity_y", ctypes.c_float),        # Velocity in world space Y
        ("world_velocity_z", ctypes.c_float),        # Velocity in world space Z
        ("world_forward_dir_x", ctypes.c_int16),     # World space forward X direction (normalised)
        ("world_forward_dir_y", ctypes.c_int16),     # World space forward Y direction (normalised)
        ("world_forward_dir_z", ctypes.c_int16),     # World space forward Z direction (normalised)
        ("world_right_dir_x", ctypes.c_int16),       # World space right X direction (normalised)
        ("world_right_dir_y", ctypes.c_int16),       # World space right Y direction (normalised)
        ("world_right_dir_z", ctypes.c_int16),       # World space right Z direction (normalised)
        ("g_force_lateral", ctypes.c_float),         # Lateral G-Force component
        ("g_force_longitudinal", ctypes.c_float),    # Longitudinal G-Force component
        ("g_force_vertical", ctypes.c_float),        # Vertical G-Force component
        ("yaw", ctypes.c_float),                     # Yaw angle in radians
        ("pitch", ctypes.c_float),                   # Pitch angle in radians
        ("roll", ctypes.c_float),                    # Roll angle in radians
    ]


class PacketMotionData(PacketStructureBase):
    """
    The motion packet gives physics data for all the cars being driven.
    N.B. For the normalised vectors below, to convert to float values divide by 32767.0f - 16-bit signed
    values are used to pack the data and on the assumption that direction values are always between -1.0f
    and 1.0f.

    Frequency: Rate as specified in menus
    Size: 1349 bytes
    Version: 1
    """
    _fields_ = [
        ("car_motion_data", MotionData * MAX_CARS),  # Data for all cars on track
    ]
