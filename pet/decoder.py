# -*- coding: utf-8 -*-
"""
Decodes Platform Event Trap (PET) based on IPMI Platform Event Trap Specification v1.0.

See: Chapter 17.16 in https://www.intel.com/content/dam/www/public/us/en/documents/product-briefs/ipmi-second-gen-interface-spec-v2-rev1-1.pdf
See: https://www.intel.com/content/dam/www/public/us/en/documents/product-briefs/platform-event-trap.pdf
"""
from pet.constants import *


def decode_guid(guid_bytes):
    if is_unspecified(guid_bytes):
        return None
    else:
        return {
            'time_low': guid_bytes[0:4],
            'time_mid': guid_bytes[4:6],
            'time_hi_and_version': guid_bytes[6:8],
            'clock_seq_hi_and_reserved': guid_bytes[8],
            'clock_seq_low': guid_bytes[9],
            'node': guid_bytes[10:16]
        }


def decode_sequence(sequence_number_bytes):
    sequence_number = int.from_bytes(sequence_number_bytes, byteorder='big')
    return sequence_number if not is_unspecified(sequence_number_bytes) else None


def decode_local_timestamp(local_timestamp_bytes):
    seconds = int.from_bytes(local_timestamp_bytes, byteorder='big')
    return PET_EPOCH + datetime.timedelta(seconds=seconds) if not is_unspecified(local_timestamp_bytes) else None


def decode_utc_offset(utc_offset_bytes):
    minutes = int.from_bytes(utc_offset_bytes, byteorder='big')
    return minutes if not is_unspecified(utc_offset_bytes, unspecified=0xFF) else None


def decode_source_type(source_type_byte):
    if is_unspecified(source_type_byte, 0xFF):
        return None
    else:
        for key, value in SOURCE_TYPES.items():
            if source_type_byte in key:
                return value


def decode_event_severity(severity_byte):
    return SEVERITY_TYPES[severity_byte] if not is_unspecified(severity_byte, 0x00) else None


def decode_sensor_device(sensor_device_byte):
    return sensor_device_byte if not is_unspecified(sensor_device_byte, 0xFF) else None


def decode_sensor_number(sensor_number_byte):
    return sensor_number_byte if not is_unspecified(sensor_number_byte, 0xFF) else None


# TODO
def decode_entity(entity_byte):
    return int(entity_byte)


def decode_entity_instance(entity_instance_byte):
    return entity_instance_byte if not is_unspecified(entity_instance_byte, 0xFF) else None


def decode_event_data(event_data_bytes):
    return {f'EventData{index + 1}': "0x{:02X}".format(event_data_bytes[index]) for index in range(0, 8)}


def decode_language_code(language_code_byte):
    return LANGUAGE_CODES[int(language_code_byte)]


def decode_manufacturer_id(manufacturer_id_bytes):
    manufacturer_id = int.from_bytes(manufacturer_id_bytes, byteorder='little')
    return manufacturer_id if not is_unspecified(manufacturer_id_bytes, 0xFF) else None


def decode_system_id(system_id_bytes):
    return int.from_bytes(system_id_bytes, byteorder='big')


def is_unspecified(value, unspecified=0x0):
    return all(v == unspecified for v in value) if isinstance(value, list) else value == unspecified


def from_hex_list_to_int(hex_list):
    return int(''.join(hex_list), 16)


class DecodedPETVarbind:
    """Represents decoded only one PET variable binding in 'human readable' format."""

    def __init__(self, pet_varbind):
        self.pet_varbind = pet_varbind

    def guid(self):
        return decode_guid(self.pet_varbind.guid())

    def sequence(self):
        return decode_sequence(self.pet_varbind.sequence())

    def local_timestamp(self):
        return str(decode_local_timestamp(self.pet_varbind.local_timestamp()))

    def utc_offset(self):
        return decode_utc_offset(self.pet_varbind.utc_offset())

    def trap_source_type(self):
        return decode_source_type(self.pet_varbind.trap_source_type())

    def event_source_type(self):
        return decode_source_type(self.pet_varbind.event_source_type())

    def event_severity(self):
        return decode_event_severity(self.pet_varbind.event_severity())

    def sensor_device(self):
        return decode_sensor_device(self.pet_varbind.sensor_device())

    def sensor_number(self):
        return decode_sensor_number(self.pet_varbind.sensor_number())

    def entity(self):
        return decode_entity(self.pet_varbind.entity())

    def entity_instance(self):
        return decode_entity_instance(self.pet_varbind.entity_instance())

    def event_data(self):
        return decode_event_data(self.pet_varbind.event_data())

    def language_code(self):
        return decode_language_code(self.pet_varbind.language_code())

    def manufacturer_id(self):
        return decode_manufacturer_id(self.pet_varbind.manufacturer_id())

    def system_id(self):
        return decode_system_id(self.pet_varbind.system_id())

    def oem(self):
        return self.pet_varbind.oem()

    def to_dict(self):
        return {
            'guid': self.guid(),
            'sequence': self.sequence(),
            'local_timestamp': self.local_timestamp(),
            'utc_offset': self.utc_offset(),
            'trap_source_type': self.trap_source_type(),
            'event_source_type': self.event_source_type(),
            'event_severity': self.event_severity(),
            'sensor_device': self.sensor_device(),
            'sensor_number': self.sensor_number(),
            'entity': self.entity(),
            'entity_instance': self.entity_instance(),
            'event_data': self.event_data(),
            'language_code': self.language_code(),
            'manufacturer_id': self.manufacturer_id(),
            'system_id': self.system_id(),
            'oem': self.pet_varbind.oem()
        }
