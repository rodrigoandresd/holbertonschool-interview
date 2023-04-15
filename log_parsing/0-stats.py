#!/usr/bin/python3
import sys
from collections import defaultdict

# Define the allowed status codes
ALLOWED_STATUS_CODES = [200, 301, 400, 401, 403, 404, 405, 500]

# Initialize variables to keep track of metrics
total_file_size = 0
status_code_counts = defaultdict(int)
line_count = 0

try:
    # Read input from stdin line by line
    for line in sys.stdin:
        # Extract the fields from the input line
        try:
            _, _, _, _, _, status_code, file_size = line.split()
            status_code = int(status_code)
            file_size = int(file_size)
        except ValueError:
            # Skip the line if the fields cannot be extracted properly
            continue

        # Check if the status code is allowed
        if status_code in ALLOWED_STATUS_CODES:
            # Update the total file size
            total_file_size += file_size
            # Update the status code count
            status_code_counts[status_code] += 1

        line_count += 1

        # Print statistics after every 10 lines
        if line_count % 10 == 0:
            print("File size: {}".format(total_file_size))
            for code in sorted(status_code_counts.keys()):
                print("{}: {}".format(code, status_code_counts[code]))

except KeyboardInterrupt:
    # Handle keyboard interruption (CTRL + C)
    pass

# Print final statistics after keyboard interruption
print("File size: {}".format(total_file_size))
for code in sorted(status_code_counts.keys()):
    print("{}: {}".format(code, status_code_counts[code]))
