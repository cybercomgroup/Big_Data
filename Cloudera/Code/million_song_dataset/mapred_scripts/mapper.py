#!/usr/bin/env python
import sys
import hashlib


def hash(s):
	s = str(s)
	x = int(hashlib.sha256(s.encode('utf-8')).hexdigest(), 16) % 10**8
	return x
	
headers = True

indexes_to_parse = []

for line in sys.stdin:
	line = line.replace("\n", "")
	line = line.split(',')
	to_print = ""
	if headers:
		headers = False
		for i, h in enumerate(line):
			to_print += (str(h) + ',')
			if h in ["SongID", "AlbumName", "ArtistID", "ArtistLocation", "ArtistName", "Title", "Artist_Mbid", "Artist_7didId", "7digitalid", "Audio_Md5", "TrackId"]:
				indexes_to_parse.append(i)

	else:
		for i, attr in enumerate(line):
			temp = attr
			if i in indexes_to_parse:
				temp = hash(attr)
			to_print += (str(temp) + ',')

	to_print = to_print[:-1] # Delete last comma
	print(to_print) # Adds newline by itself.
	
		
		
