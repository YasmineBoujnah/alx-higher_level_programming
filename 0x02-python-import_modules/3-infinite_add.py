#!/usr/bin/python3
import sys

if __name__ == "__main__":
    pass

argc = len(sys.argv) - 1

result = 0

for arg in sys.argv[1:]:
    result += int(arg)

print("{:d}".format(result))
