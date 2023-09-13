#!/usr/bin/python3
"""
    script that reads stdin line by line and computes metrics
"""
import sys

import sys
import re
import signal

# Global variables to hold stats
total_size = 0
status_code_count = {
    200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0
}

def print_stats(signum=None, frame=None):
    """Function to print statistics"""
    global total_size, status_code_count

    print(f"Total file size: File size: {total_size}")
    for code, count in sorted(status_code_count.items()):
        if count > 0:
            print(f"{code}: {count}")

def main():
    global total_size, status_code_count

    # Register a signal handler for keyboard interruption
    signal.signal(signal.SIGINT, print_stats)

    # Regex pattern for parsing logs
    pattern = r'(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[.*\] "GET /projects/260 HTTP/1.1" (?P<status>\d{3}) (?P<size>\d+)'

    line_count = 0

    try:
        for line in sys.stdin:
            match = re.search(pattern, line)
            if match:
                size = int(match.group("size"))
                status = int(match.group("status"))

                total_size += size
                if status in status_code_count:
                    status_code_count[status] += 1

                line_count += 1
                if line_count % 10 == 0:
                    print_stats()
                    print("-" * 40)
    except KeyboardInterrupt:
        pass

    # Print final stats
    print_stats()

if __name__ == '__main__':
    main()
