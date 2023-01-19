#!/usr/bin/python3

import sys
from collections import defaultdict

status_codes = defaultdict(int)
file_size = 0

def print_stats():
    print("File size:", file_size)
    for code, count in status_codes.items():
        if count > 0:
            print(code + ":", count)

for line in sys.stdin:
    parts = line.split(" ")
    try:
        status_code = parts[-2]
        file_size += int(parts[-1])
        status_codes[status_code] += 1
    except:
        pass
    if sum(status_codes.values()) % 10 == 0:
        print_stats()

print_stats()
