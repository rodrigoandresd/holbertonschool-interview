#!/usr/bin/python3
"""
Given a number n this method calculates the fewest number of operations needed
to result in exactly n H characters in the file.
"""


def minOperations(n):
    """method that calculates the fewest number of operations needed"""
    if n <= 1 or type(n) is not int:
        return 0

    count = 0
    i = 2
    while i <= n:
        if n % i == 0:
            count += i
            n /= i
        else:
            i += 1

    return count
