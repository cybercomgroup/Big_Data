#!/usr/bin/env python
import sys
import h5py
import tables
import os
import msvcrt

msvcrt.setmmode(sys.stdin.fileno(), os.O_BINARY)

h5 = sys.stdin.read()
print(h5.root.metadata.songs.nrows)

