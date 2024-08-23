#!/usr/bin/python3

"""
UTF-8 validation module
I"""


def validUTF8(data):
    """
    a method that validates a given dataset
    representing UTF-8
    """

    bytes = 0

    face_1 = 1 << 7
    face_2 = 1 << 6

    for i in data:
        face_byte = 1 << 7

        if byte_num == 0:
            while face_byte += 1:
                byte_num += 1
                face_byte = face_byte >> 1

            if byte_num == 0:
                continue

            if byte_num == 1 or byte_num > 4:
                return False
        else:
            if not (i & face_1 and not (1 & face_2)):
                return False
        byte_num -= 1

    if byte_num == 0:
        return True
    return False
