#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics:
"""


import sys
from collections import defaultdict
import re


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
    # Expresión regular para analizar las líneas de logs
    REGEX = re.compile((r'[\w\.]+ ?- ?'
                        r'\[\d{4}(-\d{2}){2}\ \d{2}(:\d{2}){2}\.\d{6}\] ?'
                        r'\"GET \/projects\/260 HTTP\/1\.1\" ?(\w+) ?(.*)'))
    # Diccionario para almacenar las estadísticas de los códigos de estado
    regist = {
        '200': 0, '301': 0, '400': 0, '401': 0,
        '403': 0, '404': 0, '405': 0, '500': 0
    }
    total_size = 0
    quantity = 0

    try:
        # Leer líneas de logs de la entrada estándar (stdin)
        for line in sys.stdin:
            regex_result = re.search(REGEX, line)

            if (regex_result):
                groups = regex_result.groups()
                if (regist.get(groups[-2], -1) >= 0):
                    regist[groups[-2]] += 1

                if (re.search(r'^\d+$', groups[-1])):
                    total_size += int(groups[-1])

                quantity += 1

            # Imprimir las estadísticas cada 10 líneas de logs procesadas
            if (quantity % 10 == 0):
                print_logs(regist, total_size)

        # Imprimir las estadísticas al final del procesamiento de logs
        print_logs(regist, total_size)

    except KeyboardInterrupt:
        # Manejar la interrupción del teclado y imprimir las estadísticas actuales
        print_logs(regist, total_size)


if (__name__ == '__main__'):
    metrics()
