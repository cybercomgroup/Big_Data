import os

source = open('SongCSV_fixed.csv', 'r')

for i, row in enumerate(source):
    row = row.split(",")
    print("Row " + str(i) + ": " + str(len(row)))
