import ctypes

class PacketStructureBase(ctypes.LittleEndianStructure):
    """
    Base class for packet structures to provide common functionality.
    """
    _pack_ = 1

    def __repr__(self):
        field_values = ', '.join(f"{field[0]}={getattr(self, field[0])}" for field in self._fields_)
        return f"{self.__class__.__name__}({field_values})"