#!/usr/bin/python3

"""
UTF-8 validation module
"""


def get_bits(num):
    """returns leading sets of bits"""
    set_bits = 0
    lender = 1 << 7
    while lender & num:
        set_bits += 1
        lender = lender >> 1
    return set_bits


def validUTF8(data):
    """
    a method that validates a given dataset
    representing UTF-8
    """

    cnt = 0
    for i in range(len(data)):
        if cnt == 0:
            cnt = get_bits(data[i])
            if cnt == 0:
                continue
            if cnt == 1 or cnt > 4:
                return False
            cnt = cnt - 1
            else:
                if not (data[i] & (1 << 7) and not (data[i] & (1 << 6))):
                    return False
            cnt -= 1
    return cnt == 0
