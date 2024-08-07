#!/usr/bin/python3
"""locked boxes that can be opened"""


def minOperations(n):
    """
    Minimum operations to reach n from 1
    """

    ops = 0
    div = 2

    while n > 1:
        while n % div == 0:
            ops += div
            n //= div
        div += 1

    return ops
