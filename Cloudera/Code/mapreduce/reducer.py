#!/usr/bin/env python
import sys

surv = 0
notsurv = 0

for line in sys.stdin:
    val = line.strip()
    if val == "1":
	surv += 1
    else:
	notsurv += 1

print("Survived: " + str(surv) + "\tNot survived: " + str(notsurv))
