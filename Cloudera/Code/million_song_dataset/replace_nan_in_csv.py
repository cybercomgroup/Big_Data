import os
newline = os.linesep

source = open('SongCSV.csv', 'r')
target = open('SongCSV_fixed.csv', 'w')

for row in source:
	row = row.replace(",nan,", ",,")
	row = row.replace(",nan", ",")
	target.write(row + newline)


