"""
Contains classes representing various PETs' attributes and methods for their manipulation.
"""


def byte_list(fun):
    def wrapper(*args):
        result = fun(*args)
        if isinstance(result, list):
            return list(map(lambda s: int(s, 16), result))
        else:
            return int(result, 16)

    return wrapper


class PETVarbind:
    """Represents PET only one variable binding value in bytes as described in PET specification Table 3"""

    def __init__(self, pet_bytes):
        self.bytes = pet_bytes

    @byte_list
    def guid(self):
        return self.bytes[0:16]

    @byte_list
    def sequence(self):
        return self.bytes[16:18]

    @byte_list
    def local_timestamp(self):
        return self.bytes[18:22]

    @byte_list
    def utc_offset(self):
        return self.bytes[22:24]

    @byte_list
    def trap_source_type(self):
        return self.bytes[24]

    @byte_list
    def event_source_type(self):
        return self.bytes[25]

    @byte_list
    def event_severity(self):
        return self.bytes[26]

    @byte_list
    def sensor_device(self):
        return self.bytes[27]

    @byte_list
    def sensor_number(self):
        return self.bytes[28]

    @byte_list
    def entity(self):
        return self.bytes[29]

    @byte_list
    def entity_instance(self):
        return self.bytes[30]

    @byte_list
    def event_data(self):
        return self.bytes[31:39]

    @byte_list
    def language_code(self):
        return self.bytes[39]

    @byte_list
    def manufacturer_id(self):
        return self.bytes[40:44]

    @byte_list
    def system_id(self):
        return self.bytes[44:46]

    @byte_list
    def oem(self):
        return self.bytes[46:]
