# -*- coding: utf-8 -*-
"""PET decoder.

Usage:
  pet_decoder.py [-s byte_separator] <data>

Options:
  -s SEPARATOR, --byte-separator=SEPARATOR   Byte separator [default:  ]
  -h --help                                  Show this screen.
"""
from docopt import docopt

from pet.decoder import DecodedPETVarbind
from pet.snmp import PETVarbind

ARG_DATA = '<data>'
ARG_BYTE_SEPARATOR = '--byte-separator'


def split_bytes(bytes_string, separator):
    return bytes_string.split(separator)


if __name__ == '__main__':
    arguments = docopt(__doc__, version='PET decoder 1.0.0')
    decoded = DecodedPETVarbind(PETVarbind(split_bytes(arguments[ARG_DATA], arguments[ARG_BYTE_SEPARATOR])))
    print(decoded)
