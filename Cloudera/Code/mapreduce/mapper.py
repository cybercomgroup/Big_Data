#!/usr/bin/env python
import sys

for line in sys.stdin:
    line = line.strip()
    splits = line.split(",")
    print(splits[1])
