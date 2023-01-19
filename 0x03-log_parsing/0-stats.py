#!/usr/bin/python3

import sys

total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split(" ")
        if len(parts) != 9:
            continue
        try:
            status_code = int(parts[8])
            file_size = int(parts[9])
            if status_code in status_codes:
                status_codes[status_code] += 1
            total_size += file_size
        except ValueError:
            continue
        if line_count % 10 == 0:
            print("Total file size:", total_size)
            for code in sorted(status_codes.keys()):
                if status_codes[code] > 0:
                    print(f"{code}: {status_codes[code]}")
except KeyboardInterrupt:
    print("Total file size:", total_size)
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

