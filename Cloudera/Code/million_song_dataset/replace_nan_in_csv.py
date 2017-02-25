import os

source = open('SongCSV.csv', 'r')
target = open('SongCSV_fixed.csv', 'w')
first = True

for row in source:
    row = row.replace(",nan,", ",,")
    row = row.replace(",nan", ",")
    row = row.replace("b'", "")
    row = row.replace("'", "")
    if first:
        first = False
        target.write(row + "\n")
    else:
        target.write(row)


