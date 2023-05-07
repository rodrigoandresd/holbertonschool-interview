#!/usr/bin/python3
"""
Validate utf-8 module
"""


def validUTF8(data):
    """
    Determines if the data set represents a valid UTF-8 encoding.
    Args:
        data (list[int]): List to validate if is UTF-8 valid
    Returns:
        bool: True if data is a valid UTF-8 encoding,
        else return False
    """
    count, flag = 0, False

    for num in data:
        num = abs(num)
        # If num is inside the range 128 to 191 and
        # flag is active (a unicode of two bytes or more)
        if flag and (128 <= num <= 191):
            # One subsequent byte less
            count -= 1
            if count == 0:
                flag = False
            continue
        # if flag is active and num is not in range
        elif flag:
            return False

        # One byte
        if num < 128:
            continue
        # Two bytes
        elif num < 224:
            count = 1
        # Three bytes
        elif num < 240:
            count = 2
        # Four bytes
        elif num < 248:
            count = 3
        # Five to more bytes (invalid)
        else:
            return False

        flag = True

    return count == 0
