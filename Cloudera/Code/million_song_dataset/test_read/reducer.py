#!/usr/bin/env python
import sys

tot = 0

for line in sys.stdin:
	val = line.strip()
	val = int(val)
	tot += val

print("Total rows: " + str(tot))
