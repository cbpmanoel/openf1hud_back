from typing import Type

from .packets.common import PacketID, PacketStructureBase
from .packets.header import PacketHeader
from .packets.event_data import PacketEventData


PACKET_STRUCTURE_MAPPING: dict[PacketID, Type[PacketStructureBase]] = {
    PacketID.EVENT: PacketEventData,
}


def parse_packet(data: bytes):
    """
    Parse the packet header from the given data bytes.
    """
    header = PacketHeader.from_buffer_copy(data)

    try:
        id = PacketID(header.packet_id)
        packet_data = _from_mapping(id, data)
    except ValueError:
        raise ValueError(f"Unknown PacketID: {header.packet_id}")
    except NotImplementedError:
        raise NotImplementedError(f"No parser implemented for PacketID {header.packet_id}")
    
    return packet_data


def _from_mapping(id: PacketID, data: bytes) -> PacketStructureBase:
    """
    Helper function to create a packet structure instance from the mapping.
    """
    packet_class = PACKET_STRUCTURE_MAPPING.get(id)
    if not packet_class:
        raise NotImplementedError(f"No parser implemented for PacketID {id}")

    return packet_class.from_buffer_copy(data)
