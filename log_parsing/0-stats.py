#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics:
"""
import sys
import datetime

# Inicializar variables
total_file_size = 0
status_code_counts = {}

# Leer stdin línea por línea
for i, line in enumerate(sys.stdin, 1):
    # Parsear la línea
    parts = line.split()
    if len(parts) != 10:
        continue  # Saltar líneas que no cumplen con el formato especificado

    ip_address, _, _, date, _, request, status_code, file_size = parts

    # Actualizar el total del tamaño de archivo
    total_file_size += int(file_size)

    # Actualizar el contador de códigos de estado
    if status_code.isdigit():
        status_code = int(status_code)
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1
        else:
            status_code_counts[status_code] = 1

    # Imprimir estadísticas cada 10 líneas o al interrumpir con CTRL + C
    if i % 10 == 0:
        print("File size: {}".format(total_file_size))
        for status_code in sorted(status_code_counts):
            print("{}: {}".format(status_code, status_code_counts[status_code]))

# Imprimir estadísticas finales al finalizar la lectura de stdin
print("File size: {}".format(total_file_size))
for status_code in sorted(status_code_counts):
    print("{}: {}".format(status_code, status_code_counts[status_code]))
