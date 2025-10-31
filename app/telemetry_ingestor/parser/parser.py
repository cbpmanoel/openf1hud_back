from dataclasses import dataclass
from typing import Type

from ..packets_2025.common import PacketID, PacketStructureBase
from ..packets_2025.header_packet import PacketHeader
from ..packets_2025.event_data_packet import PacketEventData
from ..packets_2025.car_telemetry_packet import PacketCarTelemetryData


PACKET_STRUCTURE_MAPPING: dict[PacketID, Type[PacketStructureBase]] = {
    PacketID.EVENT: PacketEventData,
    PacketID.CAR_TELEMETRY: PacketCarTelemetryData,
}

HEADER_SIZE = PacketHeader.sizeof()


@dataclass
class ParsedPacket:
    """
    Container that represents a parsed telemetry packet.
    """
    header: PacketHeader
    payload: PacketStructureBase
    
    @property
    def packet_id(self) -> PacketID:
        return PacketID(self.header.packet_id)


def parse_packet(data: bytes) -> ParsedPacket:
    """
    Parse the received data into a ParsedPacket instance.
    """
    header = PacketHeader.from_buffer_copy(data)

    try:
        id = PacketID(header.packet_id)
        packet_data = _from_mapping(id, data)
    except ValueError:
        raise ValueError(f"Unknown PacketID: {header.packet_id}")
    except NotImplementedError:
        raise NotImplementedError(f"No parser implemented for PacketID {header.packet_id}")
    
    return ParsedPacket(header=header, payload=packet_data)


def _from_mapping(id: PacketID, data: bytes) -> PacketStructureBase:
    """
    Helper function to create a packet structure instance from the mapping.
    """
    packet_class = PACKET_STRUCTURE_MAPPING.get(id)
    if not packet_class:
        raise NotImplementedError(f"No parser implemented for PacketID {id}")

    # Discard the header before parsing the payload
    return packet_class.from_buffer_copy(data[HEADER_SIZE:])
