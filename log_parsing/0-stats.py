#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics:
"""
import re
from sys import stdin


def print_logs(regist, total_size):
    """
    Print logs
    Args:
        regist: Dictionary with the count of the status code
        total_size: Sizes of the file
    """
    print("File size: {:d}".format(total_size))
    for k, v in sorted(regist.items()):
        if v != 0:
            print("{:s}: {:d}".format(k, v))


def metrics():
    """
    Go through logs and print it
    """
    REGEX = re.compile((r'[\w\.]+ ?- ?'
                        r'\[\d{4}(-\d{2}){2}\ \d{2}(:\d{2}){2}\.\d{6}\] ?'
                        r'\"GET \/projects\/260 HTTP\/1\.1\" ?(\w+) ?(.*)'))
    regist = {
        '200': 0, '301': 0, '400': 0, '401': 0,
        '403': 0, '404': 0, '405': 0, '500': 0
    }
    total_size = 0
    quantity = 0

    try:
        for line in stdin:
            regex_result = re.search(REGEX, line)

            if (regex_result):
                groups = regex_result.groups()
                if (regist.get(groups[-2], -1) >= 0):
                    regist[groups[-2]] += 1

                if (re.search(r'^\d+$', groups[-1])):
                    total_size += int(groups[-1])

                quantity += 1

            if (quantity % 10 == 0):
                print_logs(regist, total_size)

        print_logs(regist, total_size)

    except KeyboardInterrupt:
        print_logs(regist, total_size)


if (__name__ == '__main__'):
    metrics()
