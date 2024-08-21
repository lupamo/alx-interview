#!/usr/bin/python3

"""
UTF-8 validation module
"""


def validUTF8(data):
    """
    a method that validates a given dataset
    representing UTF-8
    """

    for byte in data:
        lsb = byte & 0xFF

        if lsb >= 128:
            return False
        elif lsb > 192:
            return False
        elif lsb > 224:
            return False
        elif lsb > 240:
            return False
    return True
